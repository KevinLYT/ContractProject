from web3 import Web3
import json
import numpy as np
import matplotlib.pyplot as plt

# Step 1: 连接到本地的Ganache节点（Layer 1）
w3_ganache = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# 验证连接是否成功
if not w3_ganache.is_connected():
    print("Failed to connect to Ganache")
    exit()

print("Connected to Ganache network!")

# Step 2: 设置默认账户
w3_ganache.eth.default_account = w3_ganache.eth.accounts[0]  # 使用Ganache生成的第一个账户

# Step 3: 获取两个智能合约的地址和ABI
mycontract_address = "0x43d6311199236a1e4a5C06403c0d75720eF4c56A"  # 请替换为实际部署后的MyContract地址
optimized_contract_address = "0xDc869C35cBE4c4476a63E57d00260eC21CfaC760"  # 请替换为实际部署后的OptimizedMyContract地址

# 读取MyContract的ABI文件
with open('C:/Users/13621/Desktop/MyContractProject/build/contracts/MyContract.json', encoding='utf-8') as f:
    mycontract_data = json.load(f)
mycontract_abi = mycontract_data['abi']

# 读取OptimizedMyContract的ABI文件
with open('C:/Users/13621/Desktop/MyContractProject/build/contracts/OptimizedMyContract.json', encoding='utf-8') as f:
    optimized_contract_data = json.load(f)
optimized_contract_abi = optimized_contract_data['abi']

# Step 4: 获取合约实例
mycontract = w3_ganache.eth.contract(address=mycontract_address, abi=mycontract_abi)
optimized_contract = w3_ganache.eth.contract(address=optimized_contract_address, abi=optimized_contract_abi)

# Step 5: 准备发送的消息内容
recipient_address = w3_ganache.eth.accounts[1]  # 使用Ganache的第二个账户作为接收方
message_content = "Hello, this is a test message!"

# Step 6: 调用sendMessage函数并获取交易信息
def send_message(web3, contract, recipient_address, message_content):
    try:
        # 调用sendMessage函数
        tx_hash = contract.functions.sendMessage(recipient_address, message_content).transact()
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction successful with hash: {tx_hash.hex()}")
        return tx_receipt
    except Exception as e:
        print(f"Error while sending message: {e}")
        return None

# 发送交易到Ganache链
tx_receipt_mycontract = send_message(w3_ganache, mycontract, recipient_address, message_content)
tx_receipt_optimized_contract = send_message(w3_ganache, optimized_contract, recipient_address, message_content)

# Step 7: 模拟不同网络的gas消耗情况
# MyContract测量到的Ganache的gas消耗
gas_used_mycontract = tx_receipt_mycontract['gasUsed'] if tx_receipt_mycontract else 21000  # 使用基本交易的 gas 作为默认值

# OptimizedMyContract测量到的Ganache的gas消耗
gas_used_optimized = tx_receipt_optimized_contract['gasUsed'] if tx_receipt_optimized_contract else 21000

# 设置模拟的交易样本数量
num_samples = 100
np.random.seed(42)

# 模拟不同场景的 Gwei 价格和 Gas 使用量
gwei_prices = np.clip(np.random.normal(50, 20, num_samples), 10, 100)

# MyContract 数据
ganache_gas_usages_mycontract = gas_used_mycontract + np.random.randint(-1000, 1000, num_samples)
ganache_gas_costs_mycontract = [(gas * gwei) / 1e9 for gas, gwei in zip(ganache_gas_usages_mycontract, gwei_prices)]

optimism_gas_usages_mycontract = gas_used_mycontract * 0.2 + np.random.randint(-300, 300, num_samples)
optimism_gas_costs_mycontract = [(gas * gwei) / 1e9 for gas, gwei in zip(optimism_gas_usages_mycontract, gwei_prices)]

zk_gas_usages_mycontract = gas_used_mycontract * 0.1 + np.random.randint(-200, 200, num_samples)
zk_gas_costs_mycontract = [(gas * gwei) / 1e9 for gas, gwei in zip(zk_gas_usages_mycontract, gwei_prices)]

# OptimizedMyContract 数据
ganache_gas_usages_optimized = gas_used_optimized + np.random.randint(-1000, 1000, num_samples)
ganache_gas_costs_optimized = [(gas * gwei) / 1e9 for gas, gwei in zip(ganache_gas_usages_optimized, gwei_prices)]

optimism_gas_usages_optimized = gas_used_optimized * 0.2 + np.random.randint(-300, 300, num_samples)
optimism_gas_costs_optimized = [(gas * gwei) / 1e9 for gas, gwei in zip(optimism_gas_usages_optimized, gwei_prices)]

zk_gas_usages_optimized = gas_used_optimized * 0.1 + np.random.randint(-200, 200, num_samples)
zk_gas_costs_optimized = [(gas * gwei) / 1e9 for gas, gwei in zip(zk_gas_usages_optimized, gwei_prices)]

# 模拟的交易索引（从 1 到 100，每个点的序号）
transaction_indexes = np.arange(1, num_samples + 1)

# Step 8: 使用matplotlib绘制两个合约交易的gas消耗对比图
fig, axs = plt.subplots(1, 2, figsize=(20, 10))

# MyContract 的 Gas 消耗
axs[0].scatter(transaction_indexes, ganache_gas_costs_mycontract, c=gwei_prices, cmap='Blues', alpha=0.6, label='Ganache (Layer 1)')
axs[0].scatter(transaction_indexes, optimism_gas_costs_mycontract, c=gwei_prices, cmap='Oranges', alpha=0.6, label='Optimism Rollup (Layer 2)')
axs[0].scatter(transaction_indexes, zk_gas_costs_mycontract, c=gwei_prices, cmap='Greens', alpha=0.6, label='ZK Rollup (Layer 2)')
axs[0].set_title("Gas Cost Comparison: MyContract (Original)")
axs[0].set_xlabel("Transaction Index")
axs[0].set_ylabel("Gas Cost (ETH)")
axs[0].grid(axis='y', linestyle='--')
axs[0].legend()

# OptimizedMyContract 的 Gas 消耗
axs[1].scatter(transaction_indexes, ganache_gas_costs_optimized, c=gwei_prices, cmap='Blues', alpha=0.6, label='Ganache (Layer 1)')
axs[1].scatter(transaction_indexes, optimism_gas_costs_optimized, c=gwei_prices, cmap='Oranges', alpha=0.6, label='Optimism Rollup (Layer 2)')
axs[1].scatter(transaction_indexes, zk_gas_costs_optimized, c=gwei_prices, cmap='Greens', alpha=0.6, label='ZK Rollup (Layer 2)')
axs[1].set_title("Gas Cost Comparison: OptimizedMyContract")
axs[1].set_xlabel("Transaction Index")
axs[1].set_ylabel("Gas Cost (ETH)")
axs[1].grid(axis='y', linestyle='--')
axs[1].legend()

# 添加颜色条以表示 Gwei 价格
cbar = fig.colorbar(axs[1].collections[0], ax=axs, orientation='vertical', fraction=.1)
cbar.set_label('Gwei Price')

plt.show()
