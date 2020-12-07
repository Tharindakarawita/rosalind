def motif(DNA,substring):
    y = len(substring)
    for i in range(0,len(DNA)):
        x = DNA.find(substring,i,i+y)
        if x != -1:
            print(x+1,end=" ")
        else:
            exit
    return

DNA = 'AACTTTAGCATACTTTAGTTAGACTTTAGTACTTTAGTCACTTTAGAAACTTTAGACTTTAGACTTTAGATACTTTAGGCGGTTACTTTAGCGACTTTAGTAAACTTTAGTGAGGACTTTAGACTTTAGTATCTCCGAACTTTAGTACTTTAGACTTTAGACCTACTTTAGCAACTTTAGACTTTAGACTTTAGATCCCACTTTAGACTTTAGACTTTAGCGCACTTTAGACTTTAGACTTTAGACTTTAGGACTTTAGACTTTAGCCTCCTAACTTTAGCGACTTTAGGACTTTAGACTTTAGGCACTTTAGTACTTTAGACTTTAGACCTACTTTAGGGGTAACTTTAGGACAGTACTTTAGTGGCGGTACTTTAGCTCACTTTAGACTTTAGACTTTAGTTTAACTTTAGTTGCCCTACTTTAGTTGCGACTTTAGACTTTAGACTTTAGCCTACACTTTAGGAGCGAAACTTTAGGACGGGGACTTTAGCACTTTAGTACTTTAGCACTTTAGTTTGCCAGGCACTTTAGAACTTTAGACCACTTTAGGTAGACTTTAGGAGTACTTTAGAACTTTAGAAACTTTAGGAACTTTAGTCTTAGATAGGCACTTTAGGACTTTAGATACTACTTTAGACTTTAGTGCAACTTTAGTTCACTTTAGACTTTAGTAACTCCCTCGGACTTTAGCCACTTTAGTGCAACTTTAGTCCGACTTTAGCGTTAGACTTTAGACTTTAGTGCTCTGAACACTTTAGAACTTTAGGGAACTTTAGCGTACTTTAGACTTTAGACAGCACTTTAGACTTTAGCAACTTTAGGAGACTTTAGACTTTAG'
substring = 'ACTTTAGAC'
motif(DNA,substring)