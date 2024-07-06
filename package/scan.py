import subprocess
from Siosk.package.error_manage import ServerPortUsingError
from auto.clear_terminal import clear_terminal
import os
import time
import platform

os_system = platform.system()

def windows_track(port) -> int:
    port = str(port)
    def extract_pid_from_line(line) -> int:
        fields = str(line).split()
        if len(fields) >= 5:
            pid_str = fields[4]
        if pid_str.isdigit():
            return int(pid_str)
        return None
    
    def extract_pids_from_ps_output(ps_output) -> list:
        lines = str(ps_output).splitlines()
        pids = [extract_pid_from_line(line) for line in lines if extract_pid_from_line(line) is not None]
        return pids
    
    try:
        command = ["netstat", "-ano", "|", "findstr", port]
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        pids = extract_pids_from_ps_output(stdout)
        for pid_index, pid_val in enumerate(pids):
            process = subprocess.Popen(f"tasklist /FI \"PID eq {pid_val}\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            program = stdout.split("\n")[3].split(" ")[0]
            if program == "python.exe":
                return f"{program} | {str(pid_val)}"
        return True
    except Exception as e:
        return False

def unix_track(port):
    result = subprocess.check_output(['lsof', '-i', f':{port}'])
    result = result.decode('utf-8').strip().split('\n')
    if len(result) > 1:
        header = result[0]
        process_info = result[1].split()
        process_name = str(process_info[0])
        processer = process_name[:6]
        if processer != "python":
            return False
        pid = process_info[1]
        return f"{process_name} | {pid}"
    else:
        return True
        
def find_process_by_port(port):
    try:
        if os_system == "Windows":
            return_data = windows_track(port)
        else:
            return_data = unix_track(port)

        if return_data == False:
            print("\033[1;31m" + "ERROR" + "\033[0m" + ":" + f"     Is there any process is working on Port 9460?")
            raise ServerPortUsingError
        elif return_data == True:
            result_data =  f'No process found using port {port}'
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     {result_data}")
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     Directing...")
            time.sleep(3)
            os.system(clear_terminal())
            return False
        else:
            process_name, pid = str(return_data).split(" | ")
            result_data = f'1 process found using port http://127.0.0.1:9460 name: {process_name}, PID: {pid}'
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     {result_data}")
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     Directing...")
            time.sleep(3)
            os.system(clear_terminal())
            return True
        
    except subprocess.CalledProcessError:
        result_data =  f'No process found using port {port}'
        print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     {result_data}")
        print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     Directing...")
        time.sleep(3)
        os.system(clear_terminal())
        return False

