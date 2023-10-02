function getResponseFromAPI(yes) {
    return new Promise((resolve, reject) => {
        if (yes) {
            resolve();
        } else {
            reject();
        }
    });
}

getResponseFromAPI(true)
    .then(() => {
        console.log("Yup");
    })
    .catch(() => {
        console.log("Nope");
    });
