from config_info_that_shouldnt_appear_on_git import PORT, SSID, WLAN_KEY, STATIC_IP, MASK, GATEWAY, DNS_SERVER, MAC_WOL, BROADCAST_ADDRESS
from config_info_that_shouldnt_appear_on_git import STATUS_LINK, SHUTDOWN_LINK, RESTART_LINK

PORT = PORT
SSID = SSID
WLAN_KEY = WLAN_KEY

STATIC_IP = STATIC_IP
MASK = MASK
GATEWAY = GATEWAY
DNS_SERVER = DNS_SERVER
IFCONFIG = (STATIC_IP, MASK, GATEWAY, DNS_SERVER)

MAC_WOL = MAC_WOL
BROADCAST_ADDRESS = BROADCAST_ADDRESS

ENCODING = 'utf-8'
CONTROOLERS_FOLDER_PATH = "controllers"

SECONDS_UNTILL_RESET = 60 * 60 #1 Hour

STATUS_LINK = STATUS_LINK
SHUTDOWN_LINK = SHUTDOWN_LINK
RESTART_LINK = RESTART_LINK
