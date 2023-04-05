import pychat
import time
livechat = pychat.create(video_id = "A6jnAB4c7xQ")

while livechat.is_alive():
    chatdata = livechat.get()
    for c in chatdata.items:
        print("{c.datetime} {c.author.name} {c.message} {c.amountString}")
    time.sleep(5)