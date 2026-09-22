class Solution(object):
    def defangIPaddr(self, address):
        list_address = list(address)
        for index, character in enumerate(address):
            if character == ".":
                list_address[index] = "[.]"
                new_address = "".join(list_address)
 
        return(new_address)