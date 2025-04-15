//The value saved to kelvin will stay constant.
const Kelvin = 389;

let Celsius;
Celsius = Kelvin - 273;
//console.log(Celsius);

var Fahrenheit;
Fahrenheit = Math.floor(Celsius *(9/5) + 32);
//console.log(Fahrenheit);

console.log(`The temperature is ${Fahrenheit} degrees Fahrenheit`);

let Newton = Math.floor(Celsius * (33/100));
console.log(`The temperature is ${Newton} degrees Newton`);
