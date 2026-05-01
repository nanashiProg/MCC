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

// Кастомная иконка для маркера
const customIcon = L.divIcon({
    className: 'custom-marker',
    html: '<div class="dot"></div>',
    iconSize: [10, 10]
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
    const lat = e.latlng.lat;
    const lng = e.latlng.lng;
    
    if (marker) {
        marker.setLatLng(e.latlng);
    } else {
        marker = L.marker(e.latlng, { icon: customIcon }).addTo(map);
    }

    document.getElementById('latitude').value = lat.toFixed(5);
    document.getElementById('longitude').value = lng.toFixed(5);
});


// Обновление маркера из input
function updateMarkerFromInputs() {
    const lat = parseFloat(document.getElementById('latitude').value);
    const lng = parseFloat(document.getElementById('longitude').value);

    if (isNaN(lat) || isNaN(lng)) return;
    const latlng = [lat, lng];

    if (marker) {
        marker.setLatLng(latlng);
    } else {
        marker = L.marker(latlng, { icon: customIcon }).addTo(map);
    }

    map.setView(latlng);
}

// Обновление маркера при нажатии Enter в input
document.getElementById('latitude').addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        updateMarkerFromInputs();
    }
});

document.getElementById('longitude').addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        updateMarkerFromInputs();
    }
});