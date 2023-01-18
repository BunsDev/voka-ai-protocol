<template>
  <div class="MetamaskConnect">
    <el-tooltip class="box-item" effect="dark" content="点击连接MetaMask" placement="bottom" v-if="false">
      <div class="content-container" @click="LoginMetaMask">
          <img class="logo" src="@/assets/metamask-fox.svg" />
          <span class="title">Connect Metamask</span>
      </div>
    </el-tooltip>
    <div v-else>已登陆</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, defineProps } from 'vue';
import { isMetaMaskInstalled, installMetamask, isMetaMaskConnected, connectMetamask, getMetamaskSelectedAddress, MetaLogin } from '@/functions/MetamaskFunctions/MetaMaskRelatedFuncs';
import { useStore } from 'vuex';
let { state, commit, getters } = useStore();

const isLogin = ref(false);

onMounted(() => {
  isMetaLogin();
})

const props = defineProps<{
    type: string
}>()

const LoginMetaMask = async () => {
    isLogin.value = await connectMetamask();
}

const isMetaLogin = async () => {
    isLogin.value = isMetaMaskConnected();
}

const isLogin2 = computed(() => {
    return state.isLogin;
})
/*

watch(isLogin2, (newVal, oldVal) => {
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
}
</style>
