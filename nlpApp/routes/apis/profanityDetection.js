var keystone = require('keystone');
var swearjar = require('swearjar');

exports = module.exports = function(req, res) {
    var userQuery = req.query.q;

    var result = {
        profane : swearjar.profane(userQuery)
    }
    res.json(result)
}
