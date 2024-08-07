######################################################################
# Names of any others you worked with:
# AI transcript if used:
# Any extensions done:
######################################################################

def read_print(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract the name, width, and height
    name = lines[0].strip()
    width = int(lines[1].strip())
    height = int(lines[2].strip())

    # Extract the fingerprint data
    fingerprint = [line.rstrip() for line in lines[3:]]

    # Verify the dimensions of the fingerprint
    # for line in fingerprint:
    #     if len(line) != width:
    #         raise ValueError("Fingerprint dimensions do not match the specified width")

    # Create the data dictionary
    data = {
        'name': name,
        'width': width,
        'height': height,
        'fingerprint': fingerprint
    }

    # print(data)
        # Confirmed it is printing the contents in dictionary format
    return data

def simple_check(fingerprint1, fingerprint2):
    return fingerprint1['fingerprint'] == fingerprint2['fingerprint']
    

# Test the function with the provided files
filename1 = 'prints/User1_Original.txt'
fingerprint1 = read_print(filename1)
print(fingerprint1)

# Test the function with the provided files
filename2 = 'prints/User2_Original.txt'
fingerprint2 = read_print(filename2)
print(fingerprint2)

print(simple_check(fingerprint1, fingerprint1))  # Should return True
print(simple_check(fingerprint1, fingerprint2))  # Should return False
    # Confirmed that this is functioning as intended
