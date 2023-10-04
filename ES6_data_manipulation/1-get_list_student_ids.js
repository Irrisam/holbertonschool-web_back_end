export default function getListStudentIds(param_array) {
    if (param_array instanceof Array) {
      const ids_array = param_array.map((students) => students.id);
      return ids_array;
    }
    return [];
  }