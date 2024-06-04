#CMSC 201 Homework 5
#Nicole Attram - June 3, 2024

#PROBLEM 1

if __name__ == '__main__':
    start = "ATG"
    stop1 = 'TAG'
    stop2 = 'TAA'
    stop3 = 'TGA'

    def gene(string): #creates function gene for a given string
        list = [] #created empty list to hold codon
        codon=3 #set index to split up list by 3

        for i in range(0, len(string), codon):
            list.append(string[i:i+codon]) #creates a list of codons

        start_ind = [] #creates an empty set for stop indices
        for j in list:
            if list[j].upper() == start:
                start_ind.append(j)

            if list[j].upper() == stop1 or list[j].upper() == stop2 or list[j].upper() == stop3:
                stop_ind = j #adds an indice to the list for each stop codon

        codon_list = []

        if start_ind == []:
            codon_list = []

        else:
            for k in len(stop_ind):
                for l in list:
                    codon_list.append(list[start_ind:k])

        return codon_list

    user = str(input("Please insert your gene: "))

    gene_extract = gene(user.upper())