import time

def countdown_timer():
    while True:
        try:
            seconds = int(input("Enter the number of seconds to count down: "))
            if seconds > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    for i in range(seconds, -1, -1):
        hours, remainder = divmod(i, 3600)
        minutes, seconds_display = divmod(remainder, 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds_display:02d}", end='\r')
        if i > 0:
            time.sleep(1)
    
    print("\nTime's up!")

countdown_timer()
