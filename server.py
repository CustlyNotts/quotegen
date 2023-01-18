import os
import json
import random
import http.server
import socketserver

FONT_SIZE = os.environ.get('FONT_SIZE', '20')
RAW_INDEX_CONTENTS = bytes(open('./index.html').read(), 'UTF-8')
QUOTES = [
   'Live, laugh, love.',
   'Keep calm and carry on.',
   'Do what you feel in your heart to be right – for you’ll be criticized anyway.',
   'You may not control all the events that happen to you, but you can decide not to be reduced by them',
   'Truth is, everybody is going to hurt you; you just gotta find the ones worth suffering for'
   'If life gives you lemons, make lemonade',
   'You miss 100 percent of the shots you dont take',
   'Be the change you wish to see in the world',
   'Be kind, for everyone you meet is fighting a hard battle.',
   'Life is what happens when you are busy making other plans.',
   'If life were predictable it would cease to be life, and be without flavor.',
   'The way to get started is to quit talking and begin doing.',
   'The greatest glory in living lies not in never falling, but in rising every time we fall.',
   'Spread love everywhere you go. Let no one ever come to you without leaving happier.',
   'When you reach the end of your rope, tie a knot in it and hang on.',
   'lways remember that you are absolutely unique. Just like everyone else.',
   'Tell me and I forget. Teach me and I remember. Involve me and I learn.',
   'The best and most beautiful things in the world cannot be seen or even touched — they must be felt with the heart.',
   'Do not go where the path may lead, go instead where there is no path and leave a trail.',
   'It is during our darkest moments that we must focus to see the light.',
   'Learning to unlearn is the highest form of learning.'
]

def get_quote():
   return {'size': FONT_SIZE, 'text': random.choice(QUOTES)}

class Server(http.server.SimpleHTTPRequestHandler):
   def do_GET(self):
       path = self.path
       if path == '/' or path == '/index.html':
           self.send_response(200, 'OK')
           self.send_header('Content-type', 'text/html')
           self.end_headers()
           self.wfile.write(RAW_INDEX_CONTENTS)
       elif path == '/quote':
           quote = get_quote()
           self.send_response(200, 'OK')
           self.send_header('Content-type', 'application/json')
           self.end_headers()
           self.wfile.write(bytes(json.dumps(quote), 'UTF-8'))
       else:
           self.send_response(404, 'NOT FOUND')

if __name__ == '__main__':
   print('Starting server...')
   socketserver.TCPServer(('0.0.0.0', 8080), Server).serve_forever()

