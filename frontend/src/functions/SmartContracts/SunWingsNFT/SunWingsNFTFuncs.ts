import MetaMaskOnboarding from "@metamask/onboarding";
import { ElMessage } from "element-plus";
import Web3 from 'web3';
import { abi } from './SunWingsNFTABI';
import { callContractMethod } from '@/functions/MetamaskFunctions/MetaMaskRelatedFuncs';

const onboarding = new MetaMaskOnboarding();
const { ethereum } = window as any;

const contract_abi = JSON.parse(abi);
const SunWingsNFT_contract_address = "0x8897E7c5E044d7897628150389343B70f84cA6c9";
const contract_address = SunWingsNFT_contract_address;
const provider = "https://polygon-mumbai.infura.io/v3/46f3f0763c7f4b8ebbe94c74ffb969cf";

const web3Provider = new Web3.providers.HttpProvider(provider);
const web3 = new Web3(web3Provider);
const contract = new web3.eth.Contract(contract_abi, contract_address);

/// 通过指定group id，mint指定组的NFT
export async function mintNFTByGroupId(address: string, groupId: number) {
    const res = await callContractMethod(contract_address, contract.methods.mint(address, groupId).encodeABI());
    return res;
}

/// 获取address拥有的NFT数量
export async function getNFTNum(address: string) {
    let num = 0;
    await contract.methods.balanceOf(address).call().then(function(res: any) {
        num = res;
        return res || '获取失败';
    });
    return num;
}

/// 根据group id查询指定NFT组的解禁时间
/// 表示方式是unix timestamp in seconds
export async function getUnlockTimeStampByGroupID(groupId: number) {
    let unlockTimeStamp = 32503694400; // 3000.01.01 12:00
    await contract.methods.groupUnlockTimeStamp(groupId).call().then(function(res: any) {
        unlockTimeStamp = res;
        return res || '获取失败';
    });
    return unlockTimeStamp;
}

/// 根据group id查询指定NFT组是否被锁定
export async function isGroupLocked(groupId: number) {
    let locked = true;
    await contract.methods.isGroupLocked(groupId).call().then(function(res: any) {
        locked = res;
        return res || '获取失败';
    });
    return locked;
}

/// 根据group id查询指定NFT组中剩余NFT数量
export async function getRemainNFTNumByGroupId(groupId: number) {
    let num = 0;
    await contract.methods.remainNFTNumByGroupId(groupId).call().then(function(res: any) {
        num = res;
        return res || '获取失败';
    });
    return num;
}

/// 根据token id获取NFT对应的URI
export async function getNFTURIByTokenId(tokenId: number) {
    let uri = "";
    await contract.methods.tokenURI(tokenId).call().then(function(res: any) {
        uri = res;
        return res || '获取失败';
    });
    return uri;
}

export function timeStamp2Date(timestamp: number) {
    const date = new Date(Number(timestamp));
    return date;
}
