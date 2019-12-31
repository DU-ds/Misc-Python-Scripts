def string_search(lst, stringy):
    """returns true if any of the strings in lst are in the string stringy
        
        Args:
            lst: list
                list of strings to check
            stringy: string
                string to check
        Returns: 
            mhm: boolean
                string 
    """
    return any(s in stringy for s in lst)
