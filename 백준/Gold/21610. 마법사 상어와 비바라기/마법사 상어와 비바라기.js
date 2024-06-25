// 21610번: 마법사 상어와 비바라기

const fs = require('fs');
//const input = fs.readFileSync('run/input.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const basket = [];
for (let i = 1; i < N + 1; i++) {
  basket.push(input[i].split(' ').map(Number));
}

//  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
// 0번째는 임의의 값 삽입
const dr = [0, 0, -1, -1, -1, 0, 1, 1, 1];
const dc = [0, -1, -1, 0, 1, 1, 1, 0, -1];

// 대각선 방향 배열 (↖, ↗, ↘, ↙)
const diag_dr = [-1, -1, 1, 1];
const diag_dc = [-1, 1, 1, -1];

let clouds = [
  [N - 2, 0],
  [N - 2, 1],
  [N - 1, 0],
  [N - 1, 1],
];

// console.log(clouds);

for (let i = 0; i < M; i++) {
  const [d, s] = input[N + 1 + i].split(' ').map(Number);
  const new_clouds = [];

  // 클라우드 이동
  for (let j = 0; j < clouds.length; j++) {
    const new_r = (clouds[j][0] + dr[d] * s + N * 50) % N; // N*50을 더해서 음수 방지
    const new_c = (clouds[j][1] + dc[d] * s + N * 50) % N; // N*50을 더해서 음수 방지
    new_clouds.push([new_r, new_c]);
  }

  clouds = new_clouds;

  //   console.log(new_clouds);
  //   console.log(basket);

  for (let j = 0; j < new_clouds.length; j++) {
    const r = new_clouds[j][0];
    const c = new_clouds[j][1];
    basket[r][c] += 1;
  }

  // 대각선 물 있는지 확인
  for (let j = 0; j < new_clouds.length; j++) {
    const r = new_clouds[j][0];
    const c = new_clouds[j][1];
    let water_count = 0;

    for (let k = 0; k < 4; k++) {
      const nr = r + diag_dr[k];
      const nc = c + diag_dc[k];

      if (nr >= 0 && nr < N && nc >= 0 && nc < N && basket[nr][nc] > 0) {
        water_count += 1;
      }
    }

    basket[r][c] += water_count;
  }

  const wasCloud = Array.from(Array(N), () => Array(N).fill(false));
  for (let j = 0; j < new_clouds.length; j++) {
    const [r, c] = new_clouds[j];
    wasCloud[r][c] = true;
  }

  // 새로운 구름 형성
  const new_generated_clouds = [];
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (basket[r][c] >= 2 && !wasCloud[r][c]) {
        new_generated_clouds.push([r, c]);
        basket[r][c] -= 2;
      }
    }
  }

  clouds = new_generated_clouds;
}

let result = 0;
for (let r = 0; r < N; r++) {
  for (let c = 0; c < N; c++) {
    result += basket[r][c];
  }
}

console.log(result);
