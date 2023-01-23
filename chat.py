from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class SimpleChat(WebSocket):

    def handleMessage(self):
       print("handle msg")
       print(self.address[0] + ": " + self.data)
       for client in clients:
          if client != self:
             client.sendMessage(self.data)
          #self.address[0] + u' - ' + self.data)

    def handleConnected(self):
       print(self.address, 'connected')
       #for client in clients:
       #   client.sendMessage(self.address[0] + u' - connected')
       clients.append(self)

    def handleClose(self):
       clients.remove(self)
       print(self.address, 'closed')
       #for client in clients:
       #   client.sendMessage(self.address[0] + u' - disconnected')


#
server = SimpleWebSocketServer('localhost', 25560, SimpleChat)
server.serveforever()
