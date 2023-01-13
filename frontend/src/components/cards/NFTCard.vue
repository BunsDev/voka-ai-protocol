<template>
  <div class="NFTCard">
    <img
    :src="props.imgUrl"
    class="image"
    />
    <div style="padding: 14px">
      <span>{{ props.nftName }}</span>
      <p>解禁时间：{{ UnlockDate }}</p>
      <p>剩余数量：{{ RemainNFTNum }}</p>
      <div class="bottom">
        <el-button type="primary" @click="mintNFT" :disabled="isNFTLocked || RemainNFTNum <= 0">mint</el-button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineProps, onMounted } from 'vue';
import { getMetamaskSelectedAddress, MetaLogin } from '@/functions/MetaMaskRelatedFuncs';
import { mintNFTByGroupId, getNFTNum, getRemainNFTNumByGroupId, isGroupLocked, getUnlockTimeStampByGroupID, timeStamp2Date } from '@/functions/SmartContracts/SunWingsNFT/SunWingsNFTFuncs';
import { ElMessage, ElMessageBox, ElNotification } from "element-plus";
import type { Action } from 'element-plus'

onMounted(() => {
    getUnlockTS();
    getRemainNFT();
    isLocked();
})

const props = defineProps<{
  groupId: number
  imgUrl: string
  nftName: string
}>()

const isNFTLocked = ref(true);
const UnlockDate = ref("");
const RemainNFTNum = ref(0);

const mintNFT = async () => {
    const address  = getMetamaskSelectedAddress();
    if(!address) {
        //ElMessage.info("请链接MetaMask")
        ElMessageBox.alert('请连接MetaMask后再Mint', '未连接MetaMask', {
            // if you want to disable its autofocus
            // autofocus: false,
            confirmButtonText: 'OK',
            callback: (action: Action) => {
                MetaLogin();
            },
        })
        return;
    }
    const res = await mintNFTByGroupId(address, props.groupId - 1);
    if(res) {
        ElNotification({
            title: 'Mint成功',
            message: '恭喜您，NFT已mint成功，您可去opensea查看。',
            type: 'success',
        })
    } else {
        ElNotification({
            title: 'Mint失败',
            message: 'NFT mint失败，请查看是否链接metamask',
            type: 'warning',
        })
    }
}

const getRemainNFT = async() => {
    const remainNum: number = await getRemainNFTNumByGroupId(props.groupId - 1);
    RemainNFTNum.value = remainNum;
}

const isLocked = async() => {
    isNFTLocked.value = await isGroupLocked(props.groupId - 1);
}

const getUnlockTS = async () => {
    const timestamp: number = await getUnlockTimeStampByGroupID(props.groupId - 1);
    const date = timeStamp2Date(timestamp * 1000);
    let date_str = "";
    date_str += date.getFullYear().toString() + "年";
    date_str += date.getMonth().toString() + "月";
    date_str += date.getDay().toString() + "日";
    date_str += date.getHours().toString() + "时";
    date_str += date.getMinutes().toString() + "分";
    date_str += date.getSeconds().toString() + "秒";
    UnlockDate.value = date_str;
}

</script>

<style scoped>
.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  justify-content: space-between;
  align-items: center;
}

.image {
  width: 100%;
  display: block;
}
</style>
