export default function hasValuesFromArray(s, array) {
  return array.every((x) => s.has(x));
}
