import { createApp } from 'vue';
import App from './App.vue';
import PrimeVue from 'primevue/config';
import router from './router/Routers';
import 'primeflex/primeflex.css';
import '@fortawesome/fontawesome-free/css/all.min.css';


const app = createApp(App);

app.use(PrimeVue, {
    theme: {
    },
});

app.use(router); // Use the router with the same app instance
app.mount('#app'); // Mount the app
