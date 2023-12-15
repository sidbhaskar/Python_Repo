import os

read_fd, write_fd = os.pipe()

data = 'This is some data to be written to the pipe'

os.write(write_fd,data.encode())

read_data = os.read(read_fd, 1024)

print(read_data.decode())