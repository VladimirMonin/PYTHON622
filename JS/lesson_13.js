console.debug("lesson 13 js подключен");

// СОБЫТИЯ ФОРМЫ

// change - срабатывает, когда элемент теряет фокус и его значение было изменено
// input - срабатывает при каждом изменении значения элемента
// focus - срабатывает, когда элемент получает фокус
// blur - срабатывает, когда элемент теряет фокус
// submit - срабатывает при отправке формы

const emailInput = document.getElementById("emailInput");
const loginForm = document.getElementById("loginForm");
console.debug(emailInput);
console.debug(loginForm);

// ВЕШАЕМ НА ЭЛЕМЕНТ СЛУШАТЕЛИ ВСЕХ СОБЫТИЙ КОТОРЫЕ НАМ НУЖНЫ

emailInput.addEventListener("focus", () => {
  console.debug("emailInput получил фокус");
});

emailInput.addEventListener("blur", () => {
  console.debug("emailInput потерял фокус");
});

emailInput.addEventListener("change", () => {
  console.debug(`emailInput событие change: ${emailInput.value}`);
});

emailInput.addEventListener("input", () => {
  console.debug(`emailInput событие input: ${emailInput.value}`);
});

loginForm.addEventListener("submit", (event) => {
  event.preventDefault();
  console.debug(event);
  console.debug("loginForm событие submit");
});

// ФУНКЦИЯ КОТОРАЯ ПРИНЕМАЕТ INPUT и переключает type между password и text
function togglePasswordVisibility(input) {
  if (input.type === "password") {
    input.type = "text";
  } else {
    input.type = "password";
  }
}

const showPasswordButton = document.getElementById("showPasswordButton");
const passwordInput = document.getElementById("passwordInput");

// Добавляем слушатель на кнопку, который при клике будет переключать видимость пароля
showPasswordButton.addEventListener("click", (event) => {
  event.preventDefault(); // Предотвращаем стандартное поведение кнопки (если она внутри формы)
  togglePasswordVisibility(passwordInput);
}); 