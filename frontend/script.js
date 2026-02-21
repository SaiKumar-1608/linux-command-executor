const terminal = document.getElementById("terminal");
const input = document.getElementById("commandInput");

const BASE_URL = "https://linux-command-executor-zupv.onrender.com";
const API_URL = `${BASE_URL}/api/execute`;
const HEALTH_URL = `${BASE_URL}/api/health`;

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
   Backend Health Check
------------------------------ */
async function checkBackendHealth() {
    try {
        const response = await fetch(HEALTH_URL);
        if (!response.ok) throw new Error("Health check failed");
        console.log("Backend is reachable");
    } catch (error) {
        appendOutput("⚠ Backend is unreachable. It may be sleeping (Render free tier).", "error");
    }
}

/* -----------------------------
   Execute multi-line commands
------------------------------ */
async function executeCommand(commandBlock) {

    if (commandBlock.trim().toLowerCase() === "clear") {
        clearTerminal();
        return;
    }

    const commands = commandBlock
        .split("\n")
        .map(cmd => cmd.trim())
        .filter(cmd => cmd !== "");

    for (let cmd of commands) {

        appendOutput(`$ ${cmd}`);

        const start = performance.now();

        try {
            const response = await fetch(API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ command: cmd })
            });

            const end = performance.now();
            const time = ((end - start) / 1000).toFixed(3);

            let data;

            try {
                data = await response.json();
            } catch {
                appendOutput("Invalid response from backend", "error");
                continue;
            }

            if (!response.ok) {
                appendOutput(`Blocked: ${data.detail || "Command not allowed"}`, "error");
                appendOutput(`Executed in ${time}s`, "meta");
                continue;
            }

            appendOutput(data.output || "No output");
            appendOutput(`Executed in ${time}s`, "meta");

        } catch (err) {
            appendOutput("Unable to connect to backend (Check CORS or server status)", "error");
        }
    }
}

/* -----------------------------
   Keyboard Controls
------------------------------ */
input.addEventListener("keydown", (e) => {

    // Enter → Execute
    if (e.key === "Enter") {
        e.preventDefault();

        const cmdBlock = input.value.trim();
        if (!cmdBlock) return;

        history.push(cmdBlock);
        historyIndex = history.length;

        executeCommand(cmdBlock);
        input.value = "";
    }

    // Arrow Up → History
    if (e.key === "ArrowUp") {
        e.preventDefault();
        if (historyIndex > 0) {
            historyIndex--;
            input.value = history[historyIndex];
        }
    }

    // Arrow Down → History
    if (e.key === "ArrowDown") {
        e.preventDefault();
        if (historyIndex < history.length - 1) {
            historyIndex++;
            input.value = history[historyIndex];
        } else {
            historyIndex = history.length;
            input.value = "";
        }
    }
});

/* -----------------------------
   Init
------------------------------ */
window.onload = () => {
    input.focus();
    checkBackendHealth();
};
