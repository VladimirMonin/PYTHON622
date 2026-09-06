console.debug("Файл lesson_13_1.js загружен");

const taskInput = document.getElementById("taskInput");
const unDoneContainer = document.querySelector(".unDoneContainer");
const doneContainer = document.querySelector(".doneContainer");
const addTaskButton = document.getElementById("addTaskButton");

function createCheckbox() {
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.addEventListener("change", function () {
    const taskElement = checkbox.parentElement;
    if (checkbox.checked) {
      taskElement.classList.remove("taskUndone");
      taskElement.classList.add("taskDone");
    //   Перемещаем задачу в контейнер выполненных задач
        doneContainer.appendChild(taskElement);
    } else {
      taskElement.classList.remove("taskDone");
      taskElement.classList.add("taskUndone");
    //   Перемещаем задачу обратно в контейнер невыполненных задач
        unDoneContainer.appendChild(taskElement);
    }
  });
  return checkbox;
}

function addTask() {
  // Добываем текст задачи и проверяем его на пустоту
  const taskText = taskInput.value.trim();
  if (taskText === "") {
    alert("Пожалуйста, введите задачу.");
    return;
  }
  // Создаем элемент для задачи и добавляем его в контейнер
  const taskElement = document.createElement("div");
  //   taskElement.className = "task";
  taskElement.classList.add("task", "taskUndone");
  console.debug(taskElement.classList)
  const taskHeader = document.createElement("h3");
  taskHeader.textContent = taskText;
  taskElement.appendChild(taskHeader);
  unDoneContainer.appendChild(taskElement);
  // Очищаем поле ввода
  taskInput.value = "";

  // Создаем чекбокс для отметки задачи как выполненной
  const checkbox = createCheckbox();
  taskElement.appendChild(checkbox);
}


addTaskButton.addEventListener("click", addTask);
