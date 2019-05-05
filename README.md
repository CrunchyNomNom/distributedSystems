## distributedSystems: middleware
### Requirements:
 * python3
 * npm + node
 * ZeroC ICE
 * gRPC

### Setup:
 * ```cd grpc && npm install```

### Start:
You need to start three instances in given order to start:
 1. ```cd grpc && node currency-service.js```
 2. ```python3 server.py```
    * You will be prompted to provide number of currencies (1-4) and which you are interested in {USD, EUR, GBP, CHF}.
 3. ```python3 client.py```
    * commands:
        * register
        * login
        * quit
    * after logging in:
        * balance
        * loan (only PREMIUM account)
        * logout