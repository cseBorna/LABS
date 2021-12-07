def waitingTime(processes,n,bt,wt):
    #waiting time of first process is 0
    wt[0]=0
    
    for i in range(1,n):
        wt[i]=bt[i-1]+wt[i-1]
        
        
def turnAroundTime(processes,n,bt,wt,tat):
    for i in range(n):
        tat[i]=bt[i]+wt[i]
        
    
def averageTime(processes,n,bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    
    waitingTime(processes,n,bt,wt)
    
    turnAroundTime(processes,n,bt,wt,tat)
    
    print("Processes  BurstTime    WaitingTime   TurnAroundTime")
    
    for i in range(n):
         
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i+1) + "\t\t" +
                    str(bt[i]) + "\t " +
                    str(wt[i]) + "\t\t " +
                    str(tat[i]))
 
    print( "Average waiting time = "+str(total_wt / n))
    print("Average turn around time = "+str(total_tat / n))
    
if __name__ =="__main__":
         
    # process id's
    n=int(input("How many processes: "))
    p=[]
    for i in range(1,n+1):
       p=i
    
 
    # Burst time of all processes
    burst_time = []
    print("Enter burst time:")
    for i in range(1,n+1):
        ele=int(input())
        burst_time.append(ele)
 
    averageTime(p, n, burst_time)
    