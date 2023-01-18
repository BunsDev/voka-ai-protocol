import MetaMaskOnboarding from "@metamask/onboarding";
import Web3 from 'web3';
import store from '@/store';
import { fa } from "element-plus/es/locale";

const onboarding = new MetaMaskOnboarding();
const { ethereum } = window as any;
const provider = "https://polygon-mumbai.infura.io/v3/46f3f0763c7f4b8ebbe94c74ffb969cf";
const web3Provider = new Web3.providers.HttpProvider(provider);
const web3 = new Web3(web3Provider);

// ----------------- store related function -------------

function storeConnectMetamask() {
    store.commit('metamaskConnect');
}

function storeDisonnectMetamask() {
    store.commit('metamaskDisconnect');
}

/**
 * 修改当前MetaMask所在链
 * @param chainId 新链的chainId
 */
function changeCurrentChainId(chainId:string) {
    store.commit({
        type: 'chaingeCurrentMetamaskChainId',
        chainId: chainId
    });
}

/**
 * 检查浏览器是否安装Metamask插件
 * @returns bool，返回连接是否成功
 */
export function isMetaMaskInstalled() {
    //Have to check the ethereum binding on the window object to see if it's installed
    return Boolean(ethereum && ethereum.isMetaMask);
}

/**
 * 安装metamask插件
 */
export function installMetamask() {
    onboarding.startOnboarding();
}

/**
 * 连接成功时的回调
 */
interface connecteSucceedCallback {
    (result: any): void;
}

/**
 * 用户拒绝连接时的回调
 */
interface connecteRefuseCallback {
    (error: any): void;
}

/**其他原因导致连接失败时的回调 */
interface connecteFailedCallback {
    (error: any): void;
}

interface noMetamaskInstalledCallback {
    (): void;
}

/**
 * 连接MetaMask
 * 通过回调函数来告知调用者结果
 * 如果只需要知道连接结果，可以不用给回调函数
 * @param connectedCallBack 连接成功时的回调函数
 * @param connecteRefused 用户拒绝连接时的回调函数
 * @param connecteFailed 连接失败时的回调
 * @param metamaskNotInstalled metamask插件未安装时的回调
 * @returns bool，返回连接是否成功
 */
export async function connectMetamask(connectedCallBack?: connecteSucceedCallback,
                               connecteRefused?: connecteRefuseCallback,
                               connecteFailed?: connecteFailedCallback,
                               metamaskNotInstalled?: noMetamaskInstalledCallback) { 
    if (!isMetaMaskInstalled()) {
        if(metamaskNotInstalled) {
            metamaskNotInstalled();
        }
        return false;
    }
    await ethereum
        .request({ method: "eth_requestAccounts" })
        .then((result: any) => {
            if(connectedCallBack) {
                connectedCallBack(result);
            }
            storeConnectMetamask()
            return true;
        })
        .catch((error: any) => {
            if (error.code === 4001) {
                if(connecteRefused) {
                    connecteRefused(error);
                }
            } else {
                if(connecteFailed) {
                    connecteFailed(error);
                }
            }
        });
    return false;
}

interface metamaskNotConnectedCallback {
    (): void;
}

interface getAccountsSucceedCallback {
    (accounts: Array<string>): void;
}

interface getAccountsFailedCallback {
    (error: any): void;
}

/**
 * 获取metamask账户，通过回调函数.
 * 如果只想获取账户，可以不给回调函数，失败时返回空数组
 * @param succeed 获取账户成功时的回调，默认为空
 * @param failed 获取账户失败时的回调
 * @param metamaskNotInstall metamask未安装时的回调
 * @returns 返回数组 Array<string>，数组中是表示地址的字符串
 */
export async function getMetamaskAccounts(succeed?: getAccountsSucceedCallback,
                                          failed?: getAccountsFailedCallback,
                                          metamaskNotInstall?: metamaskNotConnectedCallback) {
    // 检查metamask是否已经安装
    if(!isMetaMaskConnected()) {
        if(metamaskNotInstall) {
            metamaskNotInstall();
        }
        return [];
    }
    //we use eth_accounts because it returns a list of addresses owned by us.
    await ethereum
        .request({
            method: "eth_accounts",
        })
        .then((result: any) => {
            if(succeed) {
                succeed(result);
            }
            /*
            if (result.length > 0) {
                login();
            } else {
                logout();
            }
            */
           return result;
        })
        .catch((error: any) => {
            console.log(error);
            if(failed) {
                failed(error);
            }
        });
        return [];
}

/**
 * 判断metamask是否连接
 * @returns Bool
 */
