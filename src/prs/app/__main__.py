import sys
import argparse
import os
import signal
import time
import random

BASE_DIR = os.path.abspath(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    __file__,
                )
            )
        )
    )
)

PID_FILE = '/var/tmp/parser_demon.pid'
WORK = True

def worker():
    
    counter = 0
    while WORK:
        counter += 1
        time.sleep(random.randrange(1, 5))
    return counter

def get_version():
    path = os.path.join(BASE_DIR, "VERSION")
    with open(path, "r") as version_file:
        return version_file.read().strip()

def create_parser():
    parser  = argparse.ArgumentParser(
        prog="News parser",
        description=(
            "МЕга крутая программа\n"
            "сайта \n"
            "tam by"
        ),
        add_help = False,
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="вывести это сообщегие",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Текущая версия.",
        version=get_version(),
    )
    parser.add_argument(
        "-d",
        "--daemon",
        action="store_true",
        help="запуск в фоновом режиме",
        required=False, 
    )
    parser.add_argument(
        "-k",
        "--kill",
        action="store_true",
        help="остановить приложение",
    )
    
    
    return parser

parser = create_parser()
args = parser.parse_args()


def stop_handler(signum, frame):
    global WORK
    print("Stop")
    sys.exit()
    WORK = False
    #sys.exit

def start(daemon):
    if daemon:
        if os.path.isfile(PID_FILE):
            print("уже рабоатет")
            return
        pid = os.fork()
        if not pid:
            signal.signal(signal.SIGTERM, stop_handler)
            try:
                result = worker()
                print(result)
            except Exception as error:
                print(error)
            finally:
                os.remove(PID_FILE)
        else:
            with open(PID_FILE, "w") as pid_file:
                pid_file.write(str(pid))
            print(f"запущен процесс '{pid}'.")
            
        
            
    else:
        try:
            result = worker()
        except KeyboardInterrupt:
            print(end="\r")
            print("stop")
            sys.exit()
def stop(daemon):
    if daemon:
        with open(PID_FILE, "r") as pid_file:
            pid = int(pid_file.read().strip())
        os.kill(pid, signal.SIGTERM)
        while os.path.isfile(PID_FILE):
            time.sleep(1)
        print(random.random(), end="\r")

if args.kill:
    try:
        stop(os.path.isfile(PID_FILE))
    except Exception as error:
        print(error)

else:
    start(args.daemon)
