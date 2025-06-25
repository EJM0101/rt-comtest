const socket = io();

function startSimulation() {
  document.getElementById("log").innerHTML = "";
  const method = document.getElementById("method").value;
  socket.emit("start_simulation", { method: method });
}

socket.on("log_update", (msg) => {
  const item = document.createElement("li");
  item.className = "list-group-item";
  item.textContent = msg;
  document.getElementById("log").appendChild(item);
});

// Réception d'une bulle animée
socket.on("bubble", (msg) => {
  animateBubble(msg);
});

// Animation DOM
function animateBubble(content = "msg") {
  const bubble = document.getElementById("bubble");
  bubble.innerText = content;
  bubble.style.display = "block";
  bubble.style.left = "0px";

  let pos = 0;
  const interval = setInterval(() => {
    pos += 5;
    bubble.style.left = `${pos}px`;
    if (pos >= 350) {
      clearInterval(interval);
      setTimeout(() => {
        bubble.style.display = "none";
      }, 500);
    }
  }, 30);
}