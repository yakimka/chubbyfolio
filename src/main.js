// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';

import BootstrapVue from 'bootstrap-vue';
import VueMatchHeights from 'vue-match-heights';
import VueViewer from 'v-viewer';
import Default from './layouts/Default.vue';
import NoSidebar from './layouts/NoSidebar.vue';
import Landing from './layouts/Landing.vue';
import Portfolio from './layouts/Portfolio.vue';
import TopPage from './components/TopPage';
import MainScreenPhoto from './components/MainScreenPhoto';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'viewerjs/dist/viewer.css';
import './assets/scss/style.scss';
import {library} from '@fortawesome/fontawesome-svg-core';
import {fas} from '@fortawesome/free-solid-svg-icons';
import {fab} from '@fortawesome/free-brands-svg-icons';
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';

library.add(fas, fab);

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(BootstrapVue);
Vue.use(VueMatchHeights);
Vue.use(VueViewer);
Vue.component('default-layout', Default);
Vue.component('no-sidebar-layout', NoSidebar);
Vue.component('landing-layout', Landing);
Vue.component('portfolio-layout', Portfolio);
Vue.component('top-page', TopPage);
Vue.component('main-screen-photo', MainScreenPhoto);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
});
