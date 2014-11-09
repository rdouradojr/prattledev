import render
import webapp2

class Handler(webapp2.RequestHandler):

  # Handles all HTTP GET requests to the '/copy_me' path
  def get(self):
    # Here is where you should put your code for when you create a
    # new handler.
    template_values = {}      
    render.TemplateResponse('copy_me.html', template_values, self.response)
