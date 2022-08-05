function cpf_generator(cpf){
    if (cpf.toString().length != 9){
        alert('CPF MUST HAVE ONLY NUMBERS WITHOUT THE 2 VERIFICATION DIGITS')
    }
    
    let number_weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    let splited_cpf = Array.from(cpf.toString()).map(Number)
    let multiply1 = []

    for(let i = 0; i < cpf.toString().length; i++){
        console.log(splited_cpf[i], number_weights[i], multiply1[i])
        multiply1[i] += splited_cpf[i] * number_weights[i]
    }
    
    let sum1 = 

    console.log(multiply1)
}

cpf_generator(467692098)