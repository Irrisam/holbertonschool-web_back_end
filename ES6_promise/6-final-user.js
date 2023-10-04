import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.allSettled([userPromise, photoPromise])
    .then((results) => {
      const fulfilledResults = results.filter((result) => result.status === 'fulfilled');
      const values = fulfilledResults.map((result) => result.value);

      return values;
    });
}
