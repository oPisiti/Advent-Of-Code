def main():
    with open("input.txt") as data:
        buffer = data.read()
    
    packet_size = 14
    latest = [buffer[i] for i in range(packet_size-1)]
    latest.insert(0, buffer[0])

    probe = 0       # Index of which position to overload next
    for i in range(3, len(buffer)):
        count = {}

        # Updating the latest char to take into consideration
        latest[probe] = buffer[i]
        probe = (probe + 1)%packet_size

        # Counting occurences
        for char in latest:
            if char not in count.keys(): count[char] =  1
            else:                        count[char] += 1 
        
        if max(count.values()) == 1:
            print(f"End of start-of-packet at index {i+1}")
            return


if __name__ == '__main__':
    main()