"""
Binary search problem from pico ctf
between 1-1000 numbers

"""
def IsItEqual(number):
    user_input = (input(f"Is it {number}? True or False"))
    if user_input == "True":
        return True
    return False

def IsItHigher():
    user_input = (input(f"Is it higher or lower?: "))
    if user_input == "higher":
        return "higher"
    return "lower"

def BinarySearch(length):
    end = length
    start = 0
    current_idx = (end - start) / 2
    while True:
        if not IsItEqual(current_idx):
            user_input = IsItHigher()
            if user_input == "higher":   # real number is higher
                start = current_idx
                current_idx = ((end - start) // 2) + current_idx
            elif user_input == "lower":  # real number is lower
                end = current_idx
                current_idx = (end - start) // 2
        else:
            return True
def main():
    BinarySearch(1000)   
main()