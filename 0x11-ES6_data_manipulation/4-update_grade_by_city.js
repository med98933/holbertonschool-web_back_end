export default function getStudentsByLocation(arr, c, grad) {
  return arr
    .filter((x) => x.location === c)
    .map((student) => {
      const gradeI = grad
        .filter((x) => x.studentId === student.id)
        .map((x) => x.grade)[0];
      const grade = gradeI || 'N/A';
      return { ...student, grade };
    });
}
