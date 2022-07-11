
# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/11/2022
# Description: A function that takes a list of names and returns the surname "Kardashian" only to the names in the list
# that start with the letter "K".

def add_surname(first_names):
    """
    Returns names with the added surname of "Kardashian" if and only if the name starts with the letter 'K'.
    """
    full_names = [name + " " + "Kardashian" for name in first_names if name[0] == "K"]
    return full_names
