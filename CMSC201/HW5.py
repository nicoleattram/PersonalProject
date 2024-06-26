#CMSC 201 Homework 5
#Nicole Attram - June 3, 2024

#PROBLEM 1
def extract_gene(sequence):  # creates function gene for a given string
    start = "ATG"
    stop1 = 'TAG'
    stop2 = 'TAA'
    stop3 = 'TGA'

    list = []  # created empty list to hold codon
    codon = 3  # set index to split up list by 3

    while sequence.lower() != 'stop':
        if sequence == 'seq': #when user inserts their own seq
            for i in range(0, len(sequence), codon):
                list.append(sequence[i:i + codon])  # creates a list of codons

            start_ind = []  # creates an empty set for stop indices
            stop_ind = []

            for j in range(0, len(list)):
                if list[j].upper() == start:
                    start_ind.append(j)

                elif list[j].upper() == stop1 or list[j].upper() == stop2 or list[j].upper() == stop3:
                    stop_ind.append(j + 1)  # adds an index to the list for each stop codon

            codon_list = []
            codons = ''  # creates empty string for codons

            if start_ind == []:
                codon_list = []

            else:
                for k in start_ind:
                    codons = ''
                    for l in range(k, stop_ind[0]):  # from start index to stop index
                        codons += list[l]
                        codons = ''.join(codons)  # joins all the codons together

                    codon_list.append(codons)
        else: #what number of codons


        return codon_list

        user = str(input("Please insert your gene or stop to end: "))


if __name__ == '__main__':

    user = str(input("How many codons do you want to creates? Please enter 'seq' to add your" +
                     " own gene or stop to end: "))

    gene_extract = extract_gene(user.upper())
    print(gene_extract)