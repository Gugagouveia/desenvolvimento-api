
fetch('http://localhost:5000.')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    
    console.error('Erro na requisição:', error);
  });
fetch('http://localhost:5000.', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ name: 'Guga', email: 'gustavoagjunior@fac.pe.senac.br' }),
})
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Erro na requisição:', error);
  });
