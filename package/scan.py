import subprocess
from Siosk.package.error_manage import ServerPortUsingError
import os
import time

def find_process_by_port(port):
    try:
        result = subprocess.check_output(['lsof', '-i', f':{port}'])
        result = result.decode('utf-8').strip().split('\n')
        if len(result) > 1:
            header = result[0]
            process_info = result[1].split()
            process_name = str(process_info[0])
            processer = process_name[:6]
            if processer != "python":
                print("\033[1;31m" + "ERROR" + "\033[0m" + ":" + f"     Is there any process is working on Port 9460?")
                raise ServerPortUsingError
            pid = process_info[1]
            result_data = f'1 process found using port http://127.0.0.1:9460 name: {process_name}, PID: {pid}'
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     {result_data}")
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     Directing...")
            time.sleep(3)
            os.system("clear")
            return True
        else:
            result_data =  f'No process found using port {port}'
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     {result_data}")
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     Directing...")
            time.sleep(3)
            os.system("clear")
            return False
    except subprocess.CalledProcessError:
        result_data =  f'No process found using port {port}'
        print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     {result_data}")
        print("\033[1;32m" + "INFO" + "\033[0m" + ":" + f"     Directing...")
        time.sleep(3)
        os.system("clear")
        return False

