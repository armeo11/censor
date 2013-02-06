Requirement
===========
1. install zmq
[mac os x]
brew install zmq
pip install pyzmq

2. install emsre
pip install esmre

Architecture
============



       +------------+    +------------+    +------------+   +------------+
       |   client   |    |   client   |    |   client   |   |   client   |
       |------------|    |------------|    |------------|   |------------|
       |  zmq(req)  |    |  zmq(req)  |    |  zmq(req)  |   |   zmq(req) |
       |            |    |            |    |            |   |            |
       |            |    |            |    |            |   |            |
       +------+-----+    +-------+----+    +-+----------+   +-----+------+
              |                  +----+      |                    |
              +---------------------+ |      |+-------------------+
                                    | |      ||
                                  +-+-+------+++
                                  |   broker   |
                                  |------------|
                                  | zmq(ROUTER)|
                                  |            |
                                  | zmq(DEALER)|
                                  +-++------+-++
                +-------------------+|      | +-------------------+
                |                    |      |                     |
                |                    |      |                     |
       +--------v---+    +-----------v+    +v-----------+   +-----v------+
       |   worker   |    |   worker   |    |   worker   |   |   worker   |
       |------------|    |------------|    |------------|   |------------|
       |  zmq(rep)  |    |  zmq(rep)  |    |  zmq(rep)  |   |  zmq(rep)  |
       |            |    |            |    |            |   |            |
       |            |    |            |    |            |   |            |
       +------------+    +------------+    +------------+   +------------+


Run
===
[terminal 1] python worker.py
[terminal 2] python broker.py
[terminal 3] python client.py
