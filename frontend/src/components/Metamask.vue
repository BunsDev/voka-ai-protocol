<template>
  <div class="metamask">
    <img src="@/assets/metamask-fox.svg" @click="MetaLogin" />
    <p>你拥有的NFT数量：{{ NFTNum }}</p>
    <el-button type="primary" @click="getNFTNum2" >获取NFT数量</el-button>
    <p>第{{ GroupID }}组NFT解禁时间：{{ UnlockDate }}</p>
    <el-button type="primary" @click="getUnlockTS" >获取解禁时间</el-button>
    <el-button type="primary" @click="mintNFT0" >mint group 0 NFT</el-button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { MetaLogin, getMetamaskSelectedAddress } from '@/functions/MetaMaskRelatedFuncs';
import { mintNFTByGroupId, getNFTNum, getNFTURIByTokenId, getUnlockTimeStampByGroupID, timeStamp2Date } from '@/functions/SmartContracts/SunWingsNFT/SunWingsNFTFuncs';

const NFTNum = ref(10);
const GroupID = ref(0);
const UnlockDate = ref("");

const mintNFT0 = async () => {
    const address  = await getMetamaskSelectedAddress();
    const tokenID = await mintNFTByGroupId(address, 0);
    console.log(tokenID);
    //alart(tokenID);
}

const getNFTNum2 = async () => {
    const address  = await getMetamaskSelectedAddress();
    NFTNum.value = await getNFTNum(address);
    const uri = await getNFTURIByTokenId(3);
    console.log(uri);
}

const getUnlockTS = async () => {
    const timestamp: number = await getUnlockTimeStampByGroupID(GroupID.value);
    const date = timeStamp2Date(timestamp * 1000);
    const date2 = timeStamp2Date(1672545600 * 1000);
    console.log(date);
    console.log(date2);
    console.log(date.getFullYear());
    UnlockDate.value = date;
}

</script>

<style scoped>
</style>
