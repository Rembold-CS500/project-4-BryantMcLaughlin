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

    print(data)
    return data
    

# Test the function with the provided file
filename = 'prints/User1_Original.txt'
read_print(filename)
