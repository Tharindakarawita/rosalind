def DNA_seq(Seq_1,Seq_2):
    x = 0
    for i  in range(len(Seq_1)):
        if Seq_1[i] == Seq_2 [i]:
            continue
        else:
            x += 1
    return print(x)

DNA_seq("GCGTAGTGATTTTGTCACCTCATTTCTGGGCCAAAGCTTCGGTCCGTACTGCAGAACTGACTAATGATTCATTCTTCGCAGTGGCTTCTTTACTTCTCATGCGGATTCGTATGCGGTTTCAACTTAGCGCCTTCGCATACAAGCGGTAATCGCGGTCCTCTGTTACCCACGTGGAGGCCCGTGCAAAGTTGACGCGAACAGGATGTCGAGAATTCCTGTAGGGAGGGTGTGTTGTAGGATCTTTGGCTCCTGACGAGAAAAAAAGGGAGCTATGCCGACCAAATGCGTCAGTGCGTATAGGGATTCAGAATAGCATTTGCTCCCGTTAGTCGAGCTAAATGGACTGAATGTAATGGTGCAAATGATCGTGCGCCTGCCGCCCTTGCGTGACCCCGTATAGCAGTTGCGGGGTCCCTGGGTTGAACGCTAGCCAATGAAAAGTGGGCCTCCAATGTGACCACTGTGTGAAATTCGTTGTGCCGTGATAGTTGCATTCGGGGACGTTACGTAGGGCAATTGTAGAGTGTGCGTTGTGAATCAAATACTGCCGTTTACGTGGTTGAAAATAGTGGTCAGATTGGATTCTCAGATTTACCGCTTTTCTATCTCTTCACGAAGAGATAATCTAACAAGTGCAATGTTAACAAAGCGTCCTGCGTTAGATTAGCTTGCTTTCCACCAGTCGGGCAGTACTGAGACAGCATAACGCTGGCGAAATCAAGCGCAGATCGGTACCGGCTAGTGGTCCTTATAGACCGGACCTCTGATTACTCCGACTCTCAACACACATAGAGTGCTACGTGAGGTAGATTTCTATAGGGGCCCAAGTACTAGCATTTGGCACGGGGTGCGTCCGTCTCACAGGATCGTTCAATTCGAGGTTCCCTTGAAGTTACGGGGTCGTGATTAGCGTTTTAAAAGAATCGCGTATTC","GCCTAGTAGTTCTTTCGCCTCGTTTATGGGCCTTAACTACCGTCCGTACGGGGTACCCGACTAAAGTCTTACCAATAAAATTGGCTAACCAAATTCTCGTACCGTTTCTCTTCTTGTGATCACAACGCGGCTTATGCAACCAGCCGTAACCTGGGGCACGTGTTATCCACACTGAGGAAAACGCTTGGAAGCACTCAAAATAATCGCCGACCTTCCGGGCGGGAAATTGTATAGTTGCGGCATCTCCGCCTGGCTGTATGACAGCCGAGTTGTTCGGACAAGTTCCGTCAATACATCGAGGGAATTCGATCACCATGGACTCTCGTTGCTCGTAATTACTATTCTGCCTGGCATGGGTGAAGCTATAGTGGGTCTGGAGGTCTGGCGAGATACCGTATCGTAACAGCGGGGACACGAGGCAGTCGCCGAGCCGTTGAAACCGAGTCTTTCGACGTCTCAACTGTATTCAGGTCGTTCAGATGTCATTAACTCATGTGGAATGCCAAAGCCCCGTCGTTGGCTAGAGTACCCTGCTGAGCAACCACTTCCATGTGGCTTGATGAAGCAAGGAGTCGGACTCGATAAGCGGATTCACGATTTTCGGATCACTTCTATGTGTGATCATGTAAGGAGTTCATGGTGTAACGTTGCTCCACCGTTAGATTTACTCGTTATCGACGACTCCAGATGGACGAGGCAAGCCTTACTTCGGCTAAATCGAAACGTTTTAGGCACAAGCTATTAGTGTAGGCAGCCAGGCGCTGTGTATTCGATGGAACTCAACACCAATAGGCCGACAATGTCGGTATCCGTAAGGATGAATCCAAGCATGAACCCTTAGCACAAGGTGGGTCAGTTAGGCAAGCTTTTTCGCCTACTGGTCCCCCCAAGGCGTGGGAGTTTTAACCCACGGTTAACAGGATATTCCTAATC")

        