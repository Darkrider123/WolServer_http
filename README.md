# HTTP server designed to remotely start/close/restart a computer

It is designed to run on a Raspberry Pi Pico W but can run on any general computer.\

The server uses [The HTTP Rest Server Framework developed by me as a base](https://github.com/cosminariton123/HTTPRestServerFramework_compatible_with_mycropython) .

## Specific configurations

### MAC_WOL

Should be the MAC of the computer you are trying to Wake Over Lan as a string.

### BROADCAST_ADDRESS

Should be the broadcast adress of your netwrok(usually ending in .255) as a string.

## Specific configurations example

MAC_WOL = "00:B0:D0:63:C2:26"\
BROADCAST_ADDRESS = "192.168.0.255"
