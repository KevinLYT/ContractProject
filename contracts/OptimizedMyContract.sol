// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OptimizedMyContract {
    struct MessageMetadata {
        string content;
        uint256 timestamp;
    }

    mapping(address => mapping(uint256 => MessageMetadata)) private receivedMessages; // 使用mapping存储消息
    mapping(address => uint256) private receivedMessageCount; // 每个用户接收的消息数量

    event MessageSent(address indexed from, address indexed to, string content, uint256 timestamp);

    function sendMessage(address _to, string calldata _content) external {
        require(_to != address(0), "Invalid recipient address");
        require(bytes(_content).length > 0, "Message content cannot be empty");

        uint256 currentCount = receivedMessageCount[_to];
        receivedMessages[_to][currentCount] = MessageMetadata(_content, block.timestamp);
        receivedMessageCount[_to] = currentCount + 1;

        emit MessageSent(msg.sender, _to, _content, block.timestamp);
    }

    function receiveMessagesContentWithSender() external view returns (string[] memory, address[] memory) {
        uint256 messageCount = receivedMessageCount[msg.sender];
        string[] memory contents = new string[](messageCount);
        address[] memory senders = new address[](messageCount);

        for (uint256 i = 0; i < messageCount; i++) {
            contents[i] = receivedMessages[msg.sender][i].content;
            senders[i] = msg.sender; // 消息是由外部调用者获取，因此发送方即为请求方
        }

        return (contents, senders);
    }
}
