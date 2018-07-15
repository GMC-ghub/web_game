import web
from gothonweb1 import map

urls = (
	'/game', 'GameEngine',
	'/', 'Index',
	'/count', 'Guess_Count'
)

app = web.application(urls, globals())

#little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session
	
render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		# this is used to "setup" the session with starting values
		session.room = map.START
		web.seeother("/game")
		
class GameEngine(object):		
	def GET(self):
		
		if session.room:
			return render.show_room(room=session.room)
		else:
#			print "go nothing"
			return render.you_died()
			
	def POST(self):
		form = web.input(action=None)
		print session.room.name

		if session.room.name == "Laser weapon armory" and form.action !='132':
			print "bombbbbbb"
			session.room = session.room.go('*')

		# there is a bug here, fix it!
		elif session.room and form.action:
			session.room = session.room.go(form.action)
					
		web.seeother("/game")

class Guess_Count(object):
	def GET(self):
#		print "in the class_G"
#		if session.room == map.bomb_code_count:
#		cd_cnt = cd_cnt + 1
#			print cd_cnt
#		if cd_cnt > 9:
		session.room = map.laser_weapon_armory
		return render.show_room(room=map.laser_weapon_armory)

if __name__ == "__main__":
	app.run()
	