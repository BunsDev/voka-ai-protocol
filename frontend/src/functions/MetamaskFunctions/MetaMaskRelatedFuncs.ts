import MetaMaskOnboarding from "@metamask/onboarding";
import { ElMessage } from "element-plus";
import Web3 from 'web3';
import store from '@/store';

const onboarding = new MetaMaskOnboarding();
const { ethereum } = window as any;
const provider = "https://polygon-mumbai.infura.io/v3/46f3f0763c7f4b8ebbe94c74ffb969cf";
const web3Provider = new Web3.providers.HttpProvider(provider);
const web3 = new Web3(web3Provider);

function login() {
    store.commit('login');
}

function logout() {
    store.commit('logout');
}

function chainCurrentChainId(chainId:string) {
    console.log(chainId);
    store.commit({
        type: 'chaingeCurrentMetamaskChainId',
        chainId: chainId
    });

}

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
        // Will open the MetaMask UI
        await ethereum
            .request({ method: "eth_requestAccounts" })
            .then((result: any) => {
                console.log(result);
            })
            .catch((error:any) => {
                if (error.code === 4001) {
                    console.log("用户拒绝请求");
                } else {
                    console.log(error);
                }
            });

        //we use eth_accounts because it returns a list of addresses owned by us.
        await ethereum
            .request({
                method: "eth_accounts",
            })
            .then((result: any) => {
                console.log(result); // 如果用户拒绝请求，这里回显示[]
                if(result.length > 0) {
                    login();
                } else {
                    logout();
                }
            })
            .catch((error:any) => {
                console.log(error);
            });
    }
}

export function getCurrentNetworkId() {
    if (!isMetaMaskInstalled()) {
        return "0";
    }
    return ethereum.networkVersion;
}

export async function isMetaMaskConnected() {
    if (!isMetaMaskInstalled()) {
        return false;
    }
    const res = await ethereum.isConnected()
}

export function getMetamaskSelectedAddress() {
    if (!isMetaMaskInstalled()) {
        return null;
    }
    if(!ethereum.isConnected()) {
        // 未登陆
        return null;
    }
    return ethereum.selectedAddress;
}

export async function signAndSendTransaction(tx: any) {
    if (!isMetaMaskInstalled()) {
        return;
    }
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

export async function addChain(networkDataArray: any) {
    if (!isMetaMaskInstalled()) {
        return false;
    }
    await ethereum
      .request({
        method: "wallet_addEthereumChain",
        params: networkDataArray,
      })
      .then((result:any) => {
          return true;
      })
      .catch((error: any) => {
        console.log(error); 
        return false;
      })
}

interface switchChainCallback {
  (): void;
}

// targetChainId必须是十六进制，比如0x13881
export async function switchChain(targetChainId: string, notExistCallBack: switchChainCallback) {
    if (!isMetaMaskInstalled()) {
        return;
    }
    try {
      await ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: targetChainId }],
      });
    } catch (switchError: any) {
      // This error code indicates that the chain has not been added to MetaMask.
      if (switchError.code === 4902) {
        notExistCallBack();
        return;
      }
      // handle other "switch" errors
      console.log(switchError); 
    }
}

export async function callContractMethod(contract_address: string, method_data: string) {
    if (!isMetaMaskInstalled()) {
        return false;
    }
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



if (isMetaMaskInstalled()) {
    ethereum.on('connect', (connectInfo: any) => {
            login();
            console.log(connectInfo);
            console.log(connectInfo.chainId);
            chainCurrentChainId(connectInfo.chainId);
    });
    
    ethereum.on('disconnect', (error: any) => {
            logout();
            console.log(error);
    });
}
