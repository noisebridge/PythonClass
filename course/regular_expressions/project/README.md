
### Goal1: Use django's email validator regex in our own script.

### Goal1 path:
    1. Source: 
        a. The emails will come from a file.
        b. One email per line in the file.
        c. We need to supply this file

    2. Checking validity:
        a. Go line by line in the file (loop)
        b. Check the email against our email regex with python's re module.
        c. Return the result (MatchObject object or None object).
    

    3. Destination / Result:
        a. Save the valid emails in a file.
        b. Save the invalid emails in a different file.


2b needs expanded, lets break down that line:

What are the steps we should take to assemble that?
1. Find a regular expression on the internet which we understand and which achieves our validation needs.
2a. Make an iterator by opening the file and looping over each candidate.
2b. For each candidate, pass it through the compiled re object and return the result.
3. Check the result, true or false, continue with path item 3 based on that test.


