// 1. Инициализируем карту и задаем центр и масштаб
var map = L.map('map').setView([55.751244, 37.618423], 12);

// 2. Добавляем слой с тайлами (внешний вид карты)
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// 3. Добавляем маркер (точку)
var marker = L.marker([55.751244, 37.618423]).addTo(map);

// 4. Добавляем всплывающее окно к маркеру
marker.bindPopup("<b>Красная площадь</b><br>Здесь можно увидеть самое сердце Москвы.").openPopup();

// 5. Пример добавления второй точки
var marker2 = L.marker([55.741469, 37.605517]).addTo(map);
marker2.bindPopup("<b>Третьяковская галерея</b>");