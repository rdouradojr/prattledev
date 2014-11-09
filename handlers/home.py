import render
import webapp2

from google.appengine.ext import ndb

class Message(ndb.Model):
  person = ndb.StringProperty(required=True)
  content = ndb.StringProperty(required=True)
  team = ndb.StringProperty(required = True)

class Handler(webapp2.RequestHandler):

  # Handles all HTTP GET requests sent to the '/' path.
  def get(self):
    
    name = self.request.get('team')
    messages = Message.query(Message.team==name)
    messages1 = Message.query()
    template_values = {
      'name': 'Prattle', 
      'date': 'Today', 
      'messages': messages,
      'messages1': messages1,
    }
    render.TemplateResponse('home.html', template_values, self.response)

  def post(self):
    name = self.request.get('moniker')
    message1 = self.request.get('team')
    message = self.request.get('message')
    Message(person=name, content=message, team=message1).put()
    render.TextResponse(name +"said " + message, self.response)                                                        
