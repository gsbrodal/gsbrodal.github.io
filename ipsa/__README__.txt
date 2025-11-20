[ENGLISH VERSION BELOW]

INTRODUKTION TIL PROGRAMMERING MED VIDENSKABELIGE ANVENDELSER
=============================================================

  * Eksamen juni 2026.

  * Hjælpemidler: Egen computer, internetadgang ikke tilladt (bortset fra til at
    hente eksamensformuleringen og at aflevere ens eksamensbesvarelse på
    wiseflow.au.dk, og for at kunne køre WISEflow Device Monitor).

  * WISEflow Device Monitor skal være aktiveret under eksamen.

  * Det er ikke lovligt at kommunikere med andre om eksamensopgaverne under
    eksamen.

  * Det er ikke tilladt at bruge en AI assistant, som f.eks. ChatGPT eller
    GitHub Copilot. Lokalt installerede AI assistenter på ens computer er heller
    ikke tilladt.

  * Sørg for at angive en kommentar i koden med en kildehenvisning, hvis man
  anvender kode fra f.eks. kursusslidesene.

  * Opgaveformulering hentes og besvarelserne afleveres på wiseflow.au.dk som en
    enkelt zip file.

      Filer der udleveres til eksamen:

      A.py, B.py...: Opgaver. Formuleringerne fremgår af doc-teksten i starten
                     af filerne. En eksamensbesvarelse består af upload af disse
                     filer med indsat kode (som zip-fil, som beskrevet
                     nedenfor).

      tests        : Folder med eksempler på test input og tilsvarende korrekte
                     output for alle opgaver.

      run_tests.py : Et program til at køre alle de udleverede tests.

  * Vægtningen af opgaverne:

     Problem  Point  Navn
        A
        B
        C

    Totalt 100 point.

  * Aflevering skal være en zip fil med opgaverne

       A.py, B.py, ... og filen run_tests.log.

    Det anbefales at man afleverer hele eksamensfolderen, inklusiv tests, ikke
    besvarede opgaver etc.
    
    Information om hvordan man laver en zip fil under macOS og
    Windows findes her:

       https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac
       https://support.microsoft.com/en-us/help/14200/windows-compress-uncompress-zip-files

    Inden man afleverer bør man køre run_tests.py en sidste gang på alle ens
    besvarelser. Resultatet af testene gemmes løbende i run_tests.log. Som
    kontrol, vil indholdet af run_tests.log blive sammenholdet med resultatet af
    den efterfølgende evaluering.
 
  * Opgaverne skal laves i Python 3.14. Der må kun bruges de standard moduler
    der følger med Python (f.eks. random, math, collections, etc., se
    https://docs.python.org/3/library/).

  * Eksamensbesvarelsen kan IKKE afleveres i en Jupyter Notebook.

  * I opgavebeskrivelser er der angivet nogle inputbetingelser, f.eks. at 
    1 <= n <= 10. Det er en garanti som alle test input vil opfylde. Det er ikke
    noget man behøver checke for (med assertions eller lignende). De skjulte
    input vil også overholde disse inputbetingelser.

  * run_tests.py kan køres på forskellige måder, hvilket beskrives i starten af
    filen. 

  * run_tests.py stopper jeres program efter 5 sekunder, men det burde være
    rigeligt til at løse de fleste testinstanser. I enkelte opgaver kan nogle af
    testinstanserne dog kræve at man har en tilstrækkelig hurtig løsning for at
    få de sidste testinstanser godkendt. Til den efterfølgende evaluering af
    programmerne vil der blive tilladt lidt mere tid.
    
  * Man får ikke point for at håndtere input ved at hard code input instanser og
    deres svar. For hvert input må man forvente at der vil være et hemmeligt
    input af samme "type", så hvis man klarer et input så bør man også klare det
    tilsvarende skjulte input i den efterfølgende evaluering.

  * I karaktergivningen har kodestruktur og læsbarhed begrænset indflydelse på
    den endelige karakter. Fokus er på funktionaliteten af koden, d.v.s, hvor
    mange testinstanser der bliver godkendt. Men sandsynligivs virker mere
    struktureret kode korrekt på flere inputinstanser.

    Det forventes ikke at man skriver kommentarer og docstring's i ens
    besvarelser, ud over de ovenstående kilder når man genbruger/ændrer
    eksisterende kode.


INTRODUCTION TO PROGRAMMING WITH SCIENTIFIC APPLICATIONS
========================================================

  * Exam June, 2026.

  * Aids: Own computer, internet access not allowed (except for downloading the
    exam and submitting your exam answers on wiseflow.au.dk, and running the
    WISEflow device monitor.)

  * WISEflow Device Monitor must be activated throughout the exam.

  * It is not allowed to communicate with others during the exam.

  * It is not allowed to use an AI assistant like, e.g., ChatGPT and GitHub
    Copilot. Locally installed AI assistants on your computer are also not
    allowed.

  * When reusing code, e.g., from course slides, you must put a comment in your
    code with a reference to the source.
  
  * The exam questions are downloaded and your answers submitted to
    wiseflow.au.dk as a single zip file.

      Files provided at the exam:

      A.py, B.py...: Exam questions. The question statements are contained in 
                     the doc-strings in the header of the files. Your exam
                     submission consists of uploading these files with inserted
                     code.

      tests        : A folder with examples of test input for all questions 
                     and the corresponding correct output.

      run_tests.py : A program to run all the provided test inputs.

  * Weight of the questions (questions are not weighted equally):

     Question  Point  Name
        A
        B
        C

    Total 100 points

  * The final submission must be a single zip file with your solutions

       A.py, B.py, ... and the file run_tests.log.

    It is recommended that one submits the complete exam folder including tests,
    not answered questions etc.
    
    Information on how to create a zip file under macOS and Windows can 
    be found here:

       https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac
       https://support.microsoft.com/en-us/help/14200/windows-compress-uncompress-zip-files

    Before submitting your solutions it is strongly recommended you run the
    script run_tests.py a final time on all your solutions. The result of
    running the test script is logged throughout the exam in the file
    run_tests.log. As a control during the grading after the exam, the content
    of run_tests.log is compared with subsequent testing to ensure consistent
    evaluation with the score you experienced obtained during the exam.
 
  * The questions should be answered using Python 3.14. You are only allowed to 
    use the standard modules installed with Python (e.g., random, math,
    collections, etc., see https://docs.python.org/3/library/).

  * Submissions CANNOT be done as a Jupyter Notebook.

  * The question statements contain some input constraints, e.g., that 
    1 <= n <= 10. It is guaranteed that all test inputs for the question satisfy
    these constraints. This is not something that you need to check (using,
    e.g., assertions). The hidden test cases used for testing after the exam
    will also satisfy these constraints.

  * The script run_tests.py can be invoked in various ways, which is described
    in the header of the file.

  * The script run_tests.py terminates your programs after 5 seconds. 5 seconds
    should be sufficient to get the majority of the test inputs accepted. For
    some of the questions some inputs might require that your code is
    sufficiently fast to get the last test inputs accepted. During the
    evaluation after the exam, slightly more time will be allowed.
    
  * You do not get points if you hard code the test inputs and outputs in
    your solution. For each test input available during the exam you should 
    expect that the hidden test cases contain an input of the same "type",
    such that for each test input accepted during the exam, one should also 
    pass the corresponding hidden test case after the exam.

  * For the grading, code structure and readability have limited influence on
    the final grade. Focus will be on the functionality, i.e., how many test
    cases are accepted. But likely, more structured code has a higher chance to
    work correctly on more inputs.
    
    You are not expected to provide comments and docstrings in your solutions,
    except for the above mentioned required references to sources when you
    reuse/modify existing code.
