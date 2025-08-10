import datetime, socket, colorama
class PortScanner:
    def __init__(self):
        self.target = str(input('target -> '))
        self.startingPort = int(input('start on port: '))
        self.endingPort = int(input('end on port: '))
        try:
            self.targetIp = socket.gethostbyname(self.target)
        except socket.gaierror:
            print('Could Not Resolve Host :(')
            exit()
    def RunScan(self):
        print(colorama.Fore.GREEN+f'Starting Scan On {self.targetIp} from *port {self.startingPort} to port {self.endingPort}*')
        self.sTime = datetime.datetime.now()
        for port in range(self.startingPort, self.endingPort + 1):
            self.s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            self.s.settimeout(0.5)
            self.result = self.s.connect_ex((self.targetIp, port))
            if self.result == 0:
                print(colorama.Fore.GREEN+f'Port {port} is OPEN')
            else:
                print(colorama.Fore.RED+f'Port {port} is CLOSED')
            self.s.close()
        self.eTime = datetime.datetime.now()
        print(f'Scan Completed in {self.eTime - self.sTime}'+colorama.Fore.RESET)
scanner = PortScanner()
scanner.RunScan()