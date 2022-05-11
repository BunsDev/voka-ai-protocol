// contracts/GameItem.sol
// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract vokaNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() ERC721("vokaNFT", "VK") {}

    function createNFT(address to, string memory tokenURI)
        public onlyOwner
        returns (uint256)
    {
        uint256 newNFTID = _tokenIds.current();
        _mint(to, newNFTID);
        _setTokenURI(newNFTID, tokenURI);

        _tokenIds.increment();
        return newNFTID;
    }
}
