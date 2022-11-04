from random import choice
students={
	1:"Aryan Kumar",
	2:"Vinay Maurya",
	3:"Siddhant Kushwaha",
	4:"Ravi Yadav",
	5:"Sonam Bharti",
	6:"Mohammad Toffiq",
	7:"Kapil Sharma",
	8:"Pranav Parashar",
	9:"Nidhi",
	10:"Alisha Rahman",
	11:"Naincy Sagar",
	12:"Vanshika Sahni",
	13:"Zainab Fatima",
	14:"Asmit Gupta",
	15:"Aman Jha",
	16:"Mohammad Safwan Ahmad",
	17:"Mehul Singh Kushwah",
	18:"Om Kumar Gupta",
	19:"Aujas Bhandari",
	20:"Aditya Kumar Gupta",
	21:"Ansh Mandal",
	22:"Shivani Meena",
	23:"Arya Lakshmi",
	24:"Monisha",
	25:"Harshit Kumaar",
	26:"Bhumika Singh",
	27:"Samridhi Gupta",
	28:"Bhavishya Yadav",
	29:"Sahil Maurya",
	30:"Numaan Khan"
}
for i in students:students[i]=students[i].upper()
def _groupmaker(y):
    def r(p,k):p.remove(k);return k
    def s(p):p.sort();return p;
    l=[i for i in range(1,31)];return[s([r(l,choice(l))for j in range(0,int(30/y))])for i in range(y)]
def _groupprinter(k):
    for i in k:
        print(f" _________________________________\n|            GROUP - {k.index(i)+1}            |")
        for j in i:print(f"| {' '*(2-len(str(j)))}{j}:{' '*((28-len(students[j]))//2)}{students[j]}{' '*(((28-len(students[j]))//2)+((28-len(students[j]))-((28-len(students[j]))//2)*2))} |")
        print(" ---------------------------------")
def main():
    while True:
        i=input("NUMBER OF GROUPS: ")
        try:
            i=int(i)
            if 30%int(i)!=0:print(f"Error: Can't make {i} groups- Groups would not have equal number of students\nSolution: Choose any number from\n    1, 2, 3, 5, 6, 10, 15, 30")
            else:break
        except:
            print(f"Error: Can't make {i} groups- not a number\nSolution: Choose any number from\n    1, 2, 3, 5, 6, 10, 15, 30")
    _groupprinter(_groupmaker(i))
main()