export function isMetaMaskConnected(): boolean {
    if (!isMetaMaskInstalled()) {
        storeDisonnectMetamask();
        return false;
    }
    ethereum.request({ method: 'eth_accounts' }).then((result: any) => {
        if(result.length > 0) {
            storeConnectMetamask()
            return true;
        } else {
            storeDisonnectMetamask();
            return false;
        }
    }).catch((error: any) => {
        storeDisonnectMetamask();
        return false;
    });
    return Boolean(ethereum.isConnected());
}

/**
 * 获取当前metamask连接的链的chainId
 * @returns string，chainId，获取失败时返回空字符串
 */
export function getCurrentNetworkId(): string {
    if (!isMetaMaskInstalled()) {
        return "";
    }
    return ethereum.networkVersion;
}

/**
 * 获取metamask当前选中的address
 * @returns string，表示address，失败时返回空字符串
 */
export function getMetamaskSelectedAddress(): string {
    if (!isMetaMaskConnected()) {
        return "";
    }
    return ethereum.selectedAddress;
}


interface sendTransactionSucceedCallback {
    (tx: any): void;
}

interface sendTransactionFailedCallback {
    (error: any): void;
}

/**
 * 
 * 利用metamask对transaction签名，并发送
 * @param tx 需要签名&发送的transaction
 * @param succeed 成功时回调函数
 * @param failed 失败时回调函数
 * @returns string, transaction的hash，失败返回null
 */
export async function signAndSendTransaction(tx: any,
                                             succeed?: sendTransactionSucceedCallback,
                                             failed?: sendTransactionFailedCallback) {
    if(!isMetaMaskConnected()) {
        return null;
    }
    await ethereum
    .request({
        method: 'eth_sendTransaction',
        params: [tx],
    })
    .then((result: any) => {
        console.log(result);
        if(succeed) {
            succeed(result);
        }
        return result;
    })
    .catch((error: any) => {
        if(failed) {
            failed(error);
        }
        console.log(error);
    });
    return null;
}

/**
 * 向Metamask增加新链
 * @param networkDataArray 数组，每一项是新链的描述信息，具体信息参考ChainInfo.ts
 * @returns Bool，表示增加是否成功
 */
export async function addChain(networkDataArray: Array<any>) {
    if (!isMetaMaskInstalled()) {
        return false;
    }
    await ethereum
        .request({
            method: "wallet_addEthereumChain",
            params: networkDataArray,
        })
        .then((result: any) => {
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

/**
 * 切换metamask所在链
 * @param targetChainId string，必须是十六进制的id，比如0x13881
 * @param notExistCallBack 目标链不存在回调
 * @returns Bool，切换是否成功
 */
export async function switchChain(targetChainId: string, notExistCallBack?: switchChainCallback) {
    if (!isMetaMaskInstalled()) {
        return false;
    }
    await ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: targetChainId }],
    })
    .then((result: any) => {
        return true;
    })
    .catch((error: any) => {
        if (error.code === 4902) {
            if(notExistCallBack) {
                notExistCallBack();
            }
        }
    });
    return false;
}

interface callContractSucceedCallback {
    (result: any): void;
}

interface callContractFailedCallback {
    (error: any): void;
}

/**
 * 调用智能合约函数
 * @param contract_address 调用智能合约的地址
 * @param method_data 调用智能合约方法的数据
 * @param succeed 成功回调
 * @param failed 失败回调
 * @returns Bool, 是否调用成功
 */
export async function callContractMethod(contract_address: string,
                                         method_data: string,
                                         succeed?: callContractSucceedCallback,
                                         failed?: callContractFailedCallback) {
    if (!isMetaMaskInstalled()) {
        return false;
    }
    let nonce;
    try {
        nonce = await web3.eth.getTransactionCount(ethereum.selectedAddress, 'latest'); //get latest nonce
    } catch {
        return false;
    }

    //the transaction
    const tx = {
        'from': ethereum.selectedAddress,
        'to': contract_address,
        'nonce': nonce.toString(),
        'gas': '500000',
        'data': method_data
    };
    let res;
    try {
        res = await signAndSendTransaction(tx, succeed, failed);
    } catch (e: any) {
        return false;
    }
    return res ? true : false;
}

/**
 * 为metamask增加时间监听
 * 需要安装metamask插件才能调用
 */
function addEventListener() {
    ethereum.on('connect', (connectInfo: any) => {
        storeConnectMetamask();
        changeCurrentChainId(connectInfo.chainId);
    });

    ethereum.on('disconnect', (error: any) => {
        storeDisonnectMetamask();
    });
}

// 没有安装metamask时，不能添加时间监听，否则会出错
if (isMetaMaskInstalled()) {
    addEventListener();
}
