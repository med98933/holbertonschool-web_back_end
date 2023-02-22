const http = require('http');
const { countStudents } = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;

const server = http.createServer((request, response) => {
  if (request.url === '/') {
    response.writeHead(200, { 'Content-Type': 'text/plain' });
    response.end('Hello Holberton School!\n');
  } else if (request.url === '/students') {
    response.writeHead(200, { 'Content-Type': 'text/plain' });
    countStudents(process.argv[2])
      .then(({ numberOfStudents, csStudents, sweStudents }) => {
        const message = `This is the list of our students\nNumber of students: ${numberOfStudents}\nNumber of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}\nNumber of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`;
        response.end(message);
      })
      .catch((err) => {
        response.end(`Error: ${err.message}`);
      });
  } else {
    response.writeHead(404, { 'Content-Type': 'text/plain' });
    response.end('Not found\n');
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = server;
