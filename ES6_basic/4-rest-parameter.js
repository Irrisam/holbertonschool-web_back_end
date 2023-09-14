export default function returnHowManyArguments(...var_num) {
  let total = 0;
  for (const arg of var_num) {
    total += arg;
  }
  return total;
}