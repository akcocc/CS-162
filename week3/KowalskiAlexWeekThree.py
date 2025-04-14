import numpy as np;

ROW=1
COL=2

def main():
    """
    Main Entry Point
    """
    # I think 16 bit ints are a nice size to work with.
    twodarray = np.random.randint(0,(2**16)-1, size=(5, 5), dtype=np.uint16);
    print("Entire Array:", twodarray);
    print(f"Value of Row {ROW+1}, Column {COL+1}:", twodarray[ROW][COL]);

    # using u32 instead of a u16 as it would most likely be too small and would just overflow
    print("Sum:", twodarray.sum(dtype=np.uint32));
    i = 0;
    for row in twodarray:
        i += 1;
        print(f"Mean of Row {i}:", row.mean(dtype=np.uint16));

    i = 0;
    # rotating the array to more easily iterate through cols not rows
    for col in np.rot90(twodarray, 1, (1, 0)):
        i += 1;
        print(f"Max of Col {i}:", col.max());

if __name__ == "__main__":
    main();
