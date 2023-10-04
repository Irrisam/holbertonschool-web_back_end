export default function cleanSet(paramSet, startString) {
  const returnString = [];
  const paramArray = Array.from(paramSet);
  if (startString !== '') {
    for (const item of paramArray) {
      if (item.startsWith(startString)) {
        returnString.push(item);
      }
    }
  }
  return returnString;
}
