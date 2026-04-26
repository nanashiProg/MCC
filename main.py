import eel

import math

# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
eel.init('web', allowed_extensions=['.js', '.html'])

R = 8.314   # универсальная газовая постоянная
M = 0.029   # молярная масса воздуха
g = 9.81    # ускорение свободного падения
r = 0.1785   # плотность гелия

# 2. Декоратор @eel.expose делает эту функцию видимой для JavaScript
@eel.expose
def process_user_data(latitude, longtitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed):
    """
    Эта функция будет вызвана из браузера.
    Она получает данные из формы и что-то с ними делает.
    """

    math_result = calculations(latitude, longtitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed)

    print(f"Python получил данные: {latitude} {longtitude} {height} {weight} {diameter} {max_diameter} {weight_ball} {chute_diameter} {speed} {chute_speed}")

    # --- Здесь ваша бизнес-логика ---
    # Сохранение в файл
    with open("results.txt", "a", encoding='utf-8') as f:
        f.write(f"{latitude}, {longtitude}, {height}, {height}, {weight}, {diameter}. {max_diameter}, {weight_ball}, {chute_diameter}, {speed}, {chute_speed}\n")

    # Можно выполнить сложные раеты, обратиться к БД и т.д.
    # result = some_long_calculation(surname, grade)

    # --- Отправка ответа обратно в JS ---
    # Eel сам сконвертирует словарь в JSON-объект для JS
    return {"status": "success",
            "message": f"Спасибо! Данные сохранены.",
            "result": math_result
    }

def calculations(latitude, longtitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed):
    V0 = 4/3 * math.pi * (int(diameter)/2)**3

    math_result = (99992*M/(R*20)-r)*V0*g



    return math_result




eel.start('index.html', mode='none', block=True, cmdline_args=['--icon-name=/web/favicon.ico'])             # Start (this blocks and enters loop)