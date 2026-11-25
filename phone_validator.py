#-- validation functions (pep 8)
def is_valid_phone(phone_text):
    """validates that the input string contains strictly 10 digits"""
    
    if not phone_text.isdigit():
       
        return False, "The phone number must contain only numeric digits"


    if len(phone_text) != 10:
        
        return False, f"expected 10 digits but received {len(phone_text)}"
    
    return True,"valid 10-digit phone number!"

if __name__=="__main__":
    print("---Phone number validator v1.0")
    raw_input = input("Enter a 10-digit phone number").strip()
    valid, message = is_valid_phone(raw_input)


    if valid:
        print(f"ok  {message}")

    else:
        print(f"invalid number : {message}")

    