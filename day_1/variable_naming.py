import re


username = input("Username : ")

print(username)

print(input("Sport : "))
print("Sport: ", input("Enter Sport: "))

# todo : invalid variable names
# 3username  ==> starts with number
# input ==> keyword
# user name ==> spaces

langs = [("ar", "Arabic"), ("en", "English")]


def is_valid_nationalid(nationalid):
    nationalids = re.findall(r"^\d{14}$", nationalid)
    if nationalids:
        return nationalids[0]
    raise ValueError(f"Invalid National ID {nationalid}")


def is_valid_opt(otp):
    otps = re.findall(r"^\d{4}$", otp)
    if otps:
        return otps[0]
    raise ValueError(f"Invalid OTP Pattern ({otp})")


def main():
    nationalid = is_valid_nationalid(input("Enter Your national id"))
    otp = is_valid_opt(input("Enter Your OTP pattern"))
    print("NationalID : ", nationalid)
    print("otp : ", otp)


installed_apps = [
    {
        "name": "facebook",
        "version": "v1.2",
        "founder": "mark",
        "users": "1B",
        "year": 2004,
    },
    {
        "name": "twitter",
        "version": "v3.5",
        "founder": "John",
        "users": "2B",
        "year": 2006,
    },
]
if __name__ == "__main__":
    main()
