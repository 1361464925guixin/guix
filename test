# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,x):
        x = 9 if x == None else int(x)
        y = int(self.get_argument('n',10))
        if y!=10:
            x=None
        if 0<y<10:
            x=y
    
        html = '''
        <html>
        <body>
        '''
        if  0 < x < 10:
            for i in range(1,x+1,1):
                for j in range (1,i+1,1):
                    if i*j>9:
                        html += str("%d*%d=%-100d" % (j,i,j*i)) + '&nbsp;&nbsp;'              
                    else:
                        html += str("%d*%d=%-100d" % (j,i,j*i)) + '&nbsp;&nbsp;&nbsp;&nbsp;' 
                html += '</br>'
            html += '''      
        </body>
        </html>'''
        self.write(html)

application = tornado.web.Application([
    (r"/([0-9])?", MainHandler)
    ], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

