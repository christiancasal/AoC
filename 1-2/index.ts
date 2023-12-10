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
let cornerCases = [
    {
        label: 'twone',
        value: 21
    },
    {
        label: 'eightwo',
        value: 82
    },
    {
        label: 'eighthree',
        value: 83
    },
    {
        label: 'nineight',
        value: 98
    },
]
let digitWord = [
	{
		label: 'one',
		value: 1
	},
	{
		label: 'two',
		value: 2
	},
	{
		label: 'three',
		value: 3
	},
	{
		label: 'four',
		value: 4
	},
	{
		label: 'five',
		value: 5
	},
	{
		label: 'six',
		value: 6
	},
	{
		label: 'seven',
		value: 7
	},
	{
		label: 'eight',
		value: 8
	},
	{
		label: 'nine',
		value: 9
	}
];

rl.on('line', (line) => {
	const result = digitReplacement(line)
    console.log('Replacement Result: ', result)
    
	const dayTwoSolution = dayOne(result)
	console.log(dayTwoSolution);
});

function dayOne(line) {
	const numberList = getNumbers(line)
    fs.appendFile('Output.txt', `\n${numberList} \n${line}`, (err) => {
        // In case of a error throw err.
        if (err) throw err;
    })
	summation += numberList
	return summation
}
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
	console.log(result)
	return Number(result)
}

function digitReplacement(line) {
    console.log('Original line: ', line)
    for (const corner of cornerCases) {
		if (line.includes(corner.label)) {
			line = line.replaceAll(corner.label, `${corner.value}`)
		}
	}
	for (const digit of digitWord) {
		if (line.includes(digit.label)) {
			line = line.replaceAll(digit.label, `${digit.value + digit.label}`)
		}
	}
	return line
}