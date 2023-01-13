import MetaMaskOnboarding from "@metamask/onboarding";
import { ElMessage } from "element-plus";
import Web3 from 'web3';
//import { useLoginStore } from "@/store/login";

const onboarding = new MetaMaskOnboarding();
const { ethereum } = window as any;
const provider = "https://polygon-mumbai.infura.io/v3/46f3f0763c7f4b8ebbe94c74ffb969cf";
const web3Provider = new Web3.providers.HttpProvider(provider);
const web3 = new Web3(web3Provider);

//const loginStore = useLoginStore();


//Created check function to see if the MetaMask extension is installed
export function isMetaMaskInstalled() {
    //Have to check the ethereum binding on the window object to see if it's installed
    return Boolean(ethereum && ethereum.isMetaMask);
}

export async function MetaLogin() {
    //Now we check to see if MetaMask is installed
    if (!isMetaMaskInstalled()) {
        //If it isn't installed we ask the user to click to install it
        ElMessage.info("请安装MetaMask!");
        onboarding.startOnboarding();
    } else {
        try {
            // Will open the MetaMask UI
            await ethereum
                .request({ method: "eth_requestAccounts" })
                .then((result: any) => {
                    console.log(result);
                })
                .catch((error:any) => {
                    console.log(error);
                });
            //we use eth_accounts because it returns a list of addresses owned by us.
            const accounts = await ethereum
                .request({
                    method: "eth_accounts",
                })
                .then((result: any) => {
                    console.log(result);
                })
                .catch((error:any) => {
                    console.log(error);
                });
            console.log("==========");
            if (accounts.length > 0) {
                ElMessage.success("Get Wallet Address Successfully!");
                return true;
            }
        } catch (error) {
            console.error(error);
            return false;
        }
        return false;
    }
}

export async function isMetaMaskLogin() {
    const res = await ethereum.isConnected()
}

export async function getMetamaskSelectedAddress(): Promise<string> {
    if(!ethereum.isConnected()) {
        // 未登陆
        return ""
    }
    return ethereum.selectedAddress;
}

export async function signAndSendTransaction(tx: any) {
    if(!ethereum.isConnected()) {
        ElMessage.warning("connect please!");
    }
    let res;
    try {
        res = await ethereum.request({
            method: 'eth_sendTransaction',
            params: [tx],
        });
    } catch(error: any) {
        throw new Error("sign&send Transaction error");
    }
    return res;
}

export async function callContractMethod(contract_address: string, method_data: string) {
    if(!ethereum.isConnected()) {
        ElMessage.warning("connect please!");
    }
    const nonce = await web3.eth.getTransactionCount(ethereum.selectedAddress, 'latest'); //get latest nonce

    //the transaction
    const tx = {
	'from': ethereum.selectedAddress,
	'to': contract_address,
	'nonce': nonce.toString(),
	'gas': '500000',
	'data': method_data
    };
    try {
        const res = await signAndSendTransaction(tx);
    } catch (e: any) {
        return false;
    }
    return true;
}


ethereum.on('connect', (connectInfo: any) => {
	console.log(connectInfo);
});
