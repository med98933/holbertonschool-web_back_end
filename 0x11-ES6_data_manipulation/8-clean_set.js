export default function cleanSet(set, startString) {
  let r = '';
  if (!startString || !startString.length) return r;
  set.forEach((x) => {
    if (x && x.startsWith(startString)) r += `${x.slice(startString.length)}-`;
  });
  return r.slice(0, r.length - 1);
}
