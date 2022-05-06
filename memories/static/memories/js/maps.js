function initMap() {
  const uluru = { lat: -25.344, lng: 131.031 };

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: uluru,
    zoomControl: true,
    mapTypeControl: false,
    scaleControl: false,
    streetViewControl: false,
    rotateControl: true,
    fullscreenControl: true,
    scrollwheel: false,
  });

  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
    draggable:true,
  });

  var lat = marker.getPosition().lat();
  var lng = marker.getPosition().lng();

  geocodeLatLng(lat, lng)

  google.maps.event.addListener(marker, 'dragend', function()
  {
      var lat = marker.getPosition().lat();
      var lng = marker.getPosition().lng();
      geocodeLatLng(lat, lng)
  });
}

function geocodeLatLng(lat, lng) {
  var requestOptions = {
    method: 'GET',
  };
  fetch("https://api.geoapify.com/v1/geocode/reverse?lat=" + lat.toString() + "&lon=" + lng.toString() + "&apiKey=dc47041477c1448599b4eab4be3141e1", requestOptions)
      .then(response => response.json())
      .then(result => document.getElementById('location_memory').value = (result.features[0].properties.formatted))
      .catch(error => window.alert('error: ' + error));
}

window.initMap = initMap;