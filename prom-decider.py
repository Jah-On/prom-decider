import random

def main():
    randos = [0,0,0]
    for i in range(1000):
        randos[random.randint(0, 2)] += 1
    if ((randos[0] > randos[1]) & (randos[0] > randos[2])):
        print("Ask someone to prom!")
    elif ((randos[1] > randos[0]) & (randos[1] > randos[2])):
        print("Go to prom!")
    else:
        print("Stay home and play Risk with ya homies.")

if __name__ == "__main__":
    main()