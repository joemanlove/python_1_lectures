"""
File Input/Output Lecture by Joe Manlove

revised 6/6/2020
revised 9/15/2026 to add docstring fix some naming.
"""


# First Method, old school, clear but error prone

# Output Code
# get a file read/write stream in write mode 
# output_file = open('test_output.txt','a')

# write a test string into the stream
# output_file.write('That plane was annoying')

# save the stream to the file
# output_file.close()

# Input Code
# create a read stream
# input_file = open('test_ output.txt', 'r')

# print the contents of the file
# print(input_file.read())

# close the stream
# input_file.close()



# Second Option, less clear, but handles errors

# try to create stream and do stuff, errors thrown
# try:
#     stream = open('testInput.txt', 'r')
#     print(stream.read())
#     # Do stuff to stream
# except FileNotFoundError:
#     print("File not found...")
# else:
#     stream.close()
# finally:
#     pass



# Third Option, least clear, but best

with open('test_output.txt', 'w') as stream:
    # Do stuff to stream
    print(stream.write("Some junk in the trunk"))
    # pass