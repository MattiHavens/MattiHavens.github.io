function yourGuess() {
    // You can store references to the value and the 
    // guesses textarea in local function variables.
    var guess = document.getElementById("guess").value;
    var guesses = document.getElementById("output");

    // First, if the guess is the same, just show the answer.
    // Append onto the textarea the result.
    if (guess == numToGuess) {
        guesses.value = guesses.value + "\r" + "You are a genius and got it correct! ("+guess+")";
    } else if (guess > numToGuess) {
        guesses.value = guesses.value + "\r" + "You guessed too high! ("+guess+")";
    } else {
        guesses.value = guesses.value + "\r" + "You guessed too low! ("+guess+")";
    }
}
    
function showNumberToGuess() {
    // Show the randomly generated number if the onclick event
    // fires and the checkbox is check; otherwise, remove the
    // number and hide using display: none;.
    if (document.getElementById('cheat').checked) {
        document.getElementById('numberToGuess').value = numToGuess;
       
    } else {
        document.getElementById('numberToGuess').value = '';
      
    }
}
// (document.getElementById('cheat').checked) 
// Randomly generate a number
function generateNumberToGuess(confirmIt) {
    var guesses = document.getElementById("output");
    
    // First, confirm this is what we want if the confirmIt
    // argument was passed.
    if (confirmIt && !confirm('Restart game with new number?')) {
        return;
    }
    
    guesses.value = '';
    numToGuess = Math.floor(Math.random()*20);
    guesses.value = "New number generated.\n";
    
    // Don't forget to hide the new number.
    document.getElementById('numberToGuess').value = '';
   
}

function showGuesses(){
    var guesses = document.getElementById('guesses');
    var btn = document.getElementById('showguesses');
    
    if (guesses.style.display != 'block') {
        guesses.style.display = 'block';
        btn.value = 'Hide My Guesses';
    } else {
        guesses.style.display = 'none';
        btn.value = 'Show My Guesses';
    }
}

window.onload = function(){
    generateNumberToGuess();
}
