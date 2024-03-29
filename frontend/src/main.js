// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'viewerjs/dist/viewer.css';
import '@/assets/scss/style.scss';
import Vue from 'vue';
import App from '@/App';
import router from '@/router';
import VueSweetalert2 from 'vue-sweetalert2';
import VueTheMask from 'vue-the-mask';

import { NavPlugin } from 'bootstrap-vue';
import VueMatchHeights from 'vue-match-heights';
import VueViewer from 'v-viewer';
import VueScrollTo from 'vue-scrollto';
import Landing from '@/layouts/Landing.vue';
import Portfolio from '@/layouts/Portfolio.vue';
import Blank from '@/layouts/Blank.vue';
import TopPage from '@/components/TopPage';
import MainScreenPhoto from '@/components/MainScreenPhoto';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faAddressBook, faPhone, faTimesCircle } from '@fortawesome/free-solid-svg-icons';
import { faFacebook, faInstagram } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import 'lazysizes';
import 'lazysizes/plugins/attrchange/ls.attrchange';

library.add(faTimesCircle, faInstagram, faFacebook, faPhone, faAddressBook);

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(NavPlugin);
Vue.use(VueMatchHeights);
Vue.use(VueViewer);
Vue.use(VueScrollTo, {
  offset: -170
});
Vue.use(VueSweetalert2);
Vue.use(VueTheMask);
Vue.component('landing-layout', Landing);
Vue.component('portfolio-layout', Portfolio);
Vue.component('blank-layout', Blank);
Vue.component('top-page', TopPage);
Vue.component('main-screen-photo', MainScreenPhoto);

Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
});

// add simple support for background images:
document.addEventListener('lazybeforeunveil', function (e) {
  const bg = e.target.getAttribute('data-bg');
  if (bg) {
    e.target.style.backgroundImage = `url(${bg})`;
  }
});
