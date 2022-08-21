import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) == 3:
        data = sys.argv[1]
        sequence = sys.argv[2]
    else:
        print(" error in command line arguments ")
        return
    # TODO: Read database file into a variable
    seq = []
    with open(data, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            seq = seq+[row]
    # TODO: Read DNA sequence file into a variable
    A = []
    with open(sequence, "r") as file:
        s = csv.reader(file)
        for row in s:
            A = A + [row]
    # TODO: Find longest match of each STR in DNA sequence

    longest = []
    for i in range(1, len(seq[0])):
        longest = longest + [str(longest_match(A[0][0], seq[0][i]))]

    # TODO: Check database for matching profiles
    for j in range(1, len(seq)):
        if longest == seq[j][1:]:
            print(seq[j][0])
            return

    print("no match")


    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()