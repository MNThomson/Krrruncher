import pika, sys, os, time, itertools, string, hashlib, sys, requests, socket

def main():
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex(('rabbitmq',15672))
		if result != 0:
			time.sleep(1)
		else:
			break
	time.sleep(15)
	connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
	channel = connection.channel()

	channel.queue_declare(queue='md5')

	def callback(ch, method, properties, body):
		print(body.decode("utf-8"))
		start(body.decode("utf-8"))

	channel.basic_consume(queue='md5', on_message_callback=callback, auto_ack=True)

	channel.start_consuming()

### Begin the hash cracking process
done = False

def start(hash):
	chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
	return _attack(chrs, hash)

def _attack(chrs, inputt):
	print("[+] Start Time: ", time.strftime('%H:%M:%S'))
	start_time = time.time()
	total_pass_try=0
	for n in range(1, 31+1):
		for xs in itertools.product(chrs, repeat=n):
			saved = ''.join(xs)
			stringg = saved
			m = hashlib.md5()
			m.update(bytes(saved, encoding='utf-8'))
			total_pass_try +=1
			if m.hexdigest() == inputt:
				time.sleep(10)
				global done
				done = True

				print("[!] found ", stringg)
				print("---Md5 cracked at %s seconds ---" % (time.time() - start_time))
				url = 'http://flaskserver:5000/api/' + inputt + '/' + stringg
				requests.get(url, allow_redirects=True)
				return 0

if __name__ == '__main__':
	main()