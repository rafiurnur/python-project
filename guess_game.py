import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("আমি ১ থেকে ১০০ এর মধ্যে একটি সংখ্যা ভেবেছি।")
    print("তুমি কি সেটা অনুমান করতে পারো?")

    while guess != number_to_guess:
        try:
            guess = int(input("তোমার অনুমান (১-১০০): "))
            attempts += 1

            if guess < number_to_guess:
                print("আরও বড় সংখ্যা অনুমান করো। 🔼")
            elif guess > number_to_guess:
                print("আরও ছোট সংখ্যা অনুমান করো। 🔽")
            else:
                print(f"অভিনন্দন! 🎉 তুমি {attempts} বার চেষ্টায় সঠিক সংখ্যা {number_to_guess} পেয়েছো!")
        except ValueError:
            print("দয়া করে একটি সঠিক সংখ্যা দাও।")

# গেম চালু
guess_the_number(6)
