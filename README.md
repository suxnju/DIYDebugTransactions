# DIY : Create a Virtual Environment for Executing Transactions

fix bugs: remember that the order of transactions depends on Block timestamp and transaction index, nonce is the index of transaction from the same user.
> ref: https://ethereum.stackexchange.com/questions/53265/what-does-a-position-means-in-an-ethereum-tx/53266

0x68a787630b352c592a9543b7dafc8bf99d757d485e9999eae193f2528ee21512出错，CALL指令也会修改Memory，会动态取值
- 暂时解决不了合约调用合约的情况，比如该合约会通过调用其他合约检测balanceOf是否与传入的参数值一样，不一样会执行转账
Skip掉所有Require判断？