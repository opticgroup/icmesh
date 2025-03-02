# how to compile meshtastic firmware
git clone --single-branch --branch 2.6 https://github.com/meshtastic/firmware.git
cd firmware
git submodule update --init --recursive --remote
pio run -e t-deck-tft -t upload --upload-port /dev/ttyACM0
