var app = require('express')()


app.use(function(req, res, next) {
  if (req.method == 'GET') {
    res.set('Access-Control-Allow-Origin', '*')
  }
  next()
})

app.get('/weeby/magic', function(req, res) {
  // Happy hacking :)
  res.send('hello, world')
})

var server = app.listen(1337, function() {
  var host = server.address().address
  var port = server.address().port
  console.log('listening at http://%s:%s', host, port)
})
