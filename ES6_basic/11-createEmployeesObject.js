export default function createEmployeesObject(departmentName, employees) {
	let return_value = {}
	return_value[departmentName] = []
	for (const employee of employees) {
		return_value[departmentName].push(employee)
	}
  return return_value
}
