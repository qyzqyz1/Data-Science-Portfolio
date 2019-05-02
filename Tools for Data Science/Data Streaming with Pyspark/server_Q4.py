import socket
# Import necessary packages
import csv
import time

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('localhost', 9999))
serv.listen(5)

# Add your code here



while True:
    print("Waiting for connection")
    conn, addr = serv.accept()
    print("Connection successful")

    # Add your code here
    with open('C:/Users/yizhe/Desktop/Data/data2.txt', encoding='utf-8', errors='ignore') as file:
        data = file.readlines()
        for line in data:
            line = line.rstrip('\n')
            line = line.strip()
            print(line)
            conn.sendto((line + "\n").encode(), ('localhost',9999))
            time.sleep(1)

    conn.close()
    print('client disconnected')
