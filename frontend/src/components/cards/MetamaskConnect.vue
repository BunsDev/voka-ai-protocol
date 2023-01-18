<template>
  <div class="MetamaskConnect">
    <el-tooltip class="box-item" effect="dark" content="点击连接MetaMask" placement="bottom" v-if="!_isConnected">
      <div class="content-container metamask-connect-button" @click="_connectMetamask">
          <img class="logo" src="@/assets/metamask-fox.svg" />
          <span class="title">Connect Metamask</span>
      </div>
    </el-tooltip>
    <div class="metamask-connected-info" v-else>
      <p class="text">Metamask Connected!</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, defineProps, watch } from 'vue';
import { isMetaMaskConnected, connectMetamask } from '@/functions/MetamaskFunctions/MetaMaskRelatedFuncs';
import { useStore } from 'vuex';
let { state } = useStore();

const props = defineProps<{
    type: string
}>()

onMounted(() => {
  isMetaMaskConnected();
})

const _connectMetamask = async () => {
    await connectMetamask();
}

const _isConnected = computed(() => {
    return state.isMetamaskConnected;
})

/*
watch(_isConnected, (newVal, oldVal) => {
    console.log(newVal);
    console.log(oldVal);
},{immediate: true, deep: true});
*/

</script>

<style scoped lang="scss">
.MetamaskConnect {
  height: 3em;
  display: flex;
  justify-content: flex-end;

  .content-container {
    border-style: solid;
    border-radius: 5px;
    border-width: 1px;
    border-color: gray;
    width: 25%;
    height: 2em;

    display: flex;
    align-items: center;
    justify-content: center;

    .logo {
      height: 1.5em;
      width: 1.5em;
      padding-right: 10px;
    }
    .title {
      font-size: 1em;
    }
  }
  .metamask-connected-info {

    .text {
      font-style: italic;
      font-size: 1em;
      color: green;
    }
  }
}
</style>
