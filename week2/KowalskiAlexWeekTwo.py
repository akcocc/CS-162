import matplotlib.pyplot as plot

def main():
    """
    Main Entry Point
    """
    print("Alex Kowalski");
    # set up your lists
    numlist = [8, 6, 5, 3]
    namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
    colorlist = ['green', 'red', 'yellow', 'pink' ]
    explodelist = [0.02, 0.02, 0.02, 0.02]
    # make the pie chart
    plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
             explode = explodelist, startangle = 225)
    plot.axis('equal')
    plot.savefig('week2/piechart.png')

if __name__ == "__main__":
    main()
