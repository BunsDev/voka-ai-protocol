<template>
  <div class="metamask">
    <img src="@/assets/metamask-fox.svg" @click="MetaLogin" />
    <p>你拥有的NFT数量：{{ NFTNum }}</p>
    <el-button type="primary" @click="getNFTNum2" >获取NFT数量</el-button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { MetaLogin, getNFTNum } from '@/functions/web3RelatedFuncs';

const NFTNum = ref(10);


const getNFTNum2 = async () => {
    NFTNum.value = await getNFTNum();
}

</script>

<style scoped>
</style>
