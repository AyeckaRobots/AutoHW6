import paramiko
import threading
import time

def run_command(ip, username, password, command):
    try:
        # Create an SSH client and set the policy to add the host key automatically
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote host
        print(f"Connecting to {ip}...")
        ssh.connect(ip, username=username, password=password)
        print(f"Connected to {ip}")

        # Open a session channel with a pseudo-terminal for real-time output
        transport = ssh.get_transport()
        channel = transport.open_session()
        channel.get_pty()  # Request a pseudo-terminal to enable real-time output
        channel.exec_command(command)

        # Continuously read from the channel until the command is finished
        while True:
            # If data is available, read it and print
            if channel.recv_ready():
                output = channel.recv(1024).decode('utf-8')
                print(f"[{ip}] {output}", end='')

            # Check if the command has finished executing
            if channel.exit_status_ready():
                # Read any remaining data
                while channel.recv_ready():
                    output = channel.recv(1024).decode('utf-8')
                    print(f"[{ip}] {output}", end='')
                break

            # Sleep briefly to avoid busy waiting
            time.sleep(0.1)

        # Close the SSH connection
        ssh.close()
        print(f"Disconnected from {ip}")

    except Exception as e:
        print(f"An error occurred with {ip}: {e}")

if __name__ == "__main__":
    recv_ip = "192.168.115.11"
    send_ip = "192.168.115.65"
    
    # Define the receiver's pre-iperf command and the iperf command
    recv_cmd2 = "sudo route add 225.1.1.1 gw 192.168.9.11"
    recv_cmd3 = "iperf -u -s -B 225.1.1.1 -i1"
    # Combine them so that iperf runs only if the route command succeeds
    full_recv_command = f"{recv_cmd2} ; {recv_cmd3}"
    
    # Define the sender command
    send_cmd = "iperf -u -c 225.1.1.1 -i1 -t 60000 -b 25M"
    
    # Each dictionary now includes the command to run on that host.
    remote_hosts = [
        {"ip": recv_ip, "username": "user", "password": "user", "command": full_recv_command},
        {"ip": send_ip, "username": "pi", "password": "password", "command": send_cmd}
    ]
    
    # Create a thread for each remote host connection
    threads = []
    for host in remote_hosts:
        t = threading.Thread(target=run_command, args=(host["ip"], host["username"], host["password"], host["command"]))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All SSH sessions completed.")
