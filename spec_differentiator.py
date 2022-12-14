from formatter import format
from printer import printer

# Defining trim names and details
trim_names = [
    "LL",
    "LT",
    "LX",
    "LY"
    ]
trim_specs = [
    "Rear Air Conditioning Controls; Rear Audio Controls; Front Seats Memory; Adaptive Front Lighting System; [PM] Premium Pkg; Dual 18-Way Power w/Dual 4-Way Power Lumbar Seat Adjusters; Semi-Aniline Perforated Leather Seat Trim; Leather-Wrapped & Wood Steering Wheel; Manual Rear Side Sun Shades; Adaptive Variable Suspension; P235/45R18 Tires; Split 9-Spoke Alloy Wheels",
    "Rear Air Conditioning Controls; Rear Audio Controls; [CK] Cold Weather Pkg; Front Seats Memory; Adaptive Front Lighting System; [PM] Premium Pkg; Dual 18-Way Power w/Dual 4-Way Power Lumbar Seat Adjusters; Semi-Aniline Perforated Leather Seat Trim; Heated Rear Seats; Leather-Wrapped & Wood Steering Wheel; Manual Rear Side Sun Shades; Adaptive Variable Suspension; P235/45R18 Tires; Split 9-Spoke Alloy Wheels",
    "Rear Air Conditioning Controls; Rear Audio Controls; [CK] Cold Weather Pkg; Front Seats Memory; Adaptive Front Lighting System; [PM] Premium Pkg; Dual 18-Way Power w/Dual 4-Way Power Lumbar Seat Adjusters; Semi-Aniline Perforated Leather Seat Trim; Leather-Wrapped & Wood Steering Wheel; Manual Rear Side Sun Shades; Adaptive Variable Suspension; P235/45R18 Tires; Split 9-Spoke Alloy Wheels",
    "Rear Air Conditioning Controls; Rear Audio Controls; [CK] Cold Weather Pkg; Front Seats Memory; Adaptive Front Lighting System; Night Vision Monitor; [PM] Premium Pkg; Dual 18-Way Power w/Dual 4-Way Power Lumbar Seat Adjusters; Semi-Aniline Perforated Leather Seat Trim; Leather-Wrapped & Wood Steering Wheel; Manual Rear Side Sun Shades; Adaptive Variable Suspension; P235/45R18 Tires; Split 9-Spoke Alloy Wheels"
]

# Dummy check
if len(trim_names) != len(trim_specs):
    print("Amount of trim names and specs do not match. Please recheck configuration")

# Main logic
ll = format(trim_specs[0])
lt = format(trim_specs[1])
lx = format(trim_specs[2])
ly = format(trim_specs[3])

print("LL:")
print(ll)
print()
print("LT:")
print(lt - ll)
print()
print("LX:")
print(lx - ll)
print()
print("LY:")
print(ly - lx)

# Loop through trims
'''
for i in range(len(trim_names)):
    spec_list = format(trim_specs[i])
    print(trim_names[i])
    printer(spec_list)
    print()
'''