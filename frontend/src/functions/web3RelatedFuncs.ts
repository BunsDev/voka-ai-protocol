import MetaMaskOnboarding from "@metamask/onboarding";
import { ElMessage } from "element-plus";
import Web3 from 'web3';
import { abi } from './NFTABI'

const onboarding = new MetaMaskOnboarding();
const { ethereum } = window as any;

const contract_abi = JSON.parse(abi);
const contract_address = "0xdbE5dB244fCc0CbA5f10804378A0df00726D8bd7";
const provider = "https://polygon-mumbai.infura.io/v3/46f3f0763c7f4b8ebbe94c74ffb969cf";

const web3Provider = new Web3.providers.HttpProvider(provider);
const web3 = new Web3(web3Provider);
const contract = new web3.eth.Contract(contract_abi, contract_address);


//Created check function to see if the MetaMask extension is installed
export function isMetaMaskInstalled() {
    //Have to check the ethereum binding on the window object to see if it's installed
    return Boolean(ethereum && ethereum.isMetaMask);
}

export async function MetaLogin() {
    //Now we check to see if MetaMask is installed
    console.log(contract);
    if (!isMetaMaskInstalled()) {
        //If it isn't installed we ask the user to click to install it
        ElMessage.info("Install MetaMask!");
        onboarding.startOnboarding();
    } else {
        try {
            // Will open the MetaMask UI
            await ethereum.request({ method: "eth_requestAccounts" });
            //we use eth_accounts because it returns a list of addresses owned by us.
            const accounts = await ethereum.request({
                method: "eth_accounts",
            });
            ElMessage.success("Get Wallet Address Successfully!");
            if (accounts.length > 0) {
                console.log(accounts);
            }
        } catch (error) {
            console.error(error);
        }
    }
}

export async function getNFTNum() {
    let num = 0;
    await contract.methods.balanceOf(ethereum.selectedAddress).call().then(function(res: any) {
        console.log(res);
        num = res;
        return res || '获取失败';
    });
    return num;
}
