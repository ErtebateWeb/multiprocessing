from multiprocessing import Process, freeze_support
from concurrent.futures import ProcessPoolExecutor
import time
def show ( name ) :
    print ( f'starting { name } ... ' )
    time.sleep ( 3 )
    print ( f'Ending {name } ... ' )
def main ( ) :
    with ProcessPoolExecutor (max_workers=2) as executor :
        names = [ ' one ' , ' Two ' , ' Three ' , " Four " ]
        executor.map ( show , names )


if __name__ == '__main__':
    freeze_support()
    main ( )