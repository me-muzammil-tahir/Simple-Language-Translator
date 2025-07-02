import translators as ts
import pandas as pd

data = pd.read_csv('F:/Practicing/columns.csv')
print(data[0:20].to_string(index=False))

while(True):
        
    user = input("Your language (e.g., 'ur' for Urdu): ").strip()
    text = input("Enter Your Text Here:\n")
    transl = input("To which language do you want to translate (e.g., 'ar' for Arabic): ").strip()

    supported_languages = data['Code'][0:20].tolist()



    
    if transl not in supported_languages or user not in supported_languages:

        print("\n Invalid language code entered. Please use one of the supported codes:")
        print(supported_languages)
        print("\n\nWant to continue? press 1 or any key to exit : ")
        user_choice = input()
        if user_choice == '1':
            continue
        else:
            break
        
    else:
        result = ts.translate_text(text, translator='google', from_language=user, to_language=transl)
        print("\nTranslated Text:\n", result)
        print("\n\nWant to Translate More? press 1 to continue or any key to exit : ")
        user_choice = input()
        if user_choice == '1':
            continue
        else:
            break
