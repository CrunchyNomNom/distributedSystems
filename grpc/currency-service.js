var PROTO_PATH = 'currency.proto';
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
var randItem = require('random-item')

var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var currencies = grpc.loadPackageDefinition(packageDefinition).currencies;

var values = {
    'USD': 3.81,
    'EUR': 4.31,
    'GBP': 5.01,
    'CHF': 3.75
}

var streams = {
    'USD': [],
    'EUR': [],
    'GBP': [],
    'CHF': []
}

function valueChange(){
    var tmp = randItem(['USD', 'EUR', 'GBP', 'CHF']);
    values[tmp] *= (1 + (Math.random() - 0.5) / 20);  // -5% - +5%
    console.log(tmp, ': ', values[tmp]);
    streams[tmp].forEach(call => {
        call.write({
            currency: tmp,
            value: values[tmp]
        });
    });
    setTimeout(() => {
        valueChange();
    }, 5000);
}

function register(call) {
    console.log(call.request);
    call.request.otherCurrency.forEach(curr => {
        streams[curr].push(call);
        call.write({
            currency: curr,
            value: values[curr]
        })
    });
}

function getServer() {
    var server = new grpc.Server();
    server.addProtoService(currencies.Currencies.service, {
        register: register,
    });
    return server;
}
    
function main(){
    var server = getServer();
    server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
    server.start();
    valueChange();
}

main();