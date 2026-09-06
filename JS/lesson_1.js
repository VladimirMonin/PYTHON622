console.log("Файл lesson_1 подключен");
console.log("пицца");

// комментарий
// "" - строка
// 1234 - число "1234" - строка

let userName = "Иванов Иван Иванович";
console.log(userName);

// Переменные в JS
// должны быть уникальными
// не должны начинаться с цифры
// могут содержать буквы, цифры, символы $ и _
// не должны совпадать с зарезервированными словами
// Существительные и прилагательные
// До четырех слов вполне допустимо, но лучше 2-3
// lowerCamelCase - нижнийВерблюжийСтиль

// Let VS Var
// let - Современный способ сделать переменную. Следит за тем чтобы переменная не была объявлена дважды.
// var - Устаревший способ сделать переменную. Не следит за тем чтобы переменная не была объявлена дважды. Может привести к ошибкам в коде.

// var salary = 1000000
// var salary = "Чебурек :("

// let salary = 1000000
// let salary = 222222222

// const salary = 1000000000000
// salary = 2222 // TypeError: invalid assignment to const 'salary'
// console.log(salary)

let userAge = 18;
userAge = 19;
console.log(userAge);

let userName2 = "Иван";
let userSurname = "Иванов";
let userAge2 = 18;
console.log("Пользователь: " + userName2 + " " + userSurname + " " + userAge2);

// Шаблонные строки
// Пользователь: Иван Иванов Возраст: 18
let finalLogString = `Пользователь: ${userName2} ${userSurname} Возраст: ${userAge2}`;
console.log(finalLogString);

let finalLogString2 = `Пользователь: ${userName2} ${userSurname} Возраст: ${userAge2*2} лет`;
console.log(finalLogString2);

// Типы данных в JS
// Числа (number) - 123, 3.14, -5
// Строки (string) - "Привет", 'Мир', `Шаблонная строка`
// Булевы значения (boolean) - true, false
// Массивы (array) - [1, 2, 3], ["яблоко", "банан", "груша"]
// Объекты (object) - {name: "Иван", age: 18}, {title: "Книга", author: "Писатель"}
// Null - null
// Undefined - undefined

// prompt - функция для получения данных от пользователя - вернет вам строку
// alert - функция для отображения информации пользователю - не возвращает ничего, просто показывает сообщение
// confirm - функция для получения подтверждения от пользователя (OK/Cancel) - вернет true или false

let promptUserName = prompt("Введите ваше имя:");
let isAdult = confirm("Вам есть 18 лет?");

console.log(`Пользователь: ${promptUserName}, Совершеннолетний: ${isAdult}`);
