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
    with open('C:/Users/yizhe/Desktop/Data/data1.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            output = str(row)[1:-1].replace(" ","")
            output = output.replace("'","")
            print(output)
            conn.sendto((output + "\n").encode(), ('localhost',9999))
            time.sleep(1)

    conn.close()
    print('client disconnected')
