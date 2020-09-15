#!/usr/bin/node
// Finds the second biggest in an array
!isNaN(process.argv[3]) ? console.log(second(process.argv.slice(2, process.argv.length))) : console.log(0);

/**
 * second - finds the second biggest
 * element in an array
 * @array: input array
 * Return: second largest array value
 */
function second (array) {
  const ints = [];

  // Ensure that all the elements in the array are integers
  for (let index = 0; index < array.length; index++) {
    ints.push(parseInt(array[index]));
  }

  return ints.sort().reverse()[1];
}
