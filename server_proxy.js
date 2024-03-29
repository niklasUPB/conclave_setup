var express = require('express');
var app = express();
var http = require('http').Server(app);

var JIFFServer = require('/home/conclave_setup/jiff/lib/jiff-server');
var jiff_instance = new JIFFServer(http, {
  logs: true,
	// 2 mal 500000 ging für 40 mit reconnect.
	//5000000 ging ganz gut 
  socketOptions: {
    pingTimeout: 50000000,
    pingInterval: 50000000
  }
});

var jiffBigNumberServer = require('/home/conclave_setup/jiff/lib/ext/jiff-server-bignumber');
jiff_instance.apply_extension(jiffBigNumberServer);

app.use("/home/conclave_setup/jiff/demos", express.static("demos"));
app.use("/home/conclave_setup/jiff/lib", express.static("lib"));
app.use("/home/conclave_setup/jiff/lib/ext", express.static("lib/ext"));
app.use("/home/conclave_setup/jiff/bignumber.js", express.static("node_modules/bignumber.js"));

http.listen(9005, function()
{
	console.log('listening on *:9005');
});
