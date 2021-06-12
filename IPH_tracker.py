def main(): # IPH tracker for hourly basis   
    
    hrs = int(input("Enter the number of hours you are working today :")) #enter the total number of hours you are working today 
    
    iph = int(input("Enter the avarage IPH of the day(plz enter a whole number nd add 1 just to just to be on the safe side) :")) #enter the average IPH per hour
    
    total = hrs * iph # total tasks for the whole shift
    
    periph = 0 # IPH per hour resolved as per the qdash

    left_tlt = 0 # tasks left to be resolved by end of day

    cmg_iph = 0 # IPH you need to mantain in the coming hours to meet the resolves 

    print("You need to do total of ", str(total)+ " tasks today.")

    for i in range(0 , hrs):

        periph = int(input(print("Enter the IPH for", str(i+1)+ " hour")))
        left_tlt = total - periph
        total = left_tlt

        print("Left tasks for the shift::", str(left_tlt))

        cmg_iph = left_tlt / (hrs - (i+1))
        
        print("Upcoming IPH ::", str(cmg_iph))

if __name__ == "__main__":
	main()
