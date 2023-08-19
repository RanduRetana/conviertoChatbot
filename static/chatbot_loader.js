(function () {
  function injectChatbotHTML() {
    const botName = window.chatbotName || 'Botberto';
    const chatbotHTML = `
      <div class="container">
        <div class="chatbox">
          <div class="chatbox__support">
            <div class="chatbox__header">
              <div class="chatbox__image--header">
                <img src="https://convierto.uc.r.appspot.com/static/images/logo.svg" alt="image">
              </div>
              <div class="chatbox__content--header">
                <h4 class="chatbox__heading--header">Tu amigo ${botName}</h4>
                <p class="chatbox__description--header">Platica con ${botName}!</p>
              </div>
            </div>
            <div class="chatbox__messages">
              <div></div>
            </div>
            <div class="chatbox__footer">
              <input type="text" placeholder="Write a message...">
              <button class="chatbox__send--footer send__button">Send</button>
            </div>
          </div>
          <div class="chatbox__button">
            <button><img src="/static/images/chatbox-icon.svg" /></button>
          </div>
        </div>
      </div>`;
    document.body.insertAdjacentHTML('beforeend', chatbotHTML);
  }

  function loadStylesheet(url) {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = url;
    document.head.appendChild(link);
  }

  function loadScript(url, callback) {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;
    script.async = true;
    script.onload = callback;
    document.head.appendChild(script);
  }

  function initializeChatbot() {
    var chatbotUrl = 'http://127.0.0.1:8080/'; // Reemplaza esto con la URL de tu servidor Flask.

    injectChatbotHTML();
    loadStylesheet(chatbotUrl + '/static/styles.css');

    // Agrega esta línea para pasar el ID del usuario al objeto chatbot
    window.chatbotUserId =
      typeof chatbotUserId !== 'undefined' ? chatbotUserId : null;

    // window.chatbot.empresaName =
    //   typeof window.empresaName !== 'undefined'
    //     ? window.empresaName
    //     : null;

    loadScript(chatbotUrl + '/static/app.js', function () {
      // Asegúrate de que app.js esté configurado para trabajar con la URL de tu servidor Flask.
      window.chatbot.serverUrl = chatbotUrl;
      setTimeout(function () {
        chatbox.open();
      }, 10000);
    });
  }

  initializeChatbot();
})();
