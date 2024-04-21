#main function called at the end of the code
def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path) 
    num_words = get_num_words(text)
    char_counts = get_char_count(text)
    chars_sorted = chars_list(char_counts)
    print("--- Begin report of books/frankenstein.txt ---") #could have used {book_path}
    print(f"{num_words} words found in the document")
    
    #this checks if the characters are in the alphabet, without that, you will get the count even for special characters, spaces and so on
    for character in chars_sorted:
        if character["char"].isalpha():
            print(f"The '{character['char']}' character was found {character['num']} times")
    print("--- End report ---")

#this counts the characters of the lowercased text
def get_char_count(text):
    lower = text.lower()
    char_count = {}
    for char in lower:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
    return char_count

#this counts the words
def get_num_words(text):
    words = text.split()
    return len(words)

#opens the txt file
def get_book_text(path):
    with open(path) as f:
        return f.read()

#returns the nums of dictionary
def sort_chars(dict):
    return dict["num"]

#returns sorted list of charactesr and their numbers
def chars_list(num_chars):
    sorted = []
    for chars in num_chars:
        sorted.append({"char": chars, "num": num_chars[chars]})
    sorted.sort(reverse=True, key=sort_chars)
    return sorted

main()