import { createUser } from './5-photo-reject';
import { signUpUser } from './4-user-promise';

export default function handleProfileSignup(firstName, lastName, fileName) {
    return Promise.allSettled([signUpUser(firstName, lastName), createUser(fileName)])
}

