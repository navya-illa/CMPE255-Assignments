const test = require("node:test");
const assert = require("node:assert/strict");
const { createTask, escapeHtml } = require("./app.js");

test("createTask trims the title and applies the selected priority", () => {
  const task = createTask("  Submit assignment  ", "high");
  assert.equal(task.title, "Submit assignment");
  assert.equal(task.priority, "high");
  assert.equal(task.completed, false);
  assert.ok(task.id);
  assert.ok(task.createdAt);
});

test("createTask uses medium priority by default", () => {
  assert.equal(createTask("Read documentation").priority, "medium");
});

test("escapeHtml prevents markup from being inserted as HTML", () => {
  assert.equal(escapeHtml('<script>alert("x")</script>'), "&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;");
});
