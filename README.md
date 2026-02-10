# 🤥 DNS Poisoning Tool

**Course:** Network Security (Seguridad Informática)  
**Student:** Junior (ID: 2024-2015)  
**Framework:** Python 3 + Scapy

## ⚠️ Disclaimer
**Educational use only.** Redirecting traffic and spoofing domains is a serious offense outside of a controlled lab.

## 🎥 Video Demonstration
[PASTE YOUR YOUTUBE/DRIVE LINK HERE]

---

## 1. Objective
This tool performs a **DNS Spoofing** attack. It sniffs network traffic for DNS queries targeting specific domains (e.g., `google.com`). When a query is detected, the script injects a forged DNS response pointing to the attacker's IP address before the legitimate DNS server can reply.
**Result:** The victim is redirected to a phishing site or a defaced page hosted by the attacker.

## 2. Network Topology
* **Attacker:** 20.24.20.2 (Running the Script + Apache Web Server).
* **Victim:** Windows 10 (DNS pointing to the Attacker).
* **Target Domain:** google.com

![Topology Screenshot](img/topology.png)

## 3. Requirements & Usage
### Installation
```bash
git clone [https://github.com/deiviRd18/D31B1-DNS-Poisoning.git](https://github.com/deiviRd18/D31B1-DNS-Poisoning.git)
cd D31B1-DNS-Poisoning
pip3 install scapy
```
A web server is required to host the fake page.

### Execution
1. **Start Web Server:**
   ```bash
   sudo service apache2 start
   ```
2. **Run DNS Spoofer:**

```Bash
sudo python3 d31b1_dns_poison.py
```
 4. Proof of Concept (PoC)
Redirection Success
Ping command showing google.com resolving to the local IP 20.24.20.2.

Browser Hijack
The victim's browser displays the attacker's custom HTML page instead of the real site.

5. Mitigation Strategies
DNSSEC (DNS Security Extensions): Cryptographically signs DNS records to ensure authenticity.

Encrypted DNS (DoH / DoT): Using DNS over HTTPS or TLS prevents local attackers from sniffing or modifying DNS requests.

VPN: Encrypts all traffic between the client and the VPN exit node.
