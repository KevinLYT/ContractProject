
# ContractProject

This project involves developing and deploying decentralized messaging contracts, simulating gas costs for different scenarios, and comparing gas usage between original and optimized smart contracts.

本项目包括开发和部署去中心化消息传递合约，模拟不同场景下的Gas费用，并比较原始和优化版智能合约的Gas使用情况。

## Prerequisites 前置条件

1. [Node.js and npm](https://nodejs.org/en/download/) - Required for running the Truffle framework.
2. [Truffle](https://www.trufflesuite.com/docs/truffle/getting-started/installation) - Used for compiling, deploying, and testing smart contracts.
3. [Ganache](https://trufflesuite.com/ganache/) - Local Ethereum blockchain environment.
4. Python 3.x - Used for gas estimation and visualization.

1. [Node.js 和 npm](https://nodejs.org/en/download/) - 运行Truffle框架所需。
2. [Truffle](https://www.trufflesuite.com/docs/truffle/getting-started/installation) - 用于编译、部署和测试智能合约。
3. [Ganache](https://trufflesuite.com/ganache/) - 本地以太坊区块链环境。
4. Python 3.x - 用于Gas估算和可视化。

## Setup Instructions 配置指南

### 1. Clone the Repository 克隆仓库

```bash
git clone https://github.com/KevinLYT/ContractProject.git
cd ContractProject
```


### 2. Install Node Dependencies 安装Node依赖

```bash
npm install
```


### 3. Install Python Dependencies 安装Python依赖

```bash
pip install web3 numpy matplotlib
```


### 4. Start Ganache 启动Ganache

Launch Ganache to create a local blockchain environment.

启动Ganache以创建本地区块链环境。

### 5. Compile and Migrate Smart Contracts 编译并部署智能合约

Compile and deploy both the original and optimized versions of the smart contracts to the local blockchain.

编译并将原始版和优化版的智能合约部署到本地区块链。

```bash
truffle compile
truffle migrate
```


### 6. Run Python Script 运行Python脚本

To compare gas costs between the original and optimized contracts, use the Python script provided:

运行Python脚本，比较原始合约和优化合约的Gas费用：

```bash
python gas_estimation_comparison.py
```


## Project Structure 项目结构

```bash
ContractProject/
├── contracts/                 # Smart contracts (智能合约)
│   ├── MyContract.sol
│   └── OptimizedMyContract.sol
├── migrations/                # Deployment scripts (部署脚本)
│   └── 2_deploy_contracts.js
├── build/                     # Compiled contracts (编译后的合约)
│   └── contracts/
├── gas_estimation_comparison.py  # Python script to estimate gas costs (Python脚本用于估算Gas费用)
├── README.md                  # Project documentation (项目文档)
└── truffle-config.js          # Truffle configuration file (Truffle配置文件)
```


## Usage 用法

1. Start the local blockchain using Ganache.

   使用Ganache启动本地区块链。

2. Deploy both `MyContract` and `OptimizedMyContract` using Truffle.

   使用Truffle部署`MyContract`和`OptimizedMyContract`。

3. Run `gas_estimation_comparison.py` to simulate and visualize gas costs across different scenarios (Layer 1, Layer 2).

   运行`gas_estimation_comparison.py`，模拟并可视化不同场景下（Layer 1，Layer 2）的Gas费用。

## Smart Contracts 智能合约

The smart contracts are written in Solidity and deployed locally using Truffle. The project includes both an original version (MyContract.sol) and an optimized version (OptimizedMyContract.sol) that incorporates gas-reducing modifications inspired by literature research.

智能合约使用Solidity编写，并使用Truffle在本地部署。项目包括原始版本 (MyContract.sol) 和优化版本 (OptimizedMyContract.sol)，后者结合了文献研究中的Gas减少改进措施。

## Gas Cost Estimation Gas费用估算

The Python script gas_estimation_comparison.py simulates multiple transactions to estimate the gas costs across different scenarios, including:

- Layer 1 (Ganache local blockchain)
- Layer 2 Optimism Rollup
- Layer 2 ZK Rollup

Python脚本 gas_estimation_comparison.py 通过模拟多笔交易来估算不同场景下的Gas费用，包括：

- Layer 1 (Ganache本地区块链)
- Layer 2 Optimism Rollup
- Layer 2 ZK Rollup

The script utilizes random Gwei values and transaction samples to generate a realistic comparison, allowing for detailed visualization of gas usage trends.

脚本利用随机的Gwei值和交易样本生成真实的比较，允许详细地可视化Gas使用趋势。

## Results and Observations 结果与观察

- The optimized smart contract showed reduced gas costs compared to the original contract in most test scenarios.
- Layer 2 solutions, such as Optimism Rollup and ZK Rollup, demonstrated significant cost savings compared to Layer 1, supporting the feasibility of using these solutions to reduce costs in a production environment.

- 优化后的智能合约相比原始合约在大多数测试场景中展示了更低的Gas费用。
- Layer 2 解决方案，例如 Optimism Rollup 和 ZK Rollup，与 Layer 1 相比展现了显著的成本节约，支持在生产环境中使用这些解决方案以降低成本的可行性。

## References 参考文献

- Li, et al. "Gas Estimation and Optimization for Smart Contracts on Ethereum." Utilized in gas estimation methodology.
- "Efficient Storage Patterns in Solidity" for optimizing mappings and data structures to reduce storage gas costs.
- "Layer 2 Solutions and Their Effect on Gas Fees" to simulate gas reduction impacts in L2.

- Li 等人的《以太坊智能合约的Gas估算与优化》。用于Gas估算方法。
- 《Solidity中的高效存储模式》用于优化映射和数据结构以减少存储的Gas成本。
- 《Layer 2解决方案及其对Gas费用的影响》，用于模拟L2中Gas减少的效果。

## Contributing 贡献

Feel free to fork the repository and submit a pull request for any improvements. Contributions are welcome.

欢迎大家fork该仓库并提交pull request进行改进。

## License 许可证

This project is licensed under the MIT License.

本项目使用MIT许可证。
