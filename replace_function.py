def replacment(chaine, mot, rep, occ):

    idexs = []

    # spliting the paragraphe:

    words = chaine.split(sep=" ")
    words = [part.split(",") for part in words]
    words = sum(words, [])
    words = [part.split(";") for part in words]
    words = sum(words, [])
    words = [part.split(".") for part in words]
    words = sum(words, [])
    words = [part.split("!") for part in words]
    words = sum(words, [])
    words = [part.split("?") for part in words]
    words = sum(words, [])
    words = [part.split("'") for part in words]
    words = sum(words, [])
    words = [word for word in words if word != ""]

    lengh = len(words)

    # finding and replacing the string:

    for i in range(lengh):

        if words[i] == mot:
            idexs.append(i)

    idx = idexs[occ - 1]
    words[idx] = rep

    # joing the list of words into one string:

    chaine = " ".join(words)
    return chaine


# the main code:


chaine = input("Paste ur paragraphe: ")
mot = input("Enter the string u want to change: ")
rep = input("Enter what u want to replace it with:  ")
occ = int(input("which occurance: "))

print("the paragraphe before modification:\n\n " + chaine)

chaine = replacment(chaine, mot, rep, occ)

print("\nthe paragraphe after modifications:\n\n " + chaine)
