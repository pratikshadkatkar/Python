import secrets
import string

def generate_otp(length=6):
    # Allowed characters: uppercase letters and digits
    characters = string.ascii_uppercase + string.digits

    # Generate a secure, unpredictable OTP
    otp = ''.join(secrets.choice(characters) for _ in range(length))

    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print("Your 6-character verification code is:", otp)