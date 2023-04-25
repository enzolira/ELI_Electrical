//  ---------------- API Clima ---------------------------------------- 
const url_clima = 'https://api.aerisapi.com/conditions/:auto?format=json&plimit=1&filter=1min&client_id=nLsPZM92FZZPUp5MVpDZj&client_secret=yzrF3jek5iEzDrjE12SQoTssjtUe1RJAOXmUabOJ';
console.log(url_clima)

function getWeatherData(){
const requestClima = new XMLHttpRequest();
requestClima.open('GET', url_clima);
requestClima.send();

requestClima.onload = function() {
if (requestClima.status === 200) {
    const data = JSON.parse(requestClima.responseText);
    const temperature = data.response[0].periods[0].tempC;
    const city = capitalizeFirstLetter(data.response[0].place.name);
    const icon = data.response[0].periods[0].icon;

    const weatherDisplay = document.getElementById('weather-display');

    const infoElement = document.createElement('small');
    infoElement.innerHTML = `${temperature}°C in ${city}`;

    const iconElement = document.createElement('img');
    iconElement.src = `https://cdn.aerisapi.com/wxicons/v2/${icon}`;
    iconElement.style.width = '30px';
    iconElement.style.height = '30px';
    iconElement.style.marginRight = '10px';
    
    
    while (weatherDisplay.firstChild) {
        weatherDisplay.removeChild(weatherDisplay.firstChild);
    }  

    weatherDisplay.appendChild(iconElement);
    weatherDisplay.appendChild(infoElement);
}
    else {
    console.log('Error al obtener datos de la API');
}
};
}

getWeatherData()
setInterval(getWeatherData, 300000)
