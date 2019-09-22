// Initialize express router
let router = require('express').Router();

// Set default API response
router.get('/', function(req, res) {
	res.json({
		status: 'API is working',
		message: 'Welcome to LockRice crafted with tears!'
	});
});

// Import lock controller
var lockController = require('../controllers/lockController');

// Lock routes 
router.route('/locks')
	.get(lockController.index)
	.post(lockController.new);

router.route('/locks/:lock_id')
	.get(lockController.view)
	.patch(lockController.update)
	.put(lockController.update)
	.delete(lockController.delete);

//Export API routes
module.exports = router;

