<template>
  <div class="nft">
    <SunWingsNFT></SunWingsNFT>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SunWingsNFT from '@/components/SunWingsNFT.vue'; // @ is an alias to /src

export default defineComponent({
  name: 'NFT',
  components: {
    SunWingsNFT,
  },
});
</script>
