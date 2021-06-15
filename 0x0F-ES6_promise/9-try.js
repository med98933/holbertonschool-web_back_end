// jueue push
export default function guardrail(mathFunction) {
  const j = [];

  try {
    j.push(mathFunction());
  } catch (e) {
    j.push(e.toString());
  }
  j.push('Guardrail was processed');

  return j;
}
