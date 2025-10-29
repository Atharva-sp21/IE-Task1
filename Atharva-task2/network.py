import time

def log(msg):
    now = time.strftime("%H:%M:%S")
    print(f"[{now}] {msg}")

class DHCPServer:
    def __init__(self):
        self.ip_pool = ["10.0.0.10", "10.0.0.11"]
        self.leases = {}

    def discover(self, mac):
        if not self.ip_pool:
            log(f"DHCP: No IPs left for {mac}")
            return None
        offer = self.ip_pool[0]
        log(f"DHCP: OFFER {offer} to {mac}")
        return offer

    def request(self, mac, ip):
        if ip in self.ip_pool:
            self.ip_pool.remove(ip)
            self.leases[mac] = ip
            log(f"DHCP: ACK {ip} to {mac}")
            return ip
        log(f"DHCP: NAK {mac}, {ip} not available")
        return None

class DNSServer:
    def __init__(self):
        self.records = {}

    def register(self, name, ip):
        self.records[name] = ip
        log(f"DNS: registered {name} -> {ip}")

    def resolve(self, name):
        ip = self.records.get(name)
        if ip:
            log(f"DNS: resolved {name} -> {ip}")
            return ip
        log(f"DNS: {name} not found")
        return None

class Client:
    def __init__(self, name, mac):
        self.name = name
        self.mac = mac
        self.ip = None

    def boot(self, dhcp):
        log(f"{self.name}: sending DHCP DISCOVER")
        offer = dhcp.discover(self.mac)
        if offer:
            log(f"{self.name}: got OFFER {offer}, sending REQUEST")
            self.ip = dhcp.request(self.mac, offer)
            if self.ip:
                log(f"{self.name}: IP acquired -> {self.ip}")
        else:
            log(f"{self.name}: no IP received")

    def register_dns(self, dns):
        if self.ip:
            dns.register(f"{self.name}.local", self.ip)

    def ping(self, target_name, dns):
        ip = dns.resolve(target_name)
        if ip:
            log(f"{self.name}: pinging {target_name} [{ip}] ... pong!")
        else:
            log(f"{self.name}: couldn’t resolve {target_name}")

def main():
    dhcp = DHCPServer()
    dns = DNSServer()

    clientA = Client("clientA", "AA:AA:AA:AA:AA:A1")
    clientB = Client("clientB", "AA:AA:AA:AA:AA:B1")

    clientA.boot(dhcp)
    clientB.boot(dhcp)

    clientA.register_dns(dns)
    clientB.register_dns(dns)

    clientA.ping("clientB.local", dns)
    clientB.ping("clientA.local", dns)

    log("Simulation complete.")

if __name__ == "__main__":
    main()
