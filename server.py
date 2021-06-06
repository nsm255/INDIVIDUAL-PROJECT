import socket
import time

def hostToIP(s,cData,cHost):
#s for socket, c for client
#try if client input weird hostname(wrong format or not exist)
	try:
		ipAddr = socket.gethostbyname(cData)
		ipAddr = bytes(ipAddr,'utf-8')
		s.sendto(ipAddr,cHost)

		#log file stuff(useless)
		log = open("data.txt", "a")
		timeLog = time.asctime( time.localtime(time.time()) )
		log.write("{0};{1};{2};{3}\n".format(cData,ipAddr,cHost,timeLog))
		log.close()

		print("Resolved {0} to {1} for {2}".format(cData.decode('utf-8'),ipAddr.decode('utf-8'),cHost))
	except:
		errorMsg = b"Error. Unable to verify the hostname."
		s.sendto(errorMsg,cHost)

def main():
	sockd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	host = ''
	port = 8888
	try:
		sockd.bind((host,port))
	except:
		print('Connection error')
		exit()
	print('Waiting for client...')
	while True:
		data,addr = sockd.recvfrom(1024)
		hostToIP(sockd,data,addr)

if __name__=='__main__':
	main()
