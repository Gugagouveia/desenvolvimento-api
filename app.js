document.addEventListener('DOMContentLoaded', () => {
    const messageElement = document.getElementById('message');
  
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('service-worker.js')
        .then(() => {
          messageElement.textContent = 'Service Worker registrado com sucesso!';
        })
        .catch((error) => {
          messageElement.textContent = 'Falha ao registrar o Service Worker: ' + error;
        });
    } else {
      messageElement.textContent = 'O seu navegador não suporta Service Worker.';
    }
  });
  
