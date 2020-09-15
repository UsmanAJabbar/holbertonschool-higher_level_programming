#!/usr/bin/node
// Lies and tries to convince you C's fun as many times as defined by the input
process.argv[2] !== undefined ? pinnochio(process.argv[2]) : console.log('Missing number of occurrences');

/**
 * pinnochio - prints out 'C is fun' as many
 * times as defined by the number being input
 * @number: number of times to print the specific
 * message
 * Return: None
 */
function pinnochio (number) {
  for (let i = 0; i < parseInt(number); i++) {
    console.log('C is fun');
  }
}
