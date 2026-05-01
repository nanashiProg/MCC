// Находим форму на странице
const form = document.getElementById('userForm');
const responseDiv = document.getElementById('serverResponse');

// При нажатии на кнопку "Отправить" выполняется эта функция
form.addEventListener('submit', async (event) => {
    // Отменяем стандартную отправку формы (перезагрузку страницы)
    event.preventDefault();

    // Собираем данные из полей ввода
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    const height = document.getElementById('height').value;
    const weight = document.getElementById('weight').value;
    const diameter = document.getElementById('diameter').value;
    const max_diameter = document.getElementById('max_diameter').value;
    const weight_ball = document.getElementById('weight_ball').value;
    const chute_diameter = document.getElementById('chute_diameter').value;
    const speed = document.getElementById('speed').value;
    const chute_speed = document.getElementById('chute_speed').value;

    // Небольшая валидация на фронте
    if (!latitude || !longtitude || !height || !weight || !diameter || !max_diameter || !weight_ball || !chute_diameter || !speed || !chute_speed) {
        responseDiv.innerHTML = '<p style="color: red;">Пожалуйста, заполните все поля!</p>';
        return;
    }
    try {
    // ★ ВЫЗОВ PYTHON-ФУНКЦИИ ★
    // Этот асинхронный вызов отправляет данные в Python-функцию process_user_data
    const result = await eel.process_user_data(latitude, longtitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed)();
    // result — это объект, который вернула функция Python
                if (result.status === 'success') {
                    responseDiv.innerHTML = `<p style="color: green;">✅ ${result.message}, ${result.result}</p>`;
                    form.reset(); // Очищаем форму
                } else {
                    responseDiv.innerHTML = `<p style="color: red;">❌ Ошибка: ${result.message}</p>`;

                }
            } catch (error) {
                console.error("Ошибка при вызове Python:", error);
                responseDiv.innerHTML = '<p style="color: red;">Произошла ошибка при отправке данных.</p>';
            }
        });
