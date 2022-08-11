class SCPI_FUNC:
    def __init__(self,inst):
        import pyvisa
        import time
        import numpy as np
        import matplotlib.pyplot as plt
        import sys  # For version_info and platform
        import time  # For sleep, clock, time and perf_counter
        self.inst=inst
        
    def wavlen(args,lmbd):
        args.inst.write(':SOUR:CHAN:WAV '+str(lambd)+'nm') #sets laser wavelength
        
    def power(args,poww):
        args.inst.write(':POW '+str(poww)+'dBM') #set laser power in dBM
        
     def switch():
        state=int( args.inst.query(':POW:STAT?')[:-1]) #gets current state of laser
        if state==0:
             args.inst.write(':POW:STAT 1') #changes the state of the laser
        else:
             args.inst.write(':POW:STAT 0') #changes the state of the laser
        
    def setup_autosweep(args,start,stop,speed):
        sig=[]
        args.inst.write(':WAV:SWE:STAR '+str(start)+'nm') #minimum wavelength
        args.inst.write(':WAV:SWE:STOP '+str(stop)+'nm') #maximum wavelength
        args.inst.write('WAV:SWE:MOD 1') #1 for one way, 3 for two way (continuous)
        args.inst.write(':WAV:SWE:SPE '+str(speed)) #speed of scan nm/s
        state=int(args.inst.query(':POW:STAT?')[:-1]) #turns on laser if off
        if state==0:
            args.inst.write(':POW:STAT 1')
        args.inst.write(':WAV '+str(start)+'nm') #sets the current wavelength to that of the sweep start

    return 

    def trigauto(args):
        args.inst.write(':WAV:SWE 1') #triggers the sweep
