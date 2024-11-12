def is_palindrome():
    text = input("Введите текст: ")
    text = text.lower()
    cleaned_text = ''.join(char for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]
print(is_palindrome())