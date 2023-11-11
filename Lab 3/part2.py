def num_of_wc_runs(n, m):
    # Memoization dictionary to store already computed results
    memo = {}
    

    def helper(s, b):
        
        # Base cases
        if b == 1: #if number of bricks is equal to 1 then we know that the number of tests required is equal to s-1
            memo[(s, b)] = s-1
            return s - 1
        if s == 1: #no tests required if there is 1 brick equal to 1
            memo[(s,b)] = 0
            return 0

        # Check if the result is already computed
        if (s, b) in memo:
            return memo[(s, b)]

      
        
        for k in range(1, s):
            # 1 - to count the current test, the first helper call is when the brick breaks
            # 2nd helper call is when the brick withstands the force setting

            tests = 1 + max(helper(k, b - 1), helper(s - k, b))
            
            if (s, b) not in memo or tests < memo[(s, b)]:
                memo[(s,b)] = tests
        

        # Memoize the result and return
        return memo[(s,b)]

  
    return helper(n, m)


result = num_of_wc_runs(10, 10)
print(f"The number of worst-case runs: {result}")


def next_setting(n,m):
    minRuns = None
    minRunsK = None

    for k in range(1,n):
        
        #need to check which has more runs, if the brick breaks at k vs if the brick doesnt break at k

        worstCase = max(num_of_wc_runs(k,m-1),num_of_wc_runs(n-k,m))

        #if the worstCase is less than minRuns, we want to set minRuns to worstCase and minRunsK to the current value of k
        #this essentially means that this initial selection value of k is more optimal than the previous

        if not minRuns or worstCase < minRuns:
            minRuns = worstCase
            minRunsK = k
    
    return minRunsK

optimalK = next_setting(100,2)

print(optimalK)