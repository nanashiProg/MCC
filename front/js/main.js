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
    if (!latitude || !longitude || !height || !weight || !diameter || !max_diameter || !weight_ball || !chute_diameter || !speed || !chute_speed) {
        responseDiv.innerHTML = '<p style="color: red;">Пожалуйста, заполните все поля!</p>';
        return;
    }
    try {
    // ★ ВЫЗОВ PYTHON-ФУНКЦИИ ★
    // Этот асинхронный вызов отправляет данные в Python-функцию process_user_data
    const result = await eel.process_user_data(latitude, longitude, height, weight, diameter, max_diameter, weight_ball, chute_diameter, speed, chute_speed)();
    // result — это объект, который вернула функция Python
                if (result.status === 'success') {
                    responseDiv.innerHTML = `<p style="color: green;">✅ ${result.message} <br>
                    Объем гелия на старте: ${result.space.toFixed(2)} <br>
                    Подъемная сила (тяга) на старте ${result.lift.toFixed(2)} <br>
                    Чистая подъемная сила: ${result.net_lift.toFixed(2)}</p>`;
                    form.reset(); // Очищаем форму
                } else {
                    responseDiv.innerHTML = `<p style="color: red;">❌ Ошибка: ${result.message}</p>`;

                }
            } catch (error) {
                console.error("Ошибка при вызове Python:", error);
                responseDiv.innerHTML = '<p style="color: red;">Произошла ошибка при отправке данных.</p>';
            }
        });

const formApi = document.getElementById('userForm_api');
const responseDivApi = document.getElementById('serverResponse_api');

formApi.addEventListener('submit', async (event) => {
    // Отменяем стандартную отправку формы (перезагрузку страницы)
    event.preventDefault();

    // Собираем данные из полей ввода
    const latitudeApi = document.getElementById('latitude_api').value;
    const longitudeApi = document.getElementById('longitude_api').value;
    const datetimelocalApi = document.getElementById('launch_datetime_api').value;
    const speedApi = document.getElementById('speed_api').value;
    const burst_altitudeApi = document.getElementById('burst_altitude_api').value;
    const chute_speedApi = document.getElementById('chute_speed_api').value;

    // Небольшая валидация на фронте
    if (!latitudeApi || !longitudeApi || !datetimelocalApi || !speedApi || !burst_altitudeApi || !chute_speedApi) {
        responseDivApi.innerHTML = '<p style="color: red;">Пожалуйста, заполните все поля!</p>';
        return;
    }
    try {
    // ★ ВЫЗОВ PYTHON-ФУНКЦИИ ★
    // Этот асинхронный вызов отправляет данные в Python-функцию process_user_data
    const resultApi = await eel.api(latitudeApi, longitudeApi, datetimelocalApi, speedApi, burst_altitudeApi, chute_speedApi)();
    // result — это объект, который вернула функция Python
                if (resultApi.status === 'success') {
                    responseDivApi.innerHTML = `<p style="color: green;">✅ ${resultApi.message}</p>`;
                    formApi.reset(); // Очищаем форму
                } else {
                    responseDivApi.innerHTML = `<p style="color: red;">❌ Ошибка: ${resultApi.message}</p>`;
                }
            } catch (error) {
                console.error("Ошибка при вызове Python:", error);
                responseDivApi.innerHTML = '<p style="color: red;">Произошла ошибка при отправке данных.</p>';
            }
        });