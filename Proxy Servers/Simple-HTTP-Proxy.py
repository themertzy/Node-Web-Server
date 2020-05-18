import SocketServer
import SimpleHTTPServer
import urllib

PORT = 1234

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.copyfile(urllib.urlopen(self.path), self.wfile)

httpd = SocketServer.ForkingTCPServer(('', PORT), Proxy)
print "serving at port", PORT
httpd.serve_forever()

#The server ignores drive letters and relative path names (such as ‘..’). However, it does not implement any other access control mechanisms, so be careful how you use it.
#The second example implements a truly minimal web proxy. When sent to a proxy, the HTTP requests should include the full URI for the target server. This server uses urllib to fetch data from the target.
