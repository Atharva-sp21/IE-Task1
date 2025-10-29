import hre from "hardhat";

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deployer:", deployer.address);

  const HelloVPN = await hre.ethers.getContractFactory("HelloVPN");
  const hello = await HelloVPN.deploy();
  await hello.waitForDeployment();

  const address = await hello.getAddress();
  console.log("HelloVPN deployed to:", address);

  const tx = await hello.setGreeting("Hello from deploy!");
  const receipt = await tx.wait();
  console.log("Initial greeting set. Gas used:", receipt.gasUsed.toString());
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
