import { expect } from "chai";
import { ethers } from "hardhat";

describe("HelloVPN", function () {
  async function deploy() {
    const [deployer] = await ethers.getSigners();
    const HelloVPN = await ethers.getContractFactory("HelloVPN");
    const hello = await HelloVPN.deploy();
    await hello.waitForDeployment();
    return { hello, deployer };
  }

  it("Test 1: Deploy and check initial values", async () => {
    const { hello, deployer } = await deploy();
    expect(await hello.getDeployerAddress()).to.equal(deployer.address);
    expect(await hello.getNodeCount()).to.equal(0n);
    expect(await hello.getGreeting()).to.equal("");
  });

  it("Test 2: Update greeting", async () => {
    const { hello } = await deploy();
    const tx = await hello.setGreeting("Hello VPN");
    await tx.wait();
    const greeting = await hello.getGreeting();
    expect(greeting).to.equal("Hello VPN");
  });

  it("Test 3: Set node count", async () => {
    const { hello } = await deploy();
    await (await hello.setNodeCount(10)).wait();
    const count = await hello.getNodeCount();
    expect(count).to.equal(10n);
  });
});
