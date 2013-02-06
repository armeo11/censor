# -*- coding: UTF8 -*-
#
#   Request-reply client in Python
#   Connects REQ socket to tcp://localhost:5559
#   Sends "Hello" to server, expects "World" back
#
import zmq

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")

#  Do 10 requests, waiting each time for a response
test = [
    'พาปุณณ์ไปหาหมอหน่อย',
    'วันนี้น้องปราณหกล้ม',
    'เมื่อเช้าปัณณ์ทะเลาะกับปราณ',
    'เปิ้ลรับน้องปุณณ์ไปด้วย'
]
for request in test:
    socket.send(request)
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"
