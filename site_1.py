from http.server import HTTPServer, BaseHTTPRequestHandler

ctg = {'Home' : ['Kitchen','Shower room','Bed room'], 'Cottage and garden': ['Tools', 'Seeds','Fertilizers'], 'For school': ['Books','Pencils','Other']}
names = ['about', 'categories']

def get_link(name):
    return f'<a href="http://localhost:8000/{name}">{name}</a>'

class MySiteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.render_index()
        elif self.path == '/about':
            self.render_about()
        elif self.path == "/categories":
            self.render_categories()
        else:
            super().do_GET()

    def render_index(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>Hello</h1>'.encode('utf-8'))
        self.wfile.write('<h2>Links:</h2>'.encode('utf-8'))
        for i in names:
            n = get_link(i)
            self.wfile.write(f'<h2>{n}</h2>'.encode('utf-8'))

    def render_about(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>About</h1>'.encode('utf-8'))
        self.wfile.write('<h2>This site is a small shop where you can find goods for home, <br>garden and summer cottage, and school supplies.</h2>'.encode('utf-8'))
    
    def render_categories(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>Categories</h1>'.encode('utf-8'))

        for i in ctg:
            self.wfile.write(('<ul>').encode('utf-8'))                       
            self.wfile.write(('<h3>' + i + '</h3>').encode('utf-8'))
            for j in ctg[i]:
                self.wfile.write(('<li><h6>' + j + '</h6></li>').encode('utf-8'))
            self.wfile.write(('</ul>').encode('utf-8')) 


def run():
    httpd = HTTPServer(('',8000), MySiteHandler)
    print("server start")
    httpd.serve_forever()

if __name__ == '__main__':
    run()