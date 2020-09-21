# firstTenDigits
A non-recursive solution to finding the first 10-digit prime in Euler's number

We import a string representing the first 1000 digits trailing the decimal.
Then split the string into every ten digit number which is not obviously non-prime.
The final step is to divide iteratively using the list of primes less than 1e5.
