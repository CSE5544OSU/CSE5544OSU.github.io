/**
 * variables
 * var
 * let
 *  * Variables defined with let cannot be Redeclared.
 * Variables defined with let must be Declared before use.
 * Variables defined with let have Block Scope.
 * const
 *  * Variables defined with const cannot be Redeclared.
 * Variables defined with const cannot be Reassigned.
 * Variables defined with const have Block Scope.
 */

// var x = 1;
// var y = 2;

// let x = 1;
// let x = 2; //error

// {
//     let y = 3;
// }
// console.log(y);

// const x = 1;
// x = 2;
// {
//     const y = 3;
// }
// console.log(y);

/**
 * data types
 * string
 * number
 * boolen
 * object
 */

// var a = true;
// var b = 'hello';

/**
 * object data types
 * object
 * array
 */

// array
let a = [1, 2, 3, 4, 5];
a.pop();
a.push(6);

//object, name:values pairs
let course = {
    id: 5544,
    name: "Introduction to data visualization",
};
// accessing object properties
console.log(course.id);
console.log(course["id"]);

//array of object
var courses = [
    {
        id: 5544,
        name: "Introduction to data visualization",
    },
    {
        id: 5542,
        name: "Real time rendering"
    }
];
console.log(courses);
console.log(courses[0].id);

//manipulate DOM using JavaScript
document.getElementById("p1").style.backgroundColor = "lightblue";
document.getElementById("p1").innerHTML = "hello";

//debugging JS code

console.log();
var sum = 0;
for (let i = 0; i < 100; i++) {
    sum += i;
}
document.getElementById("p1").innerHTML = sum;
