

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
var map = L.map('map', {
    center: [55.7558, 37.6173],
    zoom: 10,
    layers: [osm]
});

L.control.layers(baseMaps).addTo(map);