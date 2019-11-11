// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App";

// router setup
import routes from "./routes/routes";

// Plugins
import GlobalComponents from "./globalComponents";
import GlobalDirectives from "./globalDirectives";
import Notifications from "./components/NotificationPlugin";

// MaterialDashboard plugin
import MaterialDashboard from "./material-dashboard";

import Chartist from "chartist";
import store from './store';
import axios from "axios";
// Configure Axios
//
Vue.prototype.$http = axios;

const token = localStorage.getItem('token')
if(token) {
    Vue.prototype.$http.defaults.headers.common['Authorization'] = `JWT ${token}`//token
}
//End configure axios


// configure router
const router = new VueRouter({
  routes, // short for routes: routes
  linkExactActiveClass: "nav-item active"
  //End authentication section
});

//

// Added for authentication
router.beforeEach((to, from, next) => {
      if(to.matched.some(record => record.meta.requiresAuth)) {
          if(store.getters.isLoggedIn){
              next()
              return
          }
          next('/login')
      }
          else {
          next()
          }
})
//
Vue.prototype.$Chartist = Chartist;

Vue.use(VueRouter);
Vue.use(MaterialDashboard);
Vue.use(GlobalComponents);
Vue.use(GlobalDirectives);
Vue.use(Notifications);

/* eslint-disable no-new */
new Vue({
  el: "#app",
  render: h => h(App),
  router,
  store,

  data: {
    Chartist: Chartist
   // info: null,
  },


});
