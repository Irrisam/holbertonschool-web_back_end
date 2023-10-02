export default function getResponseFromAPI(Success) {
    return new Promise((resolve, reject) => {
        if (Success == True) {
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
  