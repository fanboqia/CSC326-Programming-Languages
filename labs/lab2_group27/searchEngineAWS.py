#######~~~~~~~~~~~~~~~~~~Change the library path when you test it~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~############
import re, collections, Cookie, signal, sys, os
import sqlite3
sys.path.insert(0,'bottle/')
import bottle
from bottle import route, run, template, static_file, get,post, request, response, redirect, error
from operator import itemgetter, attrgetter
sys.path.insert(0,'beaker/')
from beaker.middleware import SessionMiddleware
#######~~~~~~~~~~~~~~~~~~Submitted Lab2 Version~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~############

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)

#Static Routesb

# import urllib2
# response = urllib2.urlopen('https://github.com/benjaminp/six/blob/master/six.py')
# html = response.read()
import httplib2
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets 
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
#global variables
keyDicGlobal = {}
allUserLogInInfo = {}   # store in format {userOne_Email:{'email':'boqianfan@gmail.com','name':'boqianfan','picture':'...'},userTwo_Email:{:}}
allUserSearchWord = {}  # store in format {userOne_email: [search words], userTwo_email: [search words]}
allUserSearchHistoryCount = {} # store in format {userOne_Email:{'a': 1,'b': 2, picture':'...'},userTwo_Email:{:}}
#indicating first enter the website
visitCount = 0
signInFlag = False
#paramters
# user_email = None

LOCAL_SCOPE = 'https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email'
LOCAL_REDIRECT_URI = 'http://localhost:8080/redirect'
LOCAL_CLIENT_ID = '1094415649431-0uvji2qlf464m55q6j2stkko4f85icg4.apps.googleusercontent.com'
LOCAL_CLIENT_SECRET = 'xxxxxxxxxx'

AWS_SCOPE = 'https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email'
AWS_REDIRECT_URI = 'http://ec2-34-234-38-53.compute-1.amazonaws.com/redirect'
AWS_CLIENT_ID = '1094415649431-35qhgnqnhom2j039r30j91bhie3ten1b.apps.googleusercontent.com'
AWS_CLIENT_SECRET = 'xxxxxxxxx'

#reference on https://stackoverflow.com/questions/10486224/bottle-static-files
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/font")

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")
##############################################################################

# from bottle import route, request, response
# @route('/counter')
# def counter():
#     count = int( request.cookies.get('counter', '0') )
#     count += 1
#     response.set_cookie('counter', str(count))
#     return 'You visited this page %d times' % count

@error(404)
def errorPage(error):
	return '''<p><b>ERROR 404: PAGE NOT FOUND</b></p>
	However, if this is exactly the page you are looking for:
	Congratulations! You've finally found it.'''

@route('/signin',method = "POST")
def signIn():
	# global signInFlag
	# signInFlag = True
	flow = flow_from_clientsecrets('AWS_VERSION_GOOGLE_KEY.json', scope = AWS_SCOPE, redirect_uri = AWS_REDIRECT_URI)
	uri = flow.step1_get_authorize_url() 
	bottle.redirect(uri)

#~~~~~~~~~~~~~~one page displaying results version~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@route('/',method = "GET")
def index():
	# global user_email
	# hold a session for the current accessing user
	global allUserLogInInfo
	global allUserSearchWord
	global allUserSearchHistoryCount

	keywords = []
	keyList = []
	keyListInInputOrder = []

	#get method analysis
	if request.GET.get('keywords') != None:
		keywords = request.GET.get('keywords').lower()
	#print keywords
	#keywords = re.sub( '\s+', ' ', keywords ).strip().lower()
	# print "key words: "+str(keywords)
	if keywords:
		keyList = keywords.split()
	# print "keylistfor one time: ",keyList

	#if not in the new list, just add it; if in the new list, then don't add it
	for key in keyList:
			if key not in keyListInInputOrder:
				keyListInInputOrder.append(key)
	# print "key list in put order: ",keyListInInputOrder		

	# restricted to one request route, display only one submit result
	keyDic = {}
	for key in keyList:
		if keyDic.has_key(key):
			keyDic[key] += 1
		else:
			keyDic[key] = 1

	s = bottle.request.environ.get('beaker.session')

	# determine if the user logs in
	# logged in 
	if 'email' in s:
		print "i am logged in..."
		email = s['email']
		picture = s['picture'] 
		name = s['name']
		
		print "start to store user specific information:"

		if email not in allUserSearchWord:
			allUserSearchWord[email] = []
		if email not in allUserSearchHistoryCount:
			allUserSearchHistoryCount[email] = {}

		# store specific user search words 
		if allUserSearchWord.has_key(email):
			if len(keywords) != 0:
				allUserSearchWord[email].append(keywords)

		# store specific user search words count

		if allUserSearchHistoryCount.has_key(email):
			for key in keyList:
				if allUserSearchHistoryCount[email].has_key(key):
					allUserSearchHistoryCount[email][key] += 1
				else:
					allUserSearchHistoryCount[email][key] = 1

		print "___________email: ", allUserSearchHistoryCount[email]
		print "___________UserInfo: ", email, picture, name
		print "___________SearchWords: ", allUserSearchWord[email]

		keyTimesTuple = sorted(allUserSearchHistoryCount[email].items()[:20], key=itemgetter(1,0), reverse = True)

		return template('views/searchEngineAWSHomePage.tpl', keyTimesTuple =  keyTimesTuple, keywords = keywords, keyListInInputOrder = keyListInInputOrder, keyDic = keyDic, user_email = email,picture = picture, name = name, searchword = allUserSearchWord[email])

	# not logged in 
	else:
		print "i am not logged in..."
		return template('views/searchEngineAWSHomePage.tpl', keyTimesTuple =  None, keywords = keywords, keyListInInputOrder = keyListInInputOrder, keyDic = keyDic, user_email = None, picture = None, name = None, searchword = None)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@route('/redirect') 
