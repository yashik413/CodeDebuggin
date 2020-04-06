for i in range(int(input())): 				# input() is changed to int(input()), to make it a integer
        word = input()
        word = word.upper() 				# word is assigned to word.upper(),it has a return value
        vowels = ['A','E','I','O','U']
        count = 0 					# removed a Equal Sign to initialize count
        for j in range(1,len(word)):			# added Colon (:), length() is changed to len(); length is not a function
                if word[j] in vowels[:]:		# added Colon inside square brackets, vowels[] to vowels[:]
                        if j == 0: 			# added Equal Sign
                                count += 1		# Changed count ++ to count += 1
                        elif word[j+1] in vowels[:]: 	# added Colon inside square brackets, vowels[] to vowels[:]
                                pass			# change break to pass 
                        else:
                                count += 1		#Changed count ++ to count += 1; python has ++ increment operator
        print (count)
