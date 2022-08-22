# VOKA AI PROTOCOL

## Introduction:
***VOKA AI Protocol*** is the embodiment of a new generation of Web 3.0 technologies. 
Not only are we capable of **generating exclusive anime avatars through our proprietary AI technology**; 
we can also use existing NFT PFPs to generate digital identities. 
Furthermore, we collaborate with some of the world's top designers and clothing brands 
to create a variety of virtual outfits and sell them through the Opensea platform. 
The application scenarios for your digital identities are boundless, including: 
video conferencing, webcasting, virtual social networking, and even web3 games.

**How to use:**
1.	Connect your wallet or create an account. 
2.	The protocol will scan the available NFT for generation in your wallet.
3.	If don’t have available NFT, you can use the Anime PFP Generation to create your own anime PFP.
4.	The protocol will generate 3D avatar from the selected anime display picture.
5.	After the generation, also can modify the assets of avatar, such as: clothes, hair style/color, eyeballs, and etc. 
6.	Not only the avatar can be saved on our server, we also support avatar mint. In order to ensure the avatar exclusive, the protocol will automatically remove the anime PFP from our system once the avatar mint.
7.	Our avatar standard format is suitable for the most of 3D engines (Unity or Unreal Engine) or Metaverse scenarios (Sandbox or Decentraland). In the coming future, we will provide SDK to import avatar file for metaverse creators and gaming developers. 

**The Web 3.0 technologies use in this project**
1.	Solidity
2.	Truffle
3.	Infura
4.	OpenZeppelin NFT standard
5.	OpenSea API
6.	MetaMask API
7.	Filecoin (IPFS) NFT.Storage API

## $Bonus:
•	ERC-721 Passport Standard (ERC-721P)
We generated a new ERC721 Standard by modifying OpenZeppelina NFT standard (ERC721URIStorage.sol). We called the new ERC721 standard as “Passport” (ERC-721P). 
ERC-721P is a summary for the avatar mint which includes PFP, 3D avatar, clothes, accessories, and so on. In order to save gas fee for users, ERC-721P also can mint all items in one time. 

•	PC expression capture software:
We also provide a UE5 PC expression capture software like Hologram for live-streaming and online chat. The software is support facial and upper limb capture.  (Readme on the software folder)

## migration

1. set environment variables, `BLOCKCHAIN_PHRASE`, `INFURA_LINK`, etc.
2. migrate to specific blockchain, for instance `truffle migrate --network rinkeby` if we want migrate to testnet *rinkeby*.
