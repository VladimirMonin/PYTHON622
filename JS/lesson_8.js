// Lesson 8 - Functions
// Функции - блок кода который выполняет определенную задачу и может быть повторно использован.
// Решает проблему повторения кода, и позволяет разбить программу на более мелкие части, что делает ее более организованной и удобной для понимания.
// Решает проблему нарушения принципа DRY (Don't Repeat Yourself) - когда один и тот же код повторяется в нескольких местах, что может привести к ошибкам и затруднить поддержку кода.

// Синтаксис функции
// function имя_функции(параметры) {
//     // тело функции
// }

// Правила нейминга функций:
// JS стандартные правила - lowerCamelCase
// Не начинаются с цифры, не содержат пробелов, не используют зарезервированные слова языка
// Содержат глаголы и описывают действие, которое выполняет функция

// Плохие примеры: 1fu, myFu, xFu, xSave, cheburekFu,
// Хорошие примеры: getDailyWeather, calculateArea, saveUserData, sendEmailNotification

// Пример функции
function greet() {
  console.debug("Привет, медвед!");
}

// Вызов функции
greet(); // Привет, медвед!

let result = greet(); // Привет, медвед!
console.debug(result); // undefined - функция не возвращает значение, поэтому результат - undefined

// Функция с параметрами и return

function greetByName(name) {
  let result = `Привет, ${name}!`;
  //   console.debug("Функция greetByName отработала", result);
  return result;
}

let greeting = greetByName("Медвед");
console.debug(greeting); // Привет, Медвед!

// Совместная работа нескольких функций (поэтапная)

function getGreetString(name) {
  return `Привет, ${name}!`;
}

function greetByName(greetString) {
  console.debug(greetString);
}

// function main() {
//   let name = "Медвед";
//   let greetString = getGreetString(name);
//   greetByName(greetString);
// }

// main(); // Привет, Медвед!

// Области видимости JS
// Глобальная область - доступна во всем коде, объявляется вне всех функций и блоков.
// Локальная область - доступна только внутри функции или блока, объявляется внутри функции или блока.
// Блоковая область - доступна только внутри блока кода, объявляется внутри блока кода (например, внутри if, for, while).
//

// Глобальная область видимости - как телефонная книга города. let не даст создать две одинаковые переменные.
let someVar = 5;
// let someVar

// Локальная область видимости - как дом в городе. Тут СВОЯ ОБЛАТСЬ ВИДИМОСТИ
function someFunc() {
  // console.debug(someVar) // ReferenceError - переменная someVar из глобальной области ДОСТУПНА внутри, но JS не пойдет ее искать, потому что внутри функции НИЖЕ объявлена другая переменная с таким же именем, и она будет приоритетной для использования внутри функции
  let someVar = 1;
  console.debug(someVar); // 1
}

someFunc();
console.debug(someVar); // 5 - глобальная переменная не изменилась

function getFinalString(str1, str2) {
  let finalString = `${str1} ${str2}`;
  console.debug(finalString);
  return finalString;
}

getFinalString("Привет", "Медвед");
getFinalString("Привет", "Бобёр", "Как дела?");
getFinalString("Привет");
getFinalString();

// Практика - создание списка ToDo из промпта и нескольих функций
let todoList = document.getElementById("todoList");
console.debug(todoList);

function addTodoItem(todoString) {
  let li = document.createElement("li");
  li.textContent = todoString;
  todoList.appendChild(li);
}

function main() {
  while (true) {
    let todoString = prompt("Введите задачу для списка ToDo | стоп");
    if (todoString.toLowerCase() === "стоп") {
      break;
    }
    addTodoItem(todoString);
  }
}

main();
