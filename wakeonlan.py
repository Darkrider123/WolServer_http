from config import MAC_WOL, BROADCAST_ADDRESS

import socket
import gc

def start_home_server():
    for _ in range(5):
        send_magic_package(MAC_WOL, BROADCAST_ADDRESS)
        gc.collect()


def send_magic_package(mac_address, broadcast_address):

    MAC = mac_address
    BROADCASTADDRESS = broadcast_address
    PORT = 9

    MSG = (b"\xFF" * 6 + MAC * 16)

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    soc.sendto(MSG,(BROADCASTADDRESS,PORT))
