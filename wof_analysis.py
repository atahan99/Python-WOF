"""

Assignment: 12.1 - Wof Analysis


Description:
   This is an application that analysis the content of the phrases.txt file. 


"""


import string
import matplotlib.pyplot as plt



def main():

    wof_analysis=plt.figure()#for saving the figure
    file=open("phrases.txt")
    #filter out all non-alphabethic characters
    letters=string.ascii_uppercase
    count={}
    for i in letters:
        count[i]=0
    n=0
    for i in file:
    #reading each letter from line
        for j in i:
            if(j.isalpha()):
                n+=1 
                letter=j.upper()
                count[letter]+=1
    file.close()
    freq={}
    for i in count:
        freq[i]=count[i]/n
    #x-axis and y-axis
    #unpacking keys(items)
    x,y=zip(*freq.items())
    plt.bar(x,y)#plotting bar plot
    plt.xlabel("Letter")
    plt.ylabel("Letter Appearance Frequency")
    plt.title("Letter Frequency in Puzzle Phrases")
    plt.grid()
    #saving figure to pdf
    wof_analysis.savefig("wof_analysis_akucuk.pdf")
    plt.show()#showing the plot



if __name__ == '__main__':
    main()

