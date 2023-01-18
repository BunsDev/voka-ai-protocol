import { createStore } from 'vuex'

export default createStore({
  state: {
    isMetamaskConnected: false,
    metamaskChainId: "0x0"
  },
  getters: {
  },
  mutations: {
    metamaskConnect (state: any) {
        state.isMetamaskConnected = true;
    },
    metamaskDisconnect (state:any) {
        state.isMetamaskConnected = false;
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
