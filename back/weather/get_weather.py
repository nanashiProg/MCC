from ecmwf.opendata import Client
import xarray as xr
import numpy as np
from scipy.interpolate import interp1d

# Координаты Москвы
LAT, LON = 55.7558, 37.6173
TARGET_HEIGHT = 19500

# --- 1. Скачиваем данные (уровни от 1000 до 50) ---
print("Скачиваю данные с ECMWF...")
client = Client(source="ecmwf")

stream = "oper"

levels = [1000, 925, 850, 700, 500, 400, 300, 250, 200, 150, 100, 50]
params = ["gh", "t", "u", "v"]

client.retrieve(
    date=0, step=0, stream="oper", type="fc",
    levtype="pl", levelist=levels, param=params,
    target="data_with_gh.grib"
)
print("Файл скачан.")

# --- 2. Загружаем данные ---
print("Загружаю и анализирую данные...")
ds = xr.open_dataset("data_with_gh.grib", engine="cfgrib")

# Избавляемся от лишних измерений (например, 'step', 'number')
ds = ds.squeeze()

# Убеждаемся, что у нас только координаты (уровень, широта, долгота)
print(f"Размерности ds: {ds.dims}")

# --- 3. ТОЧНОЕ извлечение значений для Москвы ---
# Находим ближайшие индексы
lat_idx = np.argmin(np.abs(ds.latitude.values - LAT))
lon_idx = np.argmin(np.abs(ds.longitude.values - LON))

# Извлекаем высоты (geopotential height) — они уже в метрах (gpm)
# Используем .sel() для надежности
heights = ds["gh"].sel(isobaricInhPa=levels).values[:, lat_idx, lon_idx]

# Проверяем, нужно ли делить на 9.80665? НЕТ! ECMWF уже хранит gh в метрах (gpm).
# Об этом говорит официальная документация: единица gh — это gpm (геопотенциальные метры)[citation:3][citation:8].
# Делить на 9.80665 нужно только если вы скачали 'z' (геопотенциал в м2/с2), но у нас 'gh'.

# Выводим ИСПРАВЛЕННЫЕ данные для проверки
print(f"\nИСПРАВЛЕННЫЕ данные: Геопотенциальная высота для Москвы:")
for i, level in enumerate(levels):
    print(f"  {level} гПа -> {heights[i]:.0f} м")

# --- 4. Интерполяция на 2000 м (если нужно) ---
if heights.min() <= TARGET_HEIGHT <= heights.max():
    # Извлекаем температуру и ветер
    temperatures = ds["t"].sel(isobaricInhPa=levels).values[:, lat_idx, lon_idx] - 273.15
    u_winds = ds["u"].sel(isobaricInhPa=levels).values[:, lat_idx, lon_idx]
    v_winds = ds["v"].sel(isobaricInhPa=levels).values[:, lat_idx, lon_idx]

    # Интерполяция
    f_temp = interp1d(heights, temperatures, kind='cubic', fill_value='extrapolate')
    f_u = interp1d(heights, u_winds, kind='linear', fill_value='extrapolate')
    f_v = interp1d(heights, v_winds, kind='linear', fill_value='extrapolate')

    temp_at_target = f_temp(TARGET_HEIGHT)
    u_at_target = f_u(TARGET_HEIGHT)
    v_at_target = f_v(TARGET_HEIGHT)

    # Ветер
    wind_speed = np.sqrt(u_at_target ** 2 + v_at_target ** 2)
    wind_dir_rad = np.arctan2(u_at_target, v_at_target)
    wind_dir_deg = np.rad2deg(wind_dir_rad) % 360

    print(f"\nРезультаты для Москвы на высоте {TARGET_HEIGHT} м:")
    print(f"  Температура: {temp_at_target:.1f} °C")
    print(f"  Ветер: {wind_speed:.1f} м/с, направление {wind_dir_deg:.0f}°")
else:
    print(f"\nВысота {TARGET_HEIGHT} м вне диапазона ({heights.min():.0f} - {heights.max():.0f} м)")