class Connect:
    def __init__(self,port):
        import pyvisa
        import time
        import numpy as np
        import matplotlib.pyplot as plt
        import sys  # For version_info and platform
        import time  # For sleep, clock, time and perf_counter
        
        rm = pyvisa.ResourceManager()
        print(rm.list_resources())
        self.inst= rm.open_resource('GPIB0::'+str(port)+'::INSTR')
        self.inst.timeout = 25000