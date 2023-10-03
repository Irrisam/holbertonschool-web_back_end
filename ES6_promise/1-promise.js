export default function getFullResponseFromAPI(success) {
    return new Promise((resolve, reject) => {
        if (success == True) {
            resolve({
                body: 'Success',
                status: 200
            }
            );
        } else {
            reject("The fake API is not working currently");
        }
    });
  }
  