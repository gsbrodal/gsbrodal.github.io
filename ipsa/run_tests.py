'''
    This program tests your solutions for the various problems on the
    test data provided in the subfolder 'tests'.

    The program can be run in various ways (depending on your setup):

     (1) Run the program by clicking it

     (2) Command line:

          > run_tests.py A B C

         or 

          > python run_tests.py A B C 

     (3) From your IDE (e.g. in IDLE shift-F5 allows you to provide arguments)

    If no files to test are given as arguments, all .py files in the
    current folder will be tested. You can limit the set of default
    files to be tested by setting DEFAULT_FILES below.

    The optional argument --verbose=<value> determines the amount of output:
    
      -1 : Only print statistics on number of tests passed
       0 : Print names of failed tests
       1 : Print names of all tests
       2 : Print names of all tests, and details for failed tests (default)
       3 : Print details for all tests                                

    On failed tests the script by default continues with the next test.
    To abort after first failed test use --abort. E.g.

       > python run_tests.py A --verbose=3 --abort
'''


DEFAULT_FILES = None
#DEFAULT_FILES = ['A', 'B', 'C']


######################################################################
#                   Do not edit below this line                      #
######################################################################

TIMEOUT         = 5  # seconds before test killed
TEST_FOLDER     = 'tests/'
TEST_LOG_FILE   = 'run_tests.log'
DEFAULT_VERBOSE = 2
DEFAULT_ABORT   = False

import re
import subprocess
from glob import glob
import os
import sys
from tempfile import TemporaryFile

PYTHON = sys.executable  # The Python interpreter for running test programs


def purify(lines, compress_spaces=True):
    '''Remove redundant white spaces from list of lines.'''

    # remove trailing white space
    lines = [line.rstrip() for line in lines]
    # replace multiple whitespaces by single white space
    if compress_spaces:
        lines = [re.sub(r'\s+', ' ', line).strip() for line in lines]
    # remove empty lines
    lines = [line for line in lines if line]

    return lines


def load_text(file, maxsize=-1, compress_spaces=True):
    '''Load & purify text file, restricted to first maxsize bytes.'''

    if isinstance(file, str):
        with open(file) as f:
            return purify(f.readlines(maxsize), compress_spaces=compress_spaces)
    else:
        return purify(file.readlines(maxsize), compress_spaces=compress_spaces)


log_indent = 0  # current indent for terminal log messages

def log(title='', lines=[], end='\n', indent=0, mark=''):
    '''Print log message to screen in below format:

       title
       > lines[0]
       > lines[1]
       > ...

       indent = indentation for this and successive calls to log.
    '''
    
    global log_indent
    log_indent += indent
    prefix = ' ' * (log_indent - len(mark)) + mark
    
    if type(lines) == str:
        lines = [lines]
    if title:
        print(prefix + title, end=end, flush=True)
    for line in lines:
        print(prefix + '> ' + line, end=end, flush=True)


