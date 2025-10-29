// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract HelloVPN {
    string private greeting;
    uint256 private nodeCount;
    address public immutable deployer;

    constructor() {
        deployer = msg.sender;
    }

    function setGreeting(string memory _greeting) external {
        greeting = _greeting;
    }

    function getGreeting() external view returns (string memory) {
        return greeting;
    }

    function setNodeCount(uint256 _count) external {
        nodeCount = _count;
    }

    function getNodeCount() external view returns (uint256) {
        return nodeCount;
    }

    function getDeployerAddress() external view returns (address) {
        return deployer;
    }
}
