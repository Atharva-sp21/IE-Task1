# Part B – Smart Contract Development

## 1️⃣ Contract Code
![screenshot](/hello-vpn-contract/screenshots/03-contract-code.png)
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


## 2️⃣ Solidity Basics
- **constructor:** runs once at deploy, sets initial state  
- **public:** visible everywhere  
- **private:** only inside this contract  
- **view:** read-only, no gas when called externally  
- **memory:** temporary data in RAM, not stored on-chain  
- **msg.sender:** address that called the function  
- **Why types?** define storage size and prevent misuse

## 3️⃣ Understanding State
- State variables = stored data (greeting, nodeCount, deployer)  
- Stored in the contract’s persistent blockchain storage  
- Restarting your computer does NOT affect real chain; but local Hardhat data resets  
- Screenshot of state variables shown above
