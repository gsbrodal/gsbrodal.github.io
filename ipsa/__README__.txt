INTRODUCTION TO PROGRAMMING WITH SCIENTIFIC APPLICATIONS
========================================================

  * Exam June 2025.

  * Aids: all, incl. computer, headphones and internet.

  * WISEflow Device Monitor must be activated throughout the exam.

  * It is not allowed to communicate with others during the exam.

  * It is not allowed to use an AI assistant like, e.g., 
    GitHub Copilot or ChatGPT.

  * When using code found on the internet, you must add a comment in your code
    with a proper link/citation to the source.
  
  * The exam questions are downloaded and solutions handed in at wiseflow.au.dk
    as a single zip file.

      Files provided at the exam:

      A.py, B.py...: Exam questions. The question statements are contained in 
                     the doc-strings in the header of the files. The exam hand 
                     in consists of uploading these files with inserted code.

      tests        : A folder with examples of test input for all questions 
                     and the corresponding correct output.

      run_tests.py : A program to run all the provided test inputs.

  * Weight of the questions (questions are not weighted equally):

     Question  Point  Name
        A
        B
        C

    Total 100 points

  * The hand in must be a single zip file with your solutions

       A.py, B.py, ... and the file run_tests.log.

    It is recommended that one hands in the complete exam folder including
    tests, not answered questions etc.
    
    Information on how to create a zip file under macOS and Windows 10 can 
    be found here:

       https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac
       https://support.microsoft.com/en-us/help/14200/windows-compress-uncompress-zip-files

    Before handing in your solutions it is strongly recommended you run the
    script run_tests.py a final time on all your solutions. The result of
    running the test script is logged throughout the exam in the file 
    run_tests.log. As a control during the grading after the exam, the content
    of run_tests.log is compared with subsequent testing to ensure consistent
    evaluation with the score you experienced obtained during the exam.
 
  * The questions should be answered using Python 3.13. You are only allowed to 
    use the standard modules installed with Python (e.g., random, math, 
    collections, etc., see https://docs.python.org/3/library/), except if 
    the questions state one or more specific modules.

  * Hand ins CANNOT be done as Jupyter Notebooks.

  * The question statements contain some input constraints, e.g., that 
    1 <= n <= 10. It is guaranteed that all test inputs for the question
    satisfy these constraints. This is not something that you need to check
    (using, e.g., assertions). The hidden test cases used for testing 
    after the exam will also satisfy these constraints.

  * The script run_tests.py can be invoked in various ways, which is described
    in the header of the file.

    One possible way is to comment out the line

       DEFAULT_FILES = ['A', 'B', 'C']

    and add the names of the files that should be tested.

  * The script run_tests.py terminates your programs after 5 seconds.
    5 seconds should be sufficient to get the majority of the test inputs 
    accepted. For some of the questions some inputs might require that your 
    code is sufficiently fast to get the last test inputs accepted. During the 
    evaluation after the exam, slightly more time will be allowed.
    
  * You do not get points if you hard code the test inputs and outputs in
    your solution. For each test input available during the exam you should 
    expect that the hidden test cases contain an input of the same "type",
    such that for each test input accepted during the exam, one should also 
    pass the corresponding hidden test case after the exam.

  * For the grading, code structure and readability have limited influence on
    the final grade. Focus will be on the functionality, i.e., how many test 
    cases are accepted. But likely, more structured code has a higher chance
    to work correctly on more inputs.
    
    You are not expected to provide comments and documentation in your
    solutions, except for the above mentioned required citations to sources
    on the internet when you use/modify code from the internet.
