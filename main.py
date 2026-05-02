import eel
from back.calculation_start_par import startV, startF_lift, startF_net_lift

# 2. Декоратор @eel.expose делает эту функцию видимой для JavaScript



# Set front files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('front', allowed_extensions=['.js', '.html'])

@eel.expose
def process_user_data(latitude, longtitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed):
    """
    Эта функция будет вызвана из браузера.
    Она получает данные из формы и что-то с ними делает.
    """

    V0 = startV(diameter)

    F_lift = startF_lift(V0)

    F_net_lift = startF_net_lift(F_lift, weight, weight_ball)

    print(f"Python получил данные: {latitude} {longtitude} {height} {weight} {diameter} {max_diameter} {weight_ball} {chute_diameter} {speed} {chute_speed}")

    # Можно выполнить сложные расчеты, обратиться к БД и т.д.
    # result = some_long_calculation(surname, grade)

    # --- Отправка ответа обратно в JS ---
    # Eel сам сконвертирует словарь в JSON-объект для JS
    return {"status": "success",
            "message": f"Спасибо! Данные сохранены.",
            "space": V0,
            "lift": F_lift,
            "net_lift": F_net_lift
    }

try:
    eel.init('front') 
    print("Инициализация прошла успешно")
    eel.start('index.html', block=True, size=(1000,1000))
except Exception as e:
    print(f"Произошла ошибка при запуске: {e}")
    input("Нажмите Enter, чтобы выйти...")   
