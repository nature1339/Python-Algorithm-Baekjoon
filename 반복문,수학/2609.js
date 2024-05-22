const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

const gcd = (a, b) => {
    if (b === 0) return a;
    return gcd(b, a % b);
}

let a, b;


readline.on('line', function(line) {
    [a, b] = line.split(' ').map((el) => parseInt(el));
}).on('close', function(){ //이 안에 솔루션 코드 작성
    const maximum = gcd(a, b);
    const minimum = a * b / maximum;

    console.log(maximum);
    console.log(minimum);

    process.exit();
});