// GPS 1.2 - JavaScript

// YOUR FULL NAMES:
//  1. Wil
//  2.


// 0. "YOU SIGNED... WHO?!"
var clintEastwood = {
  name: "Clint Eastwood",
  age: 84,
  quote: "Go ahead punk--make my day."
};


var pamelaAnderson = {
  name: "Pam Anderson",
  age: 48,
  quote: "That's marvelous!!"
};


// 1. "Here they Come!"

var clientList = [clintEastwood, pamelaAnderson];

var adamSandler = {
 name: "Adam Sandler",
 age: 47,
 quote: "That's your home! Are you too good for your home?"

};
clientList.push(adamSandler);

var kristenBell = {
  name: "Kristen Bell",
  age: 33,
  quote: "Do you want to build a snowman?"
};
clientList.push(kristenBell);

var JimCarrey = {
  name: "Jim Carrey",
  age: 52,
  quote: "So you are telling me there is a chance? YEAH"
};
clientList.push(kristenBell);





// 2. "TIME IS MONEY!"

//YOUR CODE HERE!

function Client(name, age, quote) {
  this.name = name;
  this.age = age;
  this.quote = quote;
}

var shooterMcGavin = new Client("Shooter McGavin", 48, "Just stay out of my way... or you'll pay. Listen to what I say.");
console.log(shooterMcGavin.constructor === Client);
console.log(shooterMcGavin.age === 48);
console.log(shooterMcGavin.quote === "Just stay out of my way... or you'll pay. Listen to what I say.");

// 3. "SHOW 'EM OFF!"

function print(actor) {
  console.log(actor.name )
}


// 4. "But wait, there's more!"



// 5.  ** BONUS **


//  6.  Your Reflection: