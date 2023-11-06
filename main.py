from my_framework.my_http.http_handler import HttpHandler
from my_framework.my_socketserver.my_socketserver import SocketServer
from config import SSID, WLAN_KEY, PORT, SECONDS_UNTILL_RESET, IFCONFIG

import time

import sys

if sys.implementation.name == "micropython":
    from my_machine import pie_pico_w_instance

def main():
    global pie_pico_w_instance
    if sys.implementation.name == "micropython":
        ip = pie_pico_w_instance.connect_to_internet(SSID, WLAN_KEY, IFCONFIG=IFCONFIG)
        pie_pico_w_instance.onboard_led_on()
    else:
        import socket
        ip = socket. gethostbyname(socket.gethostname())


    if sys.implementation.name == "micropython":
        def restart_after_some_time_to_avoid_bugs(seconds_to_wait):
            for _ in range(seconds_to_wait):
                time.sleep(1)
                if pie_pico_w_instance.is_connected() is False:
                    pie_pico_w_instance.reset()
            pie_pico_w_instance.reset()

    if sys.implementation.name == "micropython":
        import _thread   
        _thread.start_new_thread(restart_after_some_time_to_avoid_bugs, (SECONDS_UNTILL_RESET,))

    address_and_port = (ip, PORT)
    http_server = SocketServer(address_and_port, HttpHandler)

    try:
        http_server.serve_forever()
    except:
        if sys.implementation.name == "micropython":
            pie_pico_w_instance.reset()

if __name__ == '__main__':
    main()
