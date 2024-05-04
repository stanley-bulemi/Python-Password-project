def check_password_strength(password):
    # Criteria for password strength
    length_criteria = 8
    complexity_criteria = 3
    unique_criteria = 0.8

    # Length check
    if len(password) < length_criteria:
        return "Password is too short. It should be at least {} characters long.".format(length_criteria)

    # Complexity check
    complexity_score = 0
    if any(char.isdigit() for char in password):
        complexity_score += 1
    if any(char.isupper() for char in password):
        complexity_score += 1
    if any(char.islower() for char in password):
        complexity_score += 1
    if any(char in "!@#$%^&*()-_+=~`[]{}\\|;:'\",.<>?/" for char in password):
        complexity_score += 1

    if complexity_score < complexity_criteria:
        return "Password is not complex enough. It should contain at least {} of the following: uppercase letters, lowercase letters, digits, and special characters.".format(complexity_criteria)

    # Uniqueness check
    unique_chars = set(password)
    unique_percentage = len(unique_chars) / len(password)
    if unique_percentage < unique_criteria:
        return "Password does not have enough unique characters. It should have at least {}% unique characters.".format(unique_criteria * 100)

    return "Password meets the criteria for strength."

# Example usage
password = input("Enter password to check its strength: ")
print(check_password_strength(password))
