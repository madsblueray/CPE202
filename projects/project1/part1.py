def perm_gen_lex(input):
    if len(input) <= 1:
        return input
    else:
        perms = []
        for removed in input:
           shorter_perms = perm_gen_lex(input.replace(removed, "")) 
           new_perms = [removed + shorter_perms[i] for i in range(len(shorter_perms))]
           for i in range(len(new_perms)):
              perms.append(new_perms[i])
        return perms

def main():
   in_ = input("Enter a short, sorted string: ")
   print(perm_gen_lex(in_))

if __name__ == "__main__":
   main()   
