let day = 'Wednesday';
let alarm;

let person =
    {
      name: 'Khaled',
      age: 25,
      weekendAlarm: 'No alarms needed',
      weekAlarm: 'Alarm set to 7AM',
      sayHello() {return `Hello, my name is ${this.name}`;},
      sayGoodbye() {return 'Goodbye!';}
    };

if (day === 'Saturday' || day === 'Sunday') {
  alarm = 'weekendAlarm';
} else {
  alarm = 'weekAlarm';
}

console.log(person['name']);
console.log(person['age']);
console.log(person[alarm]);

person.hobbies = ['coding', 'lifting'];
person.hobbies = ['coding'];
console.log(person.hobbies);


console.log(person.sayHello());

console.log(person.sayGoodbye());

let friend = {name: 'Gabriel'};
friend.sayHello = person.sayHello;

console.log(friend.sayHello());
