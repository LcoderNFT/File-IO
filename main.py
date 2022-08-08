fileName = input("Enter file name: ")
maxPrice = float(input("Enter max price: "))
infile = open(fileName)
read = infile.read()
infile.close()

read = read.splitlines()

outfile = open("out.txt", "w")
count = 0 
for i in range(0, len(read), 2):
    name = read[i]
    price = read[i+1]
    if maxPrice >= float(price):
        outfile.write(name + " " + price + "\n")
        count = count + 1
outfile.write(str(count) + " dishes are below max price")

outfile.close()
