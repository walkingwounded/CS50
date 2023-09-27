#scourgify lab. cleaning time!
import csv
import sys


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
        elif len(sys.argv) >3:
            sys.exit('Too many command-line arguments')
        elif (sys.argv[1]).endswith('.csv') == False:
            sys.exit('Not a CSV file')
        #elif (sys.argv[1]) != "before.csv": ####this line caused me so much 3days of hair pulling
            #sys.exit(f"Could not read {sys.argv[1]}")
        else:
            before_after(sys.argv[1], sys.argv[2])
            sys.exit()
    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")

def before_after(b, a):
    #adding header

    with open(a, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        writer.writeheader()
    #open, edit before.csv, store value
    with open(b) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            house = row["house"]
        #open, append and "write" after.csv
            with open(a, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
                writer.writerow({"first": first.strip(), "last": last, "house": house})



if __name__ == "__main__":
    main()





#### 1st code
# def before_after(b, a):
#     #adding header

#     with open(a, "w", newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
#         writer.writeheader()
#     #open, edit before.csv, store value
#     with open(b) as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             last, first = row["name"].split(",")
#             house = row["house"]
#         #open, append and "write" after.csv
#             with open(a, "a", newline="") as f:
#                 writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
#                 writer.writerow({"first": first.strip(), "last": last, "house": house})


#####Second Code
# def before_after(b, a):
#     #adding header
#     output = []
#     with open(a, "w", newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
#         writer.writeheader()
#         #writer.writerow({"first": 'first', "last": 'last', "house": 'house'})
#     #open, edit before.csv, store value
#     with open(b) as file:
#         reader = csv.DictReader(file)
#         #next(reader, None)
#         # reader = csv.DictReader(file, fieldnames=["name", "house"])
#         for row in reader:
#             #try:
#                 # last_first = line["name"].split(",")
#                 # house = line["house"]
#                 # first = last_first[1]
#                 # last = last_first[0]
#                 # last, first = row[0].split(",")
#                 # print(line[0])
#                     #house = reader[2]
#             last, first = row["name"].split(",")
#             house = row["house"]
#             output.append({"first": first.strip(), "last": last, "house": house})
#                 # last, first, house = file.replace('"','').replace(' ','').strip().split(',')
#                 #print(f"{first} {last} {house}")
#         #open, append and "write" after.csv
#     with open(a, "w", newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
#         writer.writerow({"first": 'first', "last": 'last', "house": 'house'})
#         for row in output:
#             writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
#             #except(ValueError):
#                 #sys.exit()