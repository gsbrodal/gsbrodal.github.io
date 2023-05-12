INTRODUKTION TIL PROGRAMMERING MED VIDENSKABELIGE ANVENDELSER
=============================================================

  * Eksamen 17. juni 2023.

  * Hjælpemidler: alle, inkl. computer, høretelefoner og internet.

  * ITX Flex skal være aktiveret under eksamen.

  * Det er ikke lovligt at kommunikere med andre om eksamensopgaverne
    under eksamen.

  * Det er ikke tilladt at bruge en AI assistant som f.eks.
    GitHub Copilot eller ChatGPT.

  * Sørg for at angive en kommentar i koden med en kildehenvisning,
    hvis man anvender kode man har fundet på internettet.

  * Opgaveformulering hentes og afleveres på eksamen.au.dk.

      Filer der udleveres til eksamen:

      A.py, B.py...: Opgaver. Formuleringerne fremgår af doc-teksten i
                     starten af filerne. En eksamensbesvarelse består af
                     upload af disse filer med indsat kode.

      tests        : Folder med eksempler på test input og korrekte svar
                     for alle opgaver.

      run_tests.py : Et program til at køre alle de udleverede tests.

  * Vægtningen af opgaverne:

     Problem  Point  Navn
        A
        B
        C

    Totalt 100 point

  * Aflevering skal være en zip fil med opgaverne

       A.py, B.py, ... og filen run_tests.log.

    Det anbefales at man afleverer hele eksamensfolderen med tests, 
    ikke besvarede opgaver etc.
    
    Information om hvordan man laver en zip fil under macOS og
    Windows 10 findes her:

       https://support.apple.com/en-gb/guide/mac-help/mchlp2528/mac
       https://support.microsoft.com/en-us/help/14200/windows-compress-uncompress-zip-files

    Inden man afleverer bør man køre run_tests.py en sidste gang på
    alle ens besvarelser. Resultatet af testene gemmes løbende i
    run_tests.log. Som kontrol, vil indholdet af run_tests.log blive
    sammenholdet med resultatet af den efterfølgende evaluering.
 
  * Opgaverne skal laves i Python 3.11. Der må kun bruges de standard
    moduler der følger med Python (f.eks. random, math, collections,
    etc., se https://docs.python.org/3/library/), såfremt der ikke er
    nævnt specifikke andre moduler i opgaveformuleringen.

  * Eksamensbesvarelsen kan IKKE afleveres i en Jupyter Notebook.

  * I opgavebeskrivelser er der angivet nogle inputbetingelser,
    f.eks. at 1 <= n <= 10. Det er en garanti som alle test input vil
    opfylde. Det er ikke noget man behøver checke for (med assertions
    eller lignende). De skjulte input vil også overholde disse
    inputbetingelser.

  * run_tests.py kan køres på forskellige måder, hvilket beskrives i
    starten af filen. 

    En mulig løsning er at udkommentere linjen

       DEFAULT_FILES = ['A', 'B', 'C']

    og angive navnene på de filer der skal testes.

  * Er kode-strukturen/læsbarheden ligegyldig til eksamen? Fokuseres
    der udelukkende på dets funktionalitet, altså antal tests det
    accepterer?
    
    Svar: Ja. Men velstruktureret kode har nok større sandsynlighed
          for at virke.

    Er det forventet vi skriver forklarende kommentarer til vores kode
    til eksamen?

    Svar: Nej. Dog skal man huske at skrive en kommentar med
          kildehenvisning hvis man kopierer kode fra internettet.

  * run_tests.py stopper jeres program efter 5 sekunder, men det burde
    være rigeligt til at løse de fleste testinstanser. I enkelte
    opgaver kan nogle af testinstanserne dog kræve at man har en
    tilstrækkelig hurtig løsning for at få de sidste testinstanser
    godkendt. Til den efterfølgende evaluering af programmerne vil der
    blive tilladt lidt mere tid.
    
  * Man får ikke point for at håndtere input ved at hard code input
    instanser og deres svar. For hvert input må man forvente at der
    vil være et hemmeligt input af samme "type", så hvis man klarer et
    input så bør man også klare det tilsvarende skjulte input.
