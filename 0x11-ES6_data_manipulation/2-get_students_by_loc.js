export default function getStudentsByLocation(array, c) {
  return array.filter((sum) => sum.location === c);
}
