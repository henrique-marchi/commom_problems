'use strict'
function containsSpecialChars(str) {
  const specialChars = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
  return specialChars.test(str);
}

function integerTest(number){
  if(Number.isInteger(parseInt(number))){
    return true
  }
}

async function get_cep(cep = document.getElementById('cep_input').value){
  if(containsSpecialChars(cep) == true){
    return alert('Special characters are not suported')
  }
  if(cep.length != 8){
    return alert('CEP must contain 8 digits')
  }
  if(integerTest(cep) != true){
    return alert('CEP must be only numbers')
  }
  fetch(`https://viacep.com.br/ws/${cep}/json/`)
    .then(response => response.json())
    .then(data => (
      document.getElementById("logradouro").value = (
        data['logradouro']
      ),
      document.getElementById("bairro").value = (
        data['bairro']
      ),
      document.getElementById("localidade").value = (
        data['localidade']
      ),
      document.getElementById("uf").value = (
        data['uf']
      )
      )
    )
}

function send(
  logradouro = document.getElementById('logradouro').value, 
  numero = document.getElementById('numero').value,
  bairro = document.getElementById('bairro').value, 
  cep = document.getElementById('cep_input').value,
  localidade = document.getElementById('localidade').value, 
  uf = document.getElementById('uf').value){
    if(logradouro == '' || numero == '' || bairro == '' || localidade == '' || uf == ''){
      return alert('All fields must be filled!')
    }
    return alert(
      `Object posted as: ${logradouro}, ${numero}, ${bairro}, ${localidade} - ${uf} / ${cep}.`
    )
}

async function get_cep_local(cep = document.getElementById('cep_input').value){
  console.log(cep)
  fetch(`http://127.0.0.1:8000/cep?cep=${cep}`)
  .then(response => response.json())
  .data(data => (
          console.log(data['logradouro']),
          document.getElementById("logradouro").value = (
            data['logradouro']
          ),
          document.getElementById("bairro").value = (
            data['bairro']
          ),
          document.getElementById("localidade").value = (
            data['localidade']
          ),
          document.getElementById("uf").value = (
            data['uf']
          )
  ))
}