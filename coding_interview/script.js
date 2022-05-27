// 1. Coding interview FizzBuzz

// for loop
// for (let i = 1; i < 101; i++) {
//   if (i % 15 === 0) {
//     console.log('FIZZ BUZZ');
//   } else if (i % 3 === 0) {
//     console.log('FIZZ');
//   } else if (i % 5 === 0) {
//     console.log('BUZZ');
//   } else {
//     console.log(i);
//   }
// }

// while loop
// let i = 0;

// while (i < 100) {
//   i++;

//   if (i % 15 === 0) {
//     console.log('Fizz Buzz');
//   } else if (i % 3 === 0) {
//     console.log('Fizz');
//   } else if (i % 5 === 0) {
//     console.log('Buzz');
//   } else {
//     console.log(i);
//   }
// }

// do while loop
let i = 1;

do {
  if (i % 15 === 0) {
    console.log('FizzBuzz');
  } else if (i % 3 === 0) {
    console.log('Fizz');
  } else if (i % 5 === 0) {
    console.log('Buzz');
  } else {
    console.log(i);
  }
  i++;
} while (i < 101);
