// contracts/GameItem.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";

contract myCounter {
    using Counters for Counters.Counter;
    Counters.Counter id;

    function increase() public returns (uint256)
    {
        uint256 newID = id.current();
        id.increment();
        return newID;
    }
}
