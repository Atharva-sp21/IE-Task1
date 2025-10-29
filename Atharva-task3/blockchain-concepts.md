**Local vs Real Blockchain**

*What are 3 differences between Hardhat local network and Ethereum mainnet?*

-> Local HardHat is free whereas Mainnet costs real ETH for gas
-> Hardhat instantly mines a black whereas ETH takes some extra time
-> Local resets everytime you stop the node whereas ETH is permanent

*Why do we develop locally first?*

-> We develop locally first because its safe, we can test our code without losing any real money

*What would change if you deployed this same contract to real Ethereum?*

-> You need to have real ETH, pay for it,wait after each transaction and it will stay permanent


**Smart Contract Basics**

*What is a smart contract?*
-> Smart contract is a small program stored and executed on the blockchain

*Once deployed, can you edit the contract code? Why or why not?*
-> No, blockchians are immutable, we cant make any changes to it once they are deployed, we will have to deploy a newer version everytime in order to make a change

*If you restart your Hardhat node, what happens to your deployed contract?*
-> When you restart the Hardhat node, it clears all local blockchain data — your deployed contract and fake ETH accounts disappear so you need to redeploy everything again.

*How is a smart contract different from a regular program or website?*
A website runs on private servers and can be changed anytime whwereas a smart contract runs on thousands of blockchain nodes and can’t be changed once deployed.

**Blockchain & Our VPN Project**

*Why would a VPN project use blockchain?*
The entire purpose of blockchain is deventralize. VPN would need a blockchain so that it doesnt remain dependant on any individual, company, etc. It can be decentralized, transparent and fair and many independent people can run it 

*What advantages does blockchain provide over a central database?*
It provides transparency, flexibility, security and decentralization. We don't need to trust on one party, it provdes honesty

*What disadvantages or challenges might blockchain add?*
It is quite complex to use, requires payment and also takes time between transactions

*Give 2 examples of what our VPN project might store on blockchain.*
* Subscription tokens - as a proof that user has paid for VPN access
* Connection logs - contains anonymous users and doesn't reveal user data.

**BASIC DEFINITION**

Blockchain - a shared online record book that everyone can see but no one can change, but whenever something is written on it, everyone's copy gets updated
Smart Contract - Code stored on blockchain that runs automatically when called.
Gas	- The fee paid to run operations or store data on the blockchain.
Wallet Address - Your public blockchain identity (like an account number).
Private Key -	Your secret password that proves you own the wallet.
Transaction - It is a recorded action, like any payment or deposit
Deployment - Uploading your contract’s code to the blockchain so others can use it.