#!/usr/bin/node
// Finds the factorial of a number
!isNaN(process.argv[2]) ? console.log(factorial(process.argv[2])) : console.log(1);

/**
 * factorial - finds the factorial of a specific number
 * @number: number that needs its factorial to be found
 * Return: None
 */
function factorial (number) {
  if (number <= 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
