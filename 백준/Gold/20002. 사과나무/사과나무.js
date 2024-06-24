// 20002번: 사과나무

// 입력
const fs = require('fs');
// const input = fs.readFileSync('run/input.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]); // 과수원의 크기

// 해당 나무를 수확했을 떄 얻을 수 있는 총 이익
const orchard = [];
for (let i = 0; i < N; i++) {
  orchard.push(input[i + 1].split(' ').map(Number));
}

// 누적합 저장
// 0행, 0열 생성 -> (1, 1)로 시작하기 위해서
const pre = Array.from({ length: N + 1 }, () => Array(N + 1).fill(0));

// 누적합을 구하는 부분 (1, 1) ~ (i, j) 저장
for (let i = 1; i < N + 1; i++) {
  for (let j = 1; j < N + 1; j++) {
    pre[i][j] =
      pre[i][j - 1] + pre[i - 1][j] - pre[i - 1][j - 1] + orchard[i - 1][j - 1];
  }
}

// 최대 총이익 초기화
max_result = pre[1][1];

// 시작점이 (i, j), 끝점이 (i+k, j+k)인 정사각형의 총 이익 구하기
// 정사각형 크기: k x k
for (let k = 0; k < N; k++) {
  for (let i = 1; i < N - k + 1; i++) {
    for (let j = 1; j < N - k + 1; j++) {
      result =
        pre[i + k][j + k] -
        pre[i - 1][j + k] -
        pre[i + k][j - 1] +
        pre[i - 1][j - 1];

      // 최대 총이익 업데이트
      max_result = Math.max(result, max_result);
    }
  }
}

// 최대 총이익 출력
console.log(max_result);
