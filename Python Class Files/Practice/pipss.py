import os

read_fd , write_fd = os.pipe()

data = (" heeloooo, this is a data given by meee !! .. ^^ ")

os.write(write_fd,data.encode())

read_data = os.read(read_fd,10)

print(read_data.decode())

os.close(write_fd)
os.close(read_fd)