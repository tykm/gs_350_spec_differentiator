'''
Takes unformatted trim details and returns formatted set.

Iterate through the list while appending chars to a letterbank, searching for the ';' as the stop. Then, join the list to efficiently concat the string.
'''
def format(details: str) -> set:
    output = set()
    chars = list()
    skip = False
    for let in details:
        # Skip iteration
        if skip:
            skip = False
            continue
        # If we find a ';', build the string then skip the starting ' ' char at the beginning of each trim detail
        if let ==';':
            output.add("".join(chars))
            chars.clear()
            skip = True
            continue
        chars.append(let)
    return output
        






"Rear Air Conditioning Controls; Rear Audio Controls; Front Seats Memory; Adaptive Front Lighting System; [PM] Premium Pkg; Dual 18-Way Power w/Dual 4-Way Power Lumbar Seat Adjusters; Semi-Aniline Perforated Leather Seat Trim; Leather-Wrapped & Wood Steering Wheel; Manual Rear Side Sun Shades; Adaptive Variable Suspension; P235/45R18 Tires; Split 9-Spoke Alloy Wheels",