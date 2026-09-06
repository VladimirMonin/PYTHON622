// let potatos = [
//   "картошка",
//   "картошка",
//   "гнилая картошка",
//   "картошка",
//   "картошка",
// ];

for (let potato of potatos) {
  console.debug(potato);
}

// PRACTICE - работа с циклом for...of
// let potatos = [
//   "картошка",
//   "картошка",
//   "гнилая картошка",
//   "картошка",
//   "картошка",
// ];

// let goodPotatos = [];
// let badPotatos = [];

// for (let potato of potatos) {
//   if (potato === "гнилая картошка") {
//     badPotatos.push(potato);
//   } else {
//     goodPotatos.push(potato);
//   }
// }

// console.debug(`Хорошая картошка: ${goodPotatos}`);
// console.debug(`Гнилая картошка: ${badPotatos}`);

// Три способа увеличить счетчик на 1:
// Классический длинный способ
// Сокращенный способ добавить ЛЮБОЕ число
// ++ Это самый простой способ увеличить счетчик на 1
// rCounter = rCounter + 1;
// rCounter += 1;

// let someString = "БронетРанспортер";
// let rCounter = 0;

// for (let char of someString) {
//   if (char.toLowerCase() === "р") {
//     rCounter++;
//   }
// }

// console.debug(`Количество букв "р" в строке: ${rCounter}`);

// let badLetter = "р";
// let userWords = prompt("Введите слова через запятую без пробела").split(",");
// let badWordsThreshold = 1;

// let goodWords = [];
// let badWords = [];

// for (let word of userWords) {
//   console.debug(`Проверяем слово: ${word}`);
//   for (let char of word) {
//     console.debug(`Проверяем букву: ${char} в слове ${word}`);
//     if (char.toLowerCase() === badLetter) {
//       console.debug(`Найдена плохая буква "${badLetter}" в слове "${word}"`);
//     }
//   }
// }

let studentsTable = [
  ["Имя", "Возраст", "Группа"],
  ["Алексей", 20, "ПИ-19"],
  ["Мария", 22, "ПИ-18"],
  ["Иван", 21, "ПИ-19"],
];

let counter = 0;

for (let student of studentsTable) {
  if (counter === 0) {
    // console.debug(`Заголовки таблицы: ${student}`);
    counter++;
    continue; // Пропускаем итерацию для заголовков
  }
  console.debug(
    `Студент: ${student[0]}, Возраст: ${student[1]}, Группа: ${student[2]}`,
  );
  counter++;
}

// TODO - Разобрать операторы управления + двумерные массивы + простой рендер элементов