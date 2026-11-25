#-- validation functions (pep 8)

def sanitize_phone(raw_text):
    """removes common formatting characters like spaces,dashes and paretheses"""
    cleaned = raw_text.replace("-","").replace(" ","").replace("(","").replace(")","")

    return cleaned


def is_valid_phone(phone_text):
    """validates that the input string contains strictly 10 digits"""
    
    if not phone_text.isdigit():
       
        return False, "The phone number must contain only numeric digits"


    if len(phone_text) != 10:
        
        return False, f"expected 10 digits but received {len(phone_text)}"
    
    return True,"valid 10-digit phone number!"

def format_phone(clean_digits):
    """formats a 10-digit string into (xxx) xxx-xxxx"""
    area_code = clean_digits[0:3]
    prefix = clean_digits[3:6]
    line_number = clean_digits[6:10]

    return f"({area_code}) {prefix}- {line_number}"


if __name__=="__main__":
    print("---Phone number validator v2.0")
    user_input = input("Enter a 10-digit phone number dashes/spaces allowed").strip()
   
    cleaned_number = sanitize_phone(user_input)

    valid, message = is_valid_phone(cleaned_number)


    if valid:
        formatted = format_phone(cleaned_number)
        print(f" ok {message}")
        print(f"standardized format : {formatted}")
        

    else:
        print(f"invalid number : {message}")

    