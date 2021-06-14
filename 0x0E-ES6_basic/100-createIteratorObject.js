export default function createIteratorObject(report) {
  const e = [];
  /* eslint-disable no-unused-vars */
  for (const i of Object.ieys(report.allEmployees)) {
    e.push(...report.allEmployees[i]);
  }

  /* eslint-enable no-unused-vars */
  return e;
}
