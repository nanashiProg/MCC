import eel
from back.calculations import calculation

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

    math_result = calculation(latitude, longtitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed)

    print(f"Python получил данные: {latitude} {longtitude} {height} {weight} {diameter} {max_diameter} {weight_ball} {chute_diameter} {speed} {chute_speed}")

    # --- Здесь ваша бизнес-логика ---
    # Сохранение в файл
    with open("results.txt", "a", encoding='utf-8') as f:
        f.write(f"{latitude}, {longtitude}, {height}, {height}, {weight}, {diameter}. {max_diameter}, {weight_ball}, {chute_diameter}, {speed}, {chute_speed}\n")

    # Можно выполнить сложные расчеты, обратиться к БД и т.д.
    # result = some_long_calculation(surname, grade)

    # --- Отправка ответа обратно в JS ---
    # Eel сам сконвертирует словарь в JSON-объект для JS
    return {"status": "success",
            "message": f"Спасибо! Данные сохранены.",
            "result": math_result
    }

eel.start('index.html',size=(1000,1000))             # Start (this blocks and enters loop)