def f(i):  
    
    time_to_wait = random.randrange(1,3)
    print "F id:",i," wait:",time_to_wait
    time.sleep(time_to_wait)
    return i

def adder(value):
    print "return of Id:",value
    global result
    result += value
    
if __name__ == '__main__':
    p=Pool(5)
    result = 0

    for i in range(5):
        p.apply_async(f, args=(i,), callback=adder)
    p.close()
    p.join()
    print result
    