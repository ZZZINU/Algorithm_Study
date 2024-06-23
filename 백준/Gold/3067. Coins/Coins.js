// 3067번: Coins

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = parseInt(input[0]);

for (let i = 0; i < T * 3; i += 3) {
  const N = parseInt(input[i + 1]);
  const coins = input[i + 2].split(' ').map(Number);
  const amount = parseInt(input[i + 3]);

  const dp = Array(amount + 1).fill(0);
  dp[0] = 1;

  for (let j = 0; j < N; j++) {
    const coin = coins[j];
    for (let k = coin; k < amount + 1; k++) {
      dp[k] += dp[k - coin];
    }
  }

  console.log(dp[amount]);
}
