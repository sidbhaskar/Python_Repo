# Create two pipes
import os

pipe1_read_fd, pipe1_write_fd = os.pipe()
pipe2_read_fd, pipe2_write_fd = os.pipe()
# Fork a child process
child_pid = os.fork()

if child_pid == 0:
# Child process
# Read data from pipe1
    data = os.read(pipe1_read_fd, 1024)
    print(f"Child process received data: {data.decode()}")
# Process the data
    processed_data = data.upper()
# Write the processed data to pipe2
    os.write(pipe2_write_fd, processed_data)
    exit(0)
# Parent process
# Write data to pipe1
data = "This is some data to be processed."
os.write(pipe1_write_fd, data.encode())
# Read processed data from pipe2
processed_data = os.read(pipe2_read_fd, 1024)
print(f"Parent process received processed data:{processed_data.decode()}")
# Wait for the child process to finish
os.waitpid(child_pid, 0)
os.close(read_fd)
os.close(write_fd)