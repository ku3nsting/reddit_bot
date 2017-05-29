# import the PRAW library for use in your application
import praw

# create an instance of the praw class -- this is the bot
jfBot = praw.Reddit(user_agent='TheJellyFoxBot',
                  client_id='mwIDSk_NS7wdfA',
                  client_secret='e20oW7onHksbD8qWBXkwzNfhYNQ',
                  username='JellyFoxBot',
                  password='Wenceslas111')
				  
# identify a specific subreddit and store in a variable
# this way your bot can interact with data in that subreddit
# I chose r/wholesomememes because it's SFW and friendly
# consult http://progur.com/2016/09/how-to-create-reddit-bot-using-praw4.html
# for an example
subreddit = jfBot.subreddit('wholesomememes')

# the subreddit object has a stream property
# use this to monitor comments being made in the subreddit
comments = subreddit.stream.comments()

# Every comment has a body and an author (these are class properties)
# we can use a loop to access those properties
for comment in comments:
	text = comment.body 			# get the body
	author = comment.author 		# get the author
	#print "found a comment by "+str(author)
	
	# The bot will reply to specific needs, instead of blanketly responding to *any*
	# needlike phrase to avoid becoming a nuisance
	#In the testing process, I realized another bot is already performing this task!
	#changed the activation string a little to avoid overlap
	
	#If hug needed
	if 'i just need a hug' in text.lower():	
		
		#report message found
		print "found a comment by "+str(author)
        
		# Generate a reply
		hug = "*hugs*".format(author)
		
		#the reply function sends the message via the Reddit API
		comment.reply(hug)
		