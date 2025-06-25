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