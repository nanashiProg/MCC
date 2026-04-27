import eel
from back.calculations import calculation

# 2. Декоратор @eel.expose делает эту функцию видимой для JavaScript

@eel.expose
def process_user_data(latitude, longtitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed):
    """
    Эта функция будет вызвана из браузера.
    Она получает данные из формы и что-то с ними делает.
    """

    math_result = calculation(latitude, longtitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed)

    print(f"Python получил данные: {latitude} {longtitude} {height} {weight} {diameter} {max_diameter} {weight_ball} {chute_diameter} {speed} {chute_speed}")

    # --- Отправка ответа обратно в JS ---
    # Eel сам сконвертирует словарь в JSON-объект для JS
    return {"status": "success",
            "message": f"Спасибо! Данные сохранены.",
            "result": math_result
    }

try:
    eel.init('web')
    print("Инициализация прошла успешно")
    eel.start('index.html', block=True)
except Exception as e:
    print(f"Произошла ошибка при запуске: {e}")
    input("Нажмите Enter, чтобы выйти...")



eel.start('index.html',size=(1000,1000))             # Start (this blocks and enters loop)