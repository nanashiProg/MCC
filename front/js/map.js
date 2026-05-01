// Слои карт
const osm = L.tileLayer(
  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  { attribution: 'OpenStreetMap' }
);

const satellite = L.tileLayer(
  'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
  { attribution: 'Esri' }
);

const dark = L.tileLayer(
  'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
  { attribution: 'CartoDB' }
);

const baseMaps = {
  "Обычная": osm,
  "Спутник": satellite,
  "Тёмная": dark
};

// Инициализация карты
const latitude = parseFloat(document.getElementById('latitude')?.value) || 55.751244;
const longitude = parseFloat(document.getElementById('longitude')?.value) || 37.618423;

var map = L.map('map', {
    center: [latitude, longitude],
    layers: [osm],
    zoom: 10
});

L.control.layers(baseMaps).addTo(map);

// Координаты при движении мыши
map.on('mousemove', function (e) {
    document.getElementById('coordinates').innerText =
        "Широта: " + e.latlng.lat.toFixed(5) +
        " | Долгота: " + e.latlng.lng.toFixed(5);
});

// Координаты при клике по карте (заполняются в форму)
let marker;
map.on('click', function (e) {
    const { lat, lng } = e.latlng;

    if (marker) {
        marker.setLatLng(e.latlng);
    } else {
        marker = L.marker(e.latlng).addTo(map);
    }

    document.getElementById('latitude').value = lat.toFixed(5);
    document.getElementById('longitude').value = lng.toFixed(5);
});
