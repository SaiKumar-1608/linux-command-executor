const terminal = document.getElementById("terminal");
const input = document.getElementById("commandInput");

const API_URL = "http://localhost:8000/api/execute";

let history = [];
let historyIndex = -1;

/* -----------------------------
   Append output to terminal
------------------------------ */
function appendOutput(text, className = "output") {
    const div = document.createElement("div");
    div.className = className;
    div.textContent = text;
    terminal.appendChild(div);
    terminal.scrollTop = terminal.scrollHeight;
}

/* -----------------------------
   Clear terminal
------------------------------ */
function clearTerminal() {
    terminal.innerHTML = "";
}

/* -----------------------------
   Execute multi-line commands
------------------------------ */
async function executeCommand(commandBlock) {

    // Handle clear locally
    if (commandBlock.trim().toLowerCase() === "clear") {
        clearTerminal();
        return;
    }

    const commands = commandBlock.split("\n").filter(cmd => cmd.trim() !== "");

    for (let cmd of commands) {

        appendOutput(`$ ${cmd}`);

        const start = performance.now();

        try {
            const response = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ command: cmd })
            });

            const data = await response.json();
            const end = performance.now();
            const time = ((end - start) / 1000).toFixed(3);

            if (!response.ok) {
                appendOutput(`Blocked: ${data.detail}`, "error");
                appendOutput(`Executed in ${time}s`, "meta");
                continue;
            }

            appendOutput(data.output || "No output");
            appendOutput(`Executed in ${time}s`, "meta");

        } catch (err) {
            appendOutput("Unable to connect to backend", "error");
        }
    }
}

/* -----------------------------
   Keyboard Controls
------------------------------ */
input.addEventListener("keydown", (e) => {

    // Enter → Execute
    if (e.key === "Enter") {
        e.preventDefault();  // 🔥 Prevent new line in textarea

        const cmdBlock = input.value.trim();
        if (!cmdBlock) return;

        history.push(cmdBlock);
        historyIndex = history.length;

        executeCommand(cmdBlock);
        input.value = "";
    }

    // Arrow Up → History
    if (e.key === "ArrowUp") {
        if (historyIndex > 0) {
            historyIndex--;
            input.value = history[historyIndex];
        }
    }

    // Arrow Down → History
    if (e.key === "ArrowDown") {
        if (historyIndex < history.length - 1) {
            historyIndex++;
            input.value = history[historyIndex];
        } else {
            input.value = "";
        }
    }
});

/* -----------------------------
   Auto focus
------------------------------ */
window.onload = () => input.focus();