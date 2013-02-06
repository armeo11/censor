# -*- coding: UTF8 -*-
#
#   Request-reply service in Python
#   Connects REP socket to tcp://localhost:5560
#   Expects "Hello" from client, replies with "World"
#
import zmq
import esm

m = esm.Index()
m.enter("ป๊อก")
m.enter('ปัณณ์')
m.enter("เปิ้ล")
m.enter("ปุณณ์")
m.enter("ปราณ")
m.fix()


def censor(message):
    for result in m.query(message):
        message = message.replace(result[1], '@@@@@@')
    return message


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")


while True:
    message = socket.recv()
    print "Received request: ", message
    result = censor(message)
    socket.send(result)
