export default function getListStudentIds(arr) {
  return arr.reduce((accumulator, x) => accumulator + x.id, 0);
}
