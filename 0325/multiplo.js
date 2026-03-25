function multiplo() {
    let n = prompt(message="Digite um número")
    n = parseInt(n)

    for (let i = 1; i <= 50; i++) {
        if (i % n == 0) {
            document.writeln("Múltiplo <br/>")
        }
        else {
            document.writeln(i + "<br/>")
        }
    }
}