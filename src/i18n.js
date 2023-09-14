import { addMessages, init } from 'svelte-i18n';

import en from './locales/en-US.json';
import fr from './locales/fr.json';

addMessages('en-US', en);
addMessages('fr', fr);

init({
    fallbackLocale: 'en-US',
    initialLocale: 'en-US',
});