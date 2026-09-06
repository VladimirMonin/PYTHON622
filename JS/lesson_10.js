// Lesson 10.
// Srpead - rest operator
// Arrow functions

// Спред и рест оператор. Выглядят как три точки, но выполняют разные функции. Спред оператор разворачивает массив, а рест оператор собирает все оставшиеся элементы в массив. Рест оператор должен быть последним параметром в функции.

// Спред оператор, превращает аргументы в массив. Я могу подать одно число, десять чисел, или даже массив чисел (через спред)
function sumMany(...nums) {
  console.debug(nums);
  let result = 0;
  for (let num of nums) {
    result += num;
  }
  console.log(`Сумма чисел ${nums} равна ${result}`);
  return result;
}

let arg1 = 1;
let arg2 = 5;
let arg3 = 12;

let argsArray = [arg1, arg2, arg3];

console.log(sumMany(arg1, arg2, arg3)); // 18
console.log(sumMany(...argsArray)); // 18

// Вспомним синтаксический сахар тернарного оператора if в js
let age = 20;
let isAdult = age >= 18 ? "Совершеннолетний" : "Несовершеннолетний";
console.debug(isAdult);

// Стрелочные функции - это более короткий синтаксис для написания функций. Более короткие вариант, автоматически может делать возврат значнеия, если в одну строку может не использовать фигурные скобки.

// Обычная функция
function multiply(a, b) {
  return a * b;
}

// Стрелочная функция
const multiplyArrow = (a, b) => a * b;

console.debug(multiply(2, 3));
console.debug(multiplyArrow(2, 3));

// Картавый массив на обработку!
let rArray = ["Рыба", "Робот", "Трактор", "Бронетранспортер"];

// Задача. Заменить букву Р на Л в любом из регистров. Ловеркейс + реплейс.
// 1. - с помощью обычной функции
// 2. - с помощью стрелочной функции + foreach

function replaceRWithL(word) {
  return word.toLowerCase().replaceAll("р", "л");
}

let result1 = [];
for (let item of rArray) {
  let finalWord = replaceRWithL(item);
  result1.push(finalWord);
}
console.debug(result1);

// Или еще короче в одну строку тогда можно без скобок вообще!)))
rArray.forEach((item) =>
  console.debug(item.toLowerCase().replaceAll("р", "л")),
);

// Альтернативный вариант уже с использованием другой функции внутри стрелки
rArray.forEach((item) => {
  let replacedItem = replaceRWithL(item);
  console.debug(replacedItem);
});

// И одно строковое решение с использованием функции внутри функции
rArray.forEach((item) => console.debug(replaceRWithL(item)));

// forEach - "для каждого" - это метод массива, который позволяет выполнить функцию для каждого элемента массива. Он принимает функцию в качестве аргумента и выполняет ее для каждого элемента массива. Внутри функции можно использовать текущий элемент массива, который передается в качестве аргумента функции.

// ForEach НЕ возвращает новый массив, он просто выполняет функцию для каждого элемента массива. Если нужно создать новый массив на основе существующего, то лучше использовать метод map.

let myFilms = ["Матрица", "Начало", "Интерстеллар", "Грань будущего"];
myFilms.forEach((film) => console.debug(`Мой любимый фильм - ${film}`));
let myFilmsNew = myFilms.forEach((film) =>
  console.debug(`Мой любимый фильм - ${film}`),
);
console.debug(myFilmsNew); // undefined, так как forEach не возвращает новый массив

// Да, вы можете сказать, твоя стрелка она же не возвращает данные. А печатает. Давайте попробуем изменить стрелку и првоерим еще раз
let myFilmsNew1 = myFilms.forEach((film) => `Мой любимый фильм - ${film}`);
console.debug(myFilmsNew1); // undefined, так как forEach не возвращает новый массив, даже если внутри функции есть return

// ДА. Мы можем сделать так. Но это не канон. Потому что есть map)))
let myFilmsNew2 = [];
myFilms.forEach((film) => {
  let message = `Мой любимый фильм - ${film}`;
  myFilmsNew2.push(message);
});

// Map - это метод массива, который позволяет создать новый массив на основе существующего, применяя функцию к каждому элементу массива. Он принимает функцию в качестве аргумента и возвращает новый массив, который содержит результаты применения функции к каждому элементу исходного массива.
let myFilmsNew3 = myFilms.map((film) => `Мой любимый фильм - ${film}`);
console.debug(myFilmsNew3); // новый массив с результатами применения функции к каждому элементу исходного массива

// Filter - это метод массива, который позволяет создать новый массив на основе существующего, включив в него только те элементы, которые удовлетворяют определенному условию. Он принимает функцию в качестве аргумента и возвращает новый массив, который содержит только те элементы исходного массива, для которых функция возвращает true. Таким образом в стрелке должно быть булево выражение, которое будет проверять условие для каждого элемента массива.

let potatos = [
  "Картошка",
  "Молодая картошка",
  "Картошка",
  "мОЛОдая картоешечка",
  "молоДАЯ бульба",
  "Буьбочка",
];

let filteredPotatos = potatos.filter((potato) =>
  potato.toLowerCase().includes("молодая"),
);
console.debug(filteredPotatos); // новый массив, который содержит только те элементы исходного массива, для которых функция возвращает true

// Как бы это могло выглядить если бы у нас НЕ было фильтра?
let filteredYoungPotatos = [];
for (let potato of potatos) {
  if (potato.toLowerCase().includes("молодая")) {
    filteredYoungPotatos.push(potato);
  }
}
console.debug(filteredYoungPotatos); // новый массив, который содержит только те элементы исходного массива, для которых функция возвращает true

// Reduce - это метод массива, который позволяет создать одно значение на основе существующего массива, применяя функцию к каждому элементу массива и аккумулируя результат. Он принимает функцию в качестве аргумента и возвращает одно значение, которое является результатом применения функции к каждому элементу исходного массива. Функция принимает два аргумента: аккумулятор (acc) и текущий элемент (curr). Аккумулятор сохраняет промежуточный результат, который обновляется на каждом шаге, а текущий элемент - это элемент массива, который обрабатывается в данный момент.

// Пример на массиве чисел. Суммируем все числа в массиве с помощью reduce.
let numbers = [1, 2, 3, 4, 5];
let sumOfNumbers = numbers.reduce((acc, curr) => acc + curr, 0);
console.debug(sumOfNumbers); // 15, так как 1 + 2 + 3 + 4 + 5 = 15

// Пример на полном цикле
let sumOfNumbers2;

for (let num of numbers) {
  sumOfNumbers2 = sumOfNumbers2 ? sumOfNumbers2 + num : num; // если sumOfNumbers2 уже есть, то добавляем к нему num, иначе присваиваем num
}

// Пример на строках. Собираем макаронного монстра!
let words = ["Макароны", "на", "твоей", "тарелке", "ожили!"];

let spaghettiMonster = words.reduce((acc, curr) => `${acc} ${curr}`);
console.debug(spaghettiMonster); // "Макароны на твоей тарелке ожили!", так как мы объединяем все слова в одну строку

//
let container = document.getElementById("container");

let productCards = [
  { name: "Телефон", price: 1000 },
  { name: "Ноутбук", price: 2000 },
  { name: "Планшет", price: 1500 },
];

productCards.forEach((product) => {
  let productCard = document.createElement("div");
  productCard.classList.add("card");
  productCard.textContent = `${product.name} - ${product.price} руб.`;
  container.appendChild(productCard);
});
