const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", (line) => {
  // 한 줄씩 입력받은 후 실행할 코드
  // 입력된 값은 line에 저장된다.
  input = line.split(" ").map((el) => parseInt(el));
  rl.close(); // 필수!! close가 없으면 입력을 무한히 받는다.
});
rl.on("close", () => {
  // 입력이 끝난 후 실행할 코드
  star(input[0]);
  process.exit();
});

function star(n) {
  for (i = 1; i <= n; i++) {
    let tmp = "";
    for (j = 1; j < i; j++) {
      tmp = tmp + " ";
    }
    for (k = 0; k <= n - i; k++) {
      tmp = tmp + "*";
    }
    console.log(tmp);
  }
}
