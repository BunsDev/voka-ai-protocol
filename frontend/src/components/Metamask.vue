<template>
  <div class="metamask">
    <img src="@/assets/metamask-fox.svg" @click="MetaLogin" />
  </div>
</template>

<script setup lang="ts">
import { MetaLogin } from '@/functions/web3RelatedFuncs';

</script>

<style scoped>
</style>