def redirect_page():

	code = request.query.get('code', '')
	flow = OAuth2WebServerFlow( client_id= AWS_CLIENT_ID, client_secret= AWS_CLIENT_SECRET,scope=AWS_SCOPE, redirect_uri=AWS_REDIRECT_URI)
	credentials = flow.step2_exchange(code) 
	token = credentials.id_token['sub']

	http = httplib2.Http()
	http = credentials.authorize(http)

	users_service = build('oauth2', 'v2', http=http) 
	user_document = users_service.userinfo().get().execute() 
	s = bottle.request.environ.get('beaker.session')
	s['email'] = user_document['email']
	s['picture'] = user_document['picture']
	s['name'] = user_document['name']
	s.save()

	# specific user information obtained
	# if the user has not registered in the database
	email = s['email']
	picture = s['picture']
	name = s['name']
	global allUserLogInInfo
	global allUserSearchWord
	global allUserSearchHistoryCount
	if email not in allUserLogInInfo:
		allUserLogInInfo[email] = {'email':email, 'picture': picture, 'name': name}
	if email not in allUserSearchWord:
		allUserSearchWord[email] = []
	if email not in allUserSearchHistoryCount:
		allUserSearchHistoryCount[email] = {}

	print "_______redirect: email : ",s['email']
	print "_______redirect: pic : ",s['picture']
	print "_______redirect: name : ",s['name']
	#email = session['user_email']
	redirect('/')

@route('/logout')
def logout():
	#when log out clear the current user_email information
	# global user_email
	# user_email = None
	s = bottle.request.environ.get('beaker.session')
	s.delete()
	#print "_______logout: email : ",s['email']
	redirect('/')

#~~~~~~~~~~~~~~two pages displaying results version~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @route('/',method = "GET")
# def index():
	
# 	# conn = sqlite3.connect('searchHistory.db')

# 	# conn.execute("CREATE TABLE IF NOT EXISTS searchWord_To_Times(keyword TEXT, frequency INTEGER);")

# 	# cursor = conn.execute("SELECT keyword,frequency from searchWord_To_Times")

# 	# for row in cursor:
#  #   		print "KEYWORD = ", row[0]
#  #   		print "FREQUENCY = ", row[1]

#    	# sort value from greatest to the smallest with maximum 20 keywords
#    	# sort by value first, then by key 
#    	keyTimesTuple = sorted(keyDicGlobal.items()[:20], key=itemgetter(1,0), reverse = True)

# 	return template('index.tpl', keyTimesTuple = keyTimesTuple, )	

# @route('/results', method = "GET")
# def results():

# 	# conn = sqlite3.connect('searchHistory.db')

# 	# conn.execute("CREATE TABLE IF NOT EXISTS searchWord_To_Times(keyword TEXT, frequency INTEGER);")

# 	#get method analysis
# 	keywords = request.GET.get('keywords').lower()
# 	#print keywords
# 	#keywords = re.sub( '\s+', ' ', keywords ).strip().lower()
# 	# print "key words: "+str(keywords)
# 	keyList = []
# 	if keywords:
# 		keyList = keywords.split()
# 	# print "keylistfor one time: ",keyList

# 	#if not in the new list, just add it; if in the new list, then don't add it
# 	keyListInInputOrder = []
# 	for key in keyList:
# 			if key not in keyListInInputOrder:
# 				keyListInInputOrder.append(key)
# 	# print "key list in put order: ",keyListInInputOrder				

# 	#store a global keyDic to count the history of 20 popular key words
# 	global keyDicGlobal

# 	for key in keyList:
# 		if keyDicGlobal.has_key(key):
# 			keyDicGlobal[key] += 1
# 		else:
# 			keyDicGlobal[key] = 1

# 	# restricted to one request route, display only one submit result
# 	keyDic = {}
# 	for key in keyList:
# 		if keyDic.has_key(key):
# 			keyDic[key] += 1
# 		else:
# 			keyDic[key] = 1


# #planning to store twenty most recent history in sqlite3 
# 	# for key in keyDic:
# 	# 	conn.execute("INSERT INTO searchWord_To_Times (keyword,frequency) VALUES(?,?)",(key,keyDic[key]))	

# 	# cursor = conn.execute("SELECT keyword,frequency from searchWord_To_Times")
# 	# for row in cursor:
#  #   		print "KEYWORD = ", row[0]
#  #   		print "FREQUENCY = ", row[1]	

# 	return template('results.tpl',keywords = keywords, keyListInInputOrder = keyListInInputOrder, keyDic = keyDic)	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~		

run(host='0.0.0.0', port=80, debug = True, app = app)



