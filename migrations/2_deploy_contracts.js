const MyContract = artifacts.require("MyContract");
const OptimizedMyContract = artifacts.require("OptimizedMyContract");

module.exports = async function (deployer) {
  // 部署原始合约
  await deployer.deploy(MyContract);

  // 部署优化后的合约
  await deployer.deploy(OptimizedMyContract);
};
