var express = require('express');
var app = express();
var http = require('http').Server(app);

var JIFFServer = require('/home/kali/Desktop/jiff/lib/jiff-server');
var jiff_instance = new JIFFServer(http, {
  logs: true,
  socketOptions: {
    pingTimeout: 10000,
    pingInterval: 2000
  }
});

var jiffBigNumberServer = require('/home/kali/Desktop/jiff/lib/ext/jiff-server-bignumber');
jiff_instance.apply_extension(jiffBigNumberServer);

app.use("/home/kali/Desktop/jiff/demos", express.static("demos"));
app.use("/home/kali/Desktop/jiff/lib", express.static("lib"));
app.use("/home/kali/Desktop/jiff/lib/ext", express.static("lib/ext"));
app.use("/home/kali/Desktop/jiff/bignumber.js", express.static("node_modules/bignumber.js"));

http.listen(9000, function()
{
	console.log('listening on *:9000');
});
