<template>
 <el-row>
    <el-col :span="8" class="left">
        <div class="left">
            <p v-if="isLogin2">connected</p>
            <p v-else>not connected</p>
        </div>
    </el-col>

    <el-col :span="8">
        <div class="middle">
            <p v-if="store.state.isLogin">你拥有的NFT数量：{{ NFTNum }}</p>
            <p v-else>请登录MetaMask</p>
        </div>
    </el-col>

    <el-col :span="8">
        <div class="right">
            <el-button plain @click="toAbout">About</el-button>
            <el-tooltip
                class="box-item"
                effect="dark"
                content="点击连接MetaMask"
                placement="bottom"
             >
                <img src="@/assets/metamask-fox.svg" @click="LoginMetaMask" />
             </el-tooltip>
        </div>
    </el-col>

  </el-row>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue';
import { useRouter } from "vue-router";
import { MetaLogin, isMetaMaskConnected, getCurrentNetworkId, getMetamaskSelectedAddress } from '@/functions/MetamaskFunctions/MetaMaskRelatedFuncs';
import { getNFTNum } from '@/functions/SmartContracts/SunWingsNFT/SunWingsNFTFuncs';
import store from '@/store';
import { useStore } from 'vuex';
const router = useRouter();
let { state, commit, getters } = useStore();

const isLogin2 = computed(() => {
    return state.isLogin;
})

watch(isLogin2, (newVal, oldVal) => {
    console.log(newVal);
    console.log(oldVal);
},{immediate: true, deep: true});



const NFTNum = ref(0);
const isLogin = ref(false);

onMounted(() => {
    console.log(getCurrentNetworkId());
    getNFTNum2();
    isMetaLogin();
    console.log(store.state.isLogin);
})



const LoginMetaMask = async () => {
    const res = await MetaLogin();
    isLogin.value = isMetaMaskConnected();
}


const isMetaLogin = async () => {
    const res = await isMetaMaskConnected();
    isLogin.value = res;
}

const getNFTNum2 = async () => {
    const address  = await getMetamaskSelectedAddress();
    NFTNum.value = await getNFTNum(address);
}

const toAbout = () => {
  router.push({
    name: "about",
  });
};

</script>

<style scoped lang="scss">
.middle {
  text-align: center;
}

.right {
  text-align: right;
}
</style>
