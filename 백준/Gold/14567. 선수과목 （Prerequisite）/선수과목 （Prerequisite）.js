const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);

const subjects_semester = Array.from({ length: N + 1 }, () => 1);

const subjects = [];

for (let i = 1; i < M + 1; i++) {
  const [prerequisite, requisite] = input[i].split(' ').map(Number);
  subjects.push([prerequisite, requisite]);
}

subjects.sort((a, b) => a[1] - b[1]);

for (const subject of subjects) {
  const [prerequisite, requisite] = subject;
  subjects_semester[requisite] = Math.max(
    subjects_semester[prerequisite] + 1,
    subjects_semester[requisite]
  );
}

for (let i = 1; i < N + 1; i++) {
  process.stdout.write(subjects_semester[i] + ' ');
}
