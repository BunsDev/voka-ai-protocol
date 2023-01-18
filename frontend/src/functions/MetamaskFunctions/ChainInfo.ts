const polygon_testnet_mumbai = [
    {
        chainId: "0x13881",
        chainName: "Mumbai",
        rpcUrls: ["https://polygon-mumbai.infura.io/v3/4458cf4d1689497b9a38b1d6bbf05e78"],
        nativeCurrency: {
          name: "MATIC Token",
          symbol: "MATIC",
          decimals: 18,
        },
        blockExplorerUrls: ["https://mumbai.polygonscan.com"],
    },
];

const chainIdMap = {
    "polygon":1,
    "mumbai":8001,

};

const chainIdMapHex = {
    "mumbai":"0x13881",
    
};

export {
    polygon_testnet_mumbai
};
