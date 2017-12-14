let randomNumbers = [375, 200, 3.14, 7, 13, 852];

// Call .filter() on randomNumbers below
let smallNumbers = randomNumbers.filter(x => x < 250);

console.log(smallNumbers);

let favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];

let longFavoriteWords = favoriteWords.filter(function(word) {
  return word.length > 7;
});

console.log(longFavoriteWords);

// Refactor the code above using arrow function syntax

let longFavoriteWords2 = favoriteWords.filter(word => word.length > 7);

console.log(longFavoriteWords2);