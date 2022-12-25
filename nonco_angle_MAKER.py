import numpy as np # Using np.arange to have float increments
import os


def MAKE_FILE(path, N, th, phi):
    path = os.path.join(path, "nonco_angle.dat")
    PATH = os.path.normpath(path)
    
    try:
        f = open(PATH, "w")  
    except OSError as error: 
        print(error)
    
    for i in range(N):
        f.write(f"  {th:.15f}E+000  {phi:.15f}E+000  F\n")
    
    f.close()


def MAKE_DIRs(N, th_start, th_end, d_th, phi_start, phi_end, d_phi):
    
    for th in np.arange(th_start, th_end + d_th, d_th):
        for phi in np.arange(phi_start, phi_end + d_phi, d_phi):
            
            # File name
            directory = f"th_{th:03d}_phi_{phi:03d}"
              
            # Parent Directory path
            parent_dir = os.getcwd()
              
            # Path
            path = os.path.join(parent_dir, directory)
            
            # Normalized Path for Windows or Linux
            PATH = os.path.normpath(path)
            
            try: 
                os.mkdir(PATH) 
                print("Directory '% s' created" % directory)
            except OSError as error: 
                print(error)
            
            MAKE_FILE(PATH, N, th, phi)


if __name__ == "__main__":
    N = 16
    
    th_start = 0
    th_end   = 100
    d_th     = 10
    
    phi_start = 0
    phi_end   = 0
    d_phi     = 5
    
    MAKE_DIRs(N, th_start, th_end, d_th, phi_start, phi_end, d_phi)

