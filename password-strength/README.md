Description: Password strength is an important metric to consider with your online footprint, and this tool takes a stab at using bit entropy in concert with a list of common passwords to check your relative password strength. 
Note that a powerful exception of this program is that it does not consider password re-use, which can expose you online. The best way to secure yourself is to use a password manager, or if you want to create a locked excel sheet that contains 
randomly generated passwords that contain upper and lowercase letters, digits and special characters.

APPROACH: I used a list of the 10,000 most common passwords according to Wikipedia and created python set out of the list, and then checked if the password was contained in that list. If it is not, I calculated the bit entropy of the password
accodording to the formula L * log_base2(S), where L = password_length & S = character_set_size. I then output the relative strength of the password according to it's entropy and a scale provided by NordVPN. 

HOW TO RUN: Download password_strenght.py and common_passwords.txt into the same directory, and run some variation of the command python3 password_strength.py 
