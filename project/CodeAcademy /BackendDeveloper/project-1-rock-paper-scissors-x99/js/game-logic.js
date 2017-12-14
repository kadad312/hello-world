// All code should be written in this file.

var userChoice = prompt('Do you choose rock, paper, or scissors?');
var computerChoice = Math.random();

console.log(computerChoice);

if (computerChoice < .33) {
 computerChoice = 'rock';
} else if (computerChoice < .66) {
 computerChoice = 'scissors';
} else computerChoice = 'paper';

console.log(computerChoice);


function compare(choice1, choice2) {
  if (choice1===choice2){
    return 'Result is a tie';
  }
  if (choice1==='rock'){
      if (choice2==='scissors') {
      return 'rock wins';
    } else {
      return 'paper wins';
    }
  }
  if (choice1==='scissors'){
      if (choice2==='rock') {
      return 'rock wins';
    } else {
      return 'scissors win';
    }
  }
  if (choice1==='paper'){
      if (choice2==='scissors') {
      return 'scissors win';
    } else {
      return 'paper wins';
    }
  }
}

console.log(compare(userChoice,computerChoice));