def run_test(program, test_in, test_out, verbose, timeout=TIMEOUT):
    '''Run program with test_in as input. Returns True if and only if
       the generated output is test_output, and the execution did not
       generate any errors.

       verbose determines the amount of printed log.
    '''

    if verbose >= 1:
        log(f'{program} {test_in} ', end='')

    # Excecute program in subprocess

    with TemporaryFile('w+') as answer_file, \
         TemporaryFile('w+') as error_file, \
         open(test_in) as in_file:
        try:
            result = subprocess.run(
                [PYTHON, program],
                input=''.join(line.rstrip() + '\n' for line in in_file),
                #stdin=in_file,  # can fail on Mac 
                stdout=answer_file,
                stderr=error_file,
                timeout=timeout,
                text=True
            )
        except Exception as e:
            exception = str(e)
        else:
            exception = ''

        # Analyze test result
        maxsize    = max(1024, 2 * os.path.getsize(test_out))
        truncated  = answer_file.tell() > maxsize

        answer_file.seek(0)
        error_file.seek(0)

        answer     = load_text(answer_file, maxsize=maxsize)
        error      = load_text(error_file)
        test_input = load_text(test_in, compress_spaces=False)
        correct    = load_text(test_out)
        
        if exception:
            error.append(exception)

    ok = not error and answer == correct

    if ok and verbose > 0:
        log('[ok]')
    if not ok and verbose >= 0:
        if verbose > 0:
            log('[failed]')
        else:
            log(f'{program} {test_in} [failed]')
    if not ok and verbose >= 2 or verbose >= 3:
        log(indent=2)
        log('Input', test_input)
        log('Correct output', correct)
        if not ok:
            if len(answer) > len(correct) + 3:
                truncated = True
                answer = answer[:len(correct) + 3]
            log('Received output')
            for i, line in enumerate(answer):
                if i < len(correct) and line == correct[i]:
                    log(lines=line)
                else:
                    log(lines=line, mark='*')
            if not answer:
                log(lines='(none)')
            elif truncated:
                log(lines='(truncated)')
            elif len(answer) < len(correct):
                log(lines='(too few lines)')
            if error:
                log('Error', error[-5:])
        log(indent=-2)

    return ok


def test_program(program, verbose):
    '''Given a program name, runs program on all test data in
       TEST_FOLDER/program/.... ending on .in, .in0, .in1...

       Returns (#tests passed, #tests performed).

       verbose = see run_test.
    '''

    global on_fail_abort
    
    if program.endswith('.py'):
        program = program[:-3]

    in_files = [file
                for file in glob(TEST_FOLDER + program + '/*.in*')
                if re.search(r'[.]in[0-9]*$', file)]
    in_files.sort()

    passed = 0
    for test_in in in_files:
        test_out = test_in.replace('.in', '.out')
        result = run_test(program + '.py', test_in, test_out, verbose=verbose)
        with open(TEST_LOG_FILE, 'a') as log_file:
            print(test_in, result, file=log_file)

        if result:
            passed += 1
        elif on_fail_abort:
            raise StopIteration 

    return (passed, len(in_files))

        
def test_all(programs=None, verbose=1):
    '''Runs test_program on all files in programs.

       Prints statistics on the number of passed tests.

       verbose = see run_test.
    '''

    results = {}
    for program in programs:
        results[program] = test_program(program, verbose=verbose)

    # Print statistics
    log('\nTests passed:\n')
    log(indent=2)
    width = max(map(len, [*results, 'Total']))
    total_passed = total_tests = 0
    for program, (passed, tests) in results.items():
        log(f'{program:{width}} {passed:3}/{tests}')
        total_passed += passed
        total_tests += tests
    final_result = f'{"Total":{width}} {total_passed:3}/{total_tests}'
    log('-' * len(final_result)) 
    log(final_result)
    log('=' * len(final_result)) 
    log(indent=-2)

######################################################################

if __name__ == '__main__':
    args = sys.argv[1:]
    verbose = DEFAULT_VERBOSE
    on_fail_abort = DEFAULT_ABORT

    # identify --verbose=... command line argument
    for arg in args:
        if arg.startswith('--'):
            if re.match('--verbose=[-]?[0-9]+$', arg):
                verbose = int(arg.split('=')[1])
            elif arg == '--abort':
                on_fail_abort = True
            else:
                raise Exception('unknown option ' + arg)

    args = [arg for arg in args if not arg.startswith('--')]

    # identify files
    if args:
        files = args
    elif DEFAULT_FILES != None:
        files = DEFAULT_FILES
    else:
        files = sorted(glob('*.py'))
        if '__file__' in globals():
            this_program = os.path.basename(__file__)
            if this_program in files:
                files.remove(this_program)

    # run the tests
    try:
        test_all(files, verbose=verbose)
    except StopIteration:  # raised on first fail if on_fail_abort == True
        pass

    if len(sys.argv) <= 1:  # potentially run by clicking
        input('\nPress [Enter] to exit')
