# Ethereum Sharding Experiment

## Dependencies

- NodeJS

## Steps

1. Login to AWS, start all 5 instances
2. Login to bootnode, run:
```
~/go-ethereum/build/bin/bootnode --nodekey=boot.key --addr=172.31.44.22:24765 --verbosity 9
```
3. Login to other nodes, run
```
cd ~/contract-sharing-experiment/transaction-generator/ && . ./eth_launch
```
4. Login to one of the miner node with
```
ssh -i "Ethereum Experiment.pem" ubuntu@example.us-west-2.compute.amazonaws.com -L 8545:localhost:8545
```
5. At local, go to project folder
```
cd /PATH/contract-sharing-experiment/transaction-generator
```
6. `npm i`
7. `node ./TG_main.js --help`
8. Charge up first n accounts in TG_worker.js with eth from the first account. You can use metamask and connect to localhost:8545 to do so.
9. Run `node ./TG_main.js` with your parameters.