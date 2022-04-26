pragma solidity ^0.4.22;

contract testContract1{
    struct CallRecord{
        address from;
        uint time;
    }

    CallRecord[] public callRecords;
    uint public numberOfCallRecords;
    address owner;

    constructor() public{
        owner = msg.sender;
        numberOfCallRecords = 0;
    }

    function call() public{
        callRecords.push(CallRecord({
            from: msg.sender,
            time: block.timestamp
        }));
    }
}