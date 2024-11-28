import pyttsx3 
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '/': ' '
}

def morse_to_text(morse_code):
    words = morse_code.strip().split(' / ')  
    decoded_message = []
    for word in words:
        letters = word.split(' ')  
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter, '') for letter in letters)
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 1.0) 
    engine.say(text) 
    engine.runAndWait()

def main():
    print("Enter Morse Code (use ' / ' to separate words): ")
    morse_code = input().strip()
    try:
        decoded_text = morse_to_text(morse_code)
        if not decoded_text.strip():
            raise ValueError("Invalid Morse code entered. Could not decode.")
        print(f"Decoded Text: {decoded_text}")
        print("Speaking the text...")
        speak_text(decoded_text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
