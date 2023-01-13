import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin: false,
    metamaskChainId: "0x0"
  },
  getters: {
  },
  mutations: {
    login (state: any) {
        state.isLogin = true;
    },
    logout (state:any) {
        state.isLogin = false;
    },
    chaingeCurrentMetamaskChainId (state: any, data: any) {
        state.metamaskChainId = data.chainId
    }
  },
  actions: {
  },
  modules: {
  }
})
