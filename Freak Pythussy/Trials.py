def wordcount(text):
    words = text.split()
    print(f"Anzahl der Wörter: {len(words)}")
    return len(words)

#wordcount(input("Gib einen Text ein: "))

def isPalindrome(word):
    word = word.lower()
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            print(f"{word} ist kein Palindrom.")
            return False
        
    print(f"{word} ist ein Palindrom.")
    return True

#print(isPalindrome(input("Gib ein Wort ein: ")))

