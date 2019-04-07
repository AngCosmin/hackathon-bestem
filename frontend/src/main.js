import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import axios from 'axios'

// Maps
import * as VueGoogleMaps from 'vue2-google-maps'

// Router
import router from './router'
import VueRouter from 'vue-router'

// Calendar
import FullCalendar from 'vue-full-calendar'

// Store
import store from './store/index'

// Datepicker
import Datetime from 'vue-datetime'

import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-datetime/dist/vue-datetime.css'

import VCharts from 'v-charts'

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://localhost:5000';

Vue.use(BootstrapVue)
Vue.use(Vuex)
Vue.use(VueRouter)
Vue.use(FullCalendar)
Vue.use(Datetime)
Vue.use(VCharts)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBfUwZZLyoHnHjmywdCtEMNaxyXI8IU2ew',
    libraries: 'places', // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)
 
    //// If you want to set the version, you can do so:
    // v: '3.26',
  },
})


new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
