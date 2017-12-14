//Getter and setter methods allow you to process data before accessing or setting property values.

let person = {
  _name: 'Lu Xun',
  _age: 137,

  set age(newAge) {
    if (typeof(newAge) === 'number') {
      this._age = newAge;
      console.log(`${newAge} is valid input.`)
    } else {
      console.log(`Invalid input, change ${newAge} to a number`);
    }
  },

  get age() {
    console.log(`${this._name} is ${this._age} years old.`);
    	return this._age;
  }

};

person.age = 'Thirty-nine';

person.age = 39;

console.log(person);

console.log(person.age);
