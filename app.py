from src.banner import NAME
import os,json
from http.server import HTTPServer,BaseHTTPRequestHandler
MODE=os.environ.get('APP_MODE','development')
if MODE not in ('production','staging'): raise SystemExit('APP_MODE must be production or staging')
if os.environ.get('REQUIRE_TOKEN')=='1' and not os.environ.get('API_TOKEN'): raise SystemExit('API_TOKEN missing')
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path=='/health': data={'status':'ok'}
  elif self.path=='/config': data={'environment':MODE}
  else: self.send_error(404);return
  body=json.dumps(data).encode();self.send_response(200);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(body)
print('Listening on '+os.environ.get('BIND','0.0.0.0')+':8080',flush=True)
HTTPServer((os.environ.get('BIND','0.0.0.0'),8080),Handler).serve_forever()
