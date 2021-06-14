export default function appendToEachArrayValue(array, appendString) {
  const indx = [];
  for (const value of array) {
    indx.push(appendString + value);
  }

  return indx;
}
