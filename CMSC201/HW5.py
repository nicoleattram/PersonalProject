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
        for j in range(0,len(list)):
            if list[j].upper() == start:
                start_ind.append(j)

            if list[j].upper() == stop1 or list[j].upper() == stop2 or list[j].upper() == stop3:
                stop_ind = j+1 #adds an index to the list for each stop codon

        codon_list = []
        codons = ''  # creates empty string for codons

        if start_ind == []:
            codon_list = []

        else:
            for k in start_ind:
                codons = ''
                for l in range(k, stop_ind): #from start index to stop index
                    codons += list[l]
                    codons = ''.join(codons) #joins all the codons together

                codon_list.append(codons)

        return codon_list

    user = str(input("Please insert your gene: "))

    gene_extract = gene(user.upper())
    print(gene_extract)