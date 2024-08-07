######################################################################
# Names of any others you worked with:
# AI transcript if used:
# Any extensions done:
######################################################################

# Mileston #1
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

# Milestone #2
def simple_check(fingerprint1, fingerprint2):
    return fingerprint1['fingerprint'] == fingerprint2['fingerprint']

# Milestone #3
def variant_check(fingerprint1, fingerprint2, threshold=95.0):
    if fingerprint1['width'] != fingerprint2['width'] or fingerprint1['height'] != fingerprint2['height']:
        return False

    match_count = 0
    total_pixels = 0

    for i in range(7, fingerprint1['height']):
        for j in range(fingerprint1['width']):
            if j < len(fingerprint1['fingerprint'][i]) and j < len(fingerprint2['fingerprint'][i]):
                if fingerprint1['fingerprint'][i][j] == fingerprint2['fingerprint'][i][j]:
                    match_count += 1
                total_pixels += 1

    match_percentage = (match_count / total_pixels) * 100
    print(f"Matching percentage: {match_percentage:.2f}%") # I added to two decimals so that it is a cleaner percentage

    return match_percentage >= threshold
    

# Test the read_print function with the provided files
filename1 = 'prints/User1_Original.txt'
fingerprint1 = read_print(filename1)
print(fingerprint1)

# Test the read_print function with the provided files
filename2 = 'prints/User2_Original.txt'
fingerprint2 = read_print(filename2)
print(fingerprint2)

# Test the simple_check function
print(simple_check(fingerprint1, fingerprint1))  # Should return True
print(simple_check(fingerprint1, fingerprint2))  # Should return False
    # Confirmed that this is functioning as intended

# Test the variant_check function
print(variant_check(fingerprint1, fingerprint1))  # Should return True if the match percentage is above 95% (which it should since they are the same fingerprint)
    # Not returning true

# Additional test cases for shifted and variantfiles
filename3 = 'prints/User1_ShiftedVariant1.txt'
fingerprint3 = read_print(filename3)
print(variant_check(fingerprint1, fingerprint3))  # Should return False if the match percentage is below 95%

filename4 = 'prints/User1_Variant1.txt'
fingerprint4 = read_print(filename4)
print(variant_check(fingerprint1, fingerprint4))  # Should return True if the match percentage is above 95%
# Not returning true