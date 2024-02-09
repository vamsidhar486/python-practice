"""
Given a valid (IPv4) Internet Protocol address S, the task is to find the defanged version of that IP address.
Defanged Version of IP Address: is in which every period “.” is replaced by “[.]”.

Examples:

Input: S = “1.1.1.1”
Output: 1[.]1[.]1[.]1

Input: S = “255.100.50.0”
Output: 255[.]100[.]50[.]0
"""

# importing regular expression module
import re


# Time Complexity : O(n)
# Space Complexity : O(n)
def defang_ip(ip):
    defang_ip = ""
    for i in ip:
        if i == '.':
            defang_ip = defang_ip + '[.]'
        else:
            defang_ip = defang_ip + i
    return defang_ip


def defang_ip2(ip):
    return re.sub("[.]", "[.]", ip)


print(defang_ip('1.1.1.1'))
print(defang_ip2('255.100.50.0'))
