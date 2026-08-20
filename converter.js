function convertToCelsiusFromKelvin(kelvin) {
const celsius = kelvin - 273.15;
return Math.round(celsius * 100) / 100;
}

console.log(convertToCelsiusFromKelvin(300));

