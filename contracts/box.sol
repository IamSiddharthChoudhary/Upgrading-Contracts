// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Box {
    uint256 private value;
    event valueChange(uint256 newVal);

    function store(uint256 newVal) public {
        value = newVal;
        emit valueChange(newVal);
    }

    function getValue() public view returns (uint256) {
        return value;
    }
}
