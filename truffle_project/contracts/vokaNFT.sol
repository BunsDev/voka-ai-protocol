// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract vokaNFT is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() ERC721("vokaNFT", "VK") {
        _tokenIds.increment();
    }

    function createNFT(address to, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newNFTID = _tokenIds.current();
        _safeMint(to, newNFTID);
        _setTokenURI(newNFTID, tokenURI);

        _tokenIds.increment();
        return newNFTID;
    }

    function createNFTArr(address to, string[] memory tokenURIArr)
        public
        returns (uint256[] memory)
    {
        uint256[] memory newNFTIDArr = new uint256[](tokenURIArr.length);
	for(uint i = 0;i < tokenURIArr.length;i++) {
		uint256 newNFTID = _tokenIds.current();
        	_safeMint(to, newNFTID);
        	_setTokenURI(newNFTID, tokenURIArr[i]);
		_tokenIds.increment();
		newNFTIDArr[i] = newNFTID;
	}
        return newNFTIDArr;
    }
}
