var userQuestion = "What is your question?";
//var randomNumber = Math.floor(Math.random() * 7);
var eightBall = '';

switch(Math.floor(Math.random() * 7)) {
  case 0:
    eightBall = 'It is certain'
    break;
	case 1:
    eightBall = 'It is decidedly so'
    break;
  case 2:
    eightBall = 'Reply hazy try again'
    break;
  case 3:
    eightBall = 'Cannot predict now'
    break;
  case 4:
    eightBall = 'Don\'t count on it'
    break;
  case 5:
    eightBall = 'My sources say no'
    break;
  case 6:
    eightBall = 'Outlook not so good'
    break;
  default:
    eightBall = 'Signs point to yes'
}

console.log('The user asked: ' + userQuestion);
console.log('The eight ball answered: ' + eightBall);


    
