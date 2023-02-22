const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      const lines = data.trim().split('\n');
      let fields = {};
      for (const line of lines) {
        const student = line.split(',');
        if (!fields[student[3]]) {
          fields[student[3]] = {
            count: 0,
            students: []
          };
        }
        if (student[0] !== '') {
          fields[student[3]].count += 1;
          fields[student[3]].students.push(student[0]);
        }
      }
      console.log(`Number of students: ${lines.length - 1}`);
      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          const studentsList = fields[field].students.join(', ');
          console.log(`Number of students in ${field}: ${fields[field].count}. List: ${studentsList}`);
        }
      }
      resolve();
    });
  });
}

module.exports = countStudents;
