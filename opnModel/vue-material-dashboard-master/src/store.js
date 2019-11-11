import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      status: '',
      token: localStorage.getItem('token') || '',
      user: {}
  },

  mutations: {

      auth_request(state){
          state.status = 'loading'
      },

      auth_success(state, commitData){ //token, user) {

          state.status = 'success'
          state.token = commitData.token
          state.user = commitData.user
      },

      auth_error(state) {
          state.status = 'error'
      },

      logout(state){
          state.status = ''
          state.token = ''
      },

  },
  actions: {
      login({commit}, user){
          return new Promise((resolve, reject) => {
              commit('auth_request')
                  axios({url: 'https://investors.opn.ninja:8081/api/auth/login/', data: user, method: 'POST'})
                  .then(resp => {
                      const token = resp.data.token
                      const user = resp.data.user
                      localStorage.setItem('token', token)
                      axios.defaults.headers.common['Authorization'] =  `JWT ${token}`//token
                      var commitData = {token, user}
                      commit('auth_success', commitData)
                      resolve(resp)
                  })
                  .catch(err => {
                      commit('auth_error')
                      localStorage.removeItem('token')
                      reject(err)
                  })
          })
                    
        },

      register({commit}, user){
          return new Promise((resolve, reject) => {
              commit('auth_request')
                  axios({url: 'https://investors.opn.ninja:8081/api/auth/registration/', data: user, method: 'POST'})
                  .then(resp => {
                      const token = resp.data.token
                      const user = resp.data.user
                      localStorage.setItem('token', token)
                      axios.defaults.headers.common['Authorization'] =  `JWT ${token}`//token
                      var commitData = {token, user}
                      commit('auth_success', {commitData})
                      resolve(resp)
                  })
                  .catch(err => {
                      commit('auth_error', err)
                          localStorage.removeItem('token')
                          reject(err)
                  })
          })
    },

      logout({commit}){
          return new Promise((resolve, reject) => {
              commit('logout')
              localStorage.removeItem('token')
              delete axios.defaults.headers.common['Authorization']
              resolve()
          })
      }

  },

    getters: {

        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,

    }
});
