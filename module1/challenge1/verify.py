import base64

def main():
    ans = input("Please enter the passphrase contained in the file: ")
    correct_decoded_string = "You_found_a_base64_encoded_string_great_job"
    if ans.strip() == correct_decoded_string:
        print("Congratulations! Here is your flag!")
        with open('/flag', 'r') as fObj:
            print(fObj.read())
    else:
        print("Sorry, that was incorrect!")

if __name__ == "__main__":
    main()
