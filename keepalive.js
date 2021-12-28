//this is for replit hosting only, ignore if you are self-hosting
//see the readme for more info
http = require('http');

http.createServer(function (req, res) {
  res.write("Securly's Marriage Bot is Online!");
  res.end();
}).listen(8080);