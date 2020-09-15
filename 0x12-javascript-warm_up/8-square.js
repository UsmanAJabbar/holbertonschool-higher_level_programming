#!/usr/bin/node
// Prints a square based off of the size defined by input
!isNaN(process.argv[2]) ? square(process.argv[2]) : console.log('Missing size');

/**
 * square - prints out a square
 * @sq_size: size of the square
 * Return: None
 */
function square (sq_size) {
  let buffer = '';
  const size = parseInt(sq_size);

  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      buffer += 'X';
    }
    i !== size - 1 ? buffer += '\n' : {};
  }
  console.log(buffer);
}
