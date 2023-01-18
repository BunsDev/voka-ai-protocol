<template>
  <div class="NFTCard">
    <img
    class="image"
    :src="props.imgUrl"
    />
    <div class="card-info">
      <p>{{ props.nftName }}</p>
      <p>Unlock Time: {{ UnlockDate }}</p>
      <p>Remaining NFT Number: {{ RemainNFTNum }}</p>
      <div class="bottom">
        <el-button type="primary" @click="mintNFT" :disabled="isNFTLocked || RemainNFTNum <= 0">mint</el-button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, defineProps, onMounted, computed, watch } from 'vue';
import { isMetaMaskInstalled, installMetamask, isMetaMaskConnected, connectMetamask, getMetamaskSelectedAddress, MetaLogin } from '@/functions/MetamaskFunctions/MetaMaskRelatedFuncs';
import { mintNFTByGroupId, getRemainNFTNumByGroupId, isGroupLocked, getUnlockTimeStampByGroupID, timeStamp2Date } from '@/functions/SmartContracts/SunWingsNFT/SunWingsNFTFuncs';
import { switchChain, addChain } from '@/functions/MetamaskFunctions/MetaMaskRelatedFuncs';
import { polygon_testnet_mumbai } from '@/functions/MetamaskFunctions/ChainInfo';
import { ElMessage, ElMessageBox, ElNotification } from "element-plus";
import type { Action } from 'element-plus'
import store from '@/store';
import { useStore } from 'vuex';
let { state, commit, getters } = useStore();

const currentChainIdInfo = computed(() => {
    return state.metamaskChainId;
})

/*
watch(currentChainIdInfo, (newVal, oldVal) => {
    console.log(newVal);
    console.log(oldVal);
},{immediate: true, deep: true});
*/

onMounted(() => {
    console.log(props.imgUrl);
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
const UnlockDate = ref("Stay tuned");
const RemainNFTNum = ref(0);

const switch2Mumbai = async() => {
    await switchChain("0x13881", () => {
        addChain(polygon_testnet_mumbai);
    });
}

const mintNFT = async () => {
    let continueMint = true;
    if (!isMetaMaskInstalled()) {
        await ElMessageBox.confirm('一键安装Metamask插件（Chrome or Firefox）','浏览器未安装Metamask插件，无法mint！', {
            confirmButtonText: '安装',
            cancelButtonText: '取消',
            type: 'warning',
            })
            .then(() => {
                installMetamask();
            })
            .catch(() => {
                continueMint = false;
            });
    }
    if(!continueMint) {
        return;
    }
    if(!isMetaMaskConnected()) {
        await ElMessageBox.confirm('连接Metamask','未连接Metamask，无法mint！', {
            confirmButtonText: '连接',
            cancelButtonText: '取消',
            type: 'warning',
            })
            .then(() => {
                connectMetamask();
            })
            .catch(() => {
                continueMint = false;
            });
    }
    if(!continueMint) {
        return;
    }
    if (currentChainIdInfo.value != "0x13881") {
        await ElMessageBox.confirm('切换到测试链Mumbai!','当前不是Mumbai测试链', {
            // if you want to disable its autofocus
            // autofocus: false,
            confirmButtonText: '好的',
            cancelButtonText: '取消',
            type: 'warning',
            })
            .then(() => {
                switch2Mumbai();
            })
            .catch(() => {
                ElMessage.info("放弃mint");
                continueMint = false;
            });
    }
    if(!continueMint) {
        return;
    }
    const address  = getMetamaskSelectedAddress();
    if(address.length <= 0) {
        ElMessage.warning("获取address失败")
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
    if(timestamp === 0) {
        return "Stay Tuned";
    }
    const date = timeStamp2Date(timestamp * 1000);
    UnlockDate.value = date.toString();
}

</script>

<style scoped lang="scss">
.NFTCard {
    .card-info {
        padding: 5px;
        p {
            margin-top: 5px;
            margin-bottom: 5px;
            font-size: 0.8em;
            width: 100%;
            overflow: hidden;
            text-overflow: ellipsis; //文本溢出显示省略号
            white-space: nowrap; //文本不会换行
        }
        .bottom {
            padding-top: 10px;
        }
    }
    .image {
      width: 100%;
      display: block;
    }
}
</style>
