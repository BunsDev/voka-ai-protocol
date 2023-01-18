import { createStore } from 'vuex'
import { WindowSize } from '@/functions/WindowSizeFunctions/WindowSizeTypes';
import { computeWindowSizeByWidth } from '@/functions/WindowSizeFunctions/WindowSizeTypes';

export default createStore({
  state: {
    isMetamaskConnected: false,
    metamaskChainId: "0x0",
    windowSizeType: WindowSize.TOOSMALL,
    windowWidth: 200
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
    },
    resizeWindow (state:any, data: any) {
      state.windowSizeType = data.size;
      state.windowWidth = data.windowWidth;
    }

  },
  actions: {
  },
  modules: {
  }
})
