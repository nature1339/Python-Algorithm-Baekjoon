let number = 5;  //전역 변수

function search() {  //함수 선언
  let number = 3; //지역 변수
  //
  //
  //
  //
  console.log(number);
}
// console.log(number);
//함수 호출(실행)
// search();



function mult2(a) {
  return a*2;
}

console.log(mult2(8));  //매개변수, 인수, 인자, parameter, argument

let multCopy = mult2(2); //호출
let multCopy2 = mult2;   //값
console.log(multCopy);
console.log(multCopy2);

let a = 14

//함수 표현식
let example = function() {  //익명 함수
  console.log("example");
}
example();

//화살표 함수
let arrow = (a) => {
  console.log("arrow");
}