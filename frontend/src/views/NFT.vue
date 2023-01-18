<template>
  <div>
    <MetamaskConnect></MetamaskConnect>
  </div>
  <div class="nft">
    <SunWingsNFT></SunWingsNFT>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MetamaskConnect from '@/components/cards/MetamaskConnect.vue'
import SunWingsNFT from '@/components/SunWingsNFT.vue'; // @ is an alias to /src

export default defineComponent({
  name: 'NFT',
  components: {
    MetamaskConnect,
    SunWingsNFT,
  },
});
</script>
