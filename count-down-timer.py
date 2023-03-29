import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:03d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print('RUN !')


countdown(int(input('Enter time in seconds: ')))
