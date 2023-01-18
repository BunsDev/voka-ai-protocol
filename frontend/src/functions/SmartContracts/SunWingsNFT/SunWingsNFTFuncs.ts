import MetaMaskOnboarding from "@metamask/onboarding";
import Web3 from 'web3';
import { abi } from './SunWingsNFTABI';
import { callContractMethod } from '@/functions/MetamaskFunctions/MetaMaskRelatedFuncs';

let onboarding;
let contract_abi;
const { ethereum } = window as any;
const SunWingsNFT_contract_address = "0x8897E7c5E044d7897628150389343B70f84cA6c9____";
const contract_address = SunWingsNFT_contract_address;
const provider = "https://polygon-mumbai.infura.io/v3/46f3f0763c7f4b8ebbe94c74ffb969cf";

let web3Provider;
let web3;
let contract: any;

function init(): boolean {
    try {
        onboarding = new MetaMaskOnboarding();
        contract_abi = JSON.parse(abi);
        web3Provider = new Web3.providers.HttpProvider(provider);
        web3 = new Web3(web3Provider);
        contract = new web3.eth.Contract(contract_abi, contract_address);
    } catch(error) {
        return false;
    }
    return true;
}


/**
 * 通过指定group id，mint指定组的NFT
 * @param address 指定新NFT的拥有者
 * @param groupId 指定新NFT的组id
 * @returns 返回mint是否成功
 */
export async function mintNFTByGroupId(address: string, groupId: number): Promise<boolean> {
    const res = await callContractMethod(contract_address, contract.methods.mint(address, groupId).encodeABI());
    return res;
}

/**
 * 根据address，获取address拥有的NFT的数量
 * @param address 
 * @returns number
 */
export async function getNFTNum(address: string): Promise<number> {
    let num = 0;
    await contract.methods.balanceOf(address).call().then(function(res: any) {
        num = res ? res : 0;
    });
    return num;
}

/**
 * 获取指定组的解禁时间（unix timestamp seconds）
 * @param groupId 
 * @returns number，表示timestamp秒的整数，获取失败返回0
 */
export async function getUnlockTimeStampByGroupID(groupId: number): Promise<number> {
    let unlockTimeStamp = 0; // 3000.01.01 12:00
    await contract.methods.groupUnlockTimeStamp(groupId).call().then(function(res: any) {
        unlockTimeStamp = res ? res : 0;
    });
    return unlockTimeStamp;
}

/**
 * 根据group id查询指定NFT组是否被锁定
 * @param groupId 
 * @returns bool，表示NFT是否被锁定，获取失败时返回true
 */
export async function isGroupLocked(groupId: number): Promise<boolean> {
    let locked = true;
    await contract.methods.isGroupLocked(groupId).call().then(function(res: any) {
        locked = res ? res : true;
    });
    return locked;
}

/**
 * 根据group id查询指定NFT组中剩余NFT数量
 * @param groupId 
 * @returns number，表示剩余数量，获取失败时返回0
 */
export async function getRemainNFTNumByGroupId(groupId: number): Promise<number> {
    let num = 0;
    await contract.methods.remainNFTNumByGroupId(groupId).call().then(function(res: any) {
        num = res ? res : 0;
    });
    return num;
}

/**
 * 根据token id获取NFT对应的URI
 * @param tokenId 
 * @returns string，获取失败时返回空字符串
 */
export async function getNFTURIByTokenId(tokenId: number): Promise<string> {
    let uri = "";
    await contract.methods.tokenURI(tokenId).call().then(function(res: any) {
        uri = res ? res : "";
    });
    return uri;
}

export function timeStamp2Date(timestamp: number) {
    const date = new Date(Number(timestamp));
    return date;
}
