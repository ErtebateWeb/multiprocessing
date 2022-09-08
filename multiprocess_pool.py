from multiprocessing import Pool , cpu_count, freeze_support
import time

start = time.perf_counter()

def show(name):
    print (f"starting {name}...")
    time.sleep(3)
    print (f"ending {name}...")



def main():
    names = ['a', 'b', 'c', 'd']

    pool = Pool()
    # pool = Pool(processes=cpu_count())
    pool.map(show , names)
    pool.close()
    pool.join()


    print("cpu count =",cpu_count())
    end = time.perf_counter()
    print("time=",round(end-start))



if __name__ == '__main__':
    freeze_support()
    main ( )
