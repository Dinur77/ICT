def find_max(numbers):
    max_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def main():
    # Define a list of numbers to find the maximum from
    numbers = [3, 5, 2, 8, 1, 10]
    
    # Call the find_max function and store the result
    max_value = find_max(numbers)
    
    # Display the maximum value to the user
    print(f"Maximum number: {max_value}")

# Standard Python practice - execute main() only when script is run directly
if __name__ == "__main__":
    main()