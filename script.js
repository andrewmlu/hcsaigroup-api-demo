document.getElementById("chatForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const userInput = document.getElementById("userInput");
    const response = document.getElementById("response");
    const message = userInput.value.trim();
    if (message) {
        const APIResponse = await sendMessageToAPI(message);
        response.innerText = APIResponse;
    }
});

async function sendMessageToAPI(message) {
    const response = await fetch('http://127.0.0.1:3000/api/chat/claude', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: message }),
    });
    if (response.ok) {
        const json = await response.json();
        return json.response;
    } else {
        throw new Error("Unable to reach the API.");
    }
}