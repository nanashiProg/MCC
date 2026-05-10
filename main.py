import eel
import requests
from back.calculation_start_par import startV, startF_lift, startF_net_lift

eel.init('front', allowed_extensions=['.js', '.html', '.css'])

# Функция, которая будет вызвана из JavaScript
# @eel.expose
# def process_user_data(latitude, longitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed):
#     """
#     Эта функция будет вызвана из браузера.
#     Она получает данные из формы и что-то с ними делает.
#     """

#     V0 = startV(diameter)

#     F_lift = startF_lift(V0)

#     F_net_lift = startF_net_lift(F_lift, weight, weight_ball)

#     print(f"Python получил данные: {latitude} {longitude} {height} {weight} {diameter} {max_diameter} {weight_ball} {chute_diameter} {speed} {chute_speed}")

#     # Отправка ответа обратно в JS 
#     return {"status": "success",
#             "message": f"Спасибо! Данные сохранены.",
#             "space": V0,
#             "lift": F_lift,
#             "net_lift": F_net_lift
#     }

@eel.expose
def api(latitude, longitude, datetimelocal, speed, burst_altitude, chute_speed):
    print(f"Получены данные из API: {latitude}, {longitude}, {datetimelocal}, {speed}, {burst_altitude}, {chute_speed}")

    url = "http://predict.cusf.co.uk/api/v1/"

    params = {
        "launch_latitude": latitude,
        "launch_longitude": longitude,
        "launch_datetime": datetimelocal,
        "ascent_rate": speed,
        "burst_altitude": burst_altitude,
        "descent_rate": chute_speed,
        "profile": "standard_profile"
    }
    

    response = requests.get(url, params=params)
    print("STATUS:", response.status_code)
    print("TEXT:", response.text)
    if response.status_code == 200:
        data = response.json()
        return {"status": "success", "message": "Данные успешно получены!", "data": data}
    else:
        return {"status": "error", "message": "Ошибка API"}
# Запуск Eel
try:
    eel.init('front') 
    print("Инициализация прошла успешно")
    eel.start('index.html', block=True, size=(1000,1000))
except Exception as e:
    print(f"Произошла ошибка при запуске: {e}")
    input("Нажмите Enter, чтобы выйти...")   
