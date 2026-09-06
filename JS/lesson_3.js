// Lesson 3 - Серия IF, ELSE IF, ELSE

// МЕТОДЫ И ОСНОВНЫЕ СВОЙСТВА СТРОК
// String.length - возвращает количество символов в строке
// String.toUpperCase() - возвращает строку, преобразованную в верхний регистр
// String.toLowerCase() - возвращает строку, преобразованную в нижний регистр
// String.trim() - возвращает строку с удаленными пробелами в начале и в конце строки
// String.includes(substring) - возвращает true, если строка содержит подстроку substring, и false в противном случае
// String.startsWith(substring) - возвращает true, если строка начинается с подстроки substring, и false в противном случае
// String.endsWith(substring) - возвращает true, если строка заканчивается на подстроку substring, и false в противном случае
// String.indexOf(substring) - возвращает индекс первого вхождения подстроки substring в строку, или -1, если подстрока не найдена
// String.slice(startIndex, endIndex) - возвращает часть строки от startIndex до endIndex (не включая endIndex)
// String.splice(startIndex, deleteCount, newSubstring) - удаляет deleteCount символов из строки, начиная с startIndex, и вставляет newSubstring на их место. Возвращает удаленные символы в виде новой строки
// String.replace(searchValue, newValue) - возвращает новую строку, в которой первое вхождение searchValue заменено на newValue
// String.replaceAll(searchValue, newValue) - возвращает новую строку, в которой все вхождения searchValue заменены на newValue

// Пример работы с методом
let sampleString1 = "  ПрИвЕт мИр!  ";
console.debug("Длина строки sampleString1:", sampleString1.length);
console.debug(
  "Строка sampleString1 в верхнем регистре:",
  sampleString1.toUpperCase(),
);
console.debug(
  "Строка sampleString1 в нижнем регистре:",
  sampleString1.toLowerCase(),
);
console.debug(
  "Строка sampleString1 с удаленными пробелами в начале и в конце:",
  sampleString1.trim(),
);

// Методы можно вызывать цепочкой, то есть один за другим
console.debug(
  "Строка sampleString1 в верхнем регистре и с удаленными пробелами в начале и в конце:",
  sampleString1.toUpperCase().trim(),
);

// Методы строк с аргумнетами
// replace() и replaceAll() - возвращают новую строку, в которой первое или все вхождения searchValue заменены на newValue
let someString2 = "Мама Мыла Раму";

console.debug(
  "Заменим мыла на ела в строке someString2:",
  someString2.replace("Мыла", "Ела"),
);

// Вызов 2х методов цепочкой с демонстрацией логической ошибки
console.debug(
  "Заменим Мыла на Ела ПОСЛЕ toLowerCase() в строке someString2:",
  someString2.toLowerCase().replace("Мыла", "Ела"),
);

// Изменим на правильный порядок методов, чтобы избежать логической ошибки
console.debug(
  "Заменим Мыла на Ела ПЕРЕД toLowerCase() в строке someString2:",
  someString2.replace("Мыла", "Ела").toLowerCase(),
);

// Строки НЕ ИЗМЕНЯЕМЫ. Методы строк возвращают новую строку, а не изменяют существующую строку. Поэтому, если мы хотим сохранить результат метода, мы должны присвоить его новой переменной или перезаписать существующую переменную.
let someString3 = someString2.replace("Мыла", "Ела").toLowerCase();

// Строка - упорядоченная неизменяемая коллекция символов.
// Получим первую букву строки someString3 с помощью индекса 0
console.debug("Первая буква строки someString3:", someString3[0]);
// someString3[0] = "Д"; // Строки неизменяемые, поэтому эта операция не изменит строку someString3

// Мы можем без проблем получить всю строку по буквам. Начиная с индекса 0 и заканчивая индексом, который равен длине строки минус 1
console.debug("Строка someString3 по буквам:");
console.debug(someString3[0]);
console.debug(someString3[1]);
console.debug(someString3[2]); // ...

// String.length
//  String.includes(substring)
//  String.indexOf(substring)

// Проверка длины строки
let userName = prompt("Введите ваше имя");
console.debug("Длина строки userName:", userName.length);

// Проверка на вхождение буквы р в строку userName
if (userName.includes("р")) {
  console.debug("В вашем имени есть буква р");
}

// Первая буква р в строке userName
console.debug(
  "Индекс первой буквы р в строке userName:",
  userName.indexOf("р"),
);

// ПРАВИЛЬНЫЙ ВАРИАНТ!

// Проверка длины строки
let userName2 = prompt("Введите ваше имя");

// Проверка на пустую строку
if (userName2.trim() === "") {
  console.error("Вы не ввели имя. Попробуйте еще раз");
}

let optimizedUserName2 = userName2.toLowerCase().trim();

console.debug("Длина строки userName2:", optimizedUserName2.length);

// Проверка на вхождение буквы р в строку userName2
if (optimizedUserName2.includes("р")) {
  console.debug("В вашем имени есть буква р");

  // Первая буква р в строке userName2
  console.debug(
    `Индекс первой буквы р в строке userName2: ${optimizedUserName2.indexOf("р")}`,
    `Номер буквы р в строке userName2: ${optimizedUserName2.indexOf("р") + 1}`,
  );
} else {
  console.debug(`В имени ${userName2} нет буквы р`);
}

// String.slice(startIndex, endIndex) - возвращает часть строки от startIndex до endIndex (не включая endIndex)
// String.splice(startIndex, deleteCount, newSubstring) - удаляет deleteCount символов

// Начнем со slice()
// Метод slice() возвращает часть строки от startIndex до endIndex (не включая endIndex)
//

let dinnerString = "Колбаска, сырок, хлебушек";
// КОЛБАСКА
// Ищем начало колбаски
let sausageStartIndex = dinnerString.indexOf("Колбаска");
console.debug("Начало колбаски:", sausageStartIndex);

// Ищем конец колбаски
let sausageEndIndex = sausageStartIndex + "Колбаска".length; // 0 + 8 = 8

// Добываем колбаску с помощью slice()
let sausage = dinnerString.slice(sausageStartIndex, sausageEndIndex);
console.debug(`Добытая колбаска: ${sausage.toLowerCase() === "колбаска"}`); // Сравниваем добытую колбаску с эталонным словом "колбаска" в нижнем регистре, чтобы избежать проблем с регистром букв

// СЫРОК
// Ищем начало сырка
let cheeseStartIndex = dinnerString.indexOf("сырок");
console.debug("Начало сырка:", cheeseStartIndex);

// Ищем конец сырка
let cheeseEndIndex = cheeseStartIndex + "сырок".length; // 9 + 5 = 14

// Добываем сырок с помощью slice()
let cheese = dinnerString.slice(cheeseStartIndex, cheeseEndIndex);
console.debug(`Добытый сырок: ${cheese.toLowerCase() === "сырок"}`); 

// ХЛЕБУШЕК
// Ищем начало хлебушка
let breadStartIndex = dinnerString.indexOf("хлебушек");
console.debug("Начало хлебушка:", breadStartIndex);

// Ищем конец хлебушка
let breadEndIndex = breadStartIndex + "хлебушек".length; // 15 + 8 = 23

// Добываем хлебушек с помощью slice()
let bread = dinnerString.slice(breadStartIndex, breadEndIndex);
console.debug(`Добытый хлебушек: ${bread.toLowerCase() === "хлебушек"}`);

// TODO - splice() !

// PRACTICE - фывафывафыа