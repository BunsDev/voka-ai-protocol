<template>
  <div class="metamask">
    <el-row justify="space-between" v-for="r in NFT_Row" :key="r">
      <el-col v-for="c in NFT_Col" :key="c" :span="5" :offset="c > 1 ? 1 : 0">
        <el-card :body-style="{ padding: '0px' }" shadow="hover">
          <NFTCard :groupId="NFT_Col*(r-1)+c" :imgUrl="require(`@/assets/idols/idol${NFT_Col * (r - 1) + c}.jpeg`)" :nftName="idolname[NFT_Col * (r - 1) + c]"></NFTCard>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import NFTCard from '@/components/cards/NFTCard.vue'; // @ is an alias to /src

const idolname: string[] = ["王柏佑 Payu","李丹尼尔 Danny","昊天 Toey","陈家瑨 Chris", "鱼俊杰 Prame","岳凯峰 Hue", "黄书豪 Mark", "苏思南 Park"];

const NFT_Row = ref(2);
const NFT_Col = ref(4);
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}
</style>
