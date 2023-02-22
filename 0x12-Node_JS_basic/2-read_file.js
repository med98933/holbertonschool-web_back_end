const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter(Boolean);
    const fields = {};
    let total = 0;

    for (const line of lines) {
      const student = line.split(',');
      const field = student[3];

      if (field in fields) {
        fields[field].push(student[0]);
      } else {
        fields[field] = [student[0]];
      }

      total++;
    }

    console.log(`Number of students: ${total}`);

    for (const field in fields) {
      const count = fields[field].length;
      const list = fields[field].join(', ');

      console.log(`Number of students in ${field}: ${count}. List: ${list}`);
    }
  } catch (err) {
    console.error(`Cannot load the database: ${err}`);
  }
}

module.exports = countStudents;
