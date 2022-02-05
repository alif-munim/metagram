import io from "socket.io-client";

export const socketService = {
  connect,
};
//window.location.hostname
function connect() {
  return new Promise((resolve, reject) => {
    const socket = io('10.0.0.3:5000', {
      query: { token: JSON.parse(localStorage.getItem("user")).token },
    });
    socket.on("connect", () => {
      resolve(socket);
    });
  });
}
