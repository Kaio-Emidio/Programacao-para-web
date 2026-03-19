function ligardesligar () {
    if (document.getElementById('lampada').src == "https://www.w3schools.com/js/pic_bulboff.gif") {
        document.getElementById('lampada').src = "https://www.w3schools.com/js/pic_bulbon.gif"
    }
    else {
        document.getElementById('lampada').src = 'https://www.w3schools.com/js/pic_bulboff.gif'
    }
}