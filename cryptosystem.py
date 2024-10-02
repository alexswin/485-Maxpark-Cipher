#Main methods: encrypt(ptext) and decrypt(ctext)

class Cipher:
    #Initialize with k_s (setup key) and FIXME: k_r (rotation key) 
    def __init__(self, k_s, k_r):
        self.k_s = k_s.upper()
        self.k_r = k_r
        
        #REMOVE DUPLICATES FROM k_s
        key_unique = []
        for i in self.k_s:
            if key_unique.count(i) == 0:
                key_unique.append(i)
        self.k_s = ""
        for i in key_unique:
            self.k_s += i
        
        #GENERATE TRANSPOSITION KEY k_t
        self.k_t = ""
        m = (len(self.k_s)//3)*3
        for i in range(m):
            self.k_t += self.k_s[i]
        
        #FILL OUT CUBE
        #Put together an array "to_put_on" with the characters of k_s along with any remaining letters of the alphabet, in order
        alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
        alphabet_remaining = []
        for i in alphabet:
            if key_unique.count(i) == 0:
                alphabet_remaining.append(i)
        to_put_on = []
        for i in key_unique:
            to_put_on.append(i)
        for i in alphabet_remaining:
            to_put_on.append(i)
        
        #Build a dictionary of cube coordinates orig_c_coords using to_put_on. E.g., orig_c_coords["A"] = [0,0,0]
        self.orig_c_coords = {}
        ctr = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if [k,j,i] != [1,1,1]:
                        self.orig_c_coords[to_put_on[ctr]] = [k,j,i]
                        ctr += 1
        
        #Build a reverse dictionary of cube coordinates. E.g., orig_coords_c["000"] = "A"
        self.orig_coords_c = {}
        for i in self.orig_c_coords:
            new_str = ""
            for j in self.orig_c_coords[i]:
                new_str += str(j)
            self.orig_coords_c[new_str] = i
        
        #Fill out scrambled cube
        #Piece together key_s_complete to be key_s along with any remaining letters of the alphabet and an underscore _ in the middle (as expected by cube_rotator.get_matrix)
        key_s_complete = ""
        for i in range(13):
            key_s_complete += to_put_on[i]
        key_s_complete += "_"
        for i in range(13,26):
            key_s_complete += to_put_on[i]
        import cube_rotator
        cube = cube_rotator.get_matrix(key_s_complete)
        cube_rotator.scramble_cube(cube, self.k_r)
        
        #Create dictionary for coordinates on scrambled cube
        self.scrambled_c_coords = {}
        for z in range(3):
            for y in range(3):
                for x in range(3):
                    if not(x==1 and y==1 and z==1):
                        #The coordinates on cube as implemented by cube_rotator's methods do not quite match the coordinates expected here. This fixes them as it builds the dictionary.
                        curr_char = cube[z][2-y][x]
                        self.scrambled_c_coords[curr_char] = [x,y,z]
        
        #Build a reverse dictionary from the first
        self.scrambled_coords_c = {}
        for i in self.scrambled_c_coords:
            new_str = ""
            for j in self.scrambled_c_coords[i]:
                new_str += str(j)
            self.scrambled_coords_c[new_str] = i
        
        
    #ENCRYPTION
    
    #Generate Stage 1 Ciphertext (private method)
    def __encrypt_to_ctext_1(self, ptext):
        ctext_1 = ""
        for i in ptext:
            curr_coords = self.orig_c_coords[i.upper()]
            ctext_1 += str(curr_coords[0]) + str(curr_coords[1]) + str(curr_coords[2])
        return ctext_1
    
    #Generate Stage 2 Ciphertext (private)
    def __encrypt_to_ctext_2(self, ctext_1):
        #Read ctext_1 into cols horizontally
        cols = []
        for y in self.k_t:
            cols.append([])
        for i in range(len(ctext_1)):
            cols[i%len(cols)].append(ctext_1[i])
        
        #Figure out where each column of cols should end up after sorting
        col_dest = []
        for i in self.k_t:
            place = 0
            for j in self.k_t:
                if j < i:
                    place += 1
            col_dest.append(place)
        
        #Build a vector col_sorter so that col_sorter[i] returns the column number of the column in cols (unsorted) that will need to end up in position i after sorting
        col_sorter = []
        for i in range(len(col_dest)):
            for j in range(len(col_dest)):
                if col_dest[j] == i:
                    col_sorter.append(j)
        
        #Alphabetize k_t into k_t_sorted and create alphabetized table
        k_t_sorted = ""
        for i in col_sorter:
            k_t_sorted += self.k_t[i]
            
        cols_sorted = []
        for i in col_sorter:
            cols_sorted.append(cols[i])
        
        #Print both tables
        #prtstr = "Pre-alphabetized table:				Alphabetized table:\n"
        #prttable1 = []
        #tmpstr = ""
        #for i in range(len(self.k_t)):
        #    tmpstr += self.k_t[i]
        #    if i < len(self.k_t) - 1:
        #        tmpstr += " | "
        #prttable1.append(tmpstr)
        #for j in range(len(cols[0])):
        #    tmpstr = ""
        #    for i in range(len(cols)):
        #        tmpstr += str(cols[i][j])
        #        if i < len(cols) - 1:
        #            tmpstr += " | "
        #    prttable1.append(tmpstr)
        #tmpstr = ""
        #prttable2 = []
        #for i in range(len(k_t_sorted)):
        #    tmpstr += k_t_sorted[i]
        #    if i < len(k_t_sorted) - 1:
        #        tmpstr += " | "
        #prttable2.append(tmpstr)
        #for j in range(len(cols_sorted[0])):
        #    tmpstr = ""
        #    for i in range(len(cols_sorted)):
        #        tmpstr += str(cols_sorted[i][j])
        #        if i < len(cols_sorted) - 1:
        #            tmpstr += " | "
        #    prttable2.append(tmpstr)
        #for i in range(len(prttable1)):
        #    prtstr += prttable1[i] + "		" + prttable2[i] + "\n"
        #print(prtstr)
        
        #Build and return ctext_2
        ctext_2 = ""
        for i in cols_sorted:
            for j in i:
                ctext_2 += str(j)
        return ctext_2
    
    #Final encryption step
    def encrypt(self, ptext):
        #Fix ptext
        new_ptext = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
        for i in ptext:
            if alphabet.count(i.upper()) > 0:
                new_ptext += i.upper()
        ptext = new_ptext
        
        while len(ptext) % (len(self.k_s)//3) != 0:
            ptext += "x"
        ptext = ptext.upper()
        #print("Trimmed plaintext: ", ptext)
        
        ctext_1 = self.__encrypt_to_ctext_1(ptext)
        #print("Stage 1 ciphertext: ", ctext_1)
        ctext_2 = self.__encrypt_to_ctext_2(ctext_1)
        #print("Stage 2 ciphertext: ", ctext_2)
        
        #Build ordered triples from ctext_2
        triples = []
        for i in range(len(ctext_2)//3):
            curr_indx = 3*i
            new_trip = []
            for j in range(curr_indx,curr_indx+3):
                new_trip.append(ctext_2[j])
            triples.append(new_trip)
        
        #Build and return ctext
        ctext = ""
        for i in triples:
            lookup = ""
            for j in i:
                lookup += str(j)
            #If (1,1,1), insert random nonalphabetic character
            if lookup == "111":
                poss_chars = ["~","!","@","#","$","%","^","&","*","(",")","-","_","+","=","|","`","?",",",".","/","[","]","{","}"]
                #import secrets
                #rindx = secrets.randbelow(len(poss_chars))
                import random
                #ctext += poss_chars[rindx]
                ctext += random.choice(poss_chars)
                #ctext += "!"
            else:
                ctext += self.scrambled_coords_c[lookup]
        #print("Final ciphertext: ", ctext)
        return ctext
    
    #DECRYPTION
    
    #Work out what ctext_2 must have been
    def __decr_ctext_2(self, ctext):
        ctext_2 = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
        for i in ctext:
            if alphabet.count(i) == 0:
                ctext_2 += "111"
            else:
                new_str = ""
                for j in self.scrambled_c_coords[i]:
                    new_str += str(j)
                ctext_2 += new_str
        return ctext_2
    
    #WOrk out what ctext_1 must have been
    def __decr_ctext_1(self, ctext_2):
        #Build table columns (post-alphabetizing)
        decr_cols_alph = []
        ctr = 0
        m = (len(self.k_s)//3)*3
        num_rows = len(ctext_2) // m
        for i in range(m):
            decr_cols_alph.append([])
            for j in range(num_rows):
                decr_cols_alph[i].append(ctext_2[ctr])
                ctr += 1
        
        #Figure out where each column of cols ended up after sorting in decr_cols_alph
        col_dest = []
        for i in self.k_t:
            place = 0
            for j in self.k_t:
                if j < i:
                    place += 1
            col_dest.append(place)
            
        #De-alphebatize these columns
        decr_cols_dealph = []
        for i in range(len(decr_cols_alph)):
            decr_cols_dealph.append(decr_cols_alph[col_dest[i]])
        
        #Return ctext_1
        ctext_1 = ""
        for i in range(num_rows):
            for j in range(len(decr_cols_dealph)):
                ctext_1 += decr_cols_dealph[j][i]
        return ctext_1
    
    #Final decryption step
    def decrypt(self, ctext):
        ctext_2 = self.__decr_ctext_2(ctext)
        ctext_1 = self.__decr_ctext_1(ctext_2)
        ptext = ""
        curr_trip = ""
        for i in ctext_1:
            curr_trip += str(i)
            if len(curr_trip) == 3:
                ptext += self.orig_coords_c[curr_trip]
                curr_trip = ""
        return ptext
    
