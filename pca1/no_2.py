def max_consecutive_ones(flag):
    max_count = 0
    current_count = 0

    for bit in flag:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0  # Reset count when encountering '0'

    return max_count  # Return the max count of consecutive 1s


def bit_stuffing(data, max_ones, flag="111110"):
    stuffed_data = ""
    count = 0

    for bit in data:
        stuffed_data += bit
        if bit == '1':
            count += 1

            if count == max_ones:
                stuffed_data += '0'  # Stuff a 0 after five consecutive 1s
                count = 0  # Reset count
        else:
            count = 0  # Reset count when a 0 is encountered

    return flag + stuffed_data + flag  # Append flag at start and end


def bit_de_stuffing(stuffed_data, max_ones, flag="111110"):
    if not stuffed_data.startswith(flag) or not stuffed_data.endswith(flag):
        print("Invalid stuffed data. Flag mismatch!")
        return None

    # Remove flag before de-stuffing
    stuffed_data = stuffed_data[len(flag):-len(flag)]
    de_stuffed_data = ""
    count = 0
    i = 0
    while i < len(stuffed_data):
        de_stuffed_data += stuffed_data[i]
        if stuffed_data[i] == '1':
            count += 1
            if count == max_ones and i + 1 < len(stuffed_data) and stuffed_data[i + 1] == '0':
                i += 1  # Skip the stuffed 0
                count = 0
        else:
            count = 0
        i += 1

    return de_stuffed_data


# User input
data = input("Enter the binary data: ")
flag = "111110"  # Fixed flag pattern
max_ones = max_consecutive_ones(flag)  # Compute max consecutive ones

# Perform bit stuffing
stuffed_data = bit_stuffing(data, max_ones, flag)
print("\nBit Stuffed Data:", stuffed_data)

# Ask user if they want to de-stuff
choice = input("\nDo you want to de-stuff the bit-stuffed data? (yes/no): ").strip().lower()
if choice == "yes":
    de_stuffed_data = bit_de_stuffing(stuffed_data, max_ones, flag)
    print("\nDe-Stuffed Data:", de_stuffed_data)
