console.debug("Файл 14_1.js подключен");

// Кнопки ищем для логики
const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");

// Элементы ищем для назначения стилей
const h1Header = document.querySelector("h1");
const pArray = document.querySelectorAll("p");
const buttonArray = [button1, button2];

// Дефолтное значение темы
let carrentTheme = "light";

// Мэппинг тема - элементы - классы
const lightThemeMapping = {
  h1: ["light_text"],
  p: ["light_text"],
  button: ["light_button"],
};

// Мэппинг тема - элементы - классы
const darkThemeMapping = {
  h1: ["dark_text"],
  p: ["dark_text"],
  button: ["dark_button"],
};

// Функция принимает объект мэппинга и назначает его тему по тегам
function setThemeByMapObj(mapObj) {
  // Устанавливаем через classList
  h1Header.classList = mapObj.h1;
  pArray.forEach((item) => (item.classList = mapObj.p));
  buttonArray.forEach((item) => (item.classList = mapObj.button));
}

// Вешаем листнер на кнопки - чтобы менять темы
button1.addEventListener("click", function () {
  setThemeByMapObj(lightThemeMapping);
});

button2.addEventListener("click", function () {
  setThemeByMapObj(darkThemeMapping);
});
