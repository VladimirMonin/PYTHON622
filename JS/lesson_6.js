// const ulList = document.getElementById("list");
// console.debug(ulList); // Вы буквально получаете доступ к элементу с id 'list' и выводите его в консоль для проверки. Объект тега UL

// let usersFilms = prompt("Введите ваши любимые фильмы через запятую").split(",");

// for (let film of usersFilms) {
//   let li = document.createElement("li");
//   li.textContent = film;
//   ulList.appendChild(li);
// }

// ОПЕРАТОРЫ УПРАВЛЕНИЯ ЦИКЛОМ

// let applesTree = [
//   "яблоко",
//   "яблоко",
//   "яблоко",
//   "яблоко",
//   "яблоко",
//   "гнилое яблоко",
//   "поклеванное яблоко",
//   "яблоко",
//   "яблоко",
//   "гнилое яблоко",
//   "яблоко",
//   "яблоко",
//   "яблоко",
//   "яблоко",
//   "гнилое яблоко",
//   "поклеванное яблоко",
//   "яблоко",
//   "яблоко",
//   "гнилое яблоко",
// ];

// let goodApples = [];
// let applesNeed = 5;

// for (let apple of applesTree) {
//   console.debug(`Проверяется яблоко ${apple}`);
//   if (apple.includes("гнилое") || apple.includes("поклеванное")) {
//     console.debug(`Яблоко ${apple} пропущено`);
//     // Continue - пропускает текущую итерацию и переходит к следующей
//     continue;
//   } else {
//     console.debug(`Яблоко ${apple} добавлено в корзину`);
//     goodApples.push(apple); // Добавляем хорошие яблоки в корзину
//   }
//   //   Break - полностью остановит цикл
//   if (goodApples.length === applesNeed) {
//     console.debug("Достаточно яблок, сбор завершен");
//     break; // Достаточно яблок, выходим из цикла
//   }
// }

// FOR - другие варианты
// for let in - при обходе массива вы получаете индекс элемента
// for (let index = 0; index < 5; index++) {
// for (let index = 0; index < applesTree.length; index++) {
//  (стартовая точка; условие продолжения; шаг)

// for (let appleIndex in applesTree) {
//   console.debug(appleIndex); // Индексы от 0 до 18
//   console.debug(applesTree[appleIndex]); // Яблоки по индексам
// }

// for (let index = 0; index < 5; index++) {
//   console.debug(index); // Индексы от 0 до 4
// }

// let index = 0;
// for (;;) {
//   if (index >= 5) {
//     break; // Останавливаем бесконечный цикл, когда индекс достигает 5
//   }
//   console.debug(index); // Индексы от 0 до 4
//   index++;
// }

// while - выполняет код, пока условие истинно
// Бесконечный цикл - потому что true всегда будет true
// while (true) {
//     console.debug("Купи слона!");
// }

// let count = 0;
// while (count < 5) {
//   console.debug(count);
//   count++;
// }

// let count1 = 0;
// while (count1 !== 5) {
//   console.debug(count1);
//   count1 = count1 + 2;
// }

let films = ["Гарри Поттер", "Властелин колец", "Матрица"];

while (films.length > 0) {
  let film = films.pop();
  console.debug(`Вы смотрели фильм ${film}`);
}

console.debug(films); // Пустой массив, так как все фильмы были удалены методом pop() в цикле while

// Задача. Взять рандомного друга. Взять рандомный подарок. Получить строку Имя + Подарок
// Отработать каждого друга и подарки, чтобы каждому достался подарок
// Не исключает стрижку бороды для девочек и маникюр для мальчиков, так как это просто рандом

let friendsNames = ["Алексей", "Мария", "Иван", "Елена"];
let randomGifts = [
  "биляш",
  "айфон",
  "книга",
  "плюшевая игрушка",
  "сертификат на стрижку бороды",
  "сертификат на мникюр",
];

// Math.random() - дает от 0 до 1, не включая 1 количество чисел после запя
// Умножая на длину моассива (4 например) мы получаем от 0 до 4 не включая 4
// Math.floor() - округляет число вниз, так что мы получаем 0, 1, 2 или 3 для массива из 4 элементов)


while (friendsNames.length > 0) {
//   console.debug(Math.random())
  let friendIndex = Math.floor(Math.random() * friendsNames.length);
  let giftIndex = Math.floor(Math.random() * randomGifts.length);

  let friend = friendsNames[friendIndex];
  let gift = randomGifts[giftIndex];
  console.debug(`${friend} получил подарок: ${gift}`);

  // Удаляем друга и подарок из массивов, чтобы они не повторялись
  friendsNames.splice(friendIndex, 1);
  randomGifts.splice(giftIndex, 1);
}

