async function sendMessage() {
    const input = document.getElementById('user-input');
    const msg = input.value;
    if (!msg) return;
  
    const chatArea = document.getElementById('chat-area');
  
    // Display user message
    const userDiv = document.createElement('div');
    userDiv.className = 'user-msg';
    userDiv.innerText = msg;
    chatArea.appendChild(userDiv);
  
    input.value = "";
  
    // Send to backend
    const res = await fetch('http://127.0.0.1:8000/chat', {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg })
    });
  
    const data = await res.json();
  
    const botDiv = document.createElement('div');
    botDiv.className = 'bot-msg';
    botDiv.innerText = data.reply;
    chatArea.appendChild(botDiv);
  
    chatArea.scrollTop = chatArea.scrollHeight;
  }
  