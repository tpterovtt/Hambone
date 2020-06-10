from utils.dtmf import *
from utils.rx import *
from utils.tx import *

from modules.masterControl import *

dtmf = DTMF()
rx   = RX()
tx   = TX()
mc   = MasterControl()

if __name__ == "__main__":

    ## MAIN LOOP
    while(True):
        rx.recordAudio()
        
        pin = dtmf.dtmfDecode()
        #pin = 2
        if(pin):
            mc.select(pin)
        
    rx.killAudio()
    