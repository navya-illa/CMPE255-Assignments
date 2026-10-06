const STORAGE_KEY = "focuslist.tasks.v1";

let tasks = loadTasks();
let activeFilter = "all";

const elements = typeof document === "undefined" ? {} : {
  form: document.querySelector("#taskForm"),
  input: document.querySelector("#taskInput"),
  priority: document.querySelector("#priorityInput"),
  list: document.querySelector("#taskList"),
  empty: document.querySelector("#emptyState"),
  progressText: document.querySelector("#progressText"),
  progressPercent: document.querySelector("#progressPercent"),
  progressRing: document.querySelector(".progress-ring"),
  clearCompleted: document.querySelector("#clearCompleted"),
  themeToggle: document.querySelector("#themeToggle")
};

function createTask(title, priority = "medium") {
  return {
    id: crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`,
    title: title.trim(),
    priority,
    completed: false,
    createdAt: new Date().toISOString()
  };
}

function loadTasks() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    return Array.isArray(saved) ? saved : [];
  } catch {
    return [];
  }
}

function saveTasks() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

function filteredTasks() {
  if (activeFilter === "active") return tasks.filter((task) => !task.completed);
  if (activeFilter === "completed") return tasks.filter((task) => task.completed);
  return tasks;
}

function render() {
  const visibleTasks = filteredTasks();
  elements.list.innerHTML = visibleTasks.map(taskTemplate).join("");
  elements.empty.hidden = visibleTasks.length > 0;

  const completed = tasks.filter((task) => task.completed).length;
  const total = tasks.length;
  const percent = total ? Math.round((completed / total) * 100) : 0;
  elements.progressText.textContent = `${completed} of ${total} completed`;
  elements.progressPercent.textContent = `${percent}%`;
  elements.progressRing.style.setProperty("--progress", `${percent}%`);
}

function taskTemplate(task) {
  const date = new Date(task.createdAt).toLocaleDateString(undefined, { month: "short", day: "numeric" });
  return `<article class="task-item ${task.completed ? "completed" : ""}" data-id="${escapeHtml(task.id)}">
    <input class="task-check" type="checkbox" ${task.completed ? "checked" : ""} aria-label="Mark ${escapeHtml(task.title)} complete" />
    <div class="task-content"><div class="task-title">${escapeHtml(task.title)}</div><div class="task-meta">Added ${date}</div></div>
    <span class="priority priority-${task.priority}">${task.priority}</span>
    <div class="task-actions"><button class="action-button edit-task" type="button" aria-label="Edit task">✎</button><button class="action-button delete-task" type="button" aria-label="Delete task">×</button></div>
  </article>`;
}

function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, (character) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[character]));
}

function taskById(id) {
  return tasks.find((task) => task.id === id);
}

if (typeof document !== "undefined") {
elements.form.addEventListener("submit", (event) => {
  event.preventDefault();
  const title = elements.input.value.trim();
  if (!title) return;
  tasks.unshift(createTask(title, elements.priority.value));
  saveTasks();
  elements.form.reset();
  elements.priority.value = "medium";
  render();
  elements.input.focus();
});

elements.list.addEventListener("click", (event) => {
  const item = event.target.closest(".task-item");
  if (!item) return;
  const task = taskById(item.dataset.id);
  if (!task) return;

  if (event.target.matches(".task-check")) task.completed = event.target.checked;
  if (event.target.matches(".delete-task")) tasks = tasks.filter((candidate) => candidate.id !== task.id);
  if (event.target.matches(".edit-task")) {
    const updatedTitle = window.prompt("Update task", task.title)?.trim();
    if (updatedTitle) task.title = updatedTitle;
  }
  saveTasks();
  render();
});

document.querySelectorAll(".filter-button").forEach((button) => {
  button.addEventListener("click", () => {
    activeFilter = button.dataset.filter;
    document.querySelectorAll(".filter-button").forEach((candidate) => candidate.classList.toggle("active", candidate === button));
    render();
  });
});

elements.clearCompleted.addEventListener("click", () => {
  tasks = tasks.filter((task) => !task.completed);
  saveTasks();
  render();
});

elements.themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  localStorage.setItem("focuslist.darkMode", document.body.classList.contains("dark"));
});

if (localStorage.getItem("focuslist.darkMode") === "true") document.body.classList.add("dark");
render();
}

if (typeof module !== "undefined") module.exports = { createTask, filteredTasks, escapeHtml };
