# text = input(str())

def ana_text(text2):
    #list volwel
    vowel = 'ueoai'
    print(f"{'STT':<5} {'Số từ':<10} {'Số ký tự':<10} {'Số nguyên âm':<15} {'Danh sách các nguyên âm'}")

    # #split text
    # word = text2.split()

    # #count word
    # count_word = len(word)

    # #count text without space
    # len_text = len(text2.replace(' ', ''))
    # #count volwer and collect exist volwer
    # vowel_count = 0
    # vowel_list = []
    for idx, text in enumerate(text2, start=1):
        #split text
        words = text.split()
        
        #count word
        word_count = len(words)
        
        #count text without space
        len_text = len(text.replace(' ', ''))
        
        #count volwer and collect exist volwer
        vowel_count = 0
        vowel_list = []
        for char in text.lower():
            if char in vowel:
                vowel_count += 1
                vowel_list.append(char)
        #replace volwer overlap
        unique_vowels = sorted(set(vowel_list))
        
        #output
        print(f"{idx:<5} {word_count:<10} {len_text:<10} {vowel_count:<15} {', '.join(unique_vowels)}")


text2 = [
    "Both sides in the argument over whether a Dubai-based firm should be allowed to manage U.S. ports today used national security as a reason for why they are right",
    "The deputy defense secretary said blocking the deal could ostracize one of the United States' few Arab allies"
]
# text2 = input(str('Nhập xâu'))
ana_text(text2)