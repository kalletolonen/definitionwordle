from csv import writer

def winner(guesses):
    print(f"You won with {guesses} guesses")

def stats(thisWord,guesses):
    list_data=[thisWord,guesses]
    
    with open('scores.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(list_data)  
        f_object.close()
    
    

