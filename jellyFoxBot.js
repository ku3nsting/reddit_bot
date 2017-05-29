var auth	 = require('reddit-oauth');
var stream   = require('reddit-stream');

var API = new auth({
	app_id: 'mwIDSk_NS7wdfA',
	app_secret: 'e20oW7onHksbD8qWBXkwzNfhYNQ'
})

API.passAuth(
	'JellyFoxBot', 'Wenceslas111',
	function(success){
		if(success){
			console.log(API.access_token);
		}
	})
	
var commentStr = new stream('comments', 'wholesomememes', 'mwIDSk_NS7wdfA');
var streaming = true;
var x;

//start the stream
commentStr.start();
console.log("stream begun!");

//get some comments from the subreddit
commentStr.on('wholesomememes', function(comments) {
  console.log('found', comments.length, 'comment(s)');
  
  for(x in comments){
  if(comments.data == "I just need a hug"){
	
	  // respond
  return reddit('/api/comment').post({
    api_type: "json",
	text: "*hugs*",
	thing_id: comments._id //parent comment
  }).then(function() {
  console.log('message sent');
});
  }
  }
  });
