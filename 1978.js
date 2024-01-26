const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

const is_prime = (num) => {
    if (num === 1) return false;
    for (let i = 2; i < num; i++) {
        if (num % i === 0)
            return false
    }

    return true;
}

let n, l;

readline.on('line', function(line) {
    if (!n) n = parseInt(line);
    else {
        l = line.split(' ').map((el) => parseInt(el));
    }
}).on('close', function(){ //이 안에 솔루션 코드 작성
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (is_prime(l[i])) count++;
    }
    console.log(count);
    process.exit();
});
