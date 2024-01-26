// # 소수 판별
// # n이 소수인지 아닌지 판별 -> i = 2 ~ (n - 1) -> n % i != 0

// # 7 % 2 = 1
// # 7 % 3 = 1
// # 7 % 4 = 3
// # 7 % 5 = 2
// # 7 % 6 = 1

// #4
// # 1 3 5 7

// # 소수 조건: 2 ~ (n-1)까지의 모든 i에 대해서 n % i != 0이면 n은 소수이다 .
// # 2 ~ (n-1)까지의 i에 대해서 하나라도 n % i == 0이면 n은 소수가 아니다.

// # true && true && true -> true
// # true && false && true -> false

// # n <- 7

// # 4
// # 1 3 5 7

// # n = 9
// # 9 % 2 == 1
// # 9 % 3 == 0 => False 반환 => 함수 끝

// # is_prime(1) -> False
// # is_prime(3) -> True
// # is_prime(5) -> True
// # is_prime(7) -> True

// n = int(input()); // # 4
// l = map(int, input().split()); // # [1, 3, 5, 7]

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

/**
 * 4
 * 1 3 5 7
 */
let n = parseInt(input[0]);
let l = input[1].split(" ").map((item) => parseInt(item));

// def is_prime(num):
//     if num == 1:
//         return False

//     for i in range(2, n): // 2~n-1
//         if num % i == 0:
//             return False // # 나머지가 0이면 소수가 아니다
// // #------------------------------
//     return True

function is_prime(num) {
  /**
   * for (초기식; 조건식(참, 거짓); 증감식) {
   *  ...
   * }
   *
   * if -> 조건식을 다루기 위한 키워드
   */
  if (num == 1) {
    return false;
  }

  for (let i = 2; i < n; i++) {
    if (num % i == 0) {
      return false;
    }
  }

  return true;
}

// count = 0
// for i in range(0, n):
//     if is_prime(l[i]):
//         count += 1

// print(count)

/**
 * if (조건식 -> 참, 거짓) {
 *    조건식이 참일 경우에 실행
 * }
 */
let count = 0;
for (let i = 0; i < n; i++) {
  if (is_prime(l[i])) {
    // is_prime(l[i])함수는 true이면 count 1더한다.
    count += 1;
  }
}

console.log(count);
