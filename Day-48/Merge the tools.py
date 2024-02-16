def merge_the_tools(s, k):
    # Split the string into substrings of length k
    substrings = [s[i:i+k] for i in range(0, len(s), k)]
    
    for substring in substrings:
        # Create a set to store unique characters
        unique_chars = set()
        # Build the string with unique characters
        result = ''
        for char in substring:
            if char not in unique_chars:
                result += char
                unique_chars.add(char)
        # Print the result
        print(result)

if __name__ == '__main__':
    string = input().strip()
    k = int(input())
    merge_the_tools(string, k)
