#!/usr/bin/node
// Adds two numbers
console.log(add(process.argv[2], process.argv[3]));

/**
 * add - adds two numbers
 * num1 - first number
 * num2 - second number
 * Return: None
 */
function add (num1, num2) {
  return parseInt(num1) + parseInt(num2);
}
