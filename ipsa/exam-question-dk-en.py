'''
    MAKE DISTINCT

    [DANSK PROBLEMFORMULERING]

    Din opgave er, givet en liste af heltal, at erstatte gentagne forekomster af
    heltal med de mindst mulige større heltal, for at gøre alle heltal unikke. 
    Den resulterende liste skal udskrives sorteret i stigende rækkefølge.

    Eksempel: Betragt input-sekvensen

      10 6 10 4 2 2 6 2 2
        
    Sekvensen indeholder 4 forekomster af 2, 2 forekomster af 6 og 2
    forekomster af 10, dvs. at 3 forekomster af 2, 1 forekomst af 6 og 1
    forekomst af 10 skal erstattes af større heltal. 2-tallene kan
    erstattes med 3, 5 og 7 (da listen allerede indeholder 4 og 6), 6-tallet kan
    erstattes med 8 (da 7 allerede er indsat), og én forekomst af
    10 kan erstattes med 11. Hvis vi sorterer den endelige liste, får vi:

      2 3 4 5 6 7 8 10 11          

    Input:  En enkelt linje med n mellemrumsseparerede heltal, hvor 
            1 <= n <= 1000 og alle heltal er mellem 1 og 1_000_000_000.

    Output: En enkelt linje med n mellemrumsseparerede unikke heltal, sorteret i 
            stigende rækkefølge, hvor gentagne heltal i inputtet er erstattet
            med de mindst mulige større heltal.

    Eksempel:

      Input:  10 6 10 4 2 2 6 2 2

      Output: 2 3 4 5 6 7 8 10 11


    [ENGLISH PROBLEM STATEMENT]

    Your task is given a list of integers, to replace repeating occurrences of
    integers with the smallest possible larger integers, to make all integers
    distinct. The resulting list should be printed sorted in increasing order.

    Example: Consider the input sequence

      10 6 10 4 2 2 6 2 2
        
    The sequence contains 4 occurrences of 2, 2 occurrences of 6, and 2
    occurrences of 10, i.e., 3 occurrences of 2, 1 occurrence of 6, and 1
    occurrence of 10 need to be replaced by larger integers. The 2's can be
    replaced by 3, 5, and 7 (since the list already contains 4 and 6), the 6 can
    be replaced by 8 (since 7 already has been inserted), and one occurrence of
    10 can be replaced by 11. If we sort the final list, we get:

      2 3 4 5 6 7 8 10 11          

    Input:  A single line of n space-separated integers, where 1 <= n <= 1000  
            and all integers between 1 and 1_000_000_000.

    Output: A single line of n space-separated distinct integers, sorted in 
            increasing order, where recurring integers in the input are replaced
            with the smallest possible larger integers.

    Example:

      Input:  10 6 10 4 2 2 6 2 2

      Output: 2 3 4 5 6 7 8 10 11
'''


# insert code
pass
