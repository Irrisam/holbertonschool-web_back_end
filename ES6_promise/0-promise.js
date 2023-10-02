export default function getResponseFromAPI(True) {
  return new Promise((resolve, reject) => {
      if (True) {
          resolve("yay");
      } else {
          reject("ohhh nooo");
      }
  });
}
