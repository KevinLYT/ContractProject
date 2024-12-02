// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MyContract {
    struct Message {
        address from;
        address to;
        string content;
        uint256 timestamp;
    }

    // 存储每个地址接收到的消息
    mapping(address => Message[]) private receivedMessages;

    // 事件：发送消息
    event MessageSent(address indexed from, address indexed to, string content, uint256 timestamp);
    event DebugMessageStored(address indexed to, uint256 messageCount);

    // 发送消息给某个地址
    function sendMessage(address _to, string calldata _content) external {
        require(_to != address(0), "Invalid recipient address");
        require(bytes(_content).length > 0, "Message content cannot be empty");

        // 创建消息结构
        Message memory newMessage = Message(msg.sender, _to, _content, block.timestamp);

        // 存储到接收地址的消息列表
        receivedMessages[_to].push(newMessage);

        // 触发事件
        emit MessageSent(msg.sender, _to, _content, block.timestamp);
        // 触发调试事件
        emit DebugMessageStored(_to, receivedMessages[_to].length);
    }

    // 获取某个地址接收到的所有消息，包括消息内容和发送方地址
    function receiveMessagesContentWithSender() external view returns (string[] memory, address[] memory) {
        uint256 messageCount = receivedMessages[msg.sender].length;
        string[] memory contents = new string[](messageCount);
        address[] memory senders = new address[](messageCount);

        for (uint256 i = 0; i < messageCount; i++) {
            contents[i] = receivedMessages[msg.sender][i].content;
            senders[i] = receivedMessages[msg.sender][i].from;
        }

        return (contents, senders);
    }

}
