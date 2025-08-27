def count_case_letters(input_string):
    uppercase_count = 0
    lowercase_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    print(f"No. of Upper case characters : {uppercase_count}")
    print(f"No. of Lower case characters : {lowercase_count}")

sample_string = 'The quick Brow Fox'
count_case_letters(sample_string)
