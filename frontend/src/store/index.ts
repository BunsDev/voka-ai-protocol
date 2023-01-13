import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin: false
  },
  getters: {
  },
  mutations: {
    login (state: any) {
        state.isLogin = true;
    },
    logout (state:any) {
        state.isLogin = false;
    }
  },
  actions: {
  },
  modules: {
  }
})
