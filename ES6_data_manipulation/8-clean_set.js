export default function cleanSet(paramSet, startString) {
  const returnString = [];
  const paramArray = Array.from(paramSet);
  if (startString !== '') {
    for (const item of paramArray) {
        if (item.startsWith(startString)){
        const withoutStart = item.substring(startString.length);
        returnString.push(withoutStart.split('-').join(''));
    }
}
}
  return returnString;
}
