/* 
    PSUEDOCODE
    1. get data from file
    2. iterate over each line
    3. one fx to get first number
    4. one fx to get the second number
    5. concat the two numbers
    6. push the result to an array
    7. when all lines are done, sum the array
*/

const fs = require('fs');
const readline = require('readline');
const filePath = 'data.txt';

// Create a readable stream for the file
const fileStream = fs.createReadStream(filePath);

// Create a readline interface
const rl = readline.createInterface({
  input: fileStream,
  crlfDelay: Infinity // Detects all line endings
});

let summation = 0;

rl.on('line', (line) => {
    const numberList = getNumbers(line)
    summation += numberList
    console.log(summation)
});

function getNumbers(line) {
    const bucket = []

    for (const char of line) {
        if (Number(char)) {
            bucket.push(char)
        }
    }

    const firstNumber = bucket[0]
    const lastNumber = bucket[bucket.length - 1]

    const result = firstNumber + lastNumber
    
    return Number(result)
}
