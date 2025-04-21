import sys
from typing import Tuple;

def build_queues() -> Tuple[list[str],list[str],list[str]]:
    """
    Takes a stream of packets from stdin/fileinput and sorts them into three
    seperate queues based on their priority.

    -------
    Returns:
        `Tuple[list[str],list[str],list[str]]`
            The sorted queues sorted by the order each packet came in.
    """
    premium = [];
    standard = [];
    economy = [];

    if len(sys.argv) == 1:
        print("No file argument found\nReading from stdin...\n");
        print("(Hint: run with `python3 KowalskiAlexWeekThreeQueues.py [file]` instead)\n");
        stream = sys.stdin
    else:
        stream = open(sys.argv[1]);
    for line in stream:
        match line[0].casefold():
            case 'p':
                premium.append(line.strip());
            case 's':
                standard.append(line.strip());
            case 'e':
                economy.append(line.strip());
            case _:
                print(f"Invalid priority flag `{line[0]}`: Dropping packet\n");

    # Reversing each queue to restore original ordering.
    premium.reverse();
    standard.reverse();
    economy.reverse();

    return (premium, standard, economy);

def process_queues(premium: list[str], standard: list[str], economy: list[str]):
    """
    Processes queues based on their priority.

    ----------
    Parameters:
        premium: `list[str]`
            highest priority, is processed first with 3 packets at a time
        standard: `list[str]`
            standard priority, is processed second with 2 packets at a time
        economy: `list[str]`
            lowest priority, is processed last with only 1 packet at a time
    """
    while (len(premium) + len(standard) + len(economy)) != 0:
        # For premium and standard, we always pop off at most 3 or 2 elements
        # respectively.
        # using the `min` function allows us to do this in a clean way without
        # any extra `if` statements
        if len(premium) != 0:
            pop_count = min(3, len(premium));

            # print `pop_count` names
            for name in premium[-pop_count:]: print(name);

            # then pop them from the queue
            premium = premium[:-pop_count]
            print();

        # same story here
        if len(standard) != 0:
            pop_count = min(2, len(standard))

            for name in standard[-pop_count:]: print(name);
            standard = standard[:-pop_count]
            print();

        # economy is easy since we're always just printing and popping
        # one element at a time
        if len(economy) != 0:
            print(economy.pop());
            print();

def main():
    """
    Main Entry Point
    """
    premium, standard, economy = build_queues();
    process_queues(premium, standard, economy);

if __name__ == "__main__":
    main();
