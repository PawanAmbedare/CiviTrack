document.addEventListener('DOMContentLoaded', function(){
  // initialize map if #map exists (uses Leaflet loaded from CDN in template)
  var mapEl = document.getElementById('map');
  if(mapEl && typeof L !== 'undefined'){
    var map = L.map('map').setView([20.0, 0.0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    var marker = null;
    map.on('click', function(e){
      var lat = e.latlng.lat.toFixed(6);
      var lng = e.latlng.lng.toFixed(6);
      if(marker) map.removeLayer(marker);
      marker = L.marker([lat,lng]).addTo(map);
      var latInput = document.getElementById('latitude') || document.getElementById('id_latitude');
      var lngInput = document.getElementById('longitude') || document.getElementById('id_longitude');
      if(latInput) latInput.value = lat;
      if(lngInput) lngInput.value = lng;
    });

    // try to use geolocation to center map
    if(navigator.geolocation){
      navigator.geolocation.getCurrentPosition(function(pos){
        var lat = pos.coords.latitude;
        var lng = pos.coords.longitude;
        map.setView([lat,lng], 14);
      });
    }
  }
});
