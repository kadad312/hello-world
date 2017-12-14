let myPlaces = ['one', 'two', 'three'];
let friendPlaces = ['four', 'five', 'three'];

for (let myPlacesIndex = 0; myPlacesIndex < myPlaces.length; myPlacesIndex++) {
    for (let friendPlacesIndex = 0; friendPlacesIndex < friendPlaces.length; friendPlacesIndex++) {
      if (myPlaces[myPlacesIndex]===friendPlaces[friendPlacesIndex]) {
        console.log(friendPlaces[friendPlacesIndex]);
      }
  };
}
