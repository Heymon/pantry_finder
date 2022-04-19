

const CONFIGURATION = {

    "mapOptions": {
        "center":{"lat":37.808611,"lng":-122.331732},
        "fullscreenControl":false,"mapTypeControl":false,
        "streetViewControl":false,
        "zoom":10,"zoomControl":false,"maxZoom":17},
    // "mapsApiKey": "AIzaSyCQqjRgORs-fN3w-_eFKGnUxQYfWP8IeDI",
    "capabilities": {"input":true,"autocomplete":true,"directions":true,"distanceMatrix":true,"details":true},
    "geocodeCache": new Map(),
  };

// Initialize and add the map
function initMap() {

    

    // The map, centered
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: CONFIGURATION.mapOptions.zoom,
      center: CONFIGURATION.mapOptions.center,
    });

    initializeAutocomplete(map)
    
}

const setPantryLocation = (inputEl, placeResult)=>{
    inputEl.value = placeResult.formatted_address;
    console.log(placeResult)

}

const geocodeSearch = (map, inputEl, query)=> {
    if (!query) {
      return;
    }

    // const handleResult = function(geocodeResult) {
    //   searchInputEl.value = geocodeResult.formatted_address;
    //   setPantryLocation(searchInputEl, geocodeResult);
    // };

    if (CONFIGURATION.geocodeCache.has(query)) {
        setPantryLocation(inputEl, geocodeCache.get(query));
    //   handleResult(geocodeCache.get(query));
        return;
    }
    const geocoder = new google.maps.Geocoder();
    const request = {address: query, bounds: map.getBounds()};
    geocoder.geocode(request, function(results, status) {
      if (status === 'OK') {
        if (results.length > 0) {
          const result = results[0];
          CONFIGURATION.geocodeCache.set(query, result);
          setPantryLocation(inputEl, result);
        //   handleResult(result);
        }
      }
    });
  };

function initializeAutocomplete(map) {

    let searchInputEl = document.querySelector("input[name='address']");
    console.log(searchInputEl);

    const autocomplete = new google.maps.places.Autocomplete(searchInputEl, {
        types: ['geocode'],
        fields: ['place_id', 'formatted_address', 'geometry.location']
    });
    autocomplete.bindTo('bounds', map);
    autocomplete.addListener('place_changed', function() {
        const placeResult = autocomplete.getPlace();
        // console.log(placeResult)
        if (!placeResult.geometry) {
            // Hitting 'Enter' without selecting a suggestion will result in a
            // placeResult with only the text input value as the 'name' field.
            geocodeSearch(map, searchInputEl, placeResult.name);
            return;
        }
        setPantryLocation(searchInputEl, placeResult);
        //set pantry info with placeResult
    })
}
      