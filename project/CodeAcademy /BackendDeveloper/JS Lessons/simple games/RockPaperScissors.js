var userInput = 'bomb';
userInput = userInput.toLowerCase();

function getComputerChoice () {
  var number = Math.floor(Math.random()*3);
  switch (number) {
    case 0:
  		return 'rock';  
    case 1:
    	return 'paper'; 
    case 2:
    return 'scissors'; 
  }
}

function determineWinner (userChoice, computerChoice) {
  if (userChoice === computerChoice) {
    return 'The game is a tie';
  }
  if (userChoice === 'rock') {
    if (computerChoice === 'paper'){
      return 'Computer won';
    } else {
      return 'User won';
    }
  }
  if (userChoice === 'paper') {
    if (computerChoice === 'scissors'){
      return 'Computer won';
    } else {
      return 'User won';
    }
  } 
  if (userChoice === 'scissors') {
    if (computerChoice === 'rock'){
      return 'Computer won';
    } else {
      return 'User won';
    }
	}
  if (userChoice === 'bomb') {
      return 'User wins!';
  }
}

function playGame () {
  var userChoice = userInput;
  var computerChoice = getComputerChoice()
  console.log('User picked: ' + userChoice)
  console.log('Computer picked: ' +   computerChoice);
  console.log(determineWinner(userChoice, computerChoice))
}

playGame();



