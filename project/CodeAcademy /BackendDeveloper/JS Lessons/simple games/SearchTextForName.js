/*jshint multistr:true */

var text = 'Lorem ipsum dolor sit amet, massa pellentesque dictum est ad libero, velit sed leo, lacus vitae nunc aliquam, hendrerit urna. Erat Khaled tempus aptent mattis aptent semper class, nulla adipiscing non sed eros wisi sem, purus et cras dolor et, nunc nullam senectus mollitia nulla. Fringilla suspendisse lectus ipsum torquent, auctor eget, luctus condimentum dolor, Khaled a tellus rhoncus, in consectetuer adipiscing etiam placerat in.' ;

var myName = 'Khaled';
var hits = [];

for (var i = 0; i < text.length; i++) {
    if (text[i] === myName[0]) {
        for (var j = i; j < i + myName.length; j++) {
            hits.push(text[j]);
        }
    }
}
if (hits === 0) {
    console.log('Your name wasn\'t found');
} else {
    console.log(hits);
}