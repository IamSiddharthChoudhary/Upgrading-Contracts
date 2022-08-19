// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract BoxV2 {
    uint256 private value;
    event valueChange(uint256 newVal);

    function store(uint256 newVal) public {
        value = newVal;
        emit valueChange(newVal);
    }

    function getValue() public view returns (uint256) {
        return value;
    }

    function increment() public {
        value = value + 1;
        emit valueChange(value);
    }
}
