# python3
# 221RDB301 Kristers Jānītis 3. grupa

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    
    c_time = [0]*n
    
    for i in range(m):
        next_thread = c_time.index(min(c_time))
        s_time = c_time[next_thread]
        c_time[next_thread] += data[i]
        output.append((next_thread, s_time))
    
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input("Enter integers: ").split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input("Enter time: ").split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread, s_time in result:
        print(thread, s_time)
    



if __name__ == "__main__":
    main()
