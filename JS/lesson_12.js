function changeColor() {
  let div = document.getElementById("redSquare");
  // Убираем класс "red" и добавляем класс "blue" через if
  if (div.classList.contains("red")) {
    div.classList.remove("red");
    div.classList.add("blue");
    console.debug("Цвет изменён на синий");
  } else {
    div.classList.remove("blue");
    div.classList.add("red");
    console.debug("Цвет изменён на красный");
  }
}

// Для работы со списком классов:
// Получить весь МАССИВ классов элемента: element.classList
// Проверить наличие класса: element.classList.contains("className") - метод массива contains
// Добавить класс: element.classList.add("className")
// Удалить класс: element.classList.remove("className")
// Метод classList специфический - toggle - переключатель класса: element.classList.toggle("className") - если класса нет, то добавляет, если есть - удаляет. Но в нашем случае мы не можем использовать toggle, так как нам нужно знать какой цвет был до изменения, чтобы вывести правильное сообщение в консоль. Поэтому мы используем if для проверки наличия класса и соответствующего изменения цвета.

function changeColor2() {
  let div = document.getElementById("greenSquare");
  // Работаем через тогл с классом green
  div.classList.toggle("green");
}

// Это обработчики событий мыши (обычно используются в JavaScript/React). Вот что каждый из них делает:

// - **onmousedown** — срабатывает, когда кнопка мыши **нажата** на элементе
// - **onmouseenter** — срабатывает, когда курсор **заходит** на элемент (не всплывает)
// - **onmouseleave** — срабатывает, когда курсор **покидает** элемент (не всплывает)
// - **onmousemove** — срабатывает при **движении** мыши над элементом
// - **onmouseout** — срабатывает, когда курсор **уходит** с элемента или его дочерних элементов (всплывает)
// - **onmouseover** — срабатывает, когда курсор **наводится** на элемент или его дочерние элементы (всплывает)
// - **onmouseup** — срабатывает, когда кнопка мыши **отпущена** над элементом
// - **onmousewheel** — срабатывает при **прокрутке** колёсика мыши (устарел, лучше использовать `onwheel`)

// **Основное отличие:**
// - `mouseenter`/`mouseleave` не всплывают (не срабатывают на дочерних элементах)
// - `mouseover`/`mouseout` всплывают

const square = document.querySelector(".square");

function squareOnClick() {
  console.debug("Событие квадрата: клик");
}
function squareOnMouseOver() {
  console.debug("Событие квадрата: наведение мыши");
}
function squareOnMouseOut() {
  console.debug("Событие квадрата: уход мыши");
}

// Обработчики событий - Listner
// Listener - это функция, которая будет вызвана при наступлении определённого события на элементе. Например, если мы хотим, чтобы при клике на квадрат выполнялась функция `squareOnClick`, то мы можем добавить её как слушатель события "click" на этот элемент. Это делается с помощью метода `addEventListener`:

// Основные методы для работы с событиями:
// - `addEventListener(event, handler)` — добавляет обработчик события к элементу
// - `removeEventListener(event, handler)` — удаляет обработчик события с элемента

// Популярные события:
// Полная загрузка документа - `DOMContentLoaded` — срабатывает, когда весь HTML был полностью загружен и обработан, без ожидания загрузки стилей, изображений и других ресурсов. Это событие полезно для выполнения кода, который должен работать с DOM сразу после его готовности.
// клик мыши - `click` — срабатывает при клике на элемент
// изменения в поле ввода - `input` — срабатывает при каждом изменении значения в поле ввода
// ввод данных в поле - `change` — срабатывает при изменении значения в поле ввода и потере фокуса

// ИЩЕМ ВСЕ ЭЛЕМЕНТЫ
const alertButton = document.getElementById("alertButton");

const alertParam1 = document.getElementById("alertParam1");
const alertParam2 = document.getElementById("alertParam2");
const alertParam3 = document.getElementById("alertParam3");
const currentMessageParam = document.getElementById("currentMessageParam");
// ТРИ ВАРИАНТА СООБЩЕНИЙ

const message1 = "Вариант 1. Привет мир!";
const message2 = "Вариант 2. События - это круто)!";
const message3 = "Вариант 3. Купи слона!";

let currentMessage = message1;

// Листнер, принемает в себя, и событие, функцию, которая должна быть запущена при наступлении этого события

function showAlert() {
  alert(currentMessage);
}

alertButton.addEventListener("click", showAlert);

// При загрузке докумнета, вписываем в параграф текущий вариант сообщения
document.addEventListener("DOMContentLoaded", () => {
  currentMessageParam.textContent = currentMessage;

  // ВОТ СЮДА
});

// PRACTICE
// Текущий результат — это то, что у вас грузится страница. Вы видите, что ваше текущее сообщение — вариант 1. И также при нажатии кнопки «Показать алерт» вы получаете алерт с текущим сообщением.

// Обработчики кнопок параметров

alertParam1.addEventListener("click", () => {
  currentMessage = message1;
  currentMessageParam.textContent = currentMessage;
});

alertParam2.addEventListener("click", () => {
  currentMessage = message2;
  currentMessageParam.textContent = currentMessage;
});

alertParam3.addEventListener("click", () => {
  currentMessage = message3;
  currentMessageParam.textContent = currentMessage;
});

const alertParam4 = document.getElementById("alertParam4");
const inputCustomMessage = document.getElementById("inputCustomMessage");

alertParam4.addEventListener("click", () => {
  currentMessage = inputCustomMessage.value;
  console.debug(inputCustomMessage)
  if (currentMessage.trim() === "") {
    currentMessage = "Пустое сообщение";
  }
  currentMessageParam.textContent = currentMessage;
});
