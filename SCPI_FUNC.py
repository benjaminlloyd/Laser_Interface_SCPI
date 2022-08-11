class SCPI_FUNC:
    def __init__(self):
        import pyvisa
        import time
        import numpy as np
        import matplotlib.pyplot as plt
        import sys  # For version_info and platform
        import time  # For sleep, clock, time and perf_counter
        
    def wavlen(args,lmbd):
        args.inst.write(':SOUR:CHAN:WAV '+str(lambd)+'nm')
        
    def power(args,poww):
        args.inst.write(':POW '+str(poww)+'dBM')
    def setup_autosweep(args,start,stop,speed):
        sig=[]
        args.inst.write(':WAV:SWE:STAR '+str(start)+'nm')
        args.inst.write(':WAV:SWE:STOP '+str(stop)+'nm')
        args.inst.write('WAV:SWE:MOD 1') #1 for one way, 3 for two way (continuous)
        args.inst.write(':WAV:SWE:SPE '+str(speed))
        state=int(args.inst.query(':POW:STAT?')[:-1])
        if state==0:
            args.inst.write(':POW:STAT 1')
        args.inst.write(':WAV '+str(start)+'nm')

    return 

    def trigauto(args):
        args.inst.write(':WAV:SWE 1')