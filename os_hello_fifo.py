import os
import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.Logger(__name__)
test_pipe = "test"


def process_a():
	fd = os.open(test_pipe, os.O_WRONLY)
	os.write(fd, b"hello fifo")
	os.close(fd)

def process_b():
	fifo = open("test", 'rb')
	msg = fifo.read()
	msg = msg.decode('utf8')
	# logger.error("Message: ", msg)
	print(msg)


if __name__ == "__main__":
	try:
		os.mkfifo(test_pipe)
	except FileExistsError as e:
		logger.error(e)
	f = os.fork()
	if f != 0:
		process_b()
	else:
		process_a()

