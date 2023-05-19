# Senior Year Story (In Python Of Course)
schools = ["FAU", "Liberty", "Palm Beach Atlantic", "Florida Polytechnic"]
activities = ["Work", "Move", "Strengthen faith", "Become independent", "Begin dating"]

def acceptance():
    print("Acceptances processing...\n")
    for school in schools:
        print("Accepted into " + school)
    print("\nAcceptance process completed \n")

def elim():
    print("Deciding which schools...\n")
    for school in range(0, len(schools)-1):
        print("Graciously decline " + schools[school])
    print("\nFinal decision: Florida Poly\n")

def main(yr):
    if  yr >= 12:
        # Begin Applications
        print("Beginning application process...\n...")
        for school in schools:
            print("Applying to " + school)
        print()
        # Receive Acceptance letters
        acceptance()
        elim()
    else:
        print("Continue until senior year")

yr = input("What year in high-school are you? \n")
main(int(yr))
