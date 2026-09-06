console.debug("9-2 подключен");

// Варианты импорта из другого файла
// 1. - импорт всего, что экспортировано из другого файла
// 2. - импорт конкретных переменных, функций и т.д. из другого файла

// 1.
// import * as person from "./lesson_9_1.js";

// console.debug(person.firstName, person.lastName);

// 2.
import {
  firstName,
  lastName,
  getFullName,
  sum,
  getMyFriendsNames,
} from "./lesson_9_1.js";

// Даст ошибку
// const firstName = "Авраам"

console.debug(firstName, lastName);

sum(1, 2);
let fullName = getFullName("Иван");
console.debug(fullName);

getMyFriendsNames("Петр", "Иван", "Сергей");

// Spread оператор - позволяет развернуть массив в отдельные элементы
// Rest оператор - позволяет собрать несколько элементов в массив

let friendsNames = ["Петр", "Иван", "Сергей"];

// Spread оператор - вызов происходит так, как будто я передал ВСЕ СТРОКИ через запятую
getMyFriendsNames(...friendsNames);