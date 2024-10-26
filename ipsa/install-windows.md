# Windows 11 installation

## CPython, pip, and IDLE

From [python.org](https://www.python.org/downloads) you can download the reference implementation of Python, nicknamed CPython (since it is coded in C):

* Open [www.python.org/downloads](https://www.python.org/downloads)
* Select "Download Python 3.13.0" or newer
* Download "Windows installer (64-bit)"
* Run the downloaded application, e.g python-3.13.0-amd64.exe
* Select "Add python.exe to PATH"
* Select "Install now"

_Note_. By default a 64-bit Windows version of Python is installed. For memory consuming Python programs on Windows (requiring above 2GB of RAM), it is important that you download the 64 bit version of Python, also available at [www.python.org/downloads/windows](https://www.python.org/downloads/windows) as "Windows installer (64-bit)". The 32-bit version is "Windows installer (32-bit)", and limits your programs to using 2GB of RAM.

Additional **Python packages** are installed using the program "pip3", included in the above download. To e.g. install the _SciPy_ package that will be used in the course (see [SciPy.org](https://www.scipy.org) for more information on the package):

* Open a Command Prompt (Windows-key + type "cmd")
* Run "pip3 install scipy"

Part of the download is **IDLE**, an **integrated development environment** for Python. Existing Python files (ending on .py) can be opened and edited in IDLE by right-clicking on the file and selecting "Edit with IDLE". The IDLE application should also appear in your Windows Start menu (or Windows-key + "IDLE").

A Python program program can be **executed** in several ways.

1. The easiest is just to double click on the file name, but this closes the output window immediately after the program terminates.
2. Open the program in IDLE and press F5 to "Run Module".
3. Execute the program from a Windows shell:
    - Open a Command Prompt (Windows-key + type "cmd")
    - Change to the relevant folder, e.g. "cd C:\Users\ _username_ \Desktop\"
    - Run the python program (here test.py on your desktop) using e.g. "python test.py"

## Anaconda - an easy start to Python

Anaconda wrote on their [webpage](https://www.anaconda.com) that it is "The Most Popular Python Data Science Platform". Anaconda bundles Python, a lot of libraries, and the [Spyder IDE](https://github.com/spyder-ide). To install Anaconda:

* Open [www.anaconda.com/download](https://www.anaconda.com/download)
* Select "Download"
* Run the download application,	e.g. Anaconda3-2023.09-Windows-x86_64.exe

_Note_: Anaconda does not necessarily support the most recent version of Python provided at [python.org](https://www.python.org).

## PyPy - for the performance demanding Python programmer

PyPy is an alternative implementation of the Python language that is often faster than CPython, but does not support the most recent versions of Python. To install PyPy:

* Open [pypy.org](https://pypy.org)
* Select "Download PyPy"
* Find the section with the most recent Python 3 implementation	and download the Windows binary (64bit) (possibly [pypy3.10-v7.3.13-win64.zip](https://downloads.python.org/pypy/pypy3.10-v7.3.13-win64.zip)).
* Unzip the download folder and move the folder to an appropriate place, e.g. C:\Program Files\
* Add the PyPy folder to your path:
    * Windows-key + "Edit the system environment variables"
    * Select "Environment variables"
    * Select "Path"
    * Select "New" and add the path to the folder with pypy3.exe, e.g. C:\Program Files\pypy3.10-v7.3.13-win64\

The speed improvements of PyPy over CPython are due to the usage of the Just-In-Time compilation technique, that e.g. also is used inside the Google Chrome browser for executing JavaScript (see the Wikipedia page on [Chrome V8](https://en.wikipedia.org/wiki/Chrome_V8) and by Java Virtual Machines for executing Java programs (bytecode) (see more on [Just-In-Time compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation) on Wikipedia).
