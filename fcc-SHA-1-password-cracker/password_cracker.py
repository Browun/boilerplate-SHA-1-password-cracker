import hashlib


def return_salts():
    """
    Returns list of encoded (utf-8) salts from `known-salts.txt`
    """
    salt_list = []
    with open("known-salts.txt", "r") as s:
        for salt in s:
            salt_list.append(salt.replace('\n', ''))
    
    return salt_list


def hash_passwords(hash, salt):
    """
    Hash each value in `top-10000-passwords.txt` and compare to provided hash, return True if matches, and the has it matched with
    """

    with open('top-10000-passwords.txt', 'r') as f:
        if salt == True:
            salts = return_salts()
            for line in f:
                line = line.replace('\n', '')
                for salt in salts:
                    salted = [(salt + line).encode('utf-8'), (line + salt).encode('utf-8')]
                    checks = [hashlib.sha1(x).hexdigest() for x in salted]

                    if hash in checks:
                        return True, line

        else:
            for line in f:
                line = line.replace('\n', '')
                value = line.encode("utf-8")
                eline = hashlib.sha1(value).hexdigest()

                if eline == hash:
                    return True, line

        return False, ''


def crack_sha1_hash(hash, use_salts=False):
    '''
    Hash the input password, with optional salt if provided, and compare against values in the replit db
    '''

    if use_salts:
        print("Using a salted hash\n")
    else:
        print("Using a non-salted hash\n")

    answer, value = hash_passwords(hash, use_salts)

    if answer == True:
        print(f"A match was found between:\nHash: {hash}\nValue: {value}\n")
        return value
    else:
        print(f"No match was found for Hash: {hash}\n")
        return "PASSWORD NOT IN DATABASE"
