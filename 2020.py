import re
import itertools
import collections
import math
import sys
import numpy

# day_1:1
number_string = '''1655
1384
1752
1919
1972
1766
1852
1835
1408
1721
1879
1846
1394
1577
1588
1097
1748
1585
765
1375
1806
1785
1824
1847
1037
1531
1989
1570
1625
1600
1832
1927
1691
1593
1936
1812
570
1391
1883
1592
1875
1185
1903
855
1331
1742
1884
1356
1944
1994
1556
1271
1572
1661
1914
1905
1581
1634
1252
1657
989
1907
1998
1040
1833
1612
1725
1680
1869
1900
1550
1768
1727
1930
1810
1841
734
1779
1774
1825
1446
1259
1552
1310
1885
1689
1929
1959
787
1642
1890
1164
1986
1796
1465
1217
1741
1480
1683
1808
1058
1970
1361
2003
1898
1668
1754
1773
1235
1158
1975
1479
1995
1648
1023
883
1553
1658
1794
1747
1978
1268
1966
1192
1886
1471
1548
1819
1551
1958
1732
1676
1745
1501
1858
1652
1596
473
1314
1814
1409
1877
1344
1735
1635
1273
871
1643
1599
1565
1695
1803
1764
1778
1823
1831
1701
282
1089
1623
1639
1568
1469
1674
1818
1992
1597
1711
1359
1851
1496
1630
1755
1529
1881
1718
1916
1325
1578
1441
1722
1545
1472
1783
1497
1791
1183
1926
1937
1255
1095
1451
1395
1665
1432
1693
1821
1938
1941
2002'''
'''number_list = list(map(int, number_string.split("\n")))
number_list1 = [i for i in number_list if 2020 - i in number_list]
print(number_list1[0] * number_list1[1])'''

# day_1:2
'''def sum_to_2020(values):
    return sum(values) == 2020


number_list_permutations = list(itertools.combinations(number_list, 3))
number_list_permutations = list(filter(sum_to_2020, number_list_permutations))[0]
ans1_2 = 1
for i in number_list_permutations:
    ans1_2 *= i
print(j)'''

# day 2:1
str_of_passwords = '''13-15 c: cqbhncccjsncqcc
2-3 v: zvdvfd
9-14 b: rbrbnbbbqdfrht
11-12 k: kkkkkkkkkkxqk
4-5 b: bqbbdm
10-12 w: kwwkwwwrwzzwwwwzwswx
1-11 g: grrmgmqgghw
4-5 m: mbmhmvmwdvxmvpw
1-13 n: ndnnnnnnnnnns
11-18 l: lllllllllllllllllll
4-5 c: cccscc
2-4 k: bkfr
9-13 k: lcmsvkknrxtkkksgvkjg
1-2 b: bhwgb
1-4 j: zjjcjj
7-11 g: nnffggdmggr
3-4 z: zzhzz
4-10 g: mggkgvgggmggkggmqg
4-5 n: dcmnl
11-15 s: gzpdvsmnzsshswzs
10-14 x: xmvpxjtlxxhxtpdhsnx
5-15 v: zzhjdpgxlsvphzv
4-8 k: dsfktqchpkk
6-7 j: jzjgjqld
12-16 r: rrrrrrrrrrrhrrrrhrr
1-2 l: lllllll
2-3 q: jqxwtggmgqmzpljdvkt
8-11 p: xpmcppppwvzp
7-8 c: vwcvkcct
4-10 d: lsmdffzdsrk
2-3 p: sxpg
4-11 p: rzlgxshhpbp
1-4 b: qbbbbbbbbbbb
6-11 m: zwmzmmlbmxgphkks
1-4 n: lnnnn
15-16 h: hhbdmbhchhhkhhrw
10-11 k: kkkqtwkkkkkkkkn
2-13 m: mggmmxmrzmwglbmmm
12-14 g: ggggrggggxgwhggggd
7-11 l: llbqsqlkvll
1-3 f: ffff
4-9 h: qvnhvcmpmfdbqhkdsg
3-8 d: ddsdddddd
14-15 j: qjjjzjjjjjbxmjs
3-5 j: jjjjtctjjjs
12-13 q: qqqqqqqqqqqqgqqq
1-8 p: xpppzdpp
13-15 f: lnlnlkcwgnfqgmfhlwm
12-17 g: gfgtgrvcxggggtggjg
6-8 r: rrrrtwrqrrr
9-12 r: ctldssjlrzhvpmqrtxd
1-6 k: qkkkdkkkkkk
17-18 x: bxrxxbxxzpbxnqxcsmn
2-4 c: ccmr
1-7 m: mmmmfrdmmmhl
9-12 d: ddddddddxddhd
13-14 f: ffffffffjffbbff
4-6 c: ccchcc
6-7 r: rrsrrrrcrrjbrrrr
9-15 w: wzfbtqrwwgtmbxn
6-7 q: qqqqqqrq
1-7 l: lgpqzhlkb
6-8 d: dhddkndp
2-5 m: bjxmmmmm
5-16 t: nbgjntfhpwtbrcftxt
5-7 k: kkkkkhbkkkkk
8-19 t: dsdstttfjhnttttvgttt
3-4 t: ttltttt
1-5 l: flfllllllllbhldll
7-10 x: xxxxxxcxxxx
2-7 t: ttttttctttt
3-12 x: vlxfwpdncxzkmkxt
1-5 b: mbbbbbdbbbtbwbhpbt
3-16 q: fpqkkkqfkqdbrxlq
5-6 p: lpcbtppjpt
6-7 w: wcwwhwv
9-13 v: vvvvvvvvvvvvvvv
1-4 g: vgggtggghgggggggg
2-9 p: mppsrrzwxdt
4-5 f: ffffdfffffdf
2-5 x: xkjss
13-14 z: zzzzzzzzzzzzbhzz
2-10 p: xmtkzpbrrj
17-18 t: ttttttttttttttttttt
2-8 j: cjjqbzpd
4-12 z: zzzkzzhzzpzzdzz
1-2 d: rdcdt
2-3 j: wnltj
7-9 r: rlrfbrdrqrbdr
3-4 s: bcsss
12-14 h: hhhhhhhhhhhbhhh
3-5 h: rfhlc
8-15 f: ffffffflffffffff
3-15 s: ssxsssssssssssss
2-4 h: hlbhshhmhhhg
12-13 r: rrrrrrrrmrvrnrr
3-5 p: ppppjp
1-2 z: zqhdkgqqzfsxkjjzg
6-8 k: kkkkkkzd
1-12 h: qhhhhhhhhxhhhhh
9-14 p: ppppppppqppppfp
2-4 t: tsttt
18-19 t: cttttllttttwxtttttt
10-11 t: rkdbpntntttfw
4-14 m: mdmmgtlmmwmbmmmk
4-6 n: xxhnpmnfnn
15-16 g: ggggggsggggggggng
14-15 k: kpjxmkrksskpbwk
15-18 f: fffffsffffffffnfffff
18-19 p: gwpplnpndvpxgzjvhbpp
8-12 l: ldclrkllbgpwllllcxms
14-19 w: pxsjbtwwhdkptwcxwvr
2-17 m: mtmmmmmmmmmmmmmmmm
12-15 b: nbcsplrmvbjbqlc
1-4 z: bzzszzzzz
1-13 t: tttttttttttttttttt
6-7 j: jjjjjmvjjjjjjjjjjj
10-13 l: llclllllljllllll
11-12 c: mzckxzsbbxcq
2-14 k: kkckkkkbkkkkkrkkkkkk
3-5 s: msssvqszssprssss
7-10 f: fffffffffrf
2-4 l: dlwrl
3-7 v: slqgljmrqrwv
4-6 d: pdddddnddddddd
6-9 f: cnfffpfzfffffff
4-17 v: vvvnvvvvvvvvvvvvvv
7-9 q: qqqqqqqqkqqqqqnqq
15-16 q: qqqqqqqqqqqqqqqqqq
10-11 g: cgtrgggggggggg
10-12 x: xxsxxsjxfxxlx
3-12 j: jjljjjjjjjjjjjj
8-9 c: ccbccczccthcc
4-17 h: hhhfhhshhhhhhhhhhhh
1-2 p: prppr
4-12 q: qqqdqqqqqqqqqqq
7-11 b: bbmbqbrtlwb
4-7 l: lllhlllllz
3-4 r: rrqc
5-14 r: rrrrcrrrrrrqrrrrrrr
10-11 d: pxdcxxjsddd
9-11 s: sssssssspssssssss
1-2 j: jfjljjjjjjjjjjjjjj
3-4 v: vqnvvv
2-3 c: wlcntvmsshxcgzc
9-14 t: rbbljpttwwjtbj
10-11 s: gnrdtfzttks
1-4 x: xpxjxhdxx
9-12 c: chccccccmpfccc
14-16 j: jjjjjjjjjjjjjxjjj
5-6 d: rpdndsbddwdd
9-13 x: thpdhlcwxcxxvxbv
4-6 g: nfsgqnvbntgwvlzlmmxg
3-4 d: dttdcdtq
2-4 n: wnntzbr
2-10 j: jtpszbpjfjcgdjg
6-7 b: bdspbvb
10-14 z: vzznzzzwzlzzqzj
7-8 c: cccccccc
7-11 h: hklhdhssfbz
7-8 h: hhhhhhqzhhhhhs
3-5 b: bcgbwbbbbbdb
5-6 q: qqlxqbgtqpkqt
8-9 q: qqqqqhqkq
2-4 q: qshp
8-13 g: gggggggrgggbgghg
1-5 k: ktcpgpk
2-13 v: mvvwnvfkjrhvvdvvtsvk
12-13 k: kxpkkkckjtkkj
12-18 h: xhqngjkxqqzqhnhhhh
11-12 k: kkkkkkkkkkkjk
2-4 r: rdgrrr
3-4 x: xwjx
2-6 c: lcqzflc
13-14 t: smlkctgbsqpftx
4-5 b: fxtdbzbqbd
4-7 s: wmsssznjzsdkgvdsxhd
2-6 z: wpptkhk
14-16 p: pppppzpppppbprppppp
6-7 c: cccccbw
1-6 h: mhhhhhh
2-3 k: cwkgk
3-4 l: llcl
3-4 m: kmmx
14-20 h: hhhhhhhhhhhrhhhhhhhh
8-12 b: bcmbpbffwghcvjb
10-15 f: fffdfqwmzfdfrfdbpf
1-2 l: hlllljl
1-3 g: vgbgg
2-4 n: zgfn
18-20 w: gmbwtzgzpmdwstsffqzw
9-19 j: jjjjjjjjkjjjjjjjjjjj
16-19 f: fffffffffffffrffffzf
8-20 l: htdlzwsllllccwlflstf
3-4 w: wwww
2-4 b: sbbz
4-6 n: nnrzbbnlcrnsbk
7-8 c: wmzjtbvw
5-7 l: cldlljlzzz
5-6 h: hhzhbhhg
4-5 f: scmrfftkc
11-12 m: flfrbmdpdkpm
6-7 v: xvvvcvkbnvvq
4-11 h: qkjphjpfllhpqnbm
2-5 b: bqbwbbwsb
1-8 c: cqcscccbccrccq
1-13 c: cccccccccccckccc
7-8 h: hhhhhhhs
1-3 l: llxl
6-8 h: hhhhsnkv
6-13 m: mmmmmmmmmmhmpmmm
6-9 n: nrnmmnbnmn
7-14 k: whkpphhkxlnnmkbhtnt
4-10 n: nnnnnnnnnhkn
3-4 c: mcnw
8-13 b: bbbbbbbgbbbbbbbbb
8-9 c: lcccdkjcjrqwck
3-13 w: szmnhsmzwpdbkhtbf
4-5 r: prrrz
9-14 m: mmmmmmmmgmmmmmm
7-8 q: kqpgrqqp
16-17 p: fzxxpcpdhmvmrnvjp
7-9 v: vvvvvvqzxs
3-4 w: qwxw
1-2 x: xqkx
9-10 v: vccmlrlhvdtttfvcxwm
11-14 h: mhvthqhvhhgmfhhhkhch
3-4 n: nqzw
2-5 j: jbjjjjjjjjjjjjjj
11-15 g: bcxggqfmgzgfrdg
3-5 v: gvwvvvrzf
6-7 t: ttzdttr
4-9 j: cgqjqdjvjbfjwdlvdgj
5-6 s: hfflrzksshjqsbvsps
1-4 p: pppn
4-5 g: dprggmpfggbkpg
2-3 k: kbhkkkk
13-15 r: srrrtstrwwxzrrzr
2-4 b: lbbnbzbb
1-4 g: fvgz
5-11 q: hxdhqrqqprpq
2-4 z: zzgm
1-13 w: wwwwhwwwwwwwwwwwww
2-3 k: kkkkk
4-8 g: nlgmhplgcv
1-2 j: zncllmvgjnj
11-13 f: fffffffffffflff
2-8 p: bphqpxkr
2-9 b: bbbbbbfbdbhjpbbbjbbb
9-10 s: zpxnstzwsw
7-16 c: ccccccccccccncsvccc
6-8 r: rrwbrqgr
6-12 v: vvvvvvvqvpvvvvzdd
8-9 z: zzzzbzzmzzz
15-16 t: tfttttntxttqtttc
9-16 b: btbrbfplbbbmbbbbkbb
7-8 q: qrqxrlqg
8-12 q: qqqqqqqpqqqw
5-8 v: jrrlpvvcvkjzjvvvv
11-14 d: dddddddddddddq
5-6 f: rfxmfzf
3-4 t: tttqt
10-14 c: bcccccccccrccfc
3-7 n: snnqplvl
5-6 z: kshzfzhlcsbqwqb
6-11 s: sssssssssmsjsgssss
3-7 v: qgcxvxvg
12-17 v: vkvbsvxkvvnjvvrvvvx
2-4 d: ddrrxbd
8-10 x: tvxxtmgbsxpxbl
7-9 r: rzrbgbrrrrrrmhm
2-4 t: ttttt
5-9 x: xxtwxxnssxlxx
3-4 p: ppdp
3-7 g: ggtgggtg
1-2 k: kbbhjdkfvjqffcss
1-2 l: lrlvlll
10-12 x: xjkbqxkxzxxq
7-9 d: dddhdkpdfdf
5-8 m: mmmmmmmwm
3-9 l: sfrjlzhcll
7-18 m: mmmmmmcmmmmmmmmmmmm
1-3 w: mwplxwwww
7-8 t: tgtctbtrtdtttt
3-6 p: lfpbbgfbpdhnqz
5-6 d: ddddrd
1-3 b: llbbbbb
4-7 r: ktbrncrrnnsrr
8-10 r: rrrrrrrfrrbrr
1-8 l: wlklvlllnljlgtzll
2-4 m: mmhmmxsm
10-12 c: cmwkcnczsxmcrmjtc
2-8 q: qmqqqqqzqq
7-9 v: xvvvvwdnzzv
3-7 j: lsjvmbrjjmpcwqnvvdgc
3-9 l: bgmllldjrzhllsclc
1-6 p: ptppfjpqpp
7-8 r: mctrrstrrxrqtmrr
7-8 d: qddddddxddddddddd
4-11 r: rrrrrrrrrrbr
4-8 s: lsfvtfss
4-9 c: zcccccccj
11-12 v: vvvvvvvvvvvm
4-8 g: rggzlfgtm
3-8 j: jjjjjjfhjsgj
3-4 m: fmhmm
15-16 l: ltllhlljtllllbtlllgl
12-13 c: cccccvcccccqccccc
6-7 q: qqnlqqhqqq
1-8 z: znjqzxpz
10-13 k: kxzmkbxnkbkktmkk
8-15 k: bskzvggzsnlnxzz
9-10 v: vbvvgvcwvs
5-8 h: qhsnhhlhwpvzfb
15-16 g: gdcgggggggtgcgtg
8-9 z: fbgdnrzfb
6-7 d: ddkdddh
4-6 w: xzgfwwlbxft
1-3 h: hkjhh
1-3 p: pwprlp
8-12 j: jdjjjjjdjjcjvjjjjjj
11-14 m: bdsfwddfkgxsmrmm
3-10 m: tmmcmfmmjmm
3-4 b: dwhbzfjxl
2-5 n: nnnnjcnnn
16-17 v: vvvfnvvvltsxhrvvm
1-7 v: qvvvvvwvvvdvv
2-14 k: nxqblwwqmhqzkm
3-4 t: ttts
5-6 c: clnnfk
12-13 s: sssssssssssts
7-14 d: ddqdnwdkdmhddg
3-4 t: tmsttm
9-11 x: xxxtxxxxxxqxwntxj
8-14 l: lllqklwlvlllmbslzlln
9-12 n: sdsnnfncxnwnrn
1-5 f: qfffff
6-9 r: rzmphlrgrr
1-4 m: grdm
4-5 s: ssxsg
1-4 n: xhnznnxnnn
2-6 r: mcwldgbqlqsckgzlrd
1-3 l: llmllll
3-4 p: pjtgdnfjfcjtcnpgxpzq
6-7 m: mmvmmmtn
17-19 h: qgmhhhwwwhqhmhhthhch
3-14 s: lhmnsfdrvnngrsfhxd
1-6 p: pppppwp
4-6 l: lzllltrl
3-4 c: rpxccsc
13-16 h: qsdznfqmsftqqthh
2-4 k: wsvkm
1-18 h: chhhhhhhlhhhhhhhhhhh
17-18 d: xddddddddddddddddddd
2-3 t: jtbrhpzjfpzhcmjql
10-11 n: gjngnnncncnn
7-13 r: rrrrrsrrrrrrlwrrr
10-12 l: llldllslbldllwl
17-19 m: mmmmmmmmmmmmmmmmfmm
10-14 n: nnnnnnnnnbnnnnn
17-18 x: xrxcxxxxxxxxxxxxxxwx
3-4 b: lvxb
5-6 r: rrrrrrr
13-18 l: lllllllllllllllllpl
8-12 m: mmmmmmmqmmmmmmmm
7-8 l: llhqlllh
3-8 p: nmrppdvpxcphxgmkpbsl
9-10 v: hvsbttgsdvvj
5-9 k: kgmvzzzckkgldk
15-20 x: xqxxxjxxxxxxxxxxxxxl
5-6 t: bbwpwtwbhwgqttzjv
6-13 n: klzcfnnjqxrhjwpjfxnk
5-8 d: pcnndzddddnsdqh
5-14 k: kblbtvkwltfklk
4-11 q: zxwdkqqkvqq
10-12 s: tsssssssssssss
3-5 r: rddsrrdksfqfrgr
7-16 h: vdvhlsjxgvrbrxnhns
3-4 z: zxtz
4-8 x: xmnxdwmh
11-12 r: gwsnfrnckrrxrx
3-9 q: qqqqqqqqwqb
9-14 f: bfnfffffvfpfffff
6-9 p: pvpppkppcpp
3-4 m: mmmz
3-5 j: jjjjmjsjjrlkjjjjj
4-6 p: jpbpjs
6-9 r: bswdsrksdrzrgrfmjr
8-10 l: lllllllxll
3-7 v: vvhvvvvv
4-11 n: mnjpbldngrrkbthhmdp
2-4 r: frlrfblsrfzrhtpk
16-17 h: nbghhnzshclxhhmkr
2-5 z: zfzvzzzzzzzq
1-5 l: lllzlfl
9-10 d: dddddddddzd
11-12 p: pspppppppbzp
5-9 t: thzttpxrdhttdwqjsg
7-10 w: tfdfwlwwzdvpnww
4-6 z: fvcljzllwhbzscx
14-15 m: mmmmmmmmmmmmmcd
8-11 d: hgdmwgsdkdbghb
13-15 v: vmvdvvqvvvkvqvvv
13-14 f: fffffffclffffffmf
2-5 s: ssscn
11-13 w: wwwwwwwwwwwwww
7-9 l: xnwrlkskll
8-14 g: vggglvcrgscpgggt
4-5 w: wwwww
5-11 w: wwwwswwwwwwwwwww
6-7 g: gggbvjg
14-18 q: wqfqqqqqqnqsqrqqqq
6-7 z: zzzztzqczzzzz
6-12 n: wnnnnnnxftnkznpvvl
10-16 j: jjjjjdjjjrhjjjjj
1-10 l: lllllllllrll
9-13 g: gdgggggggggkggn
6-8 r: rrrrrrrs
16-17 k: kkkkkxkkkkkkkkkck
11-14 b: bbbjbxbfmqscqbdmgg
3-8 d: sjdkmjppbdddhdxd
6-7 g: xhkhwgqpbg
11-12 x: xxxxnxxwgxxbdl
6-8 c: cccscccwcccccccccc
9-16 h: vhhhhhchwnghmkzhr
5-9 v: vvvdnvvvvv
4-16 n: nmqncgnbfhqnnpnbxwrl
3-5 f: fljrf
13-14 m: mmmmmmmmmmmmgfmmmmmm
5-6 g: ggnggd
2-6 w: wlvhvw
13-18 h: hhhhhhhhhhhhhhhhhvh
7-19 m: mmmmmmmmmmmmmmmmmmwm
4-12 k: mcvtrtsdkvkkfjrmkn
1-8 t: qvmrtttn
6-7 f: fffffsf
10-11 m: mmmmmmmmmjl
15-17 v: mvrhvvvvnvrvzrvvfv
10-14 m: mmtmmmnmmmmmmxm
4-16 b: vcscdqcbcxswjfdbrqbx
8-9 z: zzzzzzznzvz
4-6 g: ggnggdpgggg
2-4 d: hddxxnzzw
9-10 g: gggggggggj
4-7 k: kkkvkkkkkk
1-3 r: rrrrj
14-15 w: wwwwwwwwwwwwwwwww
2-4 n: brfmln
18-19 b: bxbbbbbghbbbbbbbbwb
10-12 q: dqqqrqwcqgqqf
2-5 g: sxfzgtrxkrmstdzfmw
3-4 d: pcddq
11-16 w: sbqwlwzwwwwwtwww
2-12 c: wrccqxtccccchcccjcj
16-17 b: bbbtbbbbbbbbbbbqb
3-13 t: tttttttmgktdthtp
1-3 t: ttcg
13-14 z: zczzzzzzdwkzqz
5-6 n: bnjhnjhnnq
2-9 b: bjbgbzmlbbklbwt
4-5 b: dtlbbwtjbkzzbghbghzk
10-16 p: ppppppqpppwnpppppppp
5-6 b: cbbwtbjkm
15-16 p: ppppppppppppppqd
4-8 m: lgmmhgktslzhbvw
2-4 h: hhdlhhhhhhhhhhh
14-18 k: ktmkkkkkwkklkjrkklfk
5-7 x: sfxxsxx
8-9 v: lkvxdpvjv
7-8 r: rrrrrrsr
4-6 b: btcbbv
7-13 n: zhnhjhnmkzdbt
7-9 j: jvjjjjjjjjjjjjxjj
1-4 v: hdvfv
2-5 f: rznpnxqwncmtkwfxcxqh
16-17 x: zxgbhltrdhxkvvxsxf
1-2 h: hkhhh
3-4 h: zhxc
4-9 z: vsmzhzwgjxfg
11-13 x: xxxxxxxtzxxxc
11-12 d: dddddddgddqj
4-11 f: zkdhqnpgbff
2-3 q: qqlqgqqqv
4-9 b: bvnblwhbbkswmrhtf
7-13 t: cztskdtqdtrkt
4-5 f: fffcsf
4-9 f: ctblqrflf
1-2 l: lmllqhlnll
3-6 v: vvqvvvvr
7-9 b: bbrhbkjbb
1-8 p: xpppppppp
7-10 k: ckkpmktkqksgkkk
1-7 m: lmmmmmmmmmmmmmm
11-15 v: vvfvvmvvvvdvkvv
10-11 b: kbbbbbbzbhbb
11-12 l: jltgggtlcggllt
10-13 q: kqnqqqqqqqqqq
6-7 c: cjcccczc
5-11 t: kdtstshrhfkcx
3-12 v: vlvfzvwvxvvhvvsvvcvm
9-10 t: xttttttttttt
8-10 z: hctlkgjzvzh
3-5 g: gtkwgk
16-17 w: wwswwwwwwwwwwwwwwqww
4-11 j: lbmwjzjxjpjhzjjpbj
4-5 c: klbxc
3-5 w: wlhvb
4-8 x: xgxxxxxxxxxxxxdxnxx
2-5 n: nnnkhn
1-2 d: dxfd
11-12 w: wjcqszwqwkcb
6-11 v: sqpgzhnvndtmvvwl
3-4 m: mmmqmmm
1-3 d: mddb
6-7 w: wwwwwnwwwwwwww
12-14 z: zzzzzxzczzzrzzz
5-10 f: mtcmmhfftft
10-14 x: hhgvmxbwgxdcnz
10-16 z: wzfzzmlmxxfhzqcbsnl
3-4 p: ppvkppp
8-11 h: hhhkhhhjhpbhhhh
6-12 f: ffffdwffrsfffrffnfpk
5-11 z: xqwzzzzbzpwk
7-9 c: crccccccscccccc
4-5 b: qpcnz
2-13 m: lmnrrzfhmbwtmqbsg
12-13 k: kkkkkkdkkkkkmk
10-14 q: sdqfbqszdjhqfq
8-13 h: hhhhhjhhhhhhbhh
2-4 g: gfdb
12-19 n: wtrhndnnnbwnnnnjnnn
5-6 n: zdwnpn
3-5 f: ffsffffff
11-16 r: rrrvrrrrrrwrrrrrlrrr
6-8 n: nnnnnfnnn
10-13 b: brnlbblbkbbbjbbhx
7-8 q: ftrfnqgqc
11-12 c: ncccccccccgcccn
3-4 z: tzzctzwzzvz
3-5 t: tzrqg
7-10 m: mmmmmmrmmqmmm
1-2 c: cdccfcccc
10-11 k: kkkkkkkkkwkk
6-18 x: qndxdgmjvpppddwkbt
8-17 c: pxhszsccndlbzkwgvx
3-4 p: qlrvwdxpqtgwjrtqcc
2-4 q: lkjq
17-19 f: pffgflzxrxfdxffffnz
3-11 x: kzsvmhcxnwj
6-7 x: lxxxxxxcm
1-8 n: nnnnnnnrn
2-5 r: rtrrnr
2-4 n: csvhrvhlp
7-8 b: lbbpdbkb
2-8 t: ztcrbvmst
3-4 r: rwrr
7-15 b: tbtrrbbpwsrvklqb
9-13 d: dcfsgddmdsjgg
2-7 d: mvdzscd
6-8 d: jrjjdndq
1-3 m: mhmvhtmmlbztvmsvmtmb
10-12 c: ctwjbpkchccmbqw
2-3 z: jvzwcrbgqbhvzbf
2-7 g: qbwsdbg
4-7 s: jsxpbmsmkhktfdq
11-13 r: rrrrrrrrrrhrqr
9-14 d: zddcdgddddxddntddm
1-15 x: jgrxxxxfxkgbmsxzx
2-17 p: kcppppkppppppppwm
12-19 k: kkkkkkkkkkkmkkkkkkkk
1-4 x: nzpxg
5-12 p: xcbppqnppqgtrm
11-14 h: dlhzhhhsbllcwhh
13-14 q: qqqqqqqqqqqqqcq
11-16 t: ttgnswrltltttjtj
14-15 t: ttttvtttftttttjtc
3-5 s: xssns
9-11 q: mlqqtqnjqfl
3-4 z: nzzhz
2-5 k: skwbwkwgzj
1-3 p: pppppcppppbpp
5-10 r: rrrrlrrrrrr
2-3 l: jlffrztcckl
3-5 t: ttftttttr
3-6 q: qtqtmnlqck
1-4 v: vxfvmvxwvvjbxp
1-5 z: tzzzzszvzzrmzmz
10-11 l: lllllblllcx
1-4 p: vppppp
6-12 v: zvrwvvvrvhzb
2-4 x: xxnv
1-7 w: hwwwwwgwgwwbwqw
3-7 w: wwwwwlfw
5-6 l: kkpltd
4-5 d: ddnrdk
3-6 c: cncvkt
8-9 j: vblczlfjjkj
7-15 d: ddddxdgdddddddjddd
4-7 z: vvmzdspzwptz
5-7 t: cdrtfqt
6-9 j: jjjjjdjjjjjjjj
2-5 j: ljptkvvfl
6-7 l: vhhnllgx
5-6 g: gpcxwvgpvvgg
5-12 q: plzqqnqzrhqgljj
8-13 k: zkckdknkxkgkvmmkd
4-10 s: jkvstssfcsrckjnzzbsl
9-11 n: nlknnnnggnvnnnnn
8-9 s: ssssrsgstk
16-18 r: rrrrrrrrrrtrrrrbrrrr
4-5 f: qxrzfcgfqfp
2-10 p: pphtppppppplwpsp
2-5 q: qqqqsq
6-15 j: xjkxkjxxkjznjjj
9-13 f: fvfvjlfmltfgf
3-6 j: jnsrcj
1-7 h: vhhhhhhh
4-5 q: qrqqqf
2-3 v: mvxb
4-11 l: lllllllllldl
7-17 k: mkcxhcmbcpjckkqznh
7-9 v: vvpgvvvvs
7-11 j: jjjjjjjjjjjs
2-12 v: mlxjljvffxgv
3-4 t: hhfn
14-16 w: kwfwwqwcfcwwfmww
5-6 j: jjjjjg
11-12 n: nnnnnnrdnnmnn
8-9 b: dsbbbfbbbb
3-4 j: jjcjjj
1-3 r: wrnr
10-11 p: pppppppppqppp
12-13 v: vvvvvvvvvwvvvv
7-9 v: vvvqvvxvdvxv
9-14 r: mmrrrrnrrxrrrwrrrrrr
5-6 k: kkkkbkkr
13-17 v: dbvgrchdpnzvxrdfv
4-9 c: ccjbccqcpcclcc
6-8 m: mbjmmxnb
2-6 h: hhdhnvcc
9-16 t: tttttttttttttttgt
12-16 n: nnnnnnnnnnnnnnnwn
3-14 z: zzdzzzzzzzzzzzz
3-8 k: pmktwckzn
9-13 q: gqqqqqqqrqqqqq
3-6 l: lllllddll
7-8 x: slxxzplxsxkcxlxxx
2-5 v: vwvvd
6-7 n: xxnnnmnnn
2-4 z: zczz
2-12 p: pppppppppppvp
2-4 h: bqwhv
5-7 t: btzttjg
4-9 c: sxcskxxbcv
1-6 c: cccccpc
9-13 l: bcsllbvbjhrflt
5-9 c: zprfctdnt
1-5 z: zzzzz
4-8 h: bpshnhxhrbk
4-7 l: bqclvxf
5-6 m: mmmmmgwcmgjj
13-18 m: mmmnmmmmmmmmpmtmmgm
1-5 w: cwwgwwwwwww
14-16 h: hhhhhhhhhhhhhqhhh
6-7 v: bvvjvvbvvv
5-13 b: pbcbbqmbcsfblc
17-18 j: jjjwjsrjjmkjjqjjjj
4-6 t: ntttpt
6-7 v: mvvnvvc
11-12 v: vclgnzbvtvvjvs
8-13 r: rlrzkjkrrxmdvzgt
5-7 n: nnnnnnsnnnnn
3-6 q: qpkjpq
2-7 v: hvgnjfrkvx
6-10 g: xgmrggggpbggfqgdpm
9-10 s: ssssssswfszsdssszss
5-6 p: pppjppwpp
2-5 d: ddddddd
9-13 p: ppjhpbppxpxxt
10-15 t: cgtcnlltzdkbcjtvxs
8-11 m: dkmmvtdmkbhmk
3-4 z: rzzqzw
4-8 z: zcxzswbzzqzxwkzz
3-4 s: jsts
2-7 b: bsbbbbbbbbbbb
11-15 l: jjkslsltvfbqshl
3-14 c: cqtxcgmcgvgfcccmg
1-8 f: fbfwffhfbxffhlx
4-11 r: drrmrrrzcfrj
5-6 p: pwpvjp
11-14 d: pnrddqwdlpdbddwg
9-10 r: rrrwrrrznrrgqsr
3-12 v: vsvvbvvkvvpdrvvv
2-5 t: mtfqjrjlthk
13-17 r: rrrrrrrrrrrrrrrrtr
7-8 n: nnnnnnhnn
3-4 r: wrpr
1-14 p: ppppppppppppppppp
8-9 m: vzkbzwnmwfqmmmmcmmnd
11-14 p: pppnpvpwppvpppppppp
17-19 h: lzhxlhhchxhbxhwvhsx
10-11 n: nnnnznnnnlp
3-12 f: kwflsfqflxpzbgxzdhzv
8-10 x: xxvxxxxvxsxxlxxxx
1-2 c: dclflczlj
4-9 w: wwwtwwwwwww
2-8 t: pfvtlbtxt
4-9 f: pnfkffkfnh
8-10 v: vjvvvvvvvvvvvv
3-13 s: mfshscgmmrvzw
6-10 g: gzggggpggkggzggggg
13-14 n: fnnnnnnnnnwnrnnn
4-14 k: lbvkwrkjkxjskg
9-11 q: qqqqqqqqsqgq
17-18 q: qqqqqqqqqqqqqqqqqd
6-9 s: spsssgsrrssss
8-14 m: qmmqjmmmmtpmnzgmm
1-7 m: bmsrmmmmmmm
14-17 k: kskdbkkkkdkkkktkqkkk
4-5 c: ccccgfc
2-5 k: kkkkzk
2-11 q: qqwqlnqqqhtdvxqrc
4-6 m: fdxkmmd
7-10 j: mjgftcmjmjj
17-18 m: mmmmmmmmmmmmmmmmnm
2-4 v: svvv
6-8 x: jxxhrxlp
4-10 s: dsvdbsssmscs
18-19 k: zwdgknqvqkgdhdhktkmr
2-7 h: jdflgfh
6-8 z: zmpzzzzzzzzgz
3-6 m: mmrmmm
4-8 w: wwtwktws
4-10 k: dkjkqkkzvk
3-7 b: bbbbbbfbbb
4-12 z: zzzzzzzzzzzzz
5-9 z: nmqdzzkzzzbj
4-11 z: fzzgzzzzzztzz
1-7 w: whwwwzrw
5-6 t: tjtttv
9-11 v: vzvhvxvvnvwvvv
2-4 t: pkjtpp
14-15 n: njpwjnsbnnnnngnnvnnn
5-15 k: qtmvkkdjkslkqvk
2-4 s: skszs
2-3 g: zggjhgxzn
16-17 p: ppppmppppppppppnppp
4-10 z: zzzzzzzzzzz
17-18 s: sssgsssskssssssssbs
5-8 m: mmmmmmmbm
1-5 l: llllmlql
3-13 z: bmdwpgvzfdlgzgl
1-4 p: pjplgjr
1-9 v: vvvzvrvvk
6-18 w: whwpwwflbcwwvwwwwst
19-20 n: nnsnnjnnnnnnnnnnnnkx
9-10 m: rlmxrnqrmkmmwmmmmm
15-17 s: lvssssslssfsssksfb
3-4 q: qqqpq
7-13 h: hhhhhhhhhhhhdhhhhhhh
2-6 h: dvkfhhmk
4-6 s: nczssv
10-12 p: pppppppppppdpprp
16-18 s: sssssssssssssssgsg
7-12 h: hhhhhhvhhhhhh
4-12 f: ffftfffffffwff
4-7 s: csqcpssbgvvmwdb
6-10 p: ppppvppppdppd
6-8 h: hxjhthhgzh
3-10 f: fffffffffsf
4-11 g: trggxlrnqrgh
2-15 w: wjxwtvkwwpgwwww
1-4 v: zjxv
7-10 f: fffffflqff
4-6 g: mgwgpbg
1-10 z: vvzzzzzvzz
6-7 f: ffffffnf
11-15 w: wxzwwqdnnwwxjlwplcl
10-11 s: hsslzjgsssvxsshnsc
4-12 n: tlxdnpznjbknt
7-8 k: mkhcvjxk
10-12 j: jjjjjjjjjjnm
2-7 c: fckckdpcksjckwcc
3-8 s: sssdxssw
12-14 t: ttttttttqttxttttpttt
6-7 g: gggggggg
5-10 f: fqffzffffffffgf
6-7 t: ztqhpbt
5-12 w: swwfwwwwwpwbwj
2-4 w: qmww
5-8 v: vvjnvvpv
7-8 p: bcbtnppbxnnwpr
4-12 z: zzkzdxntzlfbkkzzzw
8-9 s: sssssssss
15-18 h: jhvhhhcxwhhhhmhhhj
6-10 w: bwwwwwwwwwwwww
5-9 l: mtqlhlwlh
5-7 l: ljllnllblpl
15-17 h: hpgdkhsjwfnsjmhqxf
3-4 g: gggxgggg
1-2 q: qdqm
6-10 n: hnnnqknnnnnlnnnnp
13-17 q: djstfsmmqlshqqbqnf
6-7 z: qzlzxzw
7-12 g: qhghvbwdcvkgjl
7-15 z: zzzzzznzzzzzzzzzzzzh
3-6 w: zchpwvw
3-4 c: wmbjp
6-9 k: tckbvkkxkkqk
11-13 p: pcppppppppppppbp
5-7 r: rrrrsrxrr
6-10 c: ccccczcccccccccc
7-8 j: jjpjjplj
5-7 m: mjmmmjrmfmmmmmmmm
1-7 t: ttttttnttvpt
6-12 t: tttfwtttttttttttttt
7-17 x: hxwgrqqlxmrxrcwsx
3-8 g: vjcgqrjhlq
13-18 n: nnnfnnngnnnnjnnnhln
13-15 f: ffffffffffffrbff
13-15 x: xmswzjhtthggslslgx
12-13 g: ggggggggggggggg
3-9 f: cxfskjcbmhmmcpwn
5-7 h: jxzbhbh
2-3 m: mhmlmq
1-3 m: rmmmgmzvcghdtgmsmnm
14-15 s: wzssphxtsskpssr
8-14 p: kppjppgfpprftj
2-7 r: prnmlrrbm
2-5 v: vvvvtvv
1-5 n: nnnnzn
2-5 t: xtlnfwhgvltx
3-4 v: gvtv
2-8 k: kvkstkfz
2-6 j: jdjjjnjjjjzjjjj
3-4 s: sshwsssss
2-10 w: mnhkdtwdzwvsq
6-8 b: bbbbkxbbtbbkbt
14-19 h: hhhhhhhhhhhhhhhhhhhh
6-10 d: ddddddddddddddd
10-13 t: ttttttttthttjttt
4-5 c: ctscw
8-9 b: bbbvbbgmb
10-12 s: sxssshsssswsscsx
3-7 r: rdhrrkrkrrrrcrhrrr
8-10 j: wjsslzjjntjjwjs
1-4 q: gqqw
4-6 t: tjlhvrt
2-10 s: ssssssnssssssssx
7-8 x: xxxxxxfw
6-13 r: sxtcgrffrpdprnklbxbw
1-3 p: ppbppppppp
2-3 b: jbfr
1-7 m: cmmmmqm
4-5 t: tttzt
7-9 s: zwbbbssvl
10-13 w: wwwwwwwwwwwwdw
13-14 n: nnnnnnnnnnnnnmkn
5-11 q: jpbzqwqbwttgzn
4-5 k: kkkwkkk
10-17 w: sgtklkflsrfqxfwhjm
6-12 w: wwjqwwlmphwkwwwwwjw
2-13 p: ppppppppppppzp
2-16 h: tslcwztxxtchgqlxsbx
2-9 p: slptvtljpxdkf
10-12 z: tnzzghzzgzfn
3-18 f: ffxfffffffffffffff
1-2 p: prdpdghkckdgpl
6-8 x: fxxnbwrx
7-9 z: zmzkzdpgjzzz
7-14 p: pppppppppppppppb
7-10 l: xltlzllllljzxlll
18-20 n: nnnnnnnqnnnnnnnnnmnb
15-18 p: pxmqxpmqwfntrpppmf
1-15 v: kgmvwvrvmcvtrvvwv
2-8 g: gxggggggg
4-5 f: clfjfqmpffjfff
3-5 r: rpjkf
2-9 h: hhhhhshhrhh
2-5 z: zxzzz
5-11 k: kkkkkkkkkkkk
8-9 n: nnddcfntnrgnnrnnc
1-11 f: dfffffffffff
2-4 x: dzphvg
4-5 w: mnzlr
2-6 f: jhrkfmg
2-17 z: czzvvzzczznzhwzbzz
2-5 r: xrjrg
2-3 g: gggg
7-9 s: ssssssbsssss
17-19 k: kcwktkxkkbkqnwkkkkdz
1-16 f: zmxdffmfgffxrffffqf
7-8 q: qtmrkbqjq
8-9 q: qqqqqqqqx
10-18 n: nnnnnnnnnznnnnnnnnnn
16-18 x: xwxxxxxxxxxxxxxxxrxx
15-18 t: tttttftptttttttcttt
10-11 h: hfxnlbsqxphtmstbhdn
7-13 z: vdzdzmzxvfzzz
2-5 n: nnpqgnnqnb
12-16 v: pvjvvnbqzjnvvvvpjv
4-5 d: ddddk
4-8 l: lxvhlbclhgd
3-12 v: vvkvvvvvvvvvvvvvvvvv
17-18 j: jjjjjjjjjjjjjjjjdj
6-7 b: ckbdbcsbb
9-11 q: qrhxpcjjqbqt
8-14 h: hhhhhhhhhhhhklhhhhn
2-3 b: bzbjb
2-15 w: nnmdgzhsvhpvswltvt
1-5 l: lbclz
15-17 d: wlddgdxsdcdfdcgdd
18-20 q: dqsldgqqfqwsstqlmqtz
1-6 q: qqqqqdq
2-6 j: jpjjjjjj
13-15 p: ztjlhtnsgphgxccpfsp
6-13 m: ghvvmrglmmmcm
3-6 b: nbbrmrfdlbs
1-3 j: fwhjsr
7-10 p: gcppcppzpppp
4-12 r: rrrrrrrrrrrrrr
16-20 d: djdddvdsddddlmddddpm
14-19 x: xzxjxxxxxxxxxxxxxxj
11-16 w: kwclzxjjwxlwkcnwkwv
3-11 b: zhhxsgqxqbbg
10-11 q: trbhqqzhdqw
9-13 l: vcvlvqlwrlfvll
7-9 x: xxxxxxxxgx
5-6 n: nnnngnn
2-5 p: pqpppppppqpxp
4-17 z: zxrmzwwxwhqxxmqrv
5-9 v: vvvvvvvvrvvvj
6-7 x: qkhbxxkxs
3-4 d: fcmd
5-9 f: nsnlxstff
6-9 x: hrtzmhrxxbmcc
3-7 w: wwwwwwsww
5-8 g: ngkdxggg
8-13 r: rrrrphrrrrrrrrrrdrt
2-6 f: rckzvzfrnp
4-6 k: bfrpttcfbwmvhgn
7-9 w: wwwwwwswww
13-15 n: nnnnnnnnnnnnnnn
4-8 j: jjjjjjjwjjj
9-11 h: hhhhhhrhhhhhh
4-7 h: thmhwrhss
1-3 d: ddddddddddddd
10-11 c: ckrcxwcdpqc
2-4 g: kgghg
3-12 s: ssssvwssssgqs
2-7 s: sssssszs
2-10 v: wvpbjqxvzsdpgmq
12-15 n: nnnnnnbnqvrkfnn
3-5 w: wlvdw
11-14 t: pfrbxgcrwndttj
6-7 w: qnnwwpfwwhw
7-10 n: nnnvnnhnnx
3-12 c: mmfcwvxqwpcclwlxfx
2-3 p: lgpxpppp
17-19 k: rfxvmnmfzrnktfpckpr
2-9 k: kkkknkkkkkkk
15-16 t: ttjmtttmttttttwt
9-10 r: rrrrrrrrmrrrr
3-4 p: jppppxf
7-8 k: nkqbvkkt
6-8 d: dddddrdddd
6-7 q: czbqdgnc
3-5 p: rxpppsx
4-6 t: thvtwv
2-13 d: dmdddddddddddd
16-18 n: nnnnnnnnnnnnnnnnnnn
11-12 s: ssfsdsmssswssh
3-5 v: kxnvvvmvrvdvvssvvv
5-8 x: nxxxxbxxxzx
3-5 t: ctttftt
5-7 s: hssvsgj
5-8 r: rrrrrrrcrx
1-13 v: vvvvvvvvvvvvpvvvvvv
5-9 h: gxlrhsgswhchfxbwjd
2-4 w: wgwb
6-12 v: pmxnjtfsvvxvv
1-4 n: vnntn
2-3 w: wwww
3-7 f: xmfbmnvnfkkmsd
10-12 x: xxxxxxjgxxxxx
2-3 l: cllvpbtmgzmrfmq
2-4 l: llrlllnlxll
5-10 h: hdhhhzhvtchhh
8-10 q: lhqmdwcfhqngq
1-5 t: twtfvcmktthtjltqvpwc
6-8 s: sxsghtbs
3-4 m: mmmmmmmmmmmmmmmm
16-17 l: rjdpxhtblvllgvwhl
5-13 s: brhsssnfcndsh
7-13 v: swkfswvmkvjbnsgvwp
1-3 k: wlfpzk
2-4 t: tpttt
2-9 t: cntttttcgtttt
5-6 r: rrrrbh
10-12 j: jjjjjjjjjzjjdj'''
'''def is_valid(password_instruction):
    password_instruction = re.split(r'[-:\s]\s*', password_instruction)
    password_instruction[0] = int(password_instruction[0])
    password_instruction[1] = int(password_instruction[1])
    for i in password_instruction[-1]:
        if password_instruction[-2] not in i:
            password_instruction[-1] = password_instruction[-1].replace(i, '')
    if password_instruction[0] <= len(password_instruction[-1]) <= password_instruction[1]:
        return True


list_of_passwords = str_of_passwords.split("\n")
ans2_1 = 0
for i in list_of_passwords:
    if is_valid(i):
        ans2_1 += 1
print(ans2_1)
'''

# day 2:2
'''def is_valid2(password_instruction2):
    password_instruction2 = re.split(r'[-:\s]\s*', password_instruction2)
    password_instruction2[0] = int(password_instruction2[0])
    password_instruction2[1] = int(password_instruction2[1])
    p2_0 = int(password_instruction2[0])
    p2_1 = int(password_instruction2[1])
    if password_instruction2[-1][p2_0 - 1] == password_instruction2[-2] and password_instruction2[-2] != \
            password_instruction2[-1][p2_1 - 1]:
        return True
    elif password_instruction2[-1][p2_1 - 1] == password_instruction2[-2] and password_instruction2[-2] != \
            password_instruction2[-1][p2_0 - 1]:
        return True


list_of_passwords = str_of_passwords.split("\n")
ans2_2 = 0
for i in list_of_passwords:
    if is_valid2(i):
        ans2_2 += 1
print(ans2_2)'''

# day 3
'''
# day 3:1
map_design =''' '''..#.......#..##...#...#..#.#...
..##..#..#.....#.........#....#
...#.##..#.#......#.#....#.....
...#.....#......#...#..........
.......#.#..#..#....##....##...
.#......#......#.#..#....#.#...
.#..........#.....###.##..#.#..
....#...##...........#.........
##......#.#...#...#....##.#...#
.....#.....#.#..#....###...#..#
.#....#.........#...#.......#.#
.##......#.#.........#....#.#..
...#........###..#......##....#
.#.....###..........#...#....##
............#......#...#...#..#
.....#.#....#.#.#...........#.#
....#.....#...##.##.....###..#.
.....#.##......#.##.#...#.#.#..
##.....#.##.##....#..##......#.
.....#.....#........#........##
#..#...#.#.#..##....#....##..#.
.#......................##..#..
#.#.#................#.....#...
..#....#.#.#..##..#..#.....##..
.....###..#.............#....##
..#....#.#...#......###..#.....
.......####.....##......#......
..##...#..#...#.#..#......#....
..##..#..#.....#......##.##....
.#......#................#..#.#
...............#....#.......#..
#...........#.#.#........#.#...
...#...#..#.....##..#.##...#.#.
.#.#..#.#.....#...#..##....#.##
.........#...#.#.#....#.......#
............##.#..#.#........#.
#..#..#........#......####.....
..#.#...#...#...#.#...#..#..#..
#....................#.#.#....#
.......#.....#....#....##..#...
.......#.............##.....#..
..##..#.......#..#.........#..#
..##.#........#...#...#..#..#..
..##.#...#................#..#.
..#.....##...##......###.....#.
.....#.....#......#......#.....
....##.#.#....#.....#..........
...#...#.#.....#.###.....#....#
......##....#..##...##.#.......
......................##......#
.##......#...#...#...##.#.##.#.
#.......#...#.....#........#.#.
...............#......#.......#
.#..##...#....#.....###....##..
...#..###...#..#....#.#..#.....
.#...#....#.................#..
.......##....#..##......#.#....
....#.....#.....###...#....#...
..##..#..##........#...........
....#..#.#............#........
####.....##.........#....#.....
........#.....#......#......##.
#..........#........#....#...##
#..#...###.....##.....#.##...#.
......#....##.............#..#.
..#......###...#...#..##.....#.
#.##...#......##.###....#....#.
...............#....#.....###.#
#......#........#.#..##.#.....#
#..............#..##.#....#....
.##....###...#...#.#....#....#.
.......#...#.......#....#..##..
..##.#.....#..#...............#
.##..............#.......#...#.
.....#...#.#..#.........#..#...
........#.#.###......#..#......
..#.......###..#...#...........
............#.#.....#....#...#.
#...#..#......#..#......#......
..##..#......#..#.......#.....#
............#.##.....#.#...#...
....#.#...#.#...#........##....
........##...#...##.....#.#..#.
.#..........#.##...............
###.#..#...###..###..#........#
....#..#............#...#.#.#..
.#....###........#.......#...#.
..........#..#.....#......#....
..##..#.#....#..#.....##....#..
...#...............#......#....
......#.#.#...###.....##.#.....
.#...#.#.#.#....#.....#..#..#.#
..#.....#..##....#......#.#.#..
##.#....#.......#.#.#.......#..
.#.#.#........##.#....#........
...#..#...#.#.........#..#....#
#.#......#.#.#..#.#............
......#.....#.....#.......#..#.
.........#..#.##..#..###....#.#
.......#..........#..#.........
......#.#.##...#.#...##........
...........##..##.##....#......
..#..#...#.###...##.....#..#..#
.#...##.......#.#..........#..#
##......#...........#.#........
..#..#.....##..#.#.......#...#.
.#....#..#.....###.......#...#.
...#..#...#...###.#.###..#.....
.......#...#.##......#.#.#.#...
.#.......#...#...#...##........
...#........#....#..#.#...#.#..
..#............#.....#.#....#..
#.....#.#..#.#....#...#.#.#....
#......#......##.#...........#.
.#..#.........##.#........#....
.#....#.#...#........#......#..
....#..#..#....#..#.#.....#..#.
.##.#.....#..#.#...#.....#..###
#..#......#..##....##..#.......
.......#..##....#.###..........
.#......#..........#........#..
.........#.....#......#.#......
.....#..#.......#...#.#....#...
.#......#...#..#......#.....#.#
#.#.#..#.........#.......##....
...#..#.....#.#..#......#...#..
.##...#...#.#....#.....#.#...#.
..#......##......#....#.#..#...
....#.#.....#..#...........#...
.#........#....#....#...#......
..#.#.....#.......#.#.#.##..##.
...#..#.##.......#...#.........
....##.#.#..#.#..#.#.#..#.#.#.#
......#.......#.....#...##.#...
..#.##.....#....#...#...##.##.#
..##.........##.........#..#...
.....###......####..#.#...#....
...#....#....##.............#.#
.#.........#.......##..#.#.....
...#..#........#...............
........#........##......#.#...
##...#......#.....#.##........#
.............#.#........#......
.......##.........#.......#....
....#.......#......#..###....#.
.#.##........#.....#......#....
#...........##...#..##.........
.....#.#........#........##...#
#.........#..##.....#...#....#.
.........#...####..#....###....
###.#..##.......#....#....#.##.
...........#.....#.#...#..#....
.##......###.#.#.#....#........
....#..................#.###.#.
#..##...#......#...#......###..
.#.....#..##......#.#.#.#......
..##...#..#.......##.#.......#.
...#..#..##..##..##.#..####....
......#..#..............#.#####
....#....#..#...#...#.#........
.###...#.......#..#........#...
........#.#......##...#........
.#..#.......##.......#.....##..
...##..........##...........#..
......................#..#.#.#.
#..#.....#......#.....#....#.##
..#......#.....#....#...#.##.#.
............#...#...#......#.##
........##.......#......##.....
..#.##.....#....#..##...#......
........#.#...##.#..#...#....#.
...##............##.....#..#...
...###.##....#....#.#.#.#..#...
............#..#....#..#.....##
...#......##.......#......##..#
.......#......#........#.....#.
.#....#.##..........#..........
..###.........#..#...##.....#..
##....##..#.......###....#.#.#.
#.......#.#.##.................
..#..........#................#
....#.#....#...###...#......#..
.#..........#..#..##.....#...##
.#.....###....#.#...#.#........
.........##.........#..#.#.....
.#.....##....#......##.#....#..
###..#...#..#.........#......#.
..##.....#....#............#...
.....##.##....#.....#..#..#....
.......###...#..........#......
...#........#....#.##.#........
........###....##........##.#..
....#....#........#.....##.....
.#........#.#........#...#..#..
#..#..#......#....##.#..###....
...........#...#...#....#.#...#
.#..#.....#.##..#......##......
..#.#...............##..##.###.
...#.#...#............##.#..#..
.#.#....#....#................#
...#..#.#.##.#.#....#......#...
.........#..#.......##.##.#....
..............#..##.#.....#....
......#.........#...#...##.#..#
....##.....#.#...#.#.####.#....
#..#.#....#.##.......#....#....
...##....#...................##
##.#.......#....#.#.........#.#
.##.#..###...#.#.........#.....
...#.#.#..#...#...#.##....#..#.
....#.....###...#....##........
.............#....#....#....#..
#...#.....#.#...#.#............
#.#....#...........##.......#..
..#..#.........#....###.......#
....###..................##...#
.#........#.....##...#......#..
#..#......#..#.....#.##..#...#.
....#........#.##.#......#.....
#.#...#...............####...##
#.#.....##..#.####.............
##...##..#.##........#.#...#...
...#...........#............#..
...#..#..#........##...........
..#.##..#.#...#...#..#......#..
.....##......#...##.....##.....
.......##.....##....#..........
..........#.#...............#.#
#.#..........#..#..##..#...#..#
.#.#..#.###................#...
#...#...#....#...#....#.##.##..
.#................###.....##...
.....##.#.....##.#.....#.....##
.......#.......#......#.#......
..#....#......#.....#.....#..#.
#......#..##..####.....#.#..#..
.......#...###..#...#.....#....
#.#.#......#.............#..###
.#.#.......#..#.#..#..#...#.#..
..#.#......#......#.#....#.....
..#..###..#.#.....#....#.......
..........#........#......#..#.
##..........##....##..###.##...
...#....#.......#..##.......#..
##...#............##...#.#.#.#.
...........#...#.#....#.....##.
.#................#.......#...#
....##.#..#.#.........###.###.#
#..#...###..#...#......#..##...
..##........#.#..##.#..........
...#..#...#...............#.#..
##.##....#...#........#...#....
#..#......#.##.................
.....#..##.##.......#..........
...#.....#........#......#.....
.....#..#......#.....##...#....
#......#...###....#....###.....
................###..#..#..#.##
......#.......#..........#.#..#
###..#..#.##.............#.#...
....##.#.......#...#..##.......
..#.....##..#..#..#.#..........
.#.......#.#..#........##......
..............#.........#......
..#........##....#.#.#......##.
.#.#.........#.#...#.#.........
..........#..#.##.#....#...#.#.
............##....#.....###...#
#....#..#...#.#...#.....#....#.
.#...##.....#......#..#........
.#..#...###.#..##........#...#.
#..#...##.####.......#.....#...
#.##..#...#......#.#.......#.#.
#.#.....##...#.#...............
#...........##.##.#.........#..
...#...........#.#.#.#....#..#.
..#......#.#.#....##..#.#.....#
.........#.#.##...##...#.#.#...
...........#..#.####.#..#.#.###
#........#.#......#..#...#.....
...#....#......##...#.#........
......#.#....#.##....#....#..##
.......###......#.#.....#......
#..........##..................
.###.......##..#..##...##......
##.#..............#....#....##.
#....#.....#.##.....#..#....#.#
.......#.......#..#..#..##..#..
......#...........#..##....#...
.....#.......#..#......#..#..##
.##...#......#........#....#...
.....#..#....#...............##
..#.....#....#..#.##....#.#....
#.#......####...#..#.........#.
#.#........#..#........#...#...
..#..............#.......###.#.
...#.#....##.#......#........#.
....###.......##.#.....##.....#
.........#......#.#.......##.##
.......#.#....#.#...#...#....#.
....#....#....#.#.......##.....
#...#.....#..#.....#...........
#...#..#...#.#..#.............#
........###..#........#........
.............#....#..###..#.#.#
#...............#..#.#.........
##.....###..#......#...#....#..
.#...................##.#.##...
#..#........#.#...#..#...#.....
................#.#.........#..
#.....##.#.#...#..#.........##.
...#.....#....#..####.#........
....#.#...........#............
.....#........##..........#....
..#.......#.#.#.####..#......#.
#.......#...##.#.#..#.#.#......
##........#.#...###............
..##........#........#...#.#.#.
#.#..#.#.......#....#........#.
..............#....#.........#.
#....#.#........#.............#
..##...#..........#........#...
..#..#..#....#....#............''''''
list_of_tree_patterns = map_design.split()
def is_tree(x, y):
    if list(list_of_tree_patterns[y])[x] == "#":
        return True
x_cord = 0
y_cord = 0
number_of_trees = 0
j = 0
while y_cord < len(list_of_tree_patterns):
    if is_tree(x_cord, y_cord) is True:
        number_of_trees += 1
    x_cord = (x_cord + 3) % 31
    y_cord = (y_cord + 1)
print(number_of_trees)

# day 3:2
def is_tree(x, y):
    if list(list_of_tree_patterns[y])[x] == "#":
        return True

def n_tree_finder_slope(x, y):
    x_cord = 0
    y_cord = 0
    number_of_trees = 0
    j = 0
    while y_cord < len(list_of_tree_patterns):
        if is_tree(x_cord, y_cord) is True:
            number_of_trees += 1
        x_cord = (x_cord + x) % 31
        y_cord = (y_cord + y)
    return number_of_trees
print(n_tree_finder_slope(1, 1)*n_tree_finder_slope(3, 1)*n_tree_finder_slope(5, 1)*n_tree_finder_slope(7, 1)*n_tree_finder_slope(1, 2))
'''

# day 4

'''
# day 4:1
passport_details =''' '''hcl:5d90f0 cid:270 ecl:#66dc9c hgt:62cm byr:1945 pid:63201172 eyr:2026

ecl:amb byr:1943 iyr:2014 eyr:2028
pid:333051831

byr:1971
eyr:2021 iyr:2015 pid:158388040 hcl:#18171d ecl:brn hgt:179cm

byr:1936
pid:707057570 iyr:2014 ecl:amb cid:299 eyr:2030
hcl:#c0946f hgt:186cm

hgt:163cm iyr:2013 ecl:gry hcl:#86e981 byr:1939
eyr:2020 pid:241741372 cid:203

ecl:brn hcl:#341e13
pid:686617364 byr:1929 eyr:2029 hgt:160cm cid:280 iyr:2020

byr:2002 hcl:#623a2f
pid:253005469 iyr:2011 ecl:hzl hgt:184cm eyr:2027

ecl:#bb984b eyr:2040
hgt:188in
iyr:2005 hcl:c5be8e pid:174cm cid:161 byr:2004

ecl:oth iyr:2010 cid:128 hgt:153cm byr:1991
pid:24061445 eyr:2025 hcl:#54d43e

hcl:z
iyr:2023 pid:981178503 ecl:gmt eyr:2038 byr:2004

ecl:gry eyr:2022 iyr:1981 pid:566993828
byr:1941 hcl:#341e13 hgt:176cm

eyr:2027 byr:1976
pid:350079989 ecl:blu iyr:2013 hgt:180cm hcl:#866857

eyr:2029 hcl:#ceb3a1
ecl:lzr
iyr:2011 hgt:152cm byr:1986 pid:162999623
cid:240

ecl:gry iyr:2017 hcl:#18171d byr:1926
eyr:2027 hgt:68in
cid:310 pid:560836007

ecl:grn
cid:307
pid:#cdc803
byr:1975 eyr:2039 hgt:75cm
hcl:318b11 iyr:2022

ecl:brn hgt:179cm eyr:2020 iyr:2016
pid:322103252 byr:1940 hcl:#b6652a

hcl:#733820 hgt:188cm cid:70 eyr:2021 ecl:amb
byr:1996
iyr:2013 pid:412419084

hgt:164cm iyr:2011 byr:1928 eyr:2020 hcl:#733820 pid:704914380 ecl:blu

ecl:brn cid:267 eyr:2029 byr:2011
hcl:z pid:467662306 iyr:2026 hgt:104

pid:224593036 eyr:2027
ecl:brn hcl:#341e13 iyr:2014
byr:1997
hgt:181cm

eyr:2005 pid:9756449964
hcl:#fffffd byr:1999 ecl:dne hgt:152in iyr:2027

byr:1998
iyr:2017 pid:618350852 hgt:156cm cid:193 ecl:amb
hcl:#602927 eyr:2029

byr:2021 pid:3395281192
hcl:z hgt:167in ecl:grt eyr:2008 iyr:2025

cid:206 pid:735212085 eyr:2020 byr:1950 hgt:153cm
ecl:blu iyr:2019
hcl:#733820

eyr:2021 pid:551149968 iyr:2020 hcl:#6b5442
byr:1948
ecl:grn
hgt:152cm

hgt:76in cid:113 iyr:2019 eyr:2023 hcl:#888785 pid:131239468 ecl:grn
byr:1994

ecl:oth cid:240 hcl:#bed757 byr:2027 eyr:2021 pid:#ffa971 iyr:2022

cid:204 iyr:2011
ecl:blu hgt:169cm byr:1985 eyr:2020 hcl:#18171d

ecl:hzl iyr:2012 cid:344 hcl:#7d3b0c
hgt:190cm pid:599490023 byr:1954 eyr:2023

cid:333
eyr:1971 hgt:193cm
ecl:#12421d hcl:#7d3b0c iyr:1991 pid:#7149ad byr:2008

iyr:2014
hgt:151cm pid:190259199 eyr:2021 ecl:blu
byr:1975 hcl:#ceb3a1

hgt:164cm ecl:oth hcl:#c0946f pid:427760590 eyr:2023 iyr:2012
byr:1979

hgt:193cm iyr:2023 ecl:#213711 hcl:z
pid:23861701
byr:2020
eyr:1924

pid:450691994 cid:191
eyr:2028
byr:1972 ecl:oth hgt:168cm hcl:#888785

iyr:2013 hcl:#18171d hgt:170cm ecl:blu
pid:040253250 eyr:2024
byr:1954 cid:340

cid:185 byr:1956 eyr:2029 pid:454637740 ecl:hzl hcl:#efcc98 iyr:2019 hgt:73in

hcl:#efcc98
hgt:176cm
ecl:hzl cid:113 pid:747653564 iyr:2016
eyr:2020 byr:1945

hgt:69in cid:264 byr:1971 hcl:#733820 ecl:amb pid:086130104
iyr:2011
eyr:2022

iyr:2010
eyr:2034
pid:501068596
hgt:109 hcl:z byr:2018 cid:326 ecl:lzr

pid:955229652
eyr:2027 cid:175
byr:1950 iyr:2010 ecl:gry hcl:#866857 hgt:177cm

ecl:amb hcl:#888785 eyr:2020
hgt:172cm byr:1991
pid:556956304

byr:1930
eyr:2011
pid:734176827
ecl:brn hgt:182cm
hcl:z

hcl:#a97842
pid:040278061 ecl:brn hgt:168cm cid:194
byr:1973
iyr:2016 eyr:2027

hcl:#623a2f
eyr:2023
ecl:blu iyr:2016 pid:844348663 byr:1997 hgt:179cm

hgt:188cm hcl:#a97842 byr:1972
ecl:hzl pid:912948357 eyr:2026 iyr:2025

iyr:2011 eyr:2025
cid:286
pid:084736292
byr:1936
ecl:oth hcl:#a97842 hgt:166cm

iyr:2012 ecl:blu hgt:159cm byr:1980 eyr:2024 pid:811644928 cid:105 hcl:#7d3b0c

pid:530452683 hcl:#341e13
iyr:2011
hgt:163cm ecl:oth
cid:309 byr:1940

ecl:hzl
pid:144377866
hcl:#18171d hgt:193cm
iyr:2013 eyr:2028

pid:868386570
ecl:brn
hgt:161cm hcl:#18171d
byr:1956
iyr:2017
cid:307

iyr:2019 eyr:2026 ecl:brn
hcl:#866857 byr:1993 cid:299
pid:603503348 hgt:186cm

iyr:2014
pid:852954158 hgt:73in byr:2021
eyr:2020 hcl:#a97842 cid:260 ecl:oth

hgt:164cm eyr:2025 pid:113005290 byr:1955 ecl:blu iyr:2017 hcl:#b6652a

cid:179 iyr:2015
pid:317467924 eyr:2025 ecl:gry byr:1996 hgt:180cm hcl:#a55f97

hgt:172cm hcl:#efcc98 cid:53 ecl:grn iyr:2016
byr:1991 pid:337133478
eyr:2025

hgt:150 iyr:2008
pid:#3e66a7 ecl:#8b3133 eyr:2040 byr:2012 hcl:802d16

pid:577607614 byr:1924 hgt:173cm hcl:#341e13 eyr:2026 ecl:amb
iyr:2013

eyr:2020 iyr:2011 hgt:175cm hcl:316607 pid:738554684
byr:2029 ecl:dne

hgt:179cm iyr:2016
pid:178cm byr:2015
ecl:gry
hcl:#341e13
eyr:1986

byr:2005 iyr:2028 ecl:#7be9b8 eyr:1941 pid:#e7e9cb hgt:177in cid:67 hcl:#602927

ecl:#0d50e6
pid:192cm iyr:2014 eyr:2027 hgt:73cm cid:162 hcl:93ea2f
byr:1958

hcl:z
cid:292 hgt:184in eyr:2001 pid:7218132701 byr:2020
ecl:grt iyr:2014

ecl:gry
hcl:#fffffd
eyr:2026 iyr:2013
pid:117261833

pid:780384540 ecl:gry cid:52 eyr:2020 hgt:193cm hcl:#4ae223 iyr:2017
byr:1984

ecl:hzl
pid:218314886 eyr:2030 byr:1948 hcl:#c0946f hgt:185cm iyr:2013

pid:175cm cid:340 ecl:blu hcl:#cfa07d eyr:2036 iyr:2018 byr:2018 hgt:70cm

byr:1953 hgt:164cm ecl:hzl
pid:488831953 iyr:2010
hcl:#fffffd

byr:1961 hgt:165cm pid:506597451
cid:122 eyr:2020 hcl:#cfa07d ecl:gry
iyr:2016

iyr:1970
eyr:2040
byr:2008
hgt:188
ecl:#b00a46 hcl:#fffffd

hgt:179cm
byr:1972 eyr:2026
cid:62 ecl:oth
pid:996355557 iyr:2013 hcl:#a97842

ecl:amb eyr:2026 byr:1936 pid:812982189 hgt:158cm hcl:#888785 iyr:2010

iyr:2020
hcl:#7d3b0c hgt:160cm
pid:336806720
eyr:2024 ecl:#7e0ae0 byr:1992

eyr:2036 pid:178cm hcl:z
hgt:133 byr:2009 ecl:dne cid:127

byr:1938 hcl:#fd309a
cid:104 iyr:2015 eyr:2022 pid:201047563
hgt:160cm ecl:hzl

byr:2023 pid:25086180 hgt:160cm cid:180 hcl:z ecl:grt eyr:2038 iyr:2022

ecl:grn hgt:167cm
byr:2023 iyr:2026 eyr:1928 hcl:z

hcl:#efcc98 hgt:187cm byr:1925
ecl:grn
pid:753746076 iyr:2017
eyr:2021

iyr:2017
byr:1934 ecl:grn eyr:2021 hgt:163cm
pid:688172460 hcl:#b6652a

hcl:#c0946f iyr:2018 ecl:blu pid:676564085
hgt:184cm cid:152 byr:1980 eyr:2023

ecl:grt hgt:70cm iyr:2022 hcl:58716b byr:2010
pid:60834390 eyr:2037

iyr:2028 pid:270499403
ecl:xry eyr:1947 hgt:152cm byr:2025

pid:091281559 hcl:#733820
hgt:166cm
eyr:2021 ecl:grn cid:327 byr:1928
iyr:2014

eyr:2025 ecl:grn byr:1938 hcl:#ceb3a1
cid:234
pid:549433891
hgt:172cm iyr:2016

hcl:#c0946f hgt:173cm iyr:2014 eyr:2030 ecl:blu byr:1965
pid:696577272

hgt:154cm eyr:2030
pid:475642195 byr:1920 iyr:2013 hcl:#866857 ecl:blu

pid:518398763 iyr:2010
eyr:2020
hgt:183cm
ecl:brn byr:1921 hcl:#18171d

eyr:2023 pid:614116723 hcl:#7d3b0c ecl:hzl
iyr:2016 hgt:189cm byr:2000

ecl:oth hgt:178cm hcl:#733820 byr:2001 pid:862420089 eyr:2023

pid:851985534 eyr:2028 hcl:#18171d ecl:oth cid:238 byr:2001
iyr:2019 hgt:166cm

byr:1927
hgt:170cm
pid:246933107
ecl:amb iyr:2015
cid:166 eyr:2027 hcl:#b6652a

byr:1929
hcl:#7d3b0c
cid:263 pid:317156081 hgt:165cm eyr:2031 iyr:1980

hcl:#866857 eyr:2021 hgt:179cm pid:206504353 cid:84 ecl:gry iyr:2012 byr:1952

byr:1986 ecl:hzl
hcl:#a97842
iyr:2015 hgt:152cm pid:722601936 eyr:2025

byr:1921
pid:563550743 iyr:2015 ecl:hzl
eyr:2026 hcl:#fffd7b

ecl:hzl
hcl:#888785 cid:268 byr:1926 hgt:176cm pid:321394231 eyr:2021 iyr:2014

eyr:2021 cid:225
pid:770796086
ecl:gry byr:1961
hgt:154cm
hcl:#6b5442
iyr:2011

eyr:2028 iyr:1961 byr:2016
cid:98 pid:587360691 hgt:70cm ecl:#ceaf1f
hcl:#c0b6db

byr:1978
eyr:2022 hgt:184cm hcl:#7d3b0c
cid:271
ecl:amb pid:235352975
iyr:2010

eyr:2026 pid:2844744
iyr:1958 byr:2017 hcl:z
hgt:192in
ecl:#971530

iyr:2020
byr:1960 eyr:2028 cid:162 pid:491912610 hcl:#fffffd hgt:59in

iyr:2012 pid:365229485 ecl:amb byr:1933 hcl:#18171d eyr:2024

hgt:193cm pid:473100400
hcl:#efcc98
cid:201 eyr:2020 byr:1969 ecl:gry iyr:2016

eyr:2025 pid:137807160 iyr:2014
ecl:grn byr:1944 hgt:168cm hcl:#ceb3a1

byr:2008 ecl:xry
iyr:2012 hcl:#efcc98 eyr:2028 pid:272344138

eyr:2024 pid:959415175 cid:148 hcl:#efcc98
byr:1977 hgt:179cm ecl:amb

pid:253742161 ecl:hzl hcl:#602927
eyr:2021 hgt:191cm byr:1925 iyr:2010

ecl:amb hcl:#341e13
eyr:2024 iyr:2017
byr:1975
pid:838040028 hgt:172cm

hgt:172in
pid:311113967 iyr:2015 cid:111 eyr:2023 ecl:oth byr:2003 hcl:#866857

hcl:#888785 byr:1978 hgt:64in pid:442064310 eyr:2021
iyr:2011 ecl:hzl

eyr:2021 byr:1988 hcl:#a97842
pid:290578586 ecl:hzl hgt:174cm iyr:2020

byr:1998 iyr:2020 hgt:163cm ecl:oth eyr:2025
hcl:#6b5442 pid:913461954

hgt:173cm hcl:#18171d
eyr:2029 ecl:brn cid:313 byr:1980
iyr:2011 pid:810497375

byr:1975 hgt:153cm eyr:2027 hcl:#fffffd pid:857730031
ecl:gry iyr:2020

hcl:#18171d ecl:hzl
pid:185778821 hgt:178 iyr:2014 eyr:2028 byr:1974

iyr:2015 hgt:163in hcl:#c0946f ecl:#4844a6 byr:1979 pid:124626004

eyr:2024
pid:737015681 byr:1952
ecl:hzl iyr:2019
hgt:192cm hcl:#cfa07d

pid:2986469633 byr:2025 hgt:66cm hcl:z eyr:2011 iyr:2027 cid:311

byr:1962
eyr:2032
ecl:lzr iyr:2014
hgt:70cm pid:94309916
hcl:#fffffd

cid:350 hcl:#602927 iyr:2019 hgt:178cm
pid:172238204 byr:1949 ecl:hzl
eyr:2028

hgt:153cm
hcl:#ceb3a1
ecl:grn
byr:1997
pid:266747822
iyr:2011 eyr:2022

pid:839681159 hgt:150cm eyr:2024 hcl:4d6414
ecl:blu
iyr:2018 byr:1988

byr:1930 iyr:2011 pid:352711700 hgt:174cm cid:67 eyr:2020 ecl:hzl hcl:#6b5442

byr:1949 iyr:2013 hcl:#623a2f eyr:2030
hgt:176cm

hgt:164cm eyr:2026 hcl:#866857
iyr:2018 pid:922679610 byr:1974
ecl:brn
cid:114

eyr:2038 cid:317
hgt:166in pid:0384056779 byr:2013 iyr:2021
ecl:xry

cid:83 hgt:166cm eyr:2026 iyr:2018 byr:1994 ecl:brn pid:858360477 hcl:#ceb3a1

hgt:169cm eyr:2020
pid:110129489 byr:1958
ecl:oth hcl:#7d3b0c
iyr:2011

cid:279
iyr:2019 byr:1995 eyr:2026 ecl:hzl
hcl:#7d3b0c hgt:185cm pid:085427066

hcl:#c0946f
iyr:2011 eyr:2027
ecl:amb
byr:1943 pid:060674566 hgt:183in

hgt:156cm hcl:#c0946f pid:242827141
cid:152
iyr:2018
eyr:2025 byr:1963

byr:1925 cid:168 eyr:2020 hcl:#cfa07d iyr:2011 ecl:brn hgt:150cm pid:740118192

ecl:oth byr:1951 eyr:2025 cid:213
iyr:2020
hgt:154cm

eyr:2025 iyr:2018 ecl:grn cid:91 byr:1925
hgt:164cm hcl:#18171d

byr:1997
iyr:2018 eyr:2023 hcl:#602927 pid:251296833 ecl:blu
hgt:185cm

hgt:168cm pid:556895048
hcl:#341e13 ecl:oth eyr:2020 cid:64 byr:1940

byr:1996 pid:821204904 cid:250 ecl:amb eyr:2026 hgt:185cm iyr:2019

ecl:grn hcl:#b6652a iyr:2013
eyr:2028 hgt:157cm
byr:1925 pid:158cm

hgt:190cm iyr:2019 ecl:oth eyr:2028 hcl:#341e13 cid:334 pid:258135663 byr:1972

byr:1936 hgt:76in pid:748344702 cid:335
eyr:2027 hcl:#a97842 ecl:amb iyr:2015

hcl:z hgt:66cm eyr:2029
pid:#1589e0 iyr:2019 ecl:hzl

hcl:#733820 ecl:amb
iyr:2013
hgt:188cm byr:1955 pid:125663066 eyr:2020 cid:179

iyr:2017
hgt:185cm ecl:grn
cid:298 eyr:2030 hcl:#5b1c03
byr:1992 pid:092887457

eyr:2032 ecl:grn hgt:82 iyr:2022
pid:180cm byr:2003
cid:55 hcl:z

pid:257666411 eyr:2023 byr:1982 hgt:179cm hcl:#18171d ecl:brn iyr:2010

iyr:2020
ecl:amb hcl:#18171d
pid:971402454 eyr:2028

hcl:#efcc98 byr:1964 pid:577424639 eyr:2030 iyr:2010 ecl:brn hgt:169cm
cid:285

ecl:amb byr:1958 hgt:159cm hcl:#efcc98 eyr:2024 iyr:2016
pid:029502840

hcl:ac11eb
byr:2007 pid:0489471320 hgt:69cm iyr:2030 ecl:blu eyr:2033

pid:3785138563 eyr:2020 iyr:2020
hcl:#966583 byr:2008 hgt:186cm ecl:gry

iyr:2014 pid:868785127 eyr:2029
cid:220 hcl:#18171d ecl:blu byr:1948 hgt:171cm

byr:1936
pid:433437105
hcl:#c0946f eyr:2020 iyr:2019 hgt:160cm ecl:brn

iyr:2015 eyr:2024 hgt:176cm ecl:hzl
byr:1995 pid:101835436 hcl:#ceb3a1

eyr:1959
hcl:#cfa07d iyr:2010 pid:9214728
ecl:#42fda0 hgt:71 byr:2022

byr:1998 iyr:2011 cid:275 ecl:oth
pid:924517068 eyr:2024 hgt:191cm
hcl:#623a2f

hgt:157 hcl:z
byr:1923 pid:#f6ce52 iyr:1975 ecl:lzr cid:100

pid:565022102
eyr:2021 hcl:#efcc98
byr:1988 ecl:gry iyr:2012

hgt:156cm
hcl:#b6652a eyr:2021 pid:969724332
cid:126 iyr:2016
ecl:hzl byr:1988

ecl:blu hcl:#866857 hgt:153cm
pid:798083560
iyr:2015
byr:1981 eyr:2030

iyr:2013 cid:103 hcl:#efcc98 eyr:2022 byr:1964 ecl:gry
hgt:161cm pid:950689613

pid:4316019547
ecl:gmt
eyr:2029 byr:2011 iyr:2005 hgt:170cm cid:135
hcl:567fd8

hcl:#6b5442 pid:843348901 byr:1960
hgt:156cm
eyr:2028 ecl:amb

eyr:2027
pid:286247733 byr:2000 hgt:191cm
iyr:2014
hcl:#341e13 ecl:amb

ecl:gmt byr:2005 hgt:182cm pid:376332625 hcl:z iyr:2021
eyr:1949

hgt:184cm
byr:1940
cid:260 eyr:2030 ecl:brn
iyr:2011 pid:792881807

iyr:1936 eyr:2021 cid:133 hcl:#623a2f byr:2003 pid:197167496
ecl:#8896de

hgt:67in cid:110
byr:1951
pid:389358116 eyr:2028 iyr:2017
ecl:grn

hgt:161cm
cid:215
pid:116325531 iyr:2019
eyr:2025 hcl:#18171d ecl:blu
byr:1951

pid:787859682 hcl:#a97842 eyr:2020 byr:1948 hgt:190cm ecl:brn iyr:2020

pid:034440951 hgt:73cm hcl:803e55
cid:350 byr:1985
ecl:#a18487 eyr:2031
iyr:1973

hcl:#40ee86 ecl:brn
iyr:2016 byr:1922 hgt:150cm pid:449374426

eyr:2040 hcl:260be4 pid:208681353 byr:2029 ecl:gry
hgt:178cm

hcl:#18171d hgt:162cm byr:1983 eyr:2020 pid:328556776 iyr:2017 ecl:grn

eyr:2029
hcl:#a97842
pid:#7bd019 iyr:2015
hgt:168cm byr:1926
ecl:grn

ecl:grt eyr:2034 pid:640680934 hgt:189in cid:276 byr:1969 hcl:511eed iyr:2023

eyr:2039 hgt:182in cid:145
hcl:4a259b iyr:2026
byr:2004
ecl:xry pid:#a3c9ea

hcl:#866857
pid:615665716 ecl:blu hgt:164cm iyr:2020
byr:1948 eyr:2024 cid:286

hcl:#b6652a hgt:59in eyr:2027
pid:752461325 ecl:oth
byr:1932 iyr:2019

eyr:2030 byr:1936 ecl:hzl
iyr:2010 cid:263 pid:186570962 hcl:#888785
hgt:163cm

byr:1949 ecl:blu
pid:407719342
eyr:2030
hcl:#b6652a iyr:2012
hgt:186cm

pid:154cm ecl:amb byr:1944
eyr:2022
hcl:z iyr:2017

byr:1980 hcl:#d2c954 iyr:2013 ecl:brn hgt:72in
eyr:2030
pid:017095362

hgt:179cm
hcl:#ceb3a1 cid:61 eyr:2026
iyr:2011
pid:897403026 byr:1984
ecl:amb

cid:150 hgt:181cm
eyr:2028 pid:894689339
hcl:#602927 byr:1933 ecl:grn iyr:2018

pid:125553946 byr:1942 eyr:2026 hgt:193cm
iyr:2010 ecl:gry
hcl:z

eyr:2013 pid:1213613355
ecl:#b08dca hgt:190in
hcl:06adb3 cid:303 iyr:2010

iyr:2019 pid:255938897
eyr:2022 hgt:152cm
byr:1956 ecl:grn hcl:#ceb3a1

eyr:2029
pid:670713784
iyr:2020 ecl:grn
hgt:155cm hcl:#6b5442 byr:2002

byr:1925 hcl:#866857 pid:323449427 ecl:oth
eyr:2023 hgt:163cm iyr:2014

pid:841608722 byr:1955 hgt:150cm ecl:blu eyr:2029
hcl:#6b5442

eyr:2023 hcl:#efcc98
hgt:164cm ecl:gry
iyr:2018
byr:1993 pid:501920795

eyr:2030
iyr:2019 hgt:73in hcl:#bf908a
byr:1961 ecl:blu cid:86 pid:436811356

pid:#02516a hgt:131 iyr:1969 ecl:grt byr:2015
eyr:2010 hcl:z

ecl:#25fb6c cid:239 pid:167cm iyr:2021
byr:2023 hgt:75cm
hcl:z eyr:1931

pid:279251948
ecl:oth hcl:#6b5442
byr:1943 iyr:2015 hgt:173cm eyr:2039

byr:1935
iyr:2013 hgt:151cm hcl:#b6652a
ecl:grn
eyr:2023 pid:741958450

hcl:6beab7 byr:1986
hgt:85
iyr:2012 pid:#d98df3 eyr:2035
ecl:dne

byr:1929
pid:764478810 ecl:grn
hcl:#866857 iyr:2019 hgt:155cm eyr:2022 cid:277

hgt:155cm pid:450816410 eyr:2030 cid:165 byr:1969 ecl:blu hcl:#866857 iyr:2019

cid:330 pid:168777528 eyr:2024 ecl:blu hcl:#341e13
hgt:178cm iyr:2013
byr:1921

eyr:2037 iyr:1973 hcl:a4ebf3
pid:161cm
ecl:oth hgt:64cm cid:62

cid:235
hcl:538f8a hgt:70cm
iyr:1970 pid:177837127
ecl:#95700d byr:2003

ecl:hzl pid:375018246 hgt:161cm
iyr:2011 eyr:2029 hcl:#c0946f
byr:1956

hcl:#888785
iyr:2016
pid:161cm byr:1977 ecl:#0188d8 eyr:2029
cid:104 hgt:63in

byr:1979 eyr:2020 hcl:#ceb3a1 ecl:amb pid:752141341 hgt:150cm iyr:2010

cid:274 byr:1928 iyr:2018 eyr:2023 hcl:#a97842 hgt:173cm pid:186060112 ecl:gry

hcl:#341e13
ecl:blu iyr:2011
hgt:190cm cid:292 pid:974271891 eyr:2020 byr:1927

hcl:#fffffd eyr:2025
ecl:brn byr:1923 iyr:2011
pid:037981552

ecl:blu pid:412817852 hgt:150cm iyr:2026
byr:2026
eyr:2020

ecl:brn byr:1988 eyr:2026
hgt:178cm pid:008152501
hcl:#602927
iyr:2020

ecl:brn pid:877401308 byr:1923 cid:154
hgt:170cm
hcl:#fffffd
iyr:2014
eyr:2022

cid:56 hcl:ee020e pid:590581021 iyr:2018 hgt:72cm byr:2007
eyr:1964 ecl:oth

eyr:2029
iyr:2012 ecl:oth
hgt:185cm cid:235
byr:2002
pid:064901580

byr:1956 hcl:#6c1a8c pid:497814257
eyr:1964 hgt:155cm ecl:gmt iyr:2030

byr:1935 hgt:171cm cid:253 pid:033393224 hcl:#c0946f iyr:2012
ecl:blu eyr:2025

byr:1977 hcl:#602927 cid:175 iyr:2010
pid:9391986394 hgt:65in eyr:2026
ecl:amb

iyr:2011 hgt:158cm ecl:#31cae1 byr:1958 hcl:b94ad1
eyr:2023 pid:#400a21

hcl:e205b0 pid:84195182 byr:2012 eyr:2037 ecl:zzz hgt:75cm iyr:2030

pid:102379515
byr:1971
hgt:169cm
ecl:amb
eyr:2020 hcl:#cfa07d iyr:2017

pid:236611157
eyr:2020 hcl:#b6652a
iyr:2017 cid:194 byr:2001 hgt:169cm ecl:gry

iyr:2012 hcl:a256b5 eyr:2040 cid:62 hgt:177in byr:2010

eyr:2028 byr:2009 iyr:2020 ecl:brn
pid:12371575 hcl:#866857 hgt:190cm

byr:1965 eyr:2028
pid:402013776 hcl:#bc4e9e cid:183 hgt:150cm iyr:2015

pid:0269051559
byr:1936 hcl:z ecl:#ff0ab9
iyr:2014 eyr:2031
cid:346 hgt:153in

hcl:#18171d iyr:1929 hgt:157cm
eyr:2036 byr:1970
ecl:amb

hcl:#733820
eyr:2022
pid:096076686
iyr:2010
hgt:192cm
byr:1957

hcl:#ceb3a1 ecl:brn iyr:2013
eyr:2025
byr:1953 pid:751516675
hgt:175cm

byr:1928
eyr:2027
cid:85
hgt:179cm ecl:oth
pid:169307999 hcl:#3e07af iyr:2010

hgt:60cm byr:2008 hcl:z
eyr:1965 pid:167cm
cid:106
iyr:1930

hcl:#1099d9 ecl:amb pid:638820661 iyr:2014
byr:1998 eyr:2025
hgt:162cm

ecl:amb
eyr:2022 hcl:#623a2f byr:1956
hgt:154cm
iyr:2010 pid:717452826

hcl:fc9ba5
iyr:1928
eyr:2029 pid:54503219
byr:2020
ecl:#d2155a hgt:124

eyr:2027
hcl:#7d3b0c hgt:178 ecl:#63b8e6 iyr:2015 byr:1954

ecl:oth byr:1970
pid:833178609 hcl:#c0946f iyr:2016 cid:81 eyr:1976
hgt:69in

hcl:#0cf4b8 pid:499271062 hgt:62in ecl:hzl iyr:2016 byr:1922
eyr:2022

byr:1994
eyr:2029 hgt:174cm hcl:#efcc98
ecl:amb
iyr:2019 pid:297210449

ecl:hzl
eyr:2026 iyr:2017 hcl:#a97842 hgt:162cm
byr:1950

pid:091886000 hgt:179cm byr:1975 eyr:2020 cid:326
ecl:oth
iyr:2015 hcl:#a97842

hcl:#efcc98 hgt:176cm byr:1940 iyr:2016 ecl:brn pid:514758507 eyr:2024 cid:313

eyr:2026 byr:1980
hgt:155cm
iyr:2013 pid:367909831 ecl:oth

byr:1965
eyr:2021 iyr:2017
hgt:185cm
hcl:#a97842 ecl:hzl pid:238901177

hgt:156cm pid:916654189
byr:1943 eyr:2022 ecl:amb hcl:#341e13 iyr:2016

cid:305 iyr:2013
eyr:2029 hgt:163cm ecl:blu
hcl:#fffffd pid:944033881
byr:1952

pid:638190538
hcl:#866857 ecl:brn
eyr:2030 iyr:2016 cid:78 byr:1943 hgt:186cm

eyr:2024 iyr:2015
pid:231006970
cid:312 byr:2000 hcl:#623a2f hgt:190cm ecl:brn

ecl:#f89e87
hcl:#fffffd hgt:166 cid:215
iyr:1961
eyr:2027 pid:314310197 byr:1977

hcl:z eyr:1995 pid:951911095 hgt:154cm
ecl:xry
cid:154 byr:2023

hgt:66in hcl:#866857
ecl:brn
pid:328148585 byr:1984 eyr:2024

pid:456453839
eyr:2024 hcl:#fffffd byr:1990 ecl:amb

eyr:2030 cid:149 pid:983735096 hgt:179cm iyr:2014 byr:1957 ecl:gry hcl:#341e13

byr:2001 hgt:157cm
ecl:hzl eyr:2021
hcl:#ceb3a1
pid:558527031 iyr:2018

hgt:122 ecl:oth hcl:z
pid:384664729
iyr:2012 cid:298 eyr:2023

ecl:utc eyr:2024
hgt:162in iyr:2018 pid:1722490341 byr:2027
hcl:#18171d

ecl:gry iyr:2017 hcl:#602927 cid:303 byr:1950
pid:509264482 eyr:2030
hgt:164cm

hgt:192cm pid:967128169 iyr:2019 ecl:blu eyr:2024 hcl:#fffffd byr:1949 cid:301

ecl:blu
cid:71 hgt:164cm eyr:2022 hcl:#cfa07d pid:750303088
byr:1949 iyr:2014

iyr:2014
pid:401425898 byr:1981
hcl:#7d3b0c hgt:167cm eyr:2028

hcl:#602927 hgt:160cm iyr:2014
eyr:2023 byr:1940 pid:748539736 ecl:amb

eyr:2025
hcl:#c0946f pid:325296854 iyr:2020
hgt:76cm ecl:amb byr:1921

hgt:190cm
iyr:2011 pid:082777116
byr:1979 cid:73 ecl:oth hcl:#6b5442 eyr:2021

eyr:2029 ecl:amb hgt:151cm pid:144881592 byr:1964 hcl:#efcc98 iyr:2012

hcl:#efcc98
iyr:2019
eyr:2023 byr:1999 pid:645291123
ecl:brn

eyr:2029 pid:922956941 hcl:#623a2f byr:1934
ecl:grn hgt:151cm
iyr:2019

byr:1992 ecl:brn
hcl:#a97842
pid:269079906 hgt:187cm
iyr:2016 cid:218

byr:1951 ecl:oth eyr:2026 hgt:185cm
cid:82 hcl:#7d3b0c
iyr:2020 pid:052476816

eyr:2026
cid:319 iyr:2020
ecl:brn hcl:#888785
hgt:172cm pid:327064207 byr:1956

hgt:178cm
pid:638854420 byr:1995 eyr:2030 ecl:gry hcl:#7d3b0c iyr:2018

iyr:2026 hcl:#b6652a
byr:1946
hgt:186in pid:622875187 eyr:2028 ecl:gry cid:140

byr:1931 ecl:oth eyr:2030
pid:437813485
hgt:181cm
hcl:#efcc98 iyr:2018

byr:1999
ecl:amb
hgt:160cm iyr:2013 hcl:#b6652a pid:043039693
eyr:2022

byr:2025
pid:#fd7ad7 eyr:2025 hgt:63in
ecl:oth iyr:2010 hcl:#b6652a

ecl:grn
byr:1939 eyr:2025 hgt:171cm cid:134 iyr:2020 pid:090346629
hcl:#cfa07d

hcl:z
eyr:2031 cid:74
pid:50216290 ecl:utc iyr:2030
hgt:176in

byr:1971 ecl:brn hgt:190cm pid:791682756 hcl:#fffffd
iyr:2020 eyr:2027

iyr:1931 byr:2025 hgt:76cm pid:735796617 eyr:2040 ecl:utc hcl:#c0946f

hgt:163cm
hcl:#18171d
ecl:hzl
pid:628854394 cid:311 iyr:2020 eyr:2027

hcl:z
ecl:amb pid:#a8f973 hgt:94
eyr:2027 byr:2020 iyr:2012 cid:202

pid:086190379 byr:1931 ecl:blu iyr:2010 eyr:2027 hgt:175cm

ecl:#0dafcd byr:2025 iyr:2021 eyr:1970 hgt:63cm cid:260 hcl:75300a pid:208921120

pid:024722981 iyr:2011 hgt:193cm hcl:#efcc98 ecl:blu byr:2001

byr:2027
cid:123
ecl:xry hgt:183cm iyr:2019 eyr:2026
hcl:#c0946f
pid:380513483

eyr:2028 pid:302044900 iyr:2011 byr:1938 hgt:190cm ecl:amb hcl:#c0946f

eyr:2024 pid:672033747 byr:1931
iyr:2020 hcl:#f01aed ecl:brn

hgt:184cm hcl:#efcc98 pid:391597648
iyr:2020 ecl:gry
byr:1961

iyr:2013 hgt:191cm byr:1935 eyr:2028 hcl:#ceb3a1 cid:195 ecl:brn

eyr:2025 pid:322775528 hgt:155cm hcl:#efcc98 iyr:2015 byr:1996 ecl:oth

byr:1960
hgt:183cm pid:764315947 eyr:2030
hcl:#ceb3a1 ecl:brn

eyr:2029 hgt:168cm byr:1929 pid:800222003 ecl:gry hcl:#8f8aaa
iyr:2011

hcl:#623a2f ecl:hzl hgt:168cm pid:795434985 eyr:2020 iyr:2020 cid:209
byr:1970

cid:325
byr:2007 eyr:1933 hgt:188in
pid:713080083 ecl:#d624ca iyr:2030 hcl:z

hcl:#7d3b0c pid:431742871
ecl:hzl hgt:169cm cid:340
eyr:2023
iyr:2017 byr:1994''''''
list_of_details = passport_details.split("\n\n")
list_of_details2 = [i.replace("\n", " ") for i in list_of_details]
list_of_details3 = [string.split() for string in list_of_details2]
def dictionary_form(s):
    di = {}

    for i in s:
        j = i.split(":")
        x = j[0]
        y = j[1]
        di[x] = y
    return di
list_of_details4 = [dictionary_form(p) for p in list_of_details3]

def is_valid_passport(passport):
    return "ecl" in passport and "pid" in passport and "eyr" in passport and "hcl" in passport and "byr" in passport and "iyr" in passport and "hgt" in passport

valid_passports = [passports for passports in list_of_details4 if is_valid_passport(passports)]
print(len(valid_passports))'''
'''
# day 4:2
def is_valid_passport2(passport):
    has_valid_birth_year = 1920 <= int(passport["byr"]) <= 2002
    has_valid_issue_year = 2010 <= int(passport["iyr"]) <= 2020
    has_valid_expiration_year = 2020 <= int(passport["eyr"]) <= 2030

    has_valid_height = False
    height_units = passport["hgt"][-2:]
    if height_units == "cm":
        height = int(passport["hgt"][:-2])
        has_valid_height = 150 <= height <= 193
    elif height_units == "in":
        height = int(passport["hgt"][:-2])
        has_valid_height = 59 <= height <= 76

    def is_valid_hex_string(string):
        test_value = string.lower()
        is_valid = True

        for character in string:
            if character not in "0123456789abcdef":
                is_valid = False
                break

        return is_valid

    has_valid_hair_color = False
    if len(passport["hcl"]) == 7:
        digits = passport["hcl"][1:]
        has_valid_hair_color = is_valid_hex_string(digits)

    has_valid_eye_color = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def is_valid_passport_id(value):
        is_valid = False

        if len(value) == 9:
            is_valid = True

            for character in value:
                if character not in "0123456789":
                    is_valid = False
                    break

        return is_valid

    has_valid_passport_id = is_valid_passport_id(passport["pid"])

    return (
            has_valid_birth_year and
            has_valid_issue_year and
            has_valid_expiration_year and
            has_valid_height and
            has_valid_hair_color and
            has_valid_eye_color and
            has_valid_passport_id
    )

truly_valid_passports = [passport for passport in valid_passports if is_valid_passport2(passport)]
print(len(truly_valid_passports))

'''

# day 5

'''
# day 5:1
string_of_passes =''' '''BBFFFBFRLL
FBBBBBFLRL
FBBFBBBLRR
FFBBFFBLLR
FFBBFFFRLL
BBFBBFFLRL
BBFFBBBRLR
BFFBFBFLRL
FBFFFBBRLL
FFFBFBBRLL
BBFBBFFRRR
FBFFBFFRRR
FFBBBFBLLL
BBFBFBFRLL
BBFBFBBLLL
BFFBBBFRLL
BFBBFFBRLR
FFBBFFFLRL
BFBFFBBLLR
BFFFFFBLLL
FBBFFFFLLR
BBFBFBBRLL
BFBBBFBRRR
BFFBBBBRLL
BFBBBFFRRR
FFBFFBBRRR
BFFFBBFLRL
FFBFFFBRRL
FFBFBBFLRR
FFBBBBFLRL
BFFFBFFLLL
FBFBBBFRLR
BFBFBBFRLR
FBBFBFBLRL
BBFFBFBRRR
FBBBFBFRLR
BBFBBBBRLL
FFBBFFBRRL
FBFFFBBLRR
FBFFBBFRRR
FBFBBFFRLL
FBFBBBBRLL
FBBFBFFRRL
BBFBBFFLLL
FBBBFFBLRL
FFBFFBFLRL
BBFBFFBLLR
BBFFBBFRRR
FFBFBFBLLL
FBBBBFBLRR
BFFFBBBLRR
BFFBBFBLLL
FBFFBBFLRR
BFBBBBFLRL
BBFFFFBLLL
BFFFBBBRRR
FBFFFFFLLL
FBFBBFFLRR
FFBFBFBRRL
FBFBBFFLLL
FBFFBFBRLL
FBFFBFBLLR
BFFBFFFLRL
FFFBBBBLRR
BFFFFBBRLL
BFFFFFFRLL
BFBBFFFLLR
BFFFFBFRLL
BFFBFFBRRL
FBBFBBBRRR
FFBBFBFRRR
BBFBBFFLLR
FBFBFBFLRR
BFBFBFBRLR
FBBFFBFRRR
BBFBFFBRLR
BBFBBBFRLR
FFBFBBBRRL
BFBFBBBLLL
FBBBFBFRRL
FFBBFBFRLL
FFBFBBFRLR
FBBFBBFRLL
FFBFBFFLRL
FFBFFFFLLR
FFFBBFBLLL
BBFBBFBLRL
FBBFBBFLRR
FFFBBBBRLL
BBFBFBBLRR
FFFBBFBLRL
FBBFBFFLLR
FFBBFFBLRL
BBFBFFFRLL
FBBBFFFRRL
FBFFBFFLRR
FBBBBBFRRL
BFFFBFBLLL
FBFBBFFLRL
FBBFBBBRRL
BFBBBFBLRL
BFBBFBBRRR
FBBBBBBLRR
FFBFFBBLRL
FBBFFBBRLR
FBBBFBFLLR
BBFFBBFLLR
BBFBBFFRLL
FFBFFBFLLR
FBFBFFBRRL
FFBBBFFRLR
BFBBFFBLLR
BFFBBBBLLR
BBFBFBFLLL
BFFBBFFRRL
FFFBBBFRLR
FFBBBFBRLR
BFBFFBBRLL
FFBFBFBRLL
FBFFFFFLLR
FBBBFBBLRR
FBBBFBBLLL
BFFBBBFRRR
BFBFBFFLLR
FBBBBFBRLR
BFBBFFFRRR
BFBBBFFRRL
FFFBFBFLRL
FBBBBFFRRL
FBBBBBFLRR
BFFFBBFRRR
FBFBFFBLLR
FBFBFBFRLR
FFBBFFFRLR
FBFBBFBLRL
BBFBFFBRRL
FFBFBBFRLL
FBBFFBFLLR
FBBBBFBRRL
BFBBBBBRRL
BBFFFFFLRR
BBFFBBBLRL
BFFFFBBLRR
FBBFBFFLLL
FFFBBFBLLR
FBBBFFBLLL
BFFFBFBRRR
FFBFFFBRLR
BBFFBFFLRR
BBFFBFBRLL
FFBFBBBLRL
FBFBFBBRRR
BFBBFBFLLL
FFFBBBFLRR
BBFFBFBRRL
BFFFFFFLRL
BBFBFBBRRL
BBFBFFFLLR
FBBFFFBRRR
FFBBBBFRRR
FFBBFBBLLL
BFFBFFBRLL
BBFBFFFLRR
FBFBBFBLLR
FFBFBFBRRR
BBFFBFBLLL
FBBBBFFLRL
FBFBFFFLRR
BBFBBFBLRR
BFBBBFBLLL
FBFBFFFRRL
BBFFBBFRLL
BFFFFBFLRR
FBBBFBBRRR
BFFBFBFRLR
FBBFBFBLLR
FFBFFBBLLR
BFFFFBBLLL
FFFBBBFRLL
FBFFFFFRRL
BFFFBBFLRR
BFBFBBBLLR
BBFFBFFRRR
FBFBBBFRRL
FBFBBBBRLR
FBBBBFBLLR
BBFFFFBLRR
BFBFBFBLRR
BFBFBFFLLL
FFBFBFFRLL
FFBFFFFRRR
FBBBBFBLRL
FBBBBBBLRL
BFFBFBBRLR
FFFBFBFLLL
FFBBFBFLRR
BBFFFBBLLL
FBBFBFFRLL
BFBFFBFLRL
FBFBBBBLLL
BFFBBBFLRL
BBFFBBFRLR
FBFBFFFLLR
BFBFFFFRLL
BBFFBFFLRL
BFBFFFFLLR
FFBBBBBRRL
BFFFFFFLLL
BFFBFFBLRR
FFBFFFBLRL
FFBBFBBRLL
FBFBBBFRLL
FBBBFFFRRR
BFFBFFFLLR
FBFBFBFLRL
BBFFBFBRLR
BFBFFBBRRL
BFFBBBBRLR
BFBFBFBLRL
FFBFBFFLLR
FFFBBFBRLL
BFBBFFFRLR
BFBBFFBLRR
FFFBBBBRRL
FBBFBFFRLR
BFBBFBFLRL
FBFBFBFRLL
FBBFFFFRRR
BBFFFBFRLR
FFBBBFBRLL
FFBFBFFRLR
BFFFFFBRRR
FBBBBFBRLL
FBFFBFBLRR
FBBBBBBRRL
FBFBBBFRRR
FFBFBBBRLR
FBBBBBFLLL
BFFBFBFRRR
BFFBFFFLRR
BFFBFFBRRR
BFBFBFBRLL
BBFFBFFRLR
BFFFFBFRRL
FBFFBBFLLL
FBFBFFBRLR
BBFBFFBLLL
BBFBFBBLRL
BBFFBBBLLR
BBFBFFFLRL
FBFFFBFRRR
BBFFBBBRLL
BBFFFBFLRL
FBFFBFBRRL
BFFFFFFRRR
FBFFFFBRLR
BFBBBBBLRL
FBBFFFBLRR
BFFBFBFLLR
FBBFFBFLRR
BFFBBFBRRR
BFBBFFFLRL
FFBBBFBLRL
FFFBFBBLRL
BBFBFFFRRL
FFBFFFFRRL
BFBBBBBRLL
FBBFBFBLLL
FBBFBFFLRL
BFFBBFFRRR
BBFFFBBRRR
BFFFBFBLRL
BFFFFBBRRR
FBBFFFFRLR
BFBFBBBRLR
FBFBFBBRLR
FBBBFBBRLL
FFFBFBBRRL
BFBBBBBRLR
FFBFBBBRRR
BFFFFBFLLL
BFBFBFFRRR
BBFBBBFRRL
FFBFFFBLLR
BFBBBBFRRL
BBFFFBBLRR
FFBFBBBLLL
BFBBBFBRLR
FFBBFFBRRR
BFBFBBFLRR
BFBFFBFRRL
BBFFBFBLRR
BBFBBBBLRR
FFBBBFFRRL
FFFBBFFLRL
FFFBFBFRRR
BBFBBFBRRR
FFFBFBFRRL
BFBBFFBLLL
FBFBFFBLRL
FBBFBFFLRR
BBFBFFBRRR
FBFFBBBRRL
BFFBFFBLRL
FFFBBBFRRL
BFFFBFFLRR
FFBBBBFRRL
FFFBFBBLLR
BBFBFBFRRL
BFBFBFFLRL
FBFBBBFLRL
BFBBBBBLLR
FBFFFFFRLL
BFBFFBFRLR
BBFFBFBLRL
FBFFBFBRRR
BBFFFBFRRL
FBBFFFBLLL
BBFFFFBRLR
BFFBFBBRRL
FBFFFFBLRL
BBFFFFFRLL
BFFBFBBLRL
BBFFFFBLRL
BFFBBBBLRL
FBBFBFBRRL
BFFBFFFLLL
BFBFBBBRRR
FBBBBBBLLL
BFBBBFBRRL
FFBFFBBLLL
FFBBBBBRRR
BBFBBFBRLR
BFBBFFBLRL
FBFBBBBRRL
FFFBFBFLLR
BFFBBBBLLL
BFFFBBFRRL
FBBBFFBRRL
FFBFFBFLRR
FBFBFBBRRL
BBFFFBBLRL
FFBBFFBRLR
BFBFFBBRLR
BFBBFBBLRL
BFBBFFFRLL
BFFFFFBLRR
FFBBBBBLRR
FFFBBBBRRR
BBFBFFFRRR
FBFBBFBRRR
FBBFFFFLRL
FBFFBBBLRR
FBBBBFFRLR
FBBFFFFLRR
FBFFFFBLLR
FFBFBFFRRL
FFBBFFFLLR
BFFFFFFLRR
BBFFFFFRLR
FBFFFFBLLL
FBFBFFBRRR
FBBBBFFLRR
BFBBBBFRLL
BBFBFBFRLR
FFBFBBFRRR
FBFFFBBRLR
FFBFBFBLRL
FBBFFBFRLR
FFBBFBFLRL
FBBBBBBRRR
FFFBBFFRLL
BFFBFBFRRL
FBFFBBBRRR
FBFBFFBRLL
FFBFFFFLLL
FBFFBFFLRL
FFBBBFBLRR
FFFBBFFLRR
BBFFBFFLLR
FBFBBFBLLL
FFBBFBBRRL
BFFBBFFRLL
FFFBFBBRLR
BFFFFFFRRL
FBBBFBFLLL
FFBFBBFRRL
FBFBBFFRRL
BBFBFFFLLL
FBFFBBBLRL
BFBFFFBLLL
BFFBFFBRLR
BFFFBFFRLL
FFBFBBBRLL
FBBFBFBLRR
BBFBBFBRLL
FFBFBFFRRR
BBFFFFBRRL
BFFBBBBLRR
BFBFBFBRRL
BFFBBFBRLL
FBBFFBFRLL
FBFBBFFRLR
BFFBBBFLRR
BFFBBFBLRR
FFBFBFBLRR
FFBBBBFRLL
BFBFFBFLLL
FFFBBFFLLR
BFBFBFBRRR
BFFFBBBRRL
FFFBFFBRRR
FBFBBFBRRL
BBFBFBFRRR
BFFBFBFRLL
FBBBFFFRLR
FBBFFFBRLR
FBFBFBFLLR
BBFFBBFLLL
BFBBBFBRLL
FBFBBBBLRR
FBBFFBBLLL
BFFBBFBRLR
BFFFFFBRLR
FFFBBBBLRL
FFFBBFFRRR
BFFFFFBLRL
FBBBBFFLLR
BFBFFFBRLR
FBFBBFBLRR
FBBBFFFLLR
FBBBFFFLRL
BBFBBFFRLR
BFFBBFBRRL
BFBFBBBRLL
BBFBBFBLLL
BFBBFBFRRR
BBFFFBBRLL
FBBFBFBRLR
FFBBFFBLRR
FBFBBBBLLR
FBFFFBFRLL
FFFBBBBLLR
FBBFFFFRLL
BFFFFBFLLR
BBFBFBFLLR
FBBFFBBRLL
BFBBBBFRRR
FFFBBBFLRL
BFFFBBBLRL
FBBFFBFLRL
BFFBBBFRRL
FFBFFFBRRR
BFBFBBBRRL
FBFBFBBLRL
FFBBFFFLRR
FBBFBFBRLL
BBFBFBBRLR
BFBFFFBRLL
BFBFBBFLRL
BFBBFBBLRR
BFFFBBFRLL
BFFFFFFLLR
FFFBBFBRRR
FFBBFFBRLL
FBFFBFFLLL
BFFFBBBLLR
FBFFBBFRRL
FBBFBBBLLL
FBFBFBBRLL
FBBBFBFLRL
FFBFBBBLLR
FFBBBFBRRR
FFFBBFBLRR
FFBBFFFRRR
BFBBBBFLRR
FFBBBBBRLR
FBFBBFBRLR
FFBBBFFRLL
FBBFBFFRRR
FBFBFBFRRL
FBFFFFFRLR
FBBFFFBRLL
FBBFBBFRRR
BFBBBBBLLL
BFBFBFFRLR
FBFFFBBLRL
BBFFBBFLRR
FFBBFBFLLL
BFFFFBBLLR
FFBBFBBLRL
FBBBFFBLRR
BBFFFBFLRR
FFBFFFFLRL
FBFFBBFRLR
FBBFBBBRLR
FFBFFFFRLR
FBBBBBBRLR
BFFBFFBLLL
FBBBFBFLRR
BFBFFBBRRR
BFFFFFBLLR
BBFFFFBRLL
FBBFFBBRRR
FFFBBFBRLR
BFFBFFFRRR
BBFFBBFRRL
FFBBFBFRLR
BFFFBBBRLR
FFBFFBFRRL
FFBFFBBRRL
BFBFFFFLLL
BFBFFFBLRR
BBFFFBBLLR
BFBFBBBLRR
BFFBBFFLRL
FBFBFFFLRL
BBFFBFFRRL
FBBBBFBLLL
FFFBBBFLLR
BBFBBBBLLL
FFFBBFFRLR
BBFBFBBRRR
FFBBBBFRLR
BFFFBFBRLL
FFFBFBFRLR
BFBBBFFLLR
BFFBBBFLLL
BFFBBBBRRR
FBBBFFFLRR
FFBFBBFLRL
FFBBBBFLLL
FBFFFFBRRL
BFBFFBBLRR
BBFBBFFLRR
BFBBBBFRLR
BFFBFBFLRR
FFBBFBBLRR
BFBFBFFLRR
FFBBBFFLRL
FBFFBFFRLR
FFBBBFBRRL
FBBFFBBLLR
FFBBFBFLLR
FFBFFFFLRR
BFFBBFBLRL
BFBFFBFLLR
BFBFBBBLRL
FFBBFBBRRR
FFBFFBFRLR
FBBBFBBRLR
FFFBBBBLLL
BFFFBFFRLR
FBFFBBFLRL
FBBBBFFRRR
BBFBBBFLLL
BFFFFFBRLL
BFFBFFBLLR
BFFBBFFLLR
BFFBBFBLLR
FBFFFFBRLL
FBBFBBBLRL
BBFFFBBRLR
BBFBFFFRLR
FBFBFBFLLL
FBFFFFFLRR
FBFFBFBLLL
FBBFFFBRRL
FBFFFBFLLR
BFFFFBBRRL
BBFBBBFRRR
BBFFFFFRRL
BFBFFFBLRL
FBBFFBBRRL
FBFFFBFRRL
BFFFBFFLLR
FFBBFFFRRL
FFBFFFBLRR
BFFBFFFRLR
FFFBBFFLLL
BFFFBFBRRL
FFBBBFFRRR
BFBBBFBLLR
BFBBFBFLRR
FBFFFFBLRR
BFFFFBFRRR
BFBFFBFRLL
FBFFFFBRRR
BFBFBBFLLR
BFBBBFFLRL
BFBBFFBRRL
FBFFBBFLLR
BFBFFBFRRR
FFFBFBBLRR
FBBBBBFLLR
FBBFBBFLLL
BFFBFBBRRR
FBFFBFFRLL
BFFBBFFRLR
FFBFBFBLLR
FBFBFFFRRR
FBFFFBBLLL
BFBFFBFLRR
FFBFFBBLRR
FFBFBBFLLR
FFBBBBBLLL
BFFBBBBRRL
FFBBBFFLLR
FFBBBBBLLR
FBBBBBBLLR
FBFBFFBLRR
BFFBBFFLRR
FBBBFFFRLL
BFBFBBFLLL
FBFFFFFLRL
BFBBBFFRLL
FFBBBFFLRR
BBFFBBBLRR
BFBBFBFRLR
BBFFFFFRRR
BBFBFFBLRL
BFFFFBFRLR
FBFFBFFLLR
FFBBBBBRLL
BFFBFFFRLL
BFFBFBFLLL
BFFFBBBLLL
BFBFFFFRRR
BFFFFBBRLR
BFBBBBBLRR
BFBFFFBLLR
BFBBFBBLLL
FFBBFFFLLL
FBBBFBFRLL
FBBFBFBRRR
BFFFBFFRRL
BBFBBFBLLR
FFBFBFFLRR
BBFBBBFLRR
FBBFFBFRRL
BFFFBFFRRR
FFFBFBFLRR
FBBFFFFLLL
FBFFFFFRRR
FBFBFBBLLL
BBFFFBFRRR
BFFBFFFRRL
BFBFBBFRLL
FFBBBFFLLL
BBFFBBBRRR
BFBFFBBLLL
FFBFFBFLLL
FFFBBBFLLL
FBFFBBBLLR
BBFFBFBLLR
FBBBFBBLRL
FFBFFFBRLL
BBFBFBFLRL
BBFBFFBLRR
BBFFFFFLRL
BFBBBBFLLR
FBFFFBFRLR
FBBBBBBRLL
BFFFBFBRLR
BFBBFFBRLL
FFFBFBBLLL
FBFBBBFLLL
FBBBFBBRRL
FBFFFBFLLL
FBBBBBFRLL
BFFFFFFRLR
BFFFBBFLLL
FBBBBFFLLL
FFBFFBFRLL
FBFFBFBRLR
BFBBFBBRRL
BFFBFBBRLL
BFBBFBFRRL
FFBFFBFRRR
BBFBFFBRLL
BFFBBBFRLR
FBBFFFFRRL
FBFBBBFLLR
BBFFBBBRRL
BFBBFFFLRR
BFFBFBBLRR
FFFBBBFRRR
FBBBFFBRLL
BFBBFBFLLR
FFBBFBFRRL
BFBBFBFRLL
BFBBFBBRLL
FFBFFFFRLL
FBFFBFBLRL
FBFBFFFLLL
FBBFBBFRLR
BBFFFBFLLL
FBBBFFBLLR
BFFFBFFLRL
BFFFBFBLRR
BBFBBBBLRL
FBFFFBBRRR
BFFBFBBLLL
BFFFFBBLRL
FBFBBBFLRR
FFFBBFBRRL
BFBBBFFRLR
BBFFFBFLLR
FBBBBBFRRR
BFFFBFBLLR
BFBFBFBLLL
FBBBFFBRRR
FFBBBBFLRR
FBBFBBFRRL
FFBBFBBRLR
BBFBBBFLRL
BBFFFFBLLR
FFBFFBBRLL
BFBFFFFLRR
FBFFFBBLLR
FBBFFFBLRL
FBFBBBBRRR
FFBFFBBRLR
BFBBFBBLLR
FFBBFFBLLL
BBFBFBFLRR
BBFBBBFLLR
FBBBBFFRLL
FFFBBFFRRL
FFFBFBBRRR
BFBFFFFLRL
BFFBFBBLLR
FFFBFBFRLL
FBBBFBFRRR
BBFFFFFLLL
FBBBFBBLLR
FFBBBBBLRL
BBFFBFFRLL
FBBBFFFLLL
FBFFBBBRLL
FBBFFBBLRL
BFBFBFFRLL
FBFBFFFRLR
BBFFFFFLLR
BFFFBBFLLR
FFBFBBFLLL
FBFBBFFRRR
FFBBFBBLLR
BBFBFBBLLR
FFBFBFBRLR
FFBFBFFLLL
FBBFBBFLLR
BFBFBFBLLR
FBBFBBFLRL
BFBFBBFRRR
FBFBFFBLLL
BFBBBFBLRR
BFBFFFBRRR
FBFBFBBLRR
BFBBFFBRRR
FBFFFBFLRL
BFBBBFFLLL
FBFFBFFRRL
BFBFFFFRLR
BFBBBBFLLL
FBBFBBBRLL
BFBBBFFLRR
FBFBFBBLLR
FFFBBBBRLR
BFBFFFBRRL
BFBFBFFRRL
BBFBBBFRLL
FFBFFFBLLL
BFFFBBBRLL
BBFFBBFLRL
BBFBBBBLLR
FFBBBBFLLR
FBFFBBBRLR
FBFFBBBLLL
FBBFFFBLLR
FBBFBBBLLR
BFBBFBBRLR
BBFFBBBLLL
FBFBFBFRRR
BFFFFBFLRL
BBFBBFBRRL
BFBBFFFRRL
BFBFFFFRRL
BFBFFBBLRL
FBBBFFBRLR
FBBBBFBRRR
FFFBFFBRRL
BBFFFBBRRL
BBFFBFFLLL
FBFFFBBRRL
BBFFFFBRRR
BFBFBBFRRL
FBBFFBFLLL
FBFFFBFLRR
FBFBFFFRLL
FBFBBBBLRL
FBBFFBBLRR
BFFFBBFRLR
FBFBBFBRLL
BFFBBFFLLL
BFBBFFFLLL
BFBBBBBRRR
FFBBBFBLLR
BFFFFFBRRL
FFBFBBBLRR
BBFBBFFRRL
FBFBBFFLLR
FBFFBBFRLL
FBBBBBFRLR''''''
list_of_passes = string_of_passes.split("\n")
def seat_locator(instructions: str):
    instructions = list(instructions)
    lower_limit_row = 1
    upper_limit_row = 128
    lower_limit_column = 1
    upper_limit_column = 8
    for i in range(0, 7):
        if instructions[i] == "F":
            upper_limit_row -= (upper_limit_row - lower_limit_row + 1)/2
        elif instructions[i] == "B":
            lower_limit_row += (upper_limit_row - lower_limit_row + 1)/2
    for i in range(7, 10):
        if instructions[i] == "L":
            upper_limit_column -= (upper_limit_column - lower_limit_column + 1)/2
        elif instructions[i] == "R":
            lower_limit_column += (upper_limit_column - lower_limit_column + 1)/2
    return int((upper_limit_row-1)*8 + (upper_limit_column-1))
seat_IDs = []
for i in list_of_passes:
    seat_IDs.append(seat_locator(i))
print(max(seat_IDs))

# day 5:2
def seat_locator(instructions: str):
    instructions = list(instructions)
    lower_limit_row = 1
    upper_limit_row = 128
    lower_limit_column = 1
    upper_limit_column = 8
    for i in range(0, 7):
        if instructions[i] == "F":
            upper_limit_row -= (upper_limit_row - lower_limit_row + 1)/2
        elif instructions[i] == "B":
            lower_limit_row += (upper_limit_row - lower_limit_row + 1)/2
    for i in range(7, 10):
        if instructions[i] == "L":
            upper_limit_column -= (upper_limit_column - lower_limit_column + 1)/2
        elif instructions[i] == "R":
            lower_limit_column += (upper_limit_column - lower_limit_column + 1)/2
    return int((upper_limit_row-1)*8 + (upper_limit_column-1))
seat_IDs = []
for i in list_of_passes:
    seat_IDs.append(seat_locator(i))
seat_IDs.sort()
j = 0
k = 0
for i in range(seat_IDs[0], seat_IDs[-1] + 1):
    j += i
for i in seat_IDs:
    k += i
print(j - k)'''

# day 6
'''
# day 6:1
string_of_answers = ''''''xav
uavx
xavsi
yavx

efokjptizdcwmqnuh
qgfdvurtnjwpichxk
taqkcunfzpmydiwjsh

mzbg
tmg
rlvge
hgpbzn
cagkijyu

ahynbmqljzpwxokcfrtsgeud
xwzcmdhkrjnupegqlyoaft
fjnurhzoqmgwacxdlypkte
qwrjxahtlnzcfdouepmkgy
ezpqxfcmgrnhylukwajotd

jrxcnyadsgbtpvoze
secpytarvdzjgb
ycsfzgtedarbjvp
tsgejyzcdbvpra
ygtbvzredpacjs

n
n
s
n
n

mgfb
mfg

xfjengy
pubw
isroqb

hcnkeawlbfso
twocmsbefvlp
acwyseblorf
losebfcw

dixstroacjbygqpewvk
mdcpbnfqsgxvaikwujtr

u
uvk

vpuzogn
lmhxvfgkdnspq
jpvzogntyr
ajpngbcivw

bip
itb

uvqldphg
edpgfh

gm
mgfs
mg
mgq
gm

gtkm
wkcgmsvda
gmksap
mkupgt
gekrbimhj

hknejx
wjn
jano
jvwnb
ujnic

vkzmgdb
zbgvd
bzdgv
gbvdz
zdbvg

sedcuh
axyeqbs

ckysjbmawxpedqov
ilqcuxpvajwmfyko

xcv
xhevkc
vfxcy
wcvfx
cjxv

wetaojdqkip
kyedwuprqast
tadubqkflp
yanpslwqdtik
zmgacdpkxq

akdhyogxqf
ktnyzhxoaqfgwd

dbnezgquatrm
ewnqlzdjcgb
hnzdebjgql

aoxjcbpzisfmkewqlngduytv
difaqevcgyukztjwpmbsxonr

grptdzn
pzctgolskr

kvyjetqndhf
yetdvnqkf
svwdpxqgeianfk

tmyreouwn
torwnaeumy
tsewnmzypo
emosthywn
mjtkevnqcbdiwoxy

zstlfpnavdwyicuhb
twlpczyhunivda
ovnuwycptldhzai
pcyhdwtuianlvz

kwvaunqjryxtpz
wflvuzhnxmecokiyjts

kjcqzvhseaf
qgfmhsekjctv

tcpvqdrnghflmjoxawe
mdplxfqnovejsgazcrh
qxkhmvbpdoegnfjrlac

ixzcphskly
gsxioyzcahkl

stjxfn
cpdegihznsoyl
vrujnsk
wnsqmb
najbs

pxatigolezv
xkbvuitegwmo
gvijtmysxoe
svnxeqjogtik
soxevgqcit

otzmkhlquxwrani
eqdjfgmaor

exz
qze
ze
ze

xwzapvtqrgecjisfunkhd
qefspnwtkijacuhdgrz
zqjkasgnferutdwhcbpi
rwapenikhdjcsqfzgubt

fmjeqdaivksonr
pfeljvbqdsormxh
uywvtceosm

zhlao
he
h

qnyhtezxjdvpfkcsio
nvchtzepkqjoisdyfx
vifhcnxstzjpedoykq
qsivneohjzpbdcymlgxfkt
sxvkpohctnjfyqezid

ndzhflc
zfdcnh
fchznd

nrvde
ramndvu

tskgvzqmun
szckqgbvmnw
zvmsnrygaq
vcqmstinzg
jlospfehmzvndxgq

btlfvysaqerchkiux
tlyxhkrvbqufsecai
vfturxsbayicheqlk
sruhcbeqktixvfayl

vam
mv
vm
vm
vm

k
k
k
k
k

ysmikquxzc
yetmlxqsziu

ornk
orkn
rkno
koirn
onyrk

qcajzosf
sofdacj
ajoscf
djfscaeo
fosejac

rkqghbxjdol
uqbdhjkm
jhbd
cbtvadiehj
hfdbrj

nsklymutzivw
mounvbpwdg

sdpgvajmexuyqhcriok
vjksamihwpdrcxqguy
xjsevuydcamkihoqgpr
mjtcnqpgdhvuakfrbxyi

hpoyrxfmcjld
cxlpodryfmjh
jhplfcrydxmo

kembuivdhf
ipefszdh
enclshdbfk
dhreytjwxqgfao

lb
lkr

smtknclagp
pcktnslgam

bfsc
ynbf
hbxklwfep

ye
haybes
ey
eyw

ta
tan
jtap
tah
lcat

ikdqblgs
mtwlvhnbkjsdic
plzskbdi

rctauyzbdklxvpmnwqjfe
plhzdsnbmxqarwjktyfuice

ba
ab
ab
bar
ab

i
i
i
v

ursqy
qrwusy
yrsuq
qrsyu
qursy

cdgrouis
ocrigs

vjwaiph
ypva

yhuqbinztxg
kuqxeogthpid
gtmhiquxlw
gxutsafqbih

wmg
wz

gkpmdtwhnxzaoysjcevuir
hoxmkyqdcwlnvgperszi

oqagy
glxvkq
sdzbreguiwjfm

nabml
pfnyvatk

pu
pu

hbivy
byuv
tueovyb

ozqv
qzon

xjunwvbzdkqy
chfosmgre

dyn
ejxy
xydq
yx
iyp

hskfyqgtbzrvu
yvqhtgbuifrskz
hzjqfuyrbvstgk
zvkhtsfgryqbu

ons
osne
nous
suno

zymjefdwxih
dwxzyfjmieh

ib
bia

ocagmvj
jvcagm
gamcjv
vjcamg

inhlewtdbkxmpaqryg
wnkpxrhlmigtaydbqe
oihnlytpwaxrbqekdmg
mqabydwgterlphnkxi

bjedsywlgnxmpotz
pxejsongtkumzbwld
lpogxznbtwmsjed
tzpuonmjxlwbesgd

wqfsmektu
wmftqs
sqmtwf
tqmscfw
tqwmsf

snkpjbefqwhyriz
ikwrlqymjczfbevntps
qhebojfnzrkwapmsi
begirdpqnjkwuzsf
iqtbhfzpenwkrjs

y
y

gsf
gcsh
ajqgs

ulqbokwrjdcgpthniyxfzmeav
rjbumtoxecngkdvazsfilw

fwsrhjk
hjrfwks
kfjrhsw
jrhkfsw

qktgsvplh
hgol
hgly

qftenaodxkwz
bwtxaqviof

ugzpmhefkj
kgemzusfpjhd
ekfjlhpmguz
kxuepjgonfyhzq
kuzgitlhfjep

jywhzcrqa
otznge
mbuvfsk

iwhekorjgqtsdb
kjgswlbqherodti
okirgdnejtxwbqhs
ezobksgqrajhwdti

rdcoaubxhkitwsvpzygflmqnj
tcnfguzdybojqvwishrlapmkx
smjnpglbkzuafqhtdoxwiycrv
spgnmzlyurchxvwbojfqakidt
kzdtmbslqyvxcrwnauhoijgfp

kvwm
mwvk
kwvm
kvwm

hto
rhg
h
tvhi
vhfk

woxhpvfdlnezi
wemd
cqwkde
sedwuq
wcadtgrbe

moecds
wscmbnoed
sdycmeo

amnqlcytodvreiwkzgfxs
vfwmayqsghdcjztxeornkuil
xgaifqzdvowmknlysrtce
iynsxqwmafdvtklzregoc

ksvejm
eskmvj
ksmjve
vhskemj
ekmsvj

ebfkazr
dgqtkjmw
clykap
zukinrbh

oznuhklqijpmsxfcaryb
hyikolbjusmxqcfnzarp
uzxcbwqshkyamrielnopf

zlpsua
wlzdspu
luzsp

h
hkr
h
lhc
h

zfugqrjipavboys
aurvpzfeosigjqy
srnqiejtoyupgvadfzb
oqryvigjzsuafp
qgowivrzajsupfy

mrotnsaivyxbwp
iapmtxsgbyodwr
woaxsyjicpbtrfm

rdlakocwumetfpjs
cshjuyxwgatvz

wbxauycv
xbwgaove
axwnovb
fwyxmvab
xtiqwbsazvjpl

o
p
p
p
p

ombjurgkvceny
ilxtpwaz

gzjpkewnfylari
nlifyawpzgkjm

ymhesgwkxczrtbjnu
cywuetkbhnsxjrzgm
uwybxgsjnhremztkc

pcsxyiuvfnjbtkqwhlgzr
ixqnskyfwrtlgchbvjpzu
cvuqazjkhbxtlyrnwgifs

ce
ec
cge
ecg
yeh

itfhrlsvgden
svhekgidlrnf
nirlehsgfdv
sginfeldrhv
irsvdlfhegn

w
y

jqwevpgkzhdar
pazkvjqdrwh
urzhvwkpaqd

lsmqgjkb
glmksbjq
qsklgbjxm

iouyxrvbqjcemzlapk
ovlkizemjyarbcupx
zluckepmbrxivajyo
zijoveubxmlpykrcad

tjaruhsdgype
apmetysfkivjblqd

ztxyvufeh
dmcaqrhfgs

qfvujnhtaom
uvqanhfo

dxwvtmlsjqurepbgni
bueiqjanvlpwr
zlryojfupiqvec

dopjewaytmg
amreytdslkgpw
peymdawotxg
uqyahptdxzgecwm
vbohdafmpiwytge

zdkalgubsqw
dsazbkgluw
dsuzgwlbak

fibeyzxkmch
fveymznaik
vtyafiemkz
erlfizymuk

uti
u
gu
u
u

khqjtmswgl
pxnsqzgv

uhkeosrgytcpbvmanqdlwjfz
singwfcorvzadktblmupejqy
lezdusrpwbnfmkvjcxyogatq

nqlmhgrp
e
sw

hrmxwjzg
wzrtpmah
mrewhx
ywkbrnhmci
rhomuvw

cfpsboei
wtifcoybpx
iofcpb
cbpoisf
pcoibf

x
tx
x
xf

etvc
coap

gsbmanzopklyw
zorpislaqbnmywg
awbgczsdxlumypnoh
wtmkgobyaslnzjp
pmjlbsonkfwgtzay

upqwyiagtonfvrsk
dpkvuwoqfaiygsnmtxr
unorfgkpiyasqctzwvh
kbwpyrniohgufqsvat
pfqgsyuhnovktirwja

egkzlwjd
szermjwkl
kaelwjzoq

efmclagdkwhqxrosntzvib
mdhlqfabcrwsgxonizvkt
dhbqlnftivxwapoczskrgm

oxsedbl
zsblx
lrfax

tv
vta
vat
gpmosjtv

ltgeu
tudo
dtuoa
tud

ycsajei
sghikbpmr

bjfohqiwcpd
lzeysr

ghcenrzqksifd
ckwsgdnerfziq
iebsrncqmfk

idbjyxctlgpwas
wgiypblsacjuxd

ivnkjswb
bk
krb
kblc

hbmocfrual
urlfbmocha

mtvwqhag
wtxdcuen

bmdary
wjma
pexakfgu
bhijav
vlmcia

jeaposhgqcblxitkrzyn
aordjqiglcnpvekthsbzy
jhtrkqynszelcoiabpg
jkftnvbgyqploaicsehzr

q
qt
v
t
z

qidvuo
uohvqibd
udivqo
oivduq
vidqou

xjlbhrsnpat
qsavnktzbuldprxh
gxswnpftrehlymi
sahprlxnctz

axqni
aciqnx
xqian
axnrqi
qxnia

tbuicahr
banvchurti
grtbwaihclu

jylfirgmsx
lgfmxjri
xgmklqtfrwj
gxmlsfjr

ayunwcgj
gmcyn
gdtvfioexhys
bgyl
ngqyc

neyazrtkxjhbg
yxjzqknb

diljtqg
qwsnyuabx
qsfhuzv

qzpj
zjqp
qpgzthj
qfzlpjcydxsn

sbkrcjleytuidw
wcbtiljyedmsugk
zubetwdyikjcsl
lwbdieutjkcys

c
c
c
c
t

pdglkmircznxjshwytq
ikqrzgyxtdnjswmphcl
pgihtyjczwdlsqrkxnm

ysj
ysjf
fjsy
sjpy

c
ca
c

fjaounzyrck
uqzfontkrajy
auoyjknrzf

adgezcjtmlwbnkxsp
zlkjswmgabtcenpxd
wedpgjnmlzibkasxct
bkcfsemlqzujnxtgwadp

xrdzvqcyawst
vztcaqyr

p
pw
hpf

syzmig
lqpmnh

qwkysudhal
myk
tykc
ky
ykm

napugxj
pjnuxga
jxpaung
xgjnapu
jnpxaug

xcwklzsdouvejph
wvecjukzhpsnl
uzksblpwigjchv
szkwpncyudlvhfj

mazvxenotrbjpsg
xabenjzrgtmocpsv

amkxogyl
lkmyxgoa
yagkoxlm
awykgxlmo
gxayomkl

euqjn
eijrqnw
qnje
enjq
qejn

qmicpr
pc

mhfelurtibxzg
prcigefthzmbulx
behzitgmxflru
uxgrmzibtelhf
rzfluixbtmegh

trwq
t
zt

yjbcohw
jueqzodyk

tyroqsxepnbfckhuazjdwvmgli
byjcgxmurontvhspekwqildz
svtmwnbighlpxeyokjurzqcd
blprtoqjwnmyuxvdzkeisgch

mrwtb
trmbw
wtmrb
rmtewb
twmbr

jlwri
drwibj
tiwre

cz
cz
z
wusz
zeg

gxqrucimko
zhpqfvbinsy
iqlwdgtje

wyzjqgdihbxar
lwcivxtmaojgbzhp
xzuwgjrabkhfid
ihsaezxgqnybjw

jtair
kfsv
ghze

u
uj
u
u
u

epbvkzsoyqlrifatwch
tfzwlivkhsrbceoqpay
wzcqpotkrhfliavbyes
wvgeufcbopsqymritkalhz

vkaldbmyewi
rcxvlibuedgamy
lysiabjdkvme

nwhqcojkpgvfatderylibxz
hgnoiclkaebtpdfjvmzywx

gafbqnxstirzvoheydmlpwj
hqrukwtozblfyasdxvmnpgei

abpzed
dapzb
wcbdnzapj

uho
nmp

yofngr
amn
n
n
mn

zguhotqnvkepfyabr
okwtbzaqfyen
konyqtbzefa

inbtkepjylqdfxczmoauw
mzolcwaxfnbditkejpuqy
zjyoifdkmcaupenbtwxlq

yuzri
rubyi
yiur

otdbszvjhecrkiypn
ydmovicrbzfkeshqng

efc
e

orbzu
iszurwb
becjrkzup
irlznub
xbtragfdyqz

fpj
pfrd
fpr
fpwc

rklcfn
nflck

li
sli
ik
i
isv

awuhgmb
jznsiqycker

y
y
vmpdu
ok

jeionpfgkvxdmrzlyc
diblznsykpuxwqfm

mlykav
vmka
aqvrkdm
vkmiaz
rmkdvaq

uyljahgbxsvczpkdq
rowf
ntemi

xjhaitwlozdpcbv
dvnzjxblpcahoiwt
xbwdolatjhvczip

spohauibt
ipsatqnozlxvub

vuzf
fchz
zf

almqujgzovhyfkbwtindre
zvskmgitqyweoldjufranbh
jrkeqfanmvoiwblzdthguy

y
y
y
y
y

fsqxhnbtcdy
bhkqnvxdws
qsdnxihbm

c
cvip
wcqp
xrkjc

cbsfeonkqthadzimpwyg
wkybvhdsnaztcgefpqom
dipbljsqxfecakmtyoghnwz

ocxiztfw
djhaepyqu

pbyzfvq
rpqzvf

p
p
p
r

fgj
mghx
cguivrnzdw
xhmqlgf

lypf
fpyl
npylwaf
leupfy

rxyzatoj
xvfin
bxlfk
ucbqx
lx

rkixw
fk
mk
kmybf
vkqg

macdvsjophnzixyukwglqef
uhkdzsyecoixjpgqvanlfwtm
nszgjudxpfchoameiwrqylkv
hgkswmlvjyufeipaxnoczdq

hkvtprgxom
mxitpvkgdrho
mphkortnigv
kvtprlhmogd
kmverqtohgpwj

krsazmfbdtxyuijh
iebqjdruma
dimbrjua
imjurdab
ajrbuicdnvm

jzroas
vwo
om
kmvo
fo

vckphlabort
ktprcvabohl
tabrkohlcvp

lb
j
xi
p
i

ibxswpzlgak
pablwzkxs
kzablwpxs
xapzsbwkl

texidwzkyjcapn
djptyzcernia
narcjoiteqzdp
cetbjpzavigmnd

thxzfeocaqpkd
rvgoyxzlk
zkox
kxuzngo

dqsofevyrijctbxzwkghn
kjwvnobzergsihtdycqxf
robqyvzihwjsxcdfektgn
octvjeshdiwbyfngzqxkr

f
udzlmcrjehivqpx
agn
owb

vokdu
dck
knd
kd

txqlzrv
tvxlqzr
vxaqzrlt
tcxrzvql
qtzvxrl

flnc
lsk

agqspncoikwytuvre
muyijzoltcepsaxkdvhbgf

gmlyx
gakyvsl
cdthyjrioubq
myl
awezy

dfzvhkblgnj
kvzjdfgbnlh
hdknbjzfvlg
jkgvnzldfbh
jzkhfvgbnld

jvdkxqsrio
rpuqvkncfgzit

oqzmkjb
glehuw

stweunormcqdyivabxk
plgihfuzjbr

fiakobrucnqyjtxsvmw
utcfankbwvozqjxy
vqknowtacjbxyfgu
qboaxvykfcjtuwen

lqxfvjncarmowzst
sgpnhq
spnyueq
kqns

plis
i

alqp
dpml
ycntviwgf
zkeau
pkxo

cahvspxi

dgyk
kydg
gycdk
ygkd

ygxdtqsiralczwmfoke
fqeoltimdykzgwxrcas
mlrzsgafxqcidkweyot

ibpuxwfrnjygadl
ucbjmfziyklnrdxw
wbqrxjdihesvyunfl
zfubxtylwndjrpimo

ahdf
aq
awjyc
as
nah

klygiqmwhzubproas
dhetbmfiazsqrwclvugpk
ugnkxpmqirhswazlb

n
otzi
q
o
dkfx

gwoidjb
sqownkvt
oywgjxa
iwoeh

kcsfhg
gfksc
gcksf
pcgsfdk
hsckgf

lzgtrfpsxwqhi
yqzovtixp

mqyhlxgfnbtcvwejpsrdouzik
simkqtcevpohxdygbjlzrnfuw
dprugmhqkcwveixoyjbstznfl

m
m

akmrpwutnb
lnamrphkwtf
rpumnazwkft
kwrtmpvan
mjakwnsxrpt

kgstyrbauzjiqfmdl
rlpubyfadxmtijgswzcqk
bzsfnumiadjykeltgrq
qfavbdhujrglyzstkmi

zvxca
xazcv
avcxz
twxcavzk
vxzoca

kyjbqhd
yqg
mleagqy
qnlgy
rvqya

rkbfpejgaqunlhy
hogsunxedrlkbaj
ktzjmaugrnhblie
rbkgnajlehu
qelbwhuragjnk

pkbrlq
fhlvcetzujqo

dbpnjmfgzuaky
qrmnapvjswgyzfecl

oubx
uxb

k
t
ce

qo
oq

nrdoliybfmk
xbfonlytdi
odbyanilf
zdyinxfbrlmv
bnfgwdiyls

ptqr
yhpr
oifcxpumwares
rhbp
vrp

edmfbockpuzjl
mejpzldckfoub
bulkamoepdzjfc
wjblknodpmczufe
plbzukcxvdhefjmgo

sbfvdziayohutkxmcepnjgrwlq
slqbthaugnxcfejkymrpvdzwio

ovnuybcjzw
cubyavn

jlpyfemohwb
ympjolewhfb
hpjymbwolef
hmfewypjlbo
yjwlomhpfbe

yudoticgpmswxheb
imctpdhksgwavxbefuy
ytmhucixswdegkbp

femhgtsc
hgetcp
gct
schmgt
acogbzt

jdfzyhgnks
kfmgndbypsjz

qxkrsvfih
xvirkqfh
kxirvfqh
phvuixfqrmt

jwq
ovwjq
azpjnys
hjw
j

mekjycug
okyicj
jevq
dzsharjxltp

ageqsriyfoupknldjz
bqkjhmi

arqoszdiyemtlpbcukxhg
tskxzcqmelhorypiua
ikcwsfalhzymorqxpetnu

o
wj
o
o

hoqrjzemyfidak
hdofikzyrjqaem
amyjorkehdizqf
qyajdekzmfohir

rfgtpasbvquzykj
kwdcasjtyvzfuqegpib
tpangskbuorqyjfvz
qubhzfvakospgtyj
tjgvuayzfprksbq

xvsetimqaglzhubopjnkrw
vretjpaqgzidoulbmxhknsw
kxzwjmscaeulgqnpovihbrt
riwnepagmhktvusxqljobz
tugmqkbasnzhjivrlpwoxe

yawojch
aoyhjwc
wjcyoah
ocawyhj

atfkezomu
bwghcxijm
lmydqzvnpr

nfajymk
yakjmfo
skayfjm
ayjvkmfti

zbcgaxyjd
emltdhkwsug
dqgfnue
qgnvd

ibecm
ecmbtfislo
cxympeuib
iacrepxbm
ckibme

ednxkzblgoqwrys
naklxbrzsodqegwjyf

mabnelwrzy
keandpqxbmlo
gviuhjstf

xlzoysmpdgfcabiqetr
mplwsgnxcadzfhukvrqjeybo

l
l
l
p
l

zyjuwao
odfv
skqoc
omvrcqbh

fgpcjvmbxuiwtehnd
pcfsgtxbnkuihadm
cdgtfhbmxpuni

e
ea
p

ild
ld
ld
ld
lhd

hwelutk
wshulk

milbjvxorn
lbivoxrnjm
mjxivlrobn
ilxmovnjrb

inhcdkotgs
syndfwkghteico
gkhdiczostn

jgpmfyqskc
kgfyqpsmcj
pyfckjgmqs
gskpcqyjfm
pyqsjmcfgk

opbqxluhyvskn
xonskvbpuqhyl
vnijlhyqpxukgosdb

dzglxpfnt
nfptl
qynmuvrcp
zdnpk

ligcsyexbdoqt
educotylzjb
zuyockfnbhtedml
owlyuabectdf
ycdrabolte

hw
qr

utqdisoacyr
jgnbvzwmhekfxpl

s
i
i

ovbhcfp
oauvcpte
qowxkpnyjlvdismc
zvctogpfa

qtsmhpwz
qchasetf

ysmvb
byvsm

yjkvnlqcpgasibtex
ycjgqedpvnx
nuygpfzhvejqdxc
qwyjenxfvpzmcgu

tlribvnydjfex
rmpjdqsbzgcxv

hn
uhn
nh
hn
hnz

yvzrqpbel
blejaozvmypr
ebrlvfyzwp
brzpyelfv
zwbpyervlf

rtgnjiawecpmu
ejcnpgtawuirm

qhuybzmv
pnwzceb

cuijneskratyqgwxmodzhpl
wtqshpyzrcmokixgjbenf

wrthvasmxk
hvktmsarx

s
sp

td
rvjitl
tdpk
t

mgdaqpzefbxh
xfbmeadgzqcn
eragqjmlofxysdt

cvzxwpf
pxwuef
lxswpeft
wxpf

eqckjbluvodhtg
cvgujlhekoidtqb
bhdoltuvgkqjce
vhgjcektdbuloq
jdogqblchetukv

hmgwcszjqpyxil
wzplksghxcmyji
gkiczwmlyjxsh
jsgxcmzhlyviw
ujihlsyxgmdzcw

ofrubwjqkxpzaitevscmgyln
bigsuetvkorzqpajxwfldncm

qink
inrkq
knqi

jvnayiodwg
dos
tmhzeqdpo
hods
bohdklfu

i
i
i

ndwutoamyzbrpqsveg
zbdswnrevapmgty
zdtpnymegawsvrb

obwzklcynjgme
zlkeyfcgwmjn
icjzemnypwklgo
munwqycgzkelj
kcnzjsiylwpxgem

nbaeiqstvdwmhjukx
njxvowhqdfabieskmuzt
wbnsutjqdhgevkmixa
ycjswbkaqmvixlhutned

okcwymdgvfhlxzt
odygvtkmlwfxzch
wcmgjhdflxotzkyv
kaxyfglvwmodzcht
dxcafvltwokmyzgh

rejdmivax
xdamjver
ejvdxmar
rjmedxva
edrvajmx

lkqgnc
lnckg
lkgcsn
wklnhcg
lcgkn

upnosleiz
pnlszwe
esjpdnlrm
hnletqakgpsb

fb
f
f
frz

d
d
d
d
d

lyqavutgbwiehjrc
qcragbvihujlowtpy
tzyjhawliuvbqdrmgc
rglvzjtuidbcywqamh

edolzs
luoeshd

v
v
vg
v
v

scwuqekdbmarfiy
nzoxvptg

ycpvjeubrazgiodxtwn
cptzsxjmklyvdeaonbqiwr

kbmqslrvnyzpj
slxfnbqpjy
jsypwbnlq

xv
oxv
xv
vx

ulzdr
zoshulr
xduzr
zrqju
tzurvebgc

vp
v

n
fn
n
n

bmpfnxzsajwvyhqldrecout
rvnpsoxzlcmeufthkjayq
hozncuervmgqpyfatjxls
ovrxesptqajlzycfnmhu

lfjc
fc
fc
fc

jdhrx
jranxydbgt

y
y
y
y
y

tpfydje
ejpdfy
jyepdf
epjdyf

b
gphf
e
uvkc
jza

glyxuj
gjulxh

ubmeofqsxdangrchivy
yhcueqvgfasordxmb

vbtex
ubenvxzkt
txbvae

yoxb
byoex
obxky

vxhroygampneuzslckibfqdj
jqfcvnaizeluhkmrdxpy
eidxrkcnvjzhpqymaulf

dtlpjkfar
sjtprafdyel
afpgjtvlr

z
b

rwutpgkyanm
nwatgkmpuyr

jb
bj
jb
bj
jb

yvcbs
csvybh
bsvycu
csjrinybgpv
yhsvbocw

tapdxjkbuhn
uqoaigmtphcfv

gbrf
bgrf
grfb
brfg
rfbg

lhj
r

nsuvr
rntus
rnmdcsu
nusr
usnvr

mglncfrspjxqdheatkby
awokdbmlvurnzjecqsyxpth

dkphrovicb
oihkdcrvpb
kcdvhbipor
ichrbdpvok
prckhibvod

obaxmnut
otabun
haobdtun
pvfnztekujcbqyoa
tibmhoagun

mvhtqgsxc
ztljokabwni
tdyuefmqrp

gdx
jnxk
x

bwfpeojrtnqmszhya
jfduwroxmenzhky
mhfrjediyznwclokv
hfjirnwymekgzo

bzcpqi
ipcqbh
ciqpb

vbnegldq
ebgvq
equxgbv

pmcjwzqsrgye
svhujyprdftb
pjsnaryo
onsrpjy

dfqbynoxcgljpuhaesmvt
dxhecqampgnyultfjosvb
cifqxleudmvjhgaspybotn
snqvtgaphyfloxeucbdjm
ayetuxbogqcmfnsjvhpld

woqjbvaesrh
rmjaeswobqv
rqeswbjoav
owebqrvajs

fsgejt
jskg

obzeufrsykvjdqg
jqaiozpwrmbsdxkf
sjqdzfktbrlho

awqldosnzykc
dolsawqncz
wodsqznacl

ohtxrakybsecjnqviwduz
mwodbqsxihrajpcztygluknfve

m
mv
amq
m

ahoubdnlywcigjt
cynbhdivwtoglaju

bpgewx
zxpubsdwq

adhjekz
tzjkde
ewkvzjd
tvefjzdk
ejdkz

uetkosjndqgxcyvm
mclnrsaxjytqvdpg

kbhed
dix
afdt
d

xhd
hgrd

rbyavgzjflhdinqesk
snkvihbalfryjzeq
zhaivknreqfjsbly
brkljfziyensvaqh

bokdlygwhafrc
xwuronlpakqi

pnwsxh
pnrwsxh

yhrqpsbjv
dav
iwuoxlgfc

hwge
ihwejbsv
zneltwyrhfkaom
ewxjvh

oxnscztqjyafr
hyxnkjvwrufcm
pmcgrnulkfjvxy
berfkxyucijn
wencyxrfhlj

kilhnpjvdofbatcz
rhgvxiwmncfez
vizhucnqfe
cnhzivfu

umxzfpvkb
vpkxumbzf
xzkvmfbpu
uxkfzvmpb
pfxvbumzk

vmsdxahqipznu
fupiasyvlnxjzdrhq
unhagxpkvdsqzie

vdwyb
vyudwb
cdywvu
ydvw
vwjdayh

d
d
d

qlfcbhrvw
fzrbyuc

jcsonk
uckosn
kcsno

sawivom
ioas
aois

weluyo
qhcprdvg
sbkwuy
uzynje
najxiue

xbrfmeznhowj
tbycldqagk
uivcbs

uzgpwofxcaqidhntlmb
oidfhxgbnluzwmcptq
tquhizxngoacdwfpml
ldztycveqghipmxsnfowuj

n
qn

fqu
df

cxpvzgfyijsaoltueqkm
ajuxlvozygsfqpteicmk
ozeafkvtlqipjugyxsmc

z
c
z
r
z

jsapzgufkmwvdibqt
aerhpisyudxgmvwbjo
pvnudbctjgfwialms

auylqgmpcfbkihesz
zislkfqgapebch
fleshzgkqbaipc
hpnszqkiatefclbwg
esxlhdzvbfwkpagqci

j
x
x

vcypdnobl
kfabxw
wjqbig
ibzm
kb

hkodlmsgqbzjevcfayi
vfyticqwblkjsuagdpozme
ifdqbksjrxlegomhnczvya

bktgaefp
rexytwau

xwasezkctrov
pcsxbrzhdtw

gzkcdewab
lmd
xyftvqsidhur

kbvzwsdcn
pkbszvw

jsvouxke
qgzi
adrbyz

zvqpbkanyjwgtueflcdrx
cpyqrwgtjafuklzxndebv
wzdgljoaycekvbptuqxnfir
djrguhfbptyxkzceavnlwq

nhqgxmdsl
vtzpkmqdfl
uqomrjelw
zflbvqm
alxmq

smlxpqfh
tkszqhlvm
qjomlvks
qwduyrbsnlim

wpkcvmxuityzqgjdeofb
fvkyxbjdumoptiqwgecz
pbdvuetqczokmxfgywij
zifybkeudwvqgxjmcpot

porctbafwqzedgysxljkhv
jxbdhgqkftnyalsopzvwce
kozvgtxejlcpdhqsyfawb

obduynsxf
dysbxonuf
fbsoduxny
ubycdxnofs
bfysonxud

his
vfxa
xa
fax

yolm
bo

jotsmh
xfqhsbvrolc
hsgdaoz
jotyhsu
szoh

dz
dz
dz
zd
zdk

idykem
asftdpu

fbvmunwkreldcy
blaqkxzvyim
ilbvmxjkysq
laiymvoqhbgk
vpklbmyg

jvsmlog
jgwvmsplo

risldpqb
lbsiprxo
bsiprkl

nzcybwkpah
yhwcpkzna
wzhcnpayk

ixfbamn
inb
ubinke
ncbkei

elchnpjkxwtqig
nljgiceqahbx
lcugbexhqjin
idxjhmeqclgfnv
fqlhcexigndj

vmgcneztlbs
qeblzmvcngst
ngbclszmvet

ckn
c
c
c
c

yezpv
wyvlez

hfdtkslevcwnoxzi
tsfekmdjvclihzwno
etsiwvnzlkfdhoc
ckfotsdnzivhwle

e
y

cdbn
bcnd

hbupimtkawejgvfzcnoysx
zfnkwbpvchoxietmujsyg
jmehbtwivfznkupxcsgroy
gomuvnyjhwekscizbtxpf
hspzxkncvfitwjguymebo

qjw
j
rosg
jt
qjxe

s
js
s
s

sudlgxvitacpyfhkr
isuvgfkrchadnj
gvqfzrmdihucsak
qgrodskhauficv

rqefisluvyg
nyjotwizfk
iayf
yifd
ftyij

alxbdhwiscq
qgcjrwezay
ahwitmqdcu

d
d
yxl
d

zwfdsuqc
dzcw
cszudw
hzdlwb

axv
vx
vx
xv

nrw
blzfvgh

pe
elqmzvgfk
e

ygfk
xdjnublae
r

jvn
nvj
jvn
vjn

mblaqhitwdv
bljivaqxthdw

d
dc
d
d
d

e
d

vjsrl
jrlvqseb
vlsrj
lvrsj

cjfta
ajfct
tjcaf
fjbhatc

dqbfeprkzgvt
tpbfkdrqge
rwaqfedxkpbgt

owbmusnzvgpf
orgvlwkyxp
tvpwohg
wtgqcovp
gpavywoie

gczomkqlvdbn
aolduzmgbqvyec

tynrkjlgsq
qsnlytrkjg
yntgklrsqj
tygrlsnkqmj

pyfrutmwb
ubwnsrfy
yfwrspb
ydvborwf

qlsmcbh
hqlmcsgb

cowjnufayrix
rqaynwxfcoj
xogamefhkdjyrvwcnt
afrznwocyjx
cuirsyxfwloajn

htosau
bvkdcr

ewyzhgipl
lwezhbingydpk
hpzwmijeygl
ieythwpglzm

ozjphrbglsi
rguphzjoyil

b
o
ru

ritlagqevs
itslgaw
gvjsalitr
uixaolkghst

pnjoxwlurzkytdcb
jucwnytzoxbrpldk
lxpboczwtduykjrn
pyzkdnxoljvurwbct
rzupcbnxkwoytljd

snpvyotqzxubard
qorubpavdnxytzs
txpvazrqubnydos
vaotxpszyurbgnqd
pzxurabtqsvnoyd

wcybutsgnvxlpdjrmeko
ursvnedtgjbylckqwoxm

otac
cot
otc
toc

np
ndtfblp

uvaeirsy
vryjispm
smuiry
fzdbyqsrtig
rwkmycveis

jhutgyv
juyhtg
ytuhjg
hutgyj
tuhjyg

zxwyodcm
dwzyomc
wmdoczy
wxymojzdc
ylowdcmvbgz

tjefad
yokb

akbwzocshvu
kchubzawyvos
zbwukohvqasc
hzkbucowsav
zykvhoauwbsc

qsy
jq
pq

bnkryxpdvswjagzhfqtil
kgfawvzjinumhldqpytxrb

yfdr
yfrd
royfd
dryf

wsvptxyhcqfa
fysovtqwxchpa
vahfqtpsywxc
wfqaptcsvhyx

wezkdnqhgufvarycxijlobs
rzoicqxglbfhenksjwv
gwikzclbvrxsnjfoheq
hwexrfocgnjvqbzklsi

dm
yk

xyqbn
cxypns
hkgylf

mhqunico
mchio
hciwosm''''''
set_of_answers = [set(list(i)) for i in string_of_answers.split("\n\n")]
ans_6_1 = 0
for i in set_of_answers:
    j = "\n"
    i.discard(j)
    ans_6_1 += len(i)
print(ans_6_1)

# day 6:2
list_of_answers = [dict(collections.Counter(list(i.replace("\n", "")))) for i in string_of_answers.split("\n\n")]
people_in_group = [len(i.replace("\n", " ").split(" ")) for i in string_of_answers.split("\n\n")]
j = []
t = 0
for i in list_of_answers:
    f = 0
    for x in i:
        if i[x] == people_in_group[t]:
            f += 1
    j.append(f)
    t+=1
print(sum(j))
'''

# day 7
string_of_rules = '''bright olive bags contain 5 dotted white bags, 2 wavy lavender bags.
plaid brown bags contain 3 bright lime bags, 5 plaid coral bags.
dim coral bags contain 1 shiny maroon bag, 2 bright orange bags, 3 clear lavender bags.
dull olive bags contain 5 wavy purple bags, 2 plaid white bags, 4 vibrant magenta bags, 1 light brown bag.
dim yellow bags contain 1 bright cyan bag, 3 striped green bags, 5 dim white bags.
drab chartreuse bags contain 3 shiny lime bags, 2 bright indigo bags, 2 muted yellow bags, 5 dim tan bags.
dim cyan bags contain 4 drab tomato bags, 3 dotted teal bags, 1 posh purple bag, 2 faded brown bags.
striped indigo bags contain 2 wavy brown bags.
dull coral bags contain 5 mirrored salmon bags.
light violet bags contain 3 light maroon bags, 3 plaid purple bags, 1 pale lime bag, 2 pale orange bags.
clear magenta bags contain 3 muted tan bags, 3 clear lime bags, 3 bright magenta bags, 3 faded purple bags.
drab turquoise bags contain 1 dark violet bag.
dim black bags contain 4 vibrant turquoise bags.
dotted gray bags contain 1 posh salmon bag, 5 drab lime bags, 1 clear coral bag, 1 faded lime bag.
light lime bags contain 5 wavy lavender bags, 3 shiny black bags.
bright yellow bags contain 3 dotted beige bags, 4 clear purple bags, 4 faded salmon bags, 5 drab black bags.
shiny teal bags contain 3 dotted chartreuse bags, 1 wavy yellow bag, 3 clear lavender bags.
shiny crimson bags contain 2 light plum bags, 3 shiny black bags.
shiny lime bags contain 1 dim turquoise bag, 4 pale fuchsia bags.
pale lavender bags contain 3 bright lavender bags, 5 wavy blue bags.
shiny purple bags contain no other bags.
clear lime bags contain 2 drab bronze bags.
vibrant lavender bags contain 2 plaid crimson bags, 3 plaid yellow bags.
clear gray bags contain 4 shiny indigo bags, 1 vibrant salmon bag, 3 bright yellow bags, 2 light green bags.
dark lime bags contain 1 light lime bag, 3 vibrant yellow bags, 5 faded bronze bags.
bright chartreuse bags contain 5 mirrored olive bags, 2 mirrored white bags, 1 bright black bag, 2 clear olive bags.
wavy red bags contain 5 bright black bags, 4 dotted salmon bags, 4 clear tomato bags, 4 faded teal bags.
posh coral bags contain 4 posh plum bags, 4 shiny magenta bags, 4 light plum bags.
shiny coral bags contain 5 shiny yellow bags.
light bronze bags contain 2 shiny purple bags, 5 mirrored maroon bags, 2 light white bags.
mirrored olive bags contain 5 mirrored white bags.
pale crimson bags contain 2 vibrant gold bags, 1 bright yellow bag, 2 light green bags, 4 shiny gray bags.
bright cyan bags contain 1 muted plum bag, 5 dark bronze bags, 4 dotted teal bags, 5 faded fuchsia bags.
posh bronze bags contain 1 muted gold bag, 5 shiny turquoise bags, 3 wavy bronze bags.
mirrored yellow bags contain 1 dull maroon bag, 2 posh orange bags, 3 striped lime bags, 4 plaid crimson bags.
muted brown bags contain 5 mirrored indigo bags.
posh lavender bags contain 2 dotted violet bags, 3 clear orange bags.
shiny salmon bags contain 3 bright red bags, 1 light turquoise bag, 2 drab turquoise bags.
striped teal bags contain no other bags.
pale purple bags contain 1 faded yellow bag, 2 dotted beige bags, 1 dark red bag, 5 plaid yellow bags.
drab tomato bags contain 2 faded aqua bags, 2 faded purple bags.
wavy yellow bags contain 2 wavy gold bags, 1 dotted beige bag, 2 shiny gold bags, 4 posh tomato bags.
shiny yellow bags contain 3 wavy brown bags, 5 dull violet bags, 2 muted tomato bags, 4 dull magenta bags.
wavy brown bags contain no other bags.
faded teal bags contain 5 muted plum bags, 1 posh indigo bag.
vibrant tomato bags contain 1 pale blue bag.
drab red bags contain 3 light teal bags, 4 shiny lime bags.
muted beige bags contain 4 light teal bags, 2 vibrant orange bags, 1 drab turquoise bag.
dotted orange bags contain 3 plaid cyan bags, 3 shiny beige bags, 1 bright chartreuse bag.
posh fuchsia bags contain 3 posh tomato bags, 5 bright blue bags.
striped lime bags contain 4 vibrant red bags, 1 bright yellow bag, 5 faded yellow bags, 3 dim gold bags.
bright white bags contain 1 clear purple bag, 2 drab crimson bags.
wavy olive bags contain 1 pale lavender bag, 2 dotted lime bags.
clear black bags contain 2 pale yellow bags.
clear brown bags contain 2 vibrant crimson bags.
dotted aqua bags contain 4 light green bags, 4 light purple bags, 3 pale blue bags.
dull red bags contain 1 bright fuchsia bag, 2 plaid crimson bags, 5 dotted salmon bags, 1 light salmon bag.
light red bags contain 2 mirrored purple bags, 2 dull teal bags.
mirrored bronze bags contain 4 striped lavender bags, 1 dotted brown bag, 1 posh maroon bag, 1 shiny chartreuse bag.
light silver bags contain 4 dim orange bags, 1 dim aqua bag, 5 plaid crimson bags.
faded violet bags contain 5 dotted tomato bags, 3 wavy beige bags.
muted violet bags contain 1 dotted brown bag.
muted black bags contain 3 shiny purple bags, 1 dark salmon bag, 3 bright lavender bags, 2 shiny white bags.
muted tomato bags contain 3 dull magenta bags, 1 muted fuchsia bag.
faded olive bags contain 3 bright coral bags, 5 dark salmon bags, 3 dotted lavender bags, 5 vibrant purple bags.
dotted indigo bags contain 2 drab yellow bags, 5 dim coral bags, 3 striped green bags.
dull turquoise bags contain 3 dark black bags.
faded fuchsia bags contain 4 dull green bags, 5 pale lavender bags.
mirrored gray bags contain 2 mirrored brown bags, 3 shiny gray bags, 2 light maroon bags.
dull violet bags contain 5 muted tomato bags.
vibrant crimson bags contain 1 vibrant tomato bag, 1 striped maroon bag, 3 drab plum bags.
pale olive bags contain 3 shiny lime bags, 4 dim turquoise bags.
muted orange bags contain 1 dull orange bag, 5 shiny tomato bags, 5 pale yellow bags, 1 faded orange bag.
vibrant orange bags contain 5 muted yellow bags, 1 plaid salmon bag, 5 dim aqua bags.
bright brown bags contain 3 muted gray bags, 2 dull cyan bags.
clear coral bags contain 3 clear crimson bags, 4 dotted yellow bags, 1 bright orange bag.
clear blue bags contain 1 posh tan bag.
shiny cyan bags contain 3 light gold bags.
plaid tomato bags contain 3 dull magenta bags, 2 clear brown bags, 1 wavy plum bag.
dim magenta bags contain 5 dark orange bags.
mirrored plum bags contain 3 dull green bags, 4 light violet bags, 2 vibrant bronze bags, 4 vibrant tomato bags.
muted green bags contain 1 dull crimson bag, 2 drab crimson bags, 2 dim red bags.
wavy gray bags contain 3 dark silver bags.
mirrored white bags contain 4 bright yellow bags, 2 bright blue bags.
dark white bags contain 2 posh turquoise bags, 2 light plum bags.
striped maroon bags contain 5 shiny white bags, 3 shiny coral bags, 3 pale salmon bags.
shiny aqua bags contain 1 bright indigo bag, 5 dim plum bags.
vibrant chartreuse bags contain 3 drab gold bags, 1 striped cyan bag, 2 drab violet bags, 1 muted black bag.
faded chartreuse bags contain 4 bright bronze bags, 3 dark silver bags, 1 bright aqua bag.
shiny olive bags contain 1 light silver bag.
dim chartreuse bags contain 5 striped tomato bags.
vibrant red bags contain 3 mirrored beige bags.
vibrant white bags contain 4 light aqua bags.
dim gold bags contain 3 plaid gray bags.
posh chartreuse bags contain 3 wavy blue bags, 5 dull maroon bags, 5 muted yellow bags.
striped purple bags contain 4 shiny orange bags, 3 dim lavender bags, 3 muted lavender bags, 5 plaid tomato bags.
plaid white bags contain 2 striped salmon bags.
striped tomato bags contain 5 bright blue bags.
bright lime bags contain 5 dark maroon bags, 1 shiny gray bag, 3 light white bags.
vibrant yellow bags contain 3 plaid magenta bags, 3 wavy chartreuse bags, 3 bright lavender bags, 1 vibrant salmon bag.
faded red bags contain 3 plaid turquoise bags, 2 wavy cyan bags, 5 dim chartreuse bags.
dim red bags contain 4 muted coral bags.
dotted beige bags contain no other bags.
pale magenta bags contain 1 light violet bag, 2 mirrored lime bags.
muted fuchsia bags contain no other bags.
vibrant purple bags contain 5 shiny purple bags, 4 dim turquoise bags, 2 bright violet bags, 1 dotted beige bag.
pale tomato bags contain 3 dull magenta bags, 5 dim turquoise bags.
wavy gold bags contain 2 muted tomato bags, 5 posh tomato bags.
dull green bags contain 1 shiny indigo bag, 3 dull maroon bags.
muted magenta bags contain 1 clear tan bag, 5 dim tomato bags, 1 plaid purple bag, 1 wavy gray bag.
drab bronze bags contain 5 dull violet bags, 1 light green bag, 3 dim turquoise bags.
vibrant coral bags contain 5 bright black bags, 5 vibrant salmon bags.
dim gray bags contain no other bags.
mirrored black bags contain 5 mirrored lavender bags.
muted cyan bags contain 5 mirrored gold bags.
light aqua bags contain 1 dull cyan bag, 4 dull lavender bags, 2 wavy crimson bags.
mirrored gold bags contain 1 light orange bag.
vibrant cyan bags contain 2 pale chartreuse bags, 5 vibrant tan bags.
dotted green bags contain 2 vibrant tan bags.
vibrant tan bags contain 5 pale lime bags.
drab magenta bags contain 3 light gold bags, 2 posh yellow bags, 4 mirrored salmon bags, 4 muted black bags.
clear teal bags contain 3 vibrant red bags, 3 dotted crimson bags, 3 plaid fuchsia bags.
dark coral bags contain 4 posh fuchsia bags, 5 mirrored fuchsia bags.
bright plum bags contain 5 vibrant blue bags.
drab indigo bags contain 2 shiny orange bags, 3 light indigo bags, 2 drab crimson bags, 5 light purple bags.
shiny chartreuse bags contain 4 clear gold bags.
plaid coral bags contain 1 shiny white bag, 2 dotted plum bags, 5 wavy indigo bags.
dull silver bags contain 3 striped white bags, 2 faded gold bags, 3 dark fuchsia bags.
dotted teal bags contain 5 clear lime bags.
posh black bags contain 4 light plum bags, 4 dark plum bags, 4 vibrant plum bags.
wavy black bags contain 5 bright bronze bags.
mirrored magenta bags contain 3 muted olive bags, 5 striped tomato bags, 2 clear lavender bags.
posh indigo bags contain 4 clear salmon bags, 3 vibrant salmon bags.
vibrant brown bags contain 2 drab turquoise bags.
pale blue bags contain 3 vibrant silver bags, 5 plaid turquoise bags.
wavy lavender bags contain 5 plaid lime bags, 1 plaid crimson bag, 5 wavy coral bags, 1 dark gold bag.
shiny tan bags contain 5 plaid blue bags, 3 shiny bronze bags, 1 mirrored gold bag, 4 faded salmon bags.
muted purple bags contain 3 muted tan bags.
mirrored crimson bags contain 2 drab plum bags, 3 muted magenta bags, 5 dim yellow bags.
muted red bags contain 1 wavy indigo bag.
dotted tomato bags contain 5 plaid turquoise bags, 1 dull lime bag.
dull orange bags contain 2 shiny yellow bags, 1 drab bronze bag, 4 shiny lime bags.
clear aqua bags contain 3 dull cyan bags, 2 bright yellow bags, 2 shiny maroon bags.
light coral bags contain 4 wavy black bags.
posh silver bags contain 5 light bronze bags, 2 clear purple bags, 5 pale fuchsia bags, 2 dull cyan bags.
drab coral bags contain 2 posh yellow bags.
light fuchsia bags contain 2 dim gray bags.
faded cyan bags contain 1 faded orange bag.
bright aqua bags contain 1 muted black bag, 1 muted chartreuse bag, 1 wavy blue bag.
drab lavender bags contain 4 posh yellow bags.
posh gray bags contain 4 shiny lime bags, 5 dotted gold bags, 4 vibrant maroon bags.
plaid blue bags contain 5 vibrant tan bags, 5 mirrored white bags, 5 shiny purple bags, 1 clear white bag.
shiny gray bags contain 2 muted fuchsia bags, 5 plaid crimson bags, 5 faded salmon bags.
light brown bags contain 4 dotted tan bags, 5 wavy coral bags, 3 plaid teal bags.
striped magenta bags contain 2 wavy turquoise bags.
striped aqua bags contain 2 light cyan bags, 2 plaid lime bags, 2 mirrored orange bags, 1 posh lime bag.
bright teal bags contain 1 faded plum bag, 1 dark blue bag, 1 posh cyan bag, 2 striped chartreuse bags.
pale green bags contain 1 muted black bag, 4 faded olive bags, 1 wavy chartreuse bag, 5 dim maroon bags.
vibrant bronze bags contain 3 vibrant lavender bags, 3 faded blue bags, 4 dim brown bags, 4 drab chartreuse bags.
pale brown bags contain 3 faded yellow bags, 1 vibrant tomato bag.
wavy aqua bags contain 1 striped magenta bag, 1 mirrored silver bag, 1 dim gold bag.
dotted yellow bags contain 2 drab turquoise bags, 2 drab maroon bags, 1 light teal bag.
pale salmon bags contain 2 bright indigo bags, 3 wavy violet bags.
posh red bags contain 3 posh blue bags, 4 muted yellow bags, 5 dark silver bags.
wavy violet bags contain 2 dotted lime bags, 2 vibrant purple bags, 1 dull maroon bag.
drab purple bags contain 4 plaid crimson bags, 1 shiny plum bag.
light black bags contain 2 faded teal bags, 1 faded yellow bag, 2 muted fuchsia bags.
dim turquoise bags contain 4 wavy beige bags, 1 shiny plum bag, 3 muted tomato bags, 4 dull magenta bags.
dark tan bags contain 5 drab chartreuse bags, 3 dim coral bags.
striped gray bags contain 5 muted red bags, 1 bright blue bag, 5 wavy maroon bags.
muted tan bags contain 5 drab turquoise bags, 1 light maroon bag, 5 plaid purple bags.
posh green bags contain 3 dotted chartreuse bags, 4 muted yellow bags, 5 shiny gray bags, 1 dark black bag.
mirrored lime bags contain 4 clear teal bags, 5 wavy coral bags, 2 mirrored beige bags.
muted plum bags contain 5 faded yellow bags, 3 posh blue bags.
dark maroon bags contain 2 dotted lavender bags.
plaid green bags contain 3 wavy yellow bags, 1 shiny indigo bag, 4 mirrored maroon bags, 5 dim gray bags.
mirrored teal bags contain 5 dim magenta bags, 1 dark magenta bag, 3 plaid green bags.
wavy crimson bags contain 1 vibrant cyan bag, 2 light beige bags.
wavy green bags contain 4 dim tan bags, 1 dotted lime bag, 5 drab white bags, 2 bright beige bags.
shiny brown bags contain 5 dark silver bags, 3 shiny maroon bags, 5 dotted lavender bags.
muted turquoise bags contain 5 dark indigo bags, 3 drab plum bags.
mirrored lavender bags contain 2 clear salmon bags, 2 plaid maroon bags, 3 wavy cyan bags.
drab blue bags contain 3 dotted olive bags, 1 shiny chartreuse bag, 1 drab magenta bag, 2 mirrored maroon bags.
bright fuchsia bags contain 1 dark olive bag.
pale turquoise bags contain 2 striped chartreuse bags.
posh white bags contain 1 striped cyan bag, 1 plaid coral bag, 2 dim gray bags, 3 shiny red bags.
drab brown bags contain 4 plaid red bags.
pale gold bags contain 2 dim tan bags, 5 dark red bags, 4 vibrant cyan bags, 5 dark violet bags.
plaid maroon bags contain 1 shiny lime bag, 4 faded lavender bags, 2 dim tan bags, 5 vibrant purple bags.
vibrant green bags contain 1 drab purple bag, 2 faded blue bags.
bright violet bags contain 1 dotted lavender bag, 5 light chartreuse bags, 4 bright indigo bags.
bright magenta bags contain 5 shiny purple bags, 5 light teal bags, 2 pale purple bags, 4 pale silver bags.
plaid orange bags contain 1 dull green bag.
posh olive bags contain 5 dark silver bags, 3 drab yellow bags, 2 dim brown bags, 4 dull gray bags.
light teal bags contain 3 dim gray bags.
shiny beige bags contain 1 dark cyan bag, 1 vibrant yellow bag.
drab cyan bags contain 4 dim silver bags, 1 wavy maroon bag.
pale gray bags contain 2 dark salmon bags.
plaid beige bags contain 3 bright purple bags, 1 drab plum bag, 4 shiny bronze bags, 3 drab salmon bags.
dull plum bags contain 4 mirrored orange bags.
shiny violet bags contain 3 drab olive bags.
striped turquoise bags contain 1 faded green bag.
dark aqua bags contain 5 clear crimson bags.
dim crimson bags contain 3 faded chartreuse bags, 3 light orange bags, 4 striped plum bags.
faded tan bags contain 1 dark cyan bag, 1 bright silver bag.
faded brown bags contain 3 faded purple bags, 1 posh orange bag, 5 light silver bags.
mirrored coral bags contain 1 vibrant tan bag.
clear olive bags contain 2 pale olive bags.
pale lime bags contain 2 muted fuchsia bags, 1 dim gray bag, 5 dotted beige bags, 5 striped teal bags.
wavy white bags contain 3 dim indigo bags, 3 plaid green bags, 2 dull gold bags.
pale plum bags contain 5 plaid gray bags.
plaid yellow bags contain 5 dark yellow bags, 1 mirrored white bag, 5 shiny white bags, 1 shiny lime bag.
drab salmon bags contain 2 vibrant blue bags, 2 plaid plum bags, 1 shiny gray bag, 3 bright black bags.
striped fuchsia bags contain 2 striped teal bags, 5 drab black bags, 2 bright magenta bags.
mirrored fuchsia bags contain 3 drab black bags.
dark indigo bags contain 1 dull lime bag, 4 vibrant cyan bags, 1 bright gray bag, 3 pale purple bags.
posh blue bags contain 1 shiny yellow bag.
dark turquoise bags contain 4 bright yellow bags, 3 wavy bronze bags.
posh tan bags contain 4 shiny plum bags, 4 dark silver bags, 3 wavy beige bags, 1 mirrored fuchsia bag.
bright turquoise bags contain 1 dotted green bag, 4 faded silver bags, 1 plaid turquoise bag.
vibrant teal bags contain 4 plaid teal bags, 3 pale blue bags.
plaid purple bags contain 2 dim tan bags, 5 light turquoise bags.
drab plum bags contain 2 dull green bags, 5 posh lavender bags, 3 drab tan bags.
dark blue bags contain 3 mirrored indigo bags, 3 dark red bags.
vibrant black bags contain 2 shiny red bags, 5 posh brown bags, 1 mirrored yellow bag.
mirrored brown bags contain 1 shiny indigo bag, 2 shiny yellow bags, 5 shiny blue bags, 5 clear yellow bags.
dotted crimson bags contain 3 posh tomato bags, 4 vibrant blue bags, 5 dark violet bags, 5 posh violet bags.
shiny bronze bags contain 1 plaid maroon bag.
drab orange bags contain 4 dotted crimson bags, 4 clear bronze bags, 3 pale turquoise bags, 5 dim coral bags.
wavy fuchsia bags contain 4 posh fuchsia bags, 5 wavy purple bags, 2 muted cyan bags.
plaid black bags contain 2 drab crimson bags, 4 vibrant tomato bags, 4 clear bronze bags, 4 faded lavender bags.
mirrored red bags contain 3 shiny crimson bags.
faded tomato bags contain 1 clear aqua bag, 3 vibrant bronze bags.
light turquoise bags contain 2 posh silver bags, 2 shiny black bags, 5 muted blue bags.
faded crimson bags contain 5 posh blue bags, 4 dim maroon bags.
dull magenta bags contain no other bags.
dark plum bags contain 5 vibrant purple bags, 5 wavy brown bags, 2 dark indigo bags.
dotted white bags contain 1 dark teal bag, 5 dull white bags, 2 pale salmon bags, 1 dotted plum bag.
wavy indigo bags contain 5 shiny maroon bags, 4 shiny lime bags.
faded coral bags contain 5 dim indigo bags, 1 striped brown bag.
vibrant turquoise bags contain 4 dotted magenta bags, 5 bright lavender bags, 5 plaid turquoise bags, 5 striped lavender bags.
muted gray bags contain 1 mirrored white bag.
dotted gold bags contain 4 dark brown bags.
dim salmon bags contain 3 light gold bags, 4 plaid purple bags.
clear salmon bags contain 3 striped lavender bags, 5 posh teal bags, 4 vibrant turquoise bags.
vibrant olive bags contain 3 striped fuchsia bags, 3 muted indigo bags, 1 dotted yellow bag, 4 bright white bags.
bright salmon bags contain 1 drab orange bag.
muted maroon bags contain 5 dim crimson bags, 4 dark red bags, 5 plaid purple bags.
light tan bags contain 2 dotted blue bags.
dotted turquoise bags contain 4 faded lime bags, 2 dotted silver bags, 4 mirrored cyan bags.
shiny magenta bags contain 1 mirrored salmon bag, 3 dim fuchsia bags, 3 muted red bags.
dark cyan bags contain 5 dark brown bags, 5 vibrant silver bags, 5 dim green bags.
dim violet bags contain 4 vibrant turquoise bags, 1 pale crimson bag, 4 bright red bags, 3 muted black bags.
dull aqua bags contain 3 drab teal bags.
dim aqua bags contain 3 vibrant blue bags, 4 pale salmon bags, 5 shiny bronze bags, 2 dim olive bags.
light gray bags contain 4 dull white bags, 4 dim blue bags.
dull salmon bags contain 1 striped fuchsia bag, 5 dark white bags, 2 pale tan bags.
plaid teal bags contain 1 dim olive bag, 2 faded purple bags, 4 shiny gray bags, 1 shiny salmon bag.
clear tan bags contain 1 clear lime bag, 4 mirrored turquoise bags, 4 bright white bags, 3 drab bronze bags.
wavy beige bags contain 2 muted fuchsia bags, 3 clear bronze bags, 2 bright yellow bags.
plaid salmon bags contain 2 drab bronze bags, 2 drab chartreuse bags, 4 plaid crimson bags, 5 shiny lime bags.
drab lime bags contain 2 clear orange bags, 4 dotted silver bags, 5 dark maroon bags, 5 dim magenta bags.
bright crimson bags contain 5 shiny maroon bags.
clear turquoise bags contain 4 vibrant blue bags.
clear lavender bags contain 3 pale fuchsia bags, 2 bright lavender bags, 2 dark orange bags, 1 dull magenta bag.
clear green bags contain 3 clear orange bags.
pale cyan bags contain 2 dull purple bags, 1 clear olive bag.
posh lime bags contain 2 clear purple bags.
dim lavender bags contain 3 clear crimson bags, 4 striped violet bags.
faded indigo bags contain 5 dull cyan bags, 2 plaid blue bags, 4 striped teal bags.
posh aqua bags contain 5 bright aqua bags, 2 shiny indigo bags, 2 drab silver bags, 1 vibrant turquoise bag.
dark magenta bags contain 3 light silver bags.
clear cyan bags contain 3 pale fuchsia bags, 2 shiny coral bags, 1 dull magenta bag, 4 dim turquoise bags.
pale yellow bags contain 1 vibrant tan bag, 4 drab plum bags.
dim plum bags contain 4 striped gray bags, 2 posh tomato bags, 1 drab black bag.
dark purple bags contain 3 bright indigo bags, 3 dull purple bags.
clear plum bags contain 4 bright cyan bags, 5 dim turquoise bags.
faded magenta bags contain 1 muted olive bag, 3 plaid chartreuse bags.
mirrored aqua bags contain 2 clear lavender bags.
light white bags contain 3 dim gray bags, 3 bright white bags, 2 striped teal bags, 4 light green bags.
clear gold bags contain 2 wavy coral bags.
dull lavender bags contain 2 wavy beige bags, 3 drab black bags.
dark yellow bags contain 3 wavy gray bags, 1 dark salmon bag, 2 vibrant tan bags.
dotted black bags contain 4 dim plum bags, 2 bright white bags.
posh tomato bags contain 5 wavy beige bags, 1 dim gray bag, 3 shiny lime bags, 5 bright black bags.
bright indigo bags contain 4 striped teal bags, 1 shiny yellow bag, 5 dotted beige bags.
dim purple bags contain 5 dark tan bags, 5 striped lavender bags.
posh plum bags contain 5 posh maroon bags.
pale bronze bags contain 5 shiny silver bags.
striped crimson bags contain 2 dark indigo bags.
plaid fuchsia bags contain 1 shiny lime bag, 4 mirrored orange bags.
dark orange bags contain 2 dotted lavender bags, 1 posh blue bag, 2 muted yellow bags.
dim blue bags contain 2 clear yellow bags.
clear violet bags contain 2 shiny bronze bags.
shiny blue bags contain 4 dark salmon bags, 5 posh plum bags.
dull lime bags contain 5 plaid green bags, 3 bright black bags, 4 drab maroon bags.
muted lavender bags contain 1 dark gray bag, 2 bright crimson bags.
plaid gray bags contain 5 bright black bags, 5 pale silver bags.
light yellow bags contain 2 mirrored crimson bags.
muted chartreuse bags contain 1 pale fuchsia bag, 1 plaid purple bag.
dim lime bags contain 3 dull maroon bags, 3 bright red bags, 3 drab black bags.
light purple bags contain 5 dull violet bags, 5 vibrant lavender bags.
posh orange bags contain 5 pale salmon bags, 5 light chartreuse bags, 1 dark red bag.
vibrant violet bags contain 3 shiny gray bags.
pale silver bags contain 5 mirrored salmon bags.
light tomato bags contain 2 dim tan bags, 1 faded silver bag, 4 plaid yellow bags, 3 drab gold bags.
posh salmon bags contain 3 bright plum bags.
dotted plum bags contain 4 pale gold bags, 1 vibrant lavender bag, 2 pale blue bags.
shiny lavender bags contain 1 dull gray bag, 4 muted teal bags, 2 dotted yellow bags, 2 bright turquoise bags.
dim beige bags contain 2 wavy yellow bags, 2 drab violet bags, 1 wavy gold bag, 5 clear cyan bags.
posh cyan bags contain 2 clear lavender bags, 4 clear salmon bags, 4 posh tan bags.
light maroon bags contain 5 dark violet bags, 3 plaid lime bags, 3 wavy gold bags, 5 dotted lime bags.
dotted lime bags contain 3 clear bronze bags, 5 dim turquoise bags.
dim bronze bags contain 3 light fuchsia bags.
faded black bags contain 3 light bronze bags, 2 bright beige bags.
striped white bags contain 1 mirrored white bag.
clear red bags contain 1 pale orange bag, 2 clear orange bags, 1 dull maroon bag, 3 dark bronze bags.
muted lime bags contain 5 dim fuchsia bags.
vibrant gold bags contain 4 wavy blue bags, 3 clear gray bags, 5 vibrant turquoise bags.
clear silver bags contain 3 light violet bags, 5 dull turquoise bags.
muted indigo bags contain 3 dark orange bags, 4 light gold bags.
bright green bags contain 4 dark red bags.
vibrant plum bags contain 5 dull tomato bags, 4 bright cyan bags, 4 plaid purple bags.
wavy cyan bags contain 4 muted plum bags.
plaid cyan bags contain 4 clear orange bags, 3 dull chartreuse bags.
faded salmon bags contain 1 dim gray bag.
shiny turquoise bags contain 3 light aqua bags, 1 vibrant beige bag, 4 clear turquoise bags, 1 faded silver bag.
dotted silver bags contain 5 dotted blue bags, 1 dotted salmon bag.
striped black bags contain 2 plaid crimson bags, 5 dotted silver bags, 5 dull maroon bags.
dull indigo bags contain 4 dim magenta bags, 4 shiny magenta bags, 2 pale yellow bags, 1 plaid cyan bag.
bright coral bags contain 1 shiny coral bag, 2 muted tomato bags, 4 drab crimson bags.
faded bronze bags contain 5 posh cyan bags, 5 light beige bags, 1 drab yellow bag, 3 striped lime bags.
drab green bags contain 1 clear cyan bag.
pale black bags contain 2 muted yellow bags.
muted salmon bags contain 4 plaid crimson bags, 2 vibrant lime bags.
dark violet bags contain 4 clear cyan bags, 1 mirrored maroon bag, 5 drab black bags.
faded aqua bags contain 3 pale fuchsia bags, 1 clear teal bag, 5 light white bags.
vibrant indigo bags contain 5 light turquoise bags.
bright blue bags contain 1 shiny purple bag, 1 wavy brown bag.
dark olive bags contain 2 wavy beige bags.
vibrant beige bags contain 3 wavy beige bags, 1 posh violet bag, 4 dark teal bags.
dotted olive bags contain 5 dotted magenta bags.
muted coral bags contain 2 vibrant silver bags, 3 dim coral bags.
dark chartreuse bags contain 4 faded tomato bags, 2 light violet bags, 4 clear silver bags.
light green bags contain no other bags.
bright gray bags contain 2 drab yellow bags, 2 muted indigo bags.
posh crimson bags contain 5 plaid indigo bags, 3 wavy lime bags, 2 dull turquoise bags, 5 faded salmon bags.
drab yellow bags contain 3 shiny purple bags, 4 dark salmon bags, 3 shiny coral bags, 2 shiny plum bags.
dull white bags contain 3 plaid lavender bags, 4 dark beige bags, 1 posh beige bag.
drab olive bags contain 1 shiny cyan bag, 3 bright fuchsia bags.
striped olive bags contain 2 drab aqua bags, 3 muted chartreuse bags, 2 clear red bags, 1 posh turquoise bag.
posh purple bags contain 1 dull lime bag, 2 dull plum bags, 3 dark black bags.
mirrored green bags contain 2 mirrored salmon bags.
dull teal bags contain 1 dark gray bag, 1 posh indigo bag, 5 light coral bags.
dim indigo bags contain 5 dark maroon bags.
faded gray bags contain 4 muted crimson bags.
light blue bags contain 2 plaid violet bags, 3 dim tomato bags, 4 plaid crimson bags, 5 dull orange bags.
plaid turquoise bags contain 2 muted blue bags, 5 clear white bags, 1 dull violet bag.
striped gold bags contain 2 striped brown bags, 1 wavy silver bag.
faded blue bags contain 1 dark lavender bag, 4 muted yellow bags, 2 bright yellow bags, 2 dim tan bags.
clear beige bags contain 5 dim tan bags, 4 faded blue bags, 2 bright green bags.
shiny indigo bags contain 1 shiny purple bag.
striped brown bags contain 2 light gold bags.
shiny black bags contain 1 posh red bag, 5 bright black bags, 3 posh plum bags, 5 clear white bags.
pale aqua bags contain 5 plaid purple bags, 3 wavy orange bags, 5 dotted purple bags, 4 bright lime bags.
dark beige bags contain 3 clear white bags, 3 wavy yellow bags, 3 posh turquoise bags, 2 posh tan bags.
striped green bags contain 3 posh red bags, 2 shiny salmon bags, 4 mirrored salmon bags, 3 posh teal bags.
pale violet bags contain 5 wavy turquoise bags, 1 bright aqua bag.
dim tomato bags contain 5 dim tan bags.
mirrored cyan bags contain 5 shiny indigo bags, 3 faded blue bags.
plaid magenta bags contain 3 mirrored brown bags, 5 pale olive bags, 2 clear purple bags.
dotted tan bags contain 5 plaid turquoise bags.
dull fuchsia bags contain 2 shiny crimson bags, 3 clear olive bags.
clear orange bags contain 5 dotted lime bags, 2 dark olive bags, 3 bright yellow bags, 2 wavy violet bags.
light indigo bags contain 1 drab plum bag, 5 dim lime bags.
muted aqua bags contain 5 faded red bags, 5 pale blue bags, 5 dull lavender bags.
faded plum bags contain 5 drab turquoise bags.
dark gold bags contain 4 faded salmon bags, 4 bright black bags, 4 dim chartreuse bags.
striped bronze bags contain 2 dark beige bags.
mirrored purple bags contain 3 dim turquoise bags, 4 shiny bronze bags.
faded white bags contain 4 faded tomato bags, 3 faded aqua bags, 5 faded gold bags, 4 vibrant orange bags.
wavy turquoise bags contain 2 dotted olive bags, 1 muted yellow bag.
striped blue bags contain 5 wavy bronze bags, 3 shiny chartreuse bags.
dull gray bags contain 4 pale lavender bags.
plaid plum bags contain 4 dim olive bags, 3 faded olive bags.
pale coral bags contain 1 faded yellow bag, 3 shiny plum bags, 4 striped tomato bags, 4 shiny bronze bags.
drab violet bags contain 2 plaid black bags, 5 bright violet bags, 3 pale blue bags.
vibrant gray bags contain 4 vibrant indigo bags, 1 dull beige bag, 1 dull plum bag, 1 dotted brown bag.
drab gray bags contain 5 mirrored brown bags, 5 bright coral bags.
pale chartreuse bags contain 2 dull cyan bags, 4 mirrored fuchsia bags.
dotted lavender bags contain 2 bright blue bags, 3 light chartreuse bags.
dull tomato bags contain 5 wavy yellow bags.
dull purple bags contain 5 wavy brown bags, 1 muted yellow bag.
wavy orange bags contain 4 bright orange bags, 1 dotted purple bag, 3 dull blue bags, 3 light crimson bags.
dotted purple bags contain 1 bright cyan bag, 5 wavy violet bags, 3 vibrant cyan bags.
light lavender bags contain 4 shiny salmon bags, 4 mirrored salmon bags, 2 wavy magenta bags.
plaid crimson bags contain 3 dotted salmon bags, 2 plaid maroon bags, 5 pale chartreuse bags, 3 dotted beige bags.
plaid lavender bags contain 2 clear bronze bags, 5 light silver bags, 1 bright lavender bag.
wavy lime bags contain 1 dim coral bag.
clear tomato bags contain 1 dark violet bag.
light gold bags contain 1 striped teal bag, 2 vibrant purple bags, 5 dark salmon bags.
faded turquoise bags contain 1 shiny lime bag, 1 posh orange bag, 1 plaid maroon bag.
wavy tomato bags contain 2 plaid plum bags, 1 dull lime bag, 3 dull maroon bags.
faded beige bags contain 3 clear maroon bags, 1 dotted brown bag.
dark black bags contain 1 faded salmon bag, 1 light green bag, 4 clear bronze bags, 4 dotted lavender bags.
striped violet bags contain 4 mirrored beige bags.
plaid chartreuse bags contain 2 dotted purple bags.
posh maroon bags contain 5 wavy yellow bags, 2 pale chartreuse bags.
posh yellow bags contain 5 mirrored blue bags, 2 wavy beige bags.
bright black bags contain 3 clear bronze bags, 5 wavy gray bags.
shiny tomato bags contain 3 dotted plum bags, 1 shiny orange bag, 4 faded teal bags, 1 bright lavender bag.
dotted chartreuse bags contain 2 muted yellow bags, 4 faded cyan bags, 3 striped indigo bags, 1 drab red bag.
pale tan bags contain 3 dotted chartreuse bags.
dim white bags contain 2 dim tomato bags, 3 striped indigo bags, 1 faded red bag, 3 mirrored turquoise bags.
mirrored salmon bags contain 1 pale chartreuse bag, 3 faded salmon bags, 2 dark silver bags.
vibrant fuchsia bags contain 3 dim olive bags, 1 striped magenta bag, 2 dark magenta bags, 2 drab white bags.
drab silver bags contain 2 dotted silver bags, 4 wavy yellow bags, 2 dim turquoise bags, 2 shiny maroon bags.
dull yellow bags contain 2 posh teal bags, 1 muted chartreuse bag, 1 pale salmon bag, 1 posh beige bag.
clear fuchsia bags contain 4 light turquoise bags, 1 dull white bag, 3 plaid indigo bags, 1 shiny gold bag.
dark bronze bags contain 2 faded salmon bags.
vibrant lime bags contain 3 dull chartreuse bags, 5 shiny yellow bags.
wavy tan bags contain 4 wavy indigo bags, 3 dull crimson bags.
mirrored tan bags contain 4 dim salmon bags, 5 dim tomato bags, 4 mirrored salmon bags, 3 drab indigo bags.
plaid bronze bags contain 2 dotted silver bags, 1 striped black bag, 2 dotted tomato bags.
shiny silver bags contain 2 muted salmon bags, 5 bright magenta bags, 2 drab lime bags.
mirrored violet bags contain 1 shiny yellow bag, 5 vibrant tan bags.
dotted red bags contain 3 posh beige bags, 3 posh lavender bags, 3 shiny lavender bags, 4 pale bronze bags.
mirrored chartreuse bags contain 3 dark coral bags, 1 muted cyan bag.
drab crimson bags contain 4 bright blue bags, 4 faded salmon bags.
striped salmon bags contain 4 posh fuchsia bags, 4 faded salmon bags, 3 shiny yellow bags.
dark gray bags contain 3 bright bronze bags.
striped tan bags contain 3 vibrant green bags.
dull maroon bags contain 1 muted tomato bag.
light crimson bags contain 1 posh green bag.
faded lavender bags contain 2 dotted beige bags.
clear white bags contain 2 bright bronze bags, 2 wavy gray bags, 4 dull magenta bags, 2 shiny lime bags.
dim orange bags contain 5 drab gray bags, 4 drab tan bags, 3 faded black bags, 2 pale cyan bags.
faded green bags contain 4 dim blue bags.
plaid aqua bags contain 2 drab indigo bags, 5 pale turquoise bags, 1 pale tomato bag.
dotted magenta bags contain 5 pale lavender bags, 2 shiny yellow bags, 3 posh tomato bags.
faded maroon bags contain 5 wavy plum bags, 2 shiny lime bags.
dim silver bags contain 2 dull cyan bags, 1 shiny salmon bag, 1 striped salmon bag.
dotted salmon bags contain 1 posh tomato bag, 4 bright black bags.
vibrant salmon bags contain 2 dark silver bags.
striped beige bags contain 2 clear tomato bags, 1 mirrored indigo bag, 2 pale chartreuse bags, 3 dull yellow bags.
bright orange bags contain 1 pale lime bag.
muted crimson bags contain 1 dotted lavender bag.
muted bronze bags contain 3 light green bags.
shiny fuchsia bags contain 4 plaid indigo bags, 5 bright fuchsia bags.
bright red bags contain 2 posh fuchsia bags, 2 clear cyan bags.
dim maroon bags contain 1 dotted beige bag, 2 drab black bags, 5 posh tomato bags, 3 striped lavender bags.
bright gold bags contain 5 dim chartreuse bags, 1 vibrant salmon bag, 2 faded black bags.
drab white bags contain 1 clear yellow bag, 4 pale cyan bags, 5 dark yellow bags.
clear purple bags contain 2 wavy brown bags, 3 dull magenta bags, 5 dim gray bags, 4 shiny purple bags.
dim green bags contain 2 posh turquoise bags, 4 light bronze bags.
dull blue bags contain 1 light salmon bag, 1 posh red bag, 2 clear brown bags.
bright silver bags contain 3 dotted bronze bags, 1 plaid blue bag, 2 light coral bags.
bright bronze bags contain 3 dull magenta bags, 3 light white bags.
shiny gold bags contain 3 wavy gold bags.
wavy bronze bags contain 4 dull lime bags, 2 shiny white bags, 2 dim silver bags.
muted yellow bags contain 5 dark bronze bags, 3 light white bags, 5 shiny coral bags, 4 shiny lime bags.
faded orange bags contain 3 plaid maroon bags, 5 shiny plum bags, 2 mirrored white bags.
vibrant silver bags contain 1 bright coral bag, 5 wavy blue bags, 1 mirrored maroon bag.
mirrored maroon bags contain 5 drab crimson bags, 4 striped tomato bags.
striped silver bags contain 2 dotted olive bags, 3 muted white bags, 5 dark black bags, 5 light gray bags.
drab gold bags contain 2 clear coral bags.
plaid tan bags contain 2 plaid orange bags, 2 muted beige bags, 2 mirrored purple bags.
bright beige bags contain 5 light plum bags.
light salmon bags contain 1 dark black bag, 5 mirrored salmon bags, 1 dim silver bag.
dull beige bags contain 2 dark lavender bags.
posh magenta bags contain 3 muted yellow bags.
dotted violet bags contain 1 wavy brown bag, 3 dim turquoise bags.
vibrant blue bags contain 4 wavy gray bags, 2 light turquoise bags, 1 drab bronze bag, 4 wavy cyan bags.
wavy purple bags contain 3 dotted olive bags, 2 dull lime bags.
wavy plum bags contain 3 posh chartreuse bags.
dark silver bags contain no other bags.
dark teal bags contain 4 posh red bags, 4 dark lavender bags.
plaid lime bags contain 2 muted fuchsia bags.
posh violet bags contain 5 clear olive bags.
plaid olive bags contain 4 vibrant tan bags, 5 plaid fuchsia bags.
mirrored indigo bags contain 5 posh maroon bags, 5 light turquoise bags.
vibrant maroon bags contain 4 vibrant beige bags.
light magenta bags contain 2 vibrant gray bags, 4 clear crimson bags.
clear indigo bags contain 4 light gray bags, 1 plaid blue bag.
shiny red bags contain 4 vibrant blue bags, 1 wavy brown bag, 5 striped maroon bags, 5 posh orange bags.
dark crimson bags contain 2 bright yellow bags.
dull crimson bags contain 5 striped salmon bags, 3 faded purple bags, 4 clear tomato bags.
pale red bags contain 1 dotted cyan bag, 2 dark turquoise bags.
striped plum bags contain 4 faded yellow bags, 1 posh blue bag.
dim olive bags contain 1 light green bag, 1 faded salmon bag.
dim brown bags contain 5 drab bronze bags, 2 dark red bags, 3 shiny gold bags.
pale orange bags contain 3 pale gray bags, 1 clear olive bag.
shiny green bags contain 2 clear turquoise bags, 1 mirrored aqua bag, 2 dull red bags, 4 dull bronze bags.
dotted fuchsia bags contain 3 vibrant bronze bags, 1 dull maroon bag, 5 wavy indigo bags.
posh teal bags contain 4 pale blue bags, 1 pale lime bag.
pale teal bags contain 5 muted beige bags, 5 dark salmon bags, 2 faded black bags.
vibrant aqua bags contain 5 vibrant silver bags, 5 shiny maroon bags.
light olive bags contain 2 plaid turquoise bags.
dim teal bags contain 1 muted magenta bag, 5 wavy maroon bags, 5 striped brown bags, 4 clear plum bags.
faded silver bags contain 2 dull lavender bags.
dark fuchsia bags contain 2 dim black bags, 3 dotted olive bags.
dotted cyan bags contain 3 clear gold bags.
pale beige bags contain 2 clear turquoise bags.
vibrant magenta bags contain 5 light bronze bags, 3 drab black bags.
pale indigo bags contain 2 vibrant cyan bags.
clear bronze bags contain 1 vibrant salmon bag.
pale white bags contain 4 faded orange bags.
light chartreuse bags contain no other bags.
striped chartreuse bags contain 4 clear gray bags.
dark salmon bags contain 5 wavy gray bags, 1 light chartreuse bag, 2 clear gray bags.
muted gold bags contain 3 bright lavender bags, 4 vibrant yellow bags, 3 posh silver bags.
muted white bags contain 4 muted blue bags, 1 light gold bag.
dim tan bags contain 5 posh fuchsia bags, 5 wavy brown bags, 1 dim turquoise bag.
dull black bags contain 5 dotted cyan bags, 2 posh turquoise bags, 5 pale salmon bags.
faded lime bags contain 4 mirrored orange bags, 2 vibrant orange bags, 2 dull lavender bags, 3 dotted chartreuse bags.
drab tan bags contain 5 shiny maroon bags, 4 mirrored white bags, 3 dull plum bags, 4 shiny plum bags.
muted olive bags contain 4 faded blue bags.
dull chartreuse bags contain 4 shiny cyan bags, 5 dark silver bags, 2 dark violet bags, 2 bright lavender bags.
posh turquoise bags contain 4 pale orange bags, 2 dotted yellow bags, 3 bright tomato bags, 2 vibrant turquoise bags.
dull tan bags contain 2 mirrored purple bags.
drab teal bags contain 1 dull lavender bag.
light beige bags contain 3 plaid yellow bags, 4 faded lavender bags.
wavy blue bags contain 3 shiny purple bags.
striped orange bags contain 4 vibrant cyan bags.
shiny orange bags contain 2 shiny black bags, 2 shiny coral bags.
dull brown bags contain 3 wavy bronze bags.
mirrored silver bags contain 4 vibrant tan bags, 4 faded fuchsia bags, 5 dark red bags, 3 wavy blue bags.
wavy teal bags contain 1 pale coral bag.
drab black bags contain 4 wavy brown bags, 4 striped teal bags, 2 muted fuchsia bags, 4 shiny indigo bags.
drab aqua bags contain 2 bright orange bags, 1 vibrant tan bag.
mirrored orange bags contain 2 striped salmon bags, 1 wavy gray bag, 5 pale blue bags, 4 mirrored salmon bags.
muted teal bags contain 4 drab tan bags, 4 posh beige bags, 4 faded green bags.
faded yellow bags contain 3 shiny purple bags, 3 wavy blue bags, 1 muted fuchsia bag.
shiny maroon bags contain 3 striped salmon bags, 5 wavy violet bags.
wavy silver bags contain 4 faded blue bags, 2 vibrant salmon bags, 5 plaid gray bags.
shiny white bags contain 4 dark salmon bags.
posh brown bags contain 5 drab red bags.
bright purple bags contain 2 dim silver bags.
dotted brown bags contain 1 dotted yellow bag.
striped lavender bags contain 5 shiny gold bags, 5 mirrored fuchsia bags.
dark lavender bags contain 3 bright violet bags, 5 dull violet bags, 1 shiny coral bag.
drab maroon bags contain 2 light white bags, 2 vibrant turquoise bags, 2 vibrant cyan bags.
pale maroon bags contain 3 dim red bags.
plaid gold bags contain 4 posh bronze bags.
striped coral bags contain 5 drab blue bags, 3 muted bronze bags.
drab fuchsia bags contain 1 shiny bronze bag.
light cyan bags contain 1 dotted fuchsia bag, 1 drab violet bag.
plaid silver bags contain 3 clear gray bags, 5 light teal bags, 3 vibrant tan bags, 1 bright white bag.
wavy coral bags contain 1 shiny black bag, 3 mirrored maroon bags.
posh gold bags contain 3 bright yellow bags, 2 dark lavender bags.
drab beige bags contain 5 bright gray bags, 3 pale olive bags, 3 plaid chartreuse bags.
wavy salmon bags contain 5 shiny beige bags, 1 posh violet bag.
pale fuchsia bags contain 4 wavy gray bags, 1 wavy beige bag.
dim fuchsia bags contain 1 dim beige bag, 4 muted cyan bags, 1 clear lavender bag.
bright tan bags contain 2 drab crimson bags.
striped red bags contain 2 muted black bags.
dark green bags contain 5 plaid red bags.
faded gold bags contain 2 muted white bags, 5 clear yellow bags, 1 light fuchsia bag, 4 dotted violet bags.
striped cyan bags contain 2 drab purple bags, 1 shiny fuchsia bag, 2 light salmon bags.
dull bronze bags contain 1 faded black bag, 4 dull lavender bags.
dull cyan bags contain 5 faded salmon bags, 1 clear bronze bag.
shiny plum bags contain 2 dark silver bags.
mirrored beige bags contain 3 posh red bags, 1 clear chartreuse bag, 2 muted magenta bags.
mirrored tomato bags contain 3 posh lavender bags, 4 light violet bags, 1 wavy crimson bag, 1 dim tan bag.
light plum bags contain 5 dim tan bags, 2 dotted beige bags, 4 posh blue bags, 4 light green bags.
mirrored blue bags contain 4 faded lavender bags, 4 pale salmon bags.
clear maroon bags contain 3 dark salmon bags, 2 shiny brown bags, 4 wavy purple bags, 1 plaid yellow bag.
bright maroon bags contain 4 pale turquoise bags, 4 drab violet bags, 2 clear lime bags.
plaid red bags contain 1 drab turquoise bag, 1 striped teal bag, 4 plaid yellow bags.
mirrored turquoise bags contain 3 clear orange bags, 5 bright blue bags, 3 posh plum bags.
dark brown bags contain 5 striped fuchsia bags, 5 mirrored plum bags, 1 wavy crimson bag, 4 clear gray bags.
muted silver bags contain 2 dim tan bags, 2 muted crimson bags.
dark red bags contain 2 wavy beige bags, 1 clear bronze bag, 5 shiny coral bags, 3 shiny indigo bags.
dark tomato bags contain 2 faded gray bags, 2 dim tomato bags.
muted blue bags contain 5 posh silver bags.
wavy magenta bags contain 4 faded tomato bags.
plaid violet bags contain 5 dim aqua bags, 4 drab orange bags, 4 posh lavender bags, 2 dull yellow bags.
faded purple bags contain 4 vibrant bronze bags, 5 bright bronze bags, 1 faded red bag, 4 clear tan bags.
wavy chartreuse bags contain 5 bright white bags, 2 shiny coral bags, 3 bright cyan bags.
plaid indigo bags contain 3 pale purple bags, 2 posh orange bags.
bright tomato bags contain 5 plaid blue bags, 2 posh orange bags, 1 vibrant purple bag.
wavy maroon bags contain 1 striped white bag.
bright lavender bags contain 3 faded salmon bags, 5 mirrored maroon bags, 5 posh tomato bags.
light orange bags contain 2 bright blue bags, 1 dark yellow bag, 2 clear gray bags, 2 striped salmon bags.
posh beige bags contain 2 dark orange bags.
clear chartreuse bags contain 5 striped maroon bags, 5 light chartreuse bags, 4 drab black bags.
dotted blue bags contain 4 clear cyan bags.
dotted coral bags contain 4 shiny tomato bags, 1 posh gold bag, 5 muted olive bags.
striped yellow bags contain 5 faded purple bags, 4 drab purple bags, 5 dark yellow bags, 5 muted red bags.
dull gold bags contain 1 light turquoise bag.
dotted maroon bags contain 3 dark maroon bags, 2 faded yellow bags.
clear yellow bags contain 2 plaid maroon bags, 5 bright gray bags, 4 pale olive bags, 5 shiny indigo bags.
clear crimson bags contain 5 faded yellow bags.
dotted bronze bags contain 2 muted tomato bags.'''
'''list_of_rules = [((((i.replace(",", ":")).replace(" contain", ":")).replace(".", "")).replace("bags", "bag")) \
                     .replace(" other bag", "") for i in string_of_rules.split("\n")]
d = {}
for i in list_of_rules:
    d[i.split(":")[0]] = [(i.split(":")[j])[3:] for j in range(1, len(i.split(":")))]
ans_7_1 = 0
f = ["shiny gold bag"]
for k in f:
    for i in d:
        if k in d[i]:
            ans_7_1 += 1
            f.append(i)
            d[i] = ""

print(ans_7_1)

# day 7:2
list_of_rules = [((((i.replace(",", ":")).replace(" contain", ":")).replace(".", "")).replace("bags", "bag")) \
                     .replace(": no other bag", ": 1") for i in string_of_rules.split("\n")]
d = {}
for i in list_of_rules:

    d[i.split(":")[0]] = dict(((i.split(":")[j])[3:], (i.split(":")[j])[:3]) for j in range(1, len(i.split(":"))))

ans_7_2 = 1
f2 = ["shiny gold bag"]
d2 = {}
for k in f2:
    for i in d:
        j = [i for i in list(d[i].values())]
        g = 0
        for x in j:
            g += int(x)
        ans_7_2 += g
print(ans_7_2)'''

# day 8
string_of_programs = '''acc +3
jmp +599
nop +311
jmp +605
acc -3
acc +50
acc -6
jmp +461
jmp -4
acc -7
jmp +1
acc +19
acc -18
jmp +485
nop +182
jmp +174
acc +41
acc +10
nop +570
jmp +428
acc +18
acc +33
jmp +197
jmp +202
acc +43
acc -19
acc -12
jmp +453
acc +8
jmp +55
acc +5
nop +482
acc -11
jmp +475
acc -5
acc +38
acc -16
nop +111
jmp +230
acc +41
acc -4
jmp +16
nop +147
jmp -15
nop -28
jmp +96
acc +34
acc +27
jmp -25
jmp +8
acc +8
nop +28
jmp +515
jmp +247
jmp +474
nop +392
jmp +57
nop +271
acc +20
jmp +514
acc +22
jmp +337
acc +47
acc +43
acc +42
nop +263
jmp +144
acc +26
acc +49
acc +22
jmp +170
nop +502
acc +26
acc -3
jmp +96
acc -9
nop +213
acc +1
jmp +111
nop +189
jmp +533
acc -18
acc -15
jmp +209
nop +464
jmp +463
acc +16
acc +39
acc +36
jmp +499
acc +42
jmp +1
jmp +444
acc +33
acc -5
nop +513
acc +17
jmp +377
jmp +410
acc -5
jmp +312
jmp +235
acc -4
acc +32
acc +40
jmp +477
jmp +388
jmp +112
acc +45
acc +36
jmp -68
nop +296
jmp +496
acc -19
acc +1
acc -8
jmp +1
jmp +479
jmp +195
acc -13
acc +50
acc +30
jmp +167
jmp +217
acc +17
acc +8
jmp +22
acc +46
acc -5
jmp +53
jmp +152
acc +29
acc +1
acc +24
jmp +278
acc +20
jmp +95
acc +15
jmp +1
acc +36
jmp +286
acc +44
acc +33
jmp +117
acc +12
acc +16
jmp +1
jmp +284
acc -15
nop +478
acc -17
jmp +13
nop +274
nop +217
nop +91
jmp -113
nop -58
acc +11
acc +28
nop +301
jmp +132
acc -7
acc +18
jmp +173
acc +39
nop +435
jmp +388
acc +15
acc +50
jmp +152
acc -8
acc -10
acc +15
acc +39
jmp +166
acc +14
jmp +310
nop +371
acc +26
jmp +161
acc +37
jmp -147
acc -12
acc +37
nop -78
jmp +11
acc +5
nop -130
jmp +182
acc +23
acc +17
jmp -14
acc +42
acc +16
acc +40
jmp -39
nop +325
acc +15
jmp +70
acc +39
acc +13
nop +211
jmp +210
acc -18
nop +384
acc +28
jmp -98
acc +21
acc +12
jmp +217
acc +22
acc +4
acc +12
jmp +421
acc +26
nop +298
acc +1
acc +43
jmp -15
acc +39
nop +217
nop +31
acc +17
jmp -189
jmp -68
acc -14
jmp +287
nop +62
acc +20
acc +50
jmp -5
acc +26
acc -14
acc +24
acc -2
jmp -181
acc +12
nop -89
acc +13
jmp -50
acc +39
jmp +233
nop -214
acc +47
jmp +216
acc +21
acc +30
nop +347
acc +34
jmp -240
nop -196
jmp +345
acc +48
acc +43
acc +4
nop +266
jmp +72
acc +7
acc +43
jmp +1
acc +44
acc +1
acc +21
jmp +358
acc +20
acc +28
acc +48
jmp +266
acc +14
acc +30
jmp +167
nop +18
acc +17
nop +125
acc +14
jmp -111
nop +332
acc -12
nop -177
jmp +355
acc -8
jmp -125
acc +6
jmp -185
nop +270
acc +32
acc +19
acc -9
jmp +339
jmp -13
nop +23
jmp -109
acc -4
acc +23
acc +39
nop +305
jmp +130
nop -57
acc +46
jmp +301
jmp +1
jmp +150
acc -6
nop -184
acc +18
jmp -123
acc +11
acc +40
jmp -304
acc +16
acc +26
nop -307
jmp +3
jmp -194
jmp -224
acc +8
acc +22
acc +1
acc -1
jmp +73
jmp +41
acc +40
jmp +80
acc +0
acc +39
acc +6
acc +45
jmp -186
acc +32
acc -5
jmp -99
acc +47
acc +17
acc +1
acc +0
jmp +265
jmp +264
nop +114
acc +13
jmp -108
nop -278
acc +29
acc -14
jmp -297
acc +20
acc +37
nop +175
acc -4
jmp +9
acc -11
nop +136
acc +2
jmp -37
acc +48
acc +9
acc -7
jmp +36
acc -15
jmp -118
acc -9
jmp -68
acc +26
nop -1
acc +9
jmp -15
acc +21
acc +13
acc -2
acc -17
jmp -365
acc +5
acc +8
jmp +255
acc +16
nop -312
acc -14
jmp -19
acc +32
acc +37
acc +9
jmp +1
jmp -302
jmp +1
acc +5
acc +45
acc +42
jmp +61
acc +20
acc +36
jmp +156
acc -9
jmp +117
acc -1
nop -389
jmp +242
acc +9
acc -18
jmp -5
jmp -77
acc +17
acc +30
jmp +172
acc -1
acc +11
acc -6
jmp -334
jmp +215
acc +3
acc +24
jmp +13
jmp +1
jmp -369
acc +49
acc -6
acc -14
acc -6
jmp -234
acc +13
acc +9
acc +11
nop +78
jmp +115
nop -332
nop +177
jmp +109
jmp +157
nop -372
acc +25
jmp +166
nop +171
jmp -253
acc +27
acc -11
acc -4
acc +34
jmp +98
jmp -240
acc +41
nop -381
acc -4
nop -270
jmp -328
acc +31
acc +11
acc -2
nop -163
jmp +148
jmp +1
nop -91
jmp -197
jmp +132
acc +31
nop +109
acc +43
jmp -319
acc -19
acc +49
acc +38
acc +48
jmp +86
acc -1
acc -11
acc +2
jmp -355
acc -3
acc +11
acc +39
jmp -110
acc +10
nop -465
nop -121
jmp -110
acc +0
jmp -5
nop -278
nop -199
nop +118
acc +6
jmp -47
jmp +129
acc +26
jmp -391
acc -15
acc +8
nop -86
jmp +115
nop -94
acc -7
acc +14
jmp -183
acc -16
acc +15
acc +23
jmp -178
jmp +1
jmp -365
jmp +1
jmp -320
acc +42
nop -289
acc +21
acc -17
jmp -440
acc +0
acc +5
acc +35
acc +20
jmp +29
acc -1
acc +20
acc +44
jmp +50
jmp -61
acc -2
acc +41
acc -5
jmp -410
acc +13
nop -315
acc -2
jmp -46
acc +20
acc +9
acc +38
nop -279
jmp -113
acc +48
jmp +86
jmp -151
jmp +1
acc -18
nop -291
jmp -101
jmp +49
nop -378
jmp -445
acc +36
acc +41
nop -286
acc -19
jmp -142
nop -393
acc +0
acc -3
jmp +10
acc +17
jmp -327
jmp -219
acc -5
nop -123
acc +49
acc +36
jmp -145
jmp -496
jmp +48
acc +10
jmp +11
jmp -97
acc -8
acc +22
jmp +53
jmp -316
acc +32
acc -15
acc +27
acc +33
jmp -266
jmp -10
acc +48
acc -10
acc +7
acc +5
jmp +28
acc -15
acc -19
acc -8
nop -150
jmp -388
acc +14
acc +45
acc -11
jmp -451
acc +42
acc -8
jmp -104
nop -228
acc +0
jmp -327
acc +19
acc -7
jmp +1
jmp -291
acc -8
jmp -495
jmp -61
jmp -392
acc +1
jmp -227
acc -10
jmp -286
jmp -397
jmp -539
jmp -215
acc +15
acc +36
acc -12
acc +5
jmp -147
acc +28
acc -15
acc +19
jmp +16
jmp -493
acc +7
acc +40
acc +23
nop -122
jmp -567
acc -4
acc +23
jmp -218
jmp -13
acc -18
acc -10
acc -13
nop -541
jmp -105
acc +14
acc +40
acc +0
jmp -614
acc +3
acc +14
jmp -357
jmp -510
jmp -416
acc +12
nop -245
acc +26
acc +15
jmp +1'''
'''
list_of_programs = []
f = 0
for i in string_of_programs.splitlines():
    list_of_programs.append((str(f) + i).split(" "))
    f += 1
accumulator_value = 0
j = 0
visited = []
while list_of_programs[j][0] not in visited:
    if list_of_programs[j][0][-3:] == "nop":
        visited.append(list_of_programs[j][0])
        j += 1
    elif list_of_programs[j][0][-3:] == "acc":
        visited.append(list_of_programs[j][0])
        accumulator_value += int(list_of_programs[j][1])
        j += 1
    elif list_of_programs[j][0][-3:] == "jmp":
        visited.append(list_of_programs[j][0])
        j += int(list_of_programs[j][1])
        continue
        


def input_to_instructions(input_data):
    instructions = []

    split_input = input_data.splitlines()

    for item in split_input:
        instruction = {}
        opcode_operand = item.split()
        instruction["opcode"] = opcode_operand[0]
        instruction["operand"] = int(opcode_operand[1])
        instructions.append(instruction)

    return instructions
instructions =  input_to_instructions(string_of_instructions)
def accumulator_value_and_halt_at_first_repeat(instructions, switch_opcode_address=-1):
    program_length = len(instructions)
    program_counter = 0
    accumulator = 0
    executed_instructions = set()

    while 0 <= program_counter < program_length:
        current_instruction = instructions[program_counter]

        if program_counter in executed_instructions:
            return {
                "halted": False,
                "program_counter": program_counter,
                "accumulator": accumulator
            }
        else:
            executed_instructions.add(program_counter)

        opcode = current_instruction["opcode"]
        operand = current_instruction["operand"]

        if program_counter == switch_opcode_address:
            print(f"Changing opcode at address {program_counter}")
            if opcode == "jmp":
                print("- Changing jmp to nop")
                opcode = "nop"
            elif opcode == "nop":
                print("- Changing nop to jmp")
                opcode = "jmp"

        if opcode == "jmp":
            program_counter += operand
            continue
        elif opcode == "acc":
            accumulator += operand
        elif opcode == "nop":
            pass
        else:
            print("Something went wrong in accumulator_value_at_first_repeated_instruction().")
            print(f"pc = {program_counter} acc = {accumulator}")
            print(f"instruction:\n{instruction}")

        program_counter += 1

    return {
        "halted": True,
        "program_counter": program_counter,
        "accumulator": accumulator
    }


def run_instructions_with_mods(program):
    for index in range(len(program)):
        instruction = program[index]
        if instruction["opcode"] != "acc":
            print(f"Found jmp or nop at address: {index}")
            result = accumulator_value_and_halt_at_first_repeat(program, index)
            if result["halted"]:
                print(f"Found it! {result}")
                break
            else:
                print(f"Not the correct instruction.")
run_instructions_with_mods(instructions)
'''

# day 9
string_of_numbers = '''3
48
30
21
18
50
9
37
5
31
17
39
14
45
27
23
2
4
19
35
10
32
33
28
7
34
11
6
8
12
54
13
9
15
16
60
64
17
14
18
20
23
24
25
19
21
26
22
27
46
28
29
30
31
32
38
33
37
45
63
34
35
39
51
40
41
43
60
44
47
52
58
62
55
57
59
61
64
100
65
95
73
71
69
103
74
82
83
108
147
160
87
117
91
112
107
176
114
116
148
120
125
133
190
134
152
205
183
156
216
199
202
174
211
219
194
178
198
203
223
221
354
418
236
258
323
259
267
286
469
308
489
330
439
372
368
392
527
401
611
414
521
419
424
444
457
793
494
495
594
609
702
553
722
700
638
698
773
740
895
1130
815
951
833
838
843
868
1535
1239
1282
952
1578
1398
1794
2496
1725
1360
1293
1336
1378
1671
1438
1513
1635
2895
1648
1653
1681
2203
2491
1711
2671
2191
2617
2234
2245
2776
2629
2653
4306
2731
2774
2714
2816
5288
2951
3073
3148
4139
3301
5492
4282
5847
8038
3902
3945
5264
8578
8412
4479
4874
5592
5505
5367
5445
5488
5530
5665
5767
6449
8789
7203
7093
9967
7246
14243
13050
8424
12691
9433
9450
9353
10144
15649
12734
10241
10812
10855
13954
14234
11432
14191
17097
12216
14873
14296
15517
26882
15670
23596
17777
24440
17857
18786
39113
18803
19497
23028
21053
21096
21667
22287
23071
41164
35634
23648
26407
26512
27089
40885
29813
48756
45298
36766
36563
36580
40470
41784
40550
38300
44124
40593
70698
84717
43383
43954
67195
64198
50055
85689
60228
63173
53601
83933
87082
77236
73143
73329
73346
78347
77130
78850
110283
78893
82254
83976
114652
110578
93438
87337
117250
103656
113228
113829
116774
123401
126744
126930
150273
146472
183721
151490
146675
150476
180786
189176
263449
201166
210212
187632
297560
197094
190993
180775
339652
230002
216884
277017
230603
273877
376808
273216
273402
293147
296948
367360
297151
327450
474568
361561
368407
371768
377869
378625
490761
388087
411378
397659
503819
446886
447487
490100
504005
720703
571028
671772
546618
566549
590095
594099
624601
658712
689011
729968
733329
740175
1030480
756494
766712
785746
799465
809037
1135897
894373
936986
1218700
1246594
1050623
1140717
1471237
1113167
1171219
1156644
1313612
2055631
1763809
1347723
1418979
1463297
1523206
2187124
1661085
1542240
1552458
1722732
1703410
2186520
2007540
2679850
2698884
2163790
2893951
2191340
2253884
2269811
2284386
2327863
2470256
2766702
3070455
2811020
2870929
4890224
2986503
3203325
3094698
3213543
3275190
5837157
3426142
3710950
5364207
4335403
5753205
5569813
4355130
5704971
8664511
5198792
8564225
4612249
9131113
5236958
5577722
8450501
12090653
5857432
17695338
17454860
6416868
9003864
8690533
6701332
7137092
7761545
8947652
8967379
9534195
9553922
9592088
26385871
13618977
13687459
12994524
14141947
9849207
10814680
18299708
15449520
18042589
12274300
12558764
17353633
18559467
13118200
26681983
27136471
13838424
14898637
16709197
22548446
40823930
19383402
19146010
19441295
34282039
24747844
32158717
22843731
20663887
55722567
23088980
24833064
26112724
29912397
36794928
25676964
30471833
36386870
26956624
51285507
39552928
28737061
53723334
38529412
58935316
41989741
38587305
39809897
43752867
45411731
43507618
45496951
45932711
47620511
47922044
48765944
50510028
54414025
52633588
55693685
70709491
57428457
67324366
84462123
82094923
83317515
123343079
89610252
85306848
78397202
80577046
85742608
83562764
88919349
128907230
89440329
91429662
94698655
98130539
100555632
143854354
165454905
178707585
108327273
113122142
186724475
299846617
145721568
158974248
160492125
237151230
174917100
326591559
164139810
170017375
166319654
169305372
221449415
178359678
233294683
180869991
329594715
192829194
241984893
208882905
479136123
254048841
387242583
258843710
687089200
339844239
373022715
356969004
319466373
324631935
375202559
330459464
333445182
350175363
335625026
362134566
809595587
373699185
359229669
500336364
510464706
434814087
450867798
462931746
467726615
615812714
584508305
1006555573
692594030
693165558
644098308
658077117
649925837
829931079
694854695
978191321
663904646
1066293215
709405032
697759592
869694375
732928854
1117652452
943737974
1132573679
961332504
885681885
913799544
930658361
1488008196
1200321019
1293913337
1294024145
1302175425
1341857900
1308002954
1313830483
1344780532
1625237150
1358759341
1407164624
1361664238
1827057484
1430688446
1567453967
1212510616
2269335458
1799481429
2086002904
1816340246
1844457905
2126310160
2114120563
3120970821
2412831635
2559080360
2506423953
2506534761
2837853070
2675494721
2520513570
2526341099
2557291148
2571269957
2619675240
2574174854
3615821675
3247028692
3298513520
3326631179
5201835820
3643939334
6203019694
3930460809
3660798151
5900806033
4240430723
5088326356
4919255588
4919366396
5065615121
5012958714
5027048331
6218114188
5094688424
6142162774
5083632247
5818298649
5190945197
5918188760
9534010435
6545542212
8849827205
6625144699
9244819939
8862633971
7304737485
7591258960
12399425909
7901228874
9159686311
9159797119
9838621984
9932214302
9932325110
10040007045
10096590961
10110680578
15352309084
17483058156
13446900259
14216403659
11009243846
21348129133
12463730972
19199804164
13170686911
16557359001
13929882184
14895996445
19768468457
15492487834
24148617961
17060915185
18319483430
20028916071
37519287594
31186751117
19972332155
21049250891
20136598006
41185848897
21119924424
33984872116
23472974818
28939388093
25905240291
24179930757
25634417883
36260719349
51449169778
43501890889
39797384528
28825878629
62810750745
38965462652
39641105795
84687739786
37197513191
38291815585
40001248226
49814348640
75226182001
40108930161
41256522430
43609572824
44592899242
45299855181
62165959640
60440650106
50085171048
64599880535
53005809386
54460296512
65086597978
79906314689
81901388409
66023391820
67117694214
75489328776
76162975843
76838618986
109192779777
142607022990
112251130688
93114739547
119060177047
81365452591
111323247001
95385026229
88202472066
89892754423
185355755620
136361684921
103090980434
104545467560
120483688332
129168785229
119546894490
169953358533
133141086034
141512720596
142862010806
165041091052
151652304619
153001594829
158204071577
271199199109
391682887441
169567924657
171258207014
339521283190
176750478820
270681505825
543335192060
178095226489
192983734857
207636447994
232259765663
222637874924
224092362050
240030582822
248715679719
252687980524
346318403477
274653806630
309856376196
311205666406
321220229276
426306111249
324259801843
584510182826
340826131671
547157731184
543858104200
766495979124
546897676767
354845705309
523369486349
504189401263
402187588539
433014317679
472808041769
859163989456
446730236974
712043964735
527341787154
620972210107
562544356720
598913608473
585859473036
825409630539
666051371715
930495512512
979911994446
679105507152
827653747078
743013720210
757033293848
990588341174
787860022988
801575942283
1507253781600
835201906218
1364120299003
848917825513
1206831683143
919538278743
1514307413370
974072024128
1089886143874
1148313997261
1161457965193
1148403829756
1918491259041
1264964980188
1656639712889
1345156878867
1422119227362
2180903707271
1436138801000
2355677079743
1500047014058
1544893316836
2818097678082
2368289648336
1650493767796
1754740184961
2493470876128
2063958168002
1768456104256
2576177991632
2080996243936
2950446214370
2526024944874
2238289973630
2296717827017
2413368809944
2648450843814
3268503118314
2845203892925
4248211061089
2781295679867
2858258028362
4018783416132
2936185815058
4704641919314
3313349421092
3195387084632
3405233952757
3418949872052
3523196289217
5081805525348
4494365053880
3832414272258
5258572702869
5232903642075
8952852980403
6508736505724
7555290529886
7807714474972
5584636658872
8780023743504
5794443843420
6171607449454
6200245551919
10666442184220
5639553708229
8638137594832
9366994534086
6355135687110
6600621037389
10341150777982
8834940792861
7913314925932
7355610561475
8326779326138
9417050931130
13979321924426
13199408806344
10491476344944
10817540300947
16541396329901
11224190367101
12800866589308
11379080502292
11433997551649
11811161157683
11839799260148
11994689395339
13552868634161
18166296844793
12240174745618
12955756724499
18579800928576
21112723732276
16748255718793
16772661492605
15682389887613
15268925487407
17743830257268
28588054978941
20641241298231
26780188513734
22331275605092
40497572449885
23674172297267
23428686946988
27522189147761
23245158709332
22813078053941
23273796811797
28583822650288
29704012443292
27922564633231
40823997395906
43454319352172
25195931470117
30699586981767
30951315375020
60655327818312
32455051380218
43204579035374
33012755744675
55728848192015
49229296277172
42972516903323
59792944258409
45144353659033
52012509597276
50950876094749
46058236763273
57226201591053
46086874865738
48441090179449
48009009524058
84028576431280
53118496103348
80464060904276
105659992374393
56147246845137
57650982850335
94985026500599
61650902356787
63406366755238
78541926245956
79099630610413
98959885618807
75985272647998
130050506705162
88116870562356
89030753666596
91202590422306
93585443838482'''
'''
list_of_numbers = [i for i in string_of_numbers.splitlines()]
for i in range(len(list_of_numbers) - 25):
    sliced_list = list_of_numbers[i:i+25]
    list_of_permutation_sums = [int(i[0]) + int(i[1]) for i in itertools.permutations(sliced_list, 2)]
    if int(list_of_numbers[25 + i]) not in list_of_permutation_sums:
        invalid_number = int(list_of_numbers[25 + i])
        print(int(list_of_numbers[25 + i]))
        break

for i in range(len(list_of_numbers) - 1):
    sum_ = 0
    j = 0
    # noinspection PyUnboundLocalVariable
    while sum_ < invalid_number:
        sum_ += int(list_of_numbers[i + j])
        j += 1
        if invalid_number == sum_ + int(list_of_numbers[i + j ]):
            ist_2 = [int(i) for i in list_of_numbers[i: i+j]]
            print(len(ist_2))
            print(int(min(ist_2)) + int(max(ist_2)))'''

# day 10
string_of_adapters = '''8
131
91
35
47
116
105
121
56
62
94
72
13
82
156
102
12
59
31
138
46
120
7
127
126
111
2
123
22
69
18
157
75
149
88
81
23
98
132
1
63
142
37
133
61
112
122
128
155
145
139
66
42
134
24
60
9
28
17
29
101
148
96
68
25
19
6
67
113
55
40
135
97
79
48
159
14
43
86
36
41
85
87
119
30
108
80
152
158
151
32
78
150
95
3
52
0
49'''
'''
list_of_adapters = [int(i) for i in string_of_adapters.splitlines()]
list_of_adapters.sort()
def calculate_diffs(data):
    return [data[i] - data[i - 1] for i in range(1, len(data))]
counts = collections.Counter(calculate_diffs(list_of_adapters))
print(counts[1] * (counts[3] + 1))

from collections import defaultdict

def count_seqs_1(diffs):
    c = 0
    res = defaultdict(int)
    for n in diffs:
        if n == 1:
            c += 1
        else:
            if c > 1:
                res[c] += 1
            c = 0
    if c > 1:
        res[c] += 1
    return dict(res)

seqs = count_seqs_1(calculate_diffs(list_of_adapters))

mults = {2: 2, 3: 4, 4: 7, 5: 13}
tot = 1
for l, n in seqs.items():
    tot *= mults[l] ** n

print(tot)'''

# day 11
string_of_layout = '''LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLL.LL.LLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLL.LLLLL
LLLLLLLLL.LLLLL.LLLLL.LLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL..LLLLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLL..LLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLLL.LLLLLLLLLLLLL.L.LL.L..LLLLL.LLLLLLLL
LLLLLLLLL.LLLLLLLLLLL.LLLL.LLL.LLLLL.LLLLLLLL.LL.L.LLLLLL..LL.LLLLLL.LLLL..LLL.LLLLLL.LLLLLL.L
LLLLLLLL..LLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLL.LL.LLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLL.LLL..LLLLLL.LL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
.LLL..L..........L.LL.LL..L..L.....L.....L.....L..L..L....L..L..LL..L.L..L..LLL..LL...L.LLLLL.
.LLLLLLLL.LL.L.LLLLLL.LLL..LLLLLLLLL.LLLLLLLLL.LLL.LLLLLLLLLL.L.L.LLLLLLLLLLLL.LLLLLLLLLLLLLLL
LLL.LLLLL.LLL.L.L.LLLLLLLL.LLLL.LLLL.LLLLLLLL...LL.LLLLLLLLLLLLLL.LLLLLLLLLL.L..LLL..LLLLLLLLL
LLLLLLLLLLLLLLLLLLLLL.L.LL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLLL.
LLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLL.L.LLLL.LLLL.LLLLLLLLLL
...LL.L......LL.......LLL...L.LL.LLL.L..L...L.L.LL...L.LLL.....L...L..L......L..LLLL........L.
LLLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLL.L.LLLL.LL.LL..LLLL.LL.LLLLLLL.LLLL.LLLL..LLLL.LLLL
LLLLLLL.L.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLL.LLL
.LL.LLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLL.L.LLLLLL.LLLL.LLL.LL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLLL..LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLL..LLL.LLLLLLLLL.L.LLLLLL.LLLL.LLLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLL.LL
LLLLLLLLL.LLLL..LLLLL.LLLL.LLLLLLLLLLLLLLL.LL.LLLL.LLLLLL.LL..LLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLL
LL...L.L.LL.L....LL..L..L.L.LL.L..L.L...L.LL..L.L..L....L.....L.L.L.L.......L....L.....L..LLLL
LLLLLLLLL..LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.L.LLLLL.LLLLLL..L.LLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL..LLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLL.LLLLLL..LLLL.LLLLLLLLL.L.LLLLLL...LL.L.LLL..LLLLLLL.LLLLL.L.LLL.LLLLLLLLLLL.LLLL
LLLLLLLLLLLLLLL.LLLLL.LL.LLLLLLLLLLL.LLL.LLLL.LLLL.LLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
.L..LL.L.L......LL..L..L....LL.LLLLL.L.L.L.....L.L...LLL.LL...LL..L......L....L.LL..L...L.L...
LLLLLLLLL.LLLLL.LLLLL..LLL.LLLLLLLLL.LLLLLLLL.L.LL.LLLLLLLLL.LLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLL.LLLLL.LL.LLLL.LLLLLLLLLLLLLL.LLL.LLL.LLLL.LLLL.LLLLLLLLLL
.LLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LL..LLLLLLL.LLLLLLL.LLLLLLL.LLL..LLLL.L.LLLLLLLL
L.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLL.LLLL.LLL.LL.L.LLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LL
LLLL.LLLLLLLLLL.LLLLL.LLLL.LLLLLLLL..LLLLLLLLLLLLL.LLLLLL.LLL.LLL.L.LLLLLLLLLL.LLLL.LLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLL.LLL.LL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
L.LLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLL.LLLL.L
LLLLLLLLL.LL.LL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.L.LLLLLLLLLLLL.LLLL.LLLLLLLLLL
LL..L.L.LL..L..L.LLLLL.L.L......L..L.....L..LLL.L...LL.........L...L.........LL...LL...L..L...
L.LLLLLLLLLLL.L.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLLLL
LLLLLLLLL..LLLL.LLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL.LLL.LL.LLLLLLL.LLLLL
LLLLLLL.L.LLLLLLLLLLL.LLLL.LL.LLLLLL.LLLLLLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLL.LLLLLLL.LLLLLLL.LLLL
LLLLLLLLL.LLLLL..LLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLL.LLLL
LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLL.LL.LLLLLLLLLLL.LLLLLLL.L.LL.LLLL.LL.LLLLLLL
LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLL.L.LLLLLL.LLLLLLLLLL.LLLL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLL
...L......L.L...L...L...LL..LL..LLLL..L....LLLL....L...L.L.....LL..LL...LL........LL..L.L...LL
LLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLL.LL.LLLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL..LLL.LLLL.L
LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLL.LL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LL.LLL.L.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLL
..L.L..LL.....L....LL.L.L.L..LLL......L..LLL..L..L....LL..L.LLL..L.....LL.L.L...........L..L..
LLLLLLLLLLLLLL.L.LLLL.LLLL.LL.LLLLLL.LLLLLLL..LLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLL.L.L
.LLLLLLLL.L.LLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLL.LLLLLLLLL.LL.LLL.LLLLLLL.LLLLLLL.LLLL.LLLL.LLLLLLLLL.
..LLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLL.LLLLLLLLLL
.L..L..LL..L.L.L.L...L..LL............L..LL..LL.L.L.........LL.....L...L.L.LLL.L.L..........L.
LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL..LLLL.LLLLLL.L.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLL
LLLLLLLLL.LLLLL.L.LLL.LLLL.LLLLLLLLLLLLLLLL.L.LLLL..LLLLLLLLLLLLL.LLLLLLL.LLLL.LL.L.LLLLLL.LLL
LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLL.L.LLLLLL.LLLL.LLLL.L.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLL.LL.LLLLLLL.LLLLLLL.LLLL.LLLL.L.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLL.LLLL..LL.LLLLLLL.LLLLLL.LLLLLLLLLLL.LL.LLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL.LL.LLLLLLLL.L.LLLLLL.LLLLLLL.LLL.L.LLLLLL.LLLL.LLLLLLLLLL
LLL.LLL.LLLLLLL.LLLLL..LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLL.LL.LLLLLLL.LLLLLL..LLLLLLLLL.LLLLLLLLLL
....L.L..L.L..L....L.L..L............LL.............L......L.L....L....L..L.LL.........LLL..L.
LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLL.L.LLLLLLLLLL.LLLL.LLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLL.LLLL.LL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLL..LLL.LLLL.LLLLLL.LLL
LLLLLLLLL.LLLLL.LL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.L.LLLLLLL.LLLL.LLLLLLLLLLLLLLL
LLLLLLLLL.LL..LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLLL..LLLLLLL.LLLLLLLLL.LLLLLLL.LL
.LL..L..L..LLL...L..LL.L...LL..L.....L.L...L.L...L.L..L.L........L.L..L.L..L....L.....L..L..LL
LLLLLLLLL.LLLLLLLLLL..LLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLL.LL.L.LL.LLLLLLL
LLLLLLLLL.LLL.L.LLLLLLLLLL.L.LLLLLLLLLLLLLLLLLLLLL.LL.LLL.LLLLLLL.LLLLL.LLL.LL.LLLL.LLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLL.LLLLLLL..LL.LLLLLLLLLLLLL.LLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLLLL
LLL.LLLLLLLL.LL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLL.LLLL.LLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLL.LLLLLLLLLL
..L....L........L....LL..L...LL.L.....L.LL.L..L....L....LL......L.L.....L.L..LL..L.....L.LLL.L
LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLL.LLLL.LLLLLLLLLL.LLLL.L.LLLLLLL.LLLLLLLL.LLLL.L.LLLL.LLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLL
LL.LLLLLL.LLLLL.LLL.LL.LLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLL.LLL.LLLLLLLLLLLL.LLLL.LLLLLLLL.L
LLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLL.LLLLLLLLLL.LLLLLLLLLLL.LLLLLL.L.LLLLLL.LLLL.LLLL.LLLLLLL.LL
LLL.LLLL..LLLLLLLLLLL.LLLL.LLLLLLLLL..LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLL..LLLLLLLLLLLLL.LLLLLLLLL.LLL.LLLLLL.LLLLLLL.LLLLLLLLLLLL.LLL..LLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL..LLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLL.LLLLL.L.LL.LLLLL.LL.LLLLLLL.LLLLLLLL
LLLLLLLLLLL.LLL.LLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLL.L
...LL.L..L...LL...LLL.........L.L.L..L.....LLLL.LL....L..L...L...LL..L..L......L..LLLL....L..L
LLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLL.L.LLLLLL.LLLL.LLLL.L.LLL.LLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLL
LLLLL.LLL.LLL.L.LL.LL.LLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLLL.LLLL.L.LLLLLLL..LLL.LLLL.L.LLLLLLLL
LLLLLLLLLLLLL.L.LLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLL..LL.L..LLLLLLL.LLLL.LL.LLLL.LLLL.LLLLLLLLLL
LLLLLLLL..LLLLLLLLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLL..LL.LLLLLL.L..LLL.LLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLL.L.LLLLLLLL
.L....L.LL...L...LL......LL..........L.LLL...L...L..........L.........LL..L.L.L...L..L........
LLLLLLLLL.LLLLLLLLL.L.LLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLL..LLLLLLLLL
LLLLLLLLL.LLLLL.LL.LL.LLLL.LLLL.LLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLL.LLLLLLL.LLLL.LLLL.LLLLLLLLLL
LL.LLLLLL.LLLLL.LLLLL.LLLL.LL.LLLLLL.LLLLL.LL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLL
LLLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLLL.LL.LLLLL.LLLL.LL.LLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LL
LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLL..LLL.LLLLLL.LLLLLLL.LLLLLLL.LLLL.LL.LLLLLLLLLLLL
LLLLLLLLLL.L.LL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLLL.L.LLLLL.LLLL.LLLLLLLLLLLLLLL'''
'''
lines = [line.rstrip() for line in string_of_layout.splitlines()]
lines = [list(line) for line in lines]

rows, cols = len(lines), len(lines[0])
deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def check_occupied(lines, thresh=4):
    def count_occupied(r, c, grid):
        count = 0
        for i, j in deltas:
            xi, xj = r + i, c + j
            if 0 <= xi < rows and 0 <= xj < cols and grid[xi][xj] == '#':
                count += 1
        return count
    while True:
        valid = True
        temp_grid = [r.copy() for r in lines]
        for i, r in enumerate(temp_grid):
            for j, c in enumerate(r):
                count = count_occupied(i, j, temp_grid)
                if c == 'L' and count == 0:
                    lines[i][j] = '#'
                elif c == '#' and count >= thresh:
                    lines[i][j] = 'L'
                valid &= (r[j] == lines[i][j])
        if valid:
            break
    ans = 0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == '#':
                ans += 1
    print(ans)


def check_occupied2(lines, thresh=5):
    def count_occupied2(r, c, grid):
        count = 0
        for i, j in deltas:
            xi, xj = r + i, c + j
            while 0 <= xi < rows and 0 <= xj < cols:
                if grid[xi][xj] == '#':
                    count += 1
                    break
                elif grid[xi][xj] == 'L':
                    break
                xi += i
                xj += j
        return count

    while True:
        valid = True
        temp_grid = [r.copy() for r in lines]
        for i, r in enumerate(temp_grid):
            for j, c in enumerate(r):
                count = count_occupied2(i, j, temp_grid)
                if c == 'L' and count == 0:
                    lines[i][j] = '#'
                elif c == '#' and count >= thresh:
                    lines[i][j] = 'L'
                valid &= (r[j] == lines[i][j])
        if valid:
            break
    ans = 0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == '#':
                ans += 1
    print(ans)

check_occupied(lines)
check_occupied2(lines)'''

# day 12
string_of_directions = '''F99
L180
W1
W3
R90
E5
R180
S4
F55
L90
E5
S3
R180
N2
W3
S1
F64
W4
F76
N2
F7
L180
S2
E5
S2
F87
N4
L90
F46
R90
F47
W5
N4
L270
N5
F89
L180
W2
N5
F69
E3
L90
F73
L90
N1
F28
N4
F72
L90
F24
R90
S1
F52
L90
W2
F39
E1
L180
S4
W1
S2
F61
E3
F37
S1
W3
F8
S5
L90
N5
E2
L180
F44
W3
S1
R90
F88
N1
F75
S2
W2
F37
N4
E3
R90
F47
N5
W5
L90
S4
E5
F7
R90
E5
R90
W2
F56
S2
R270
S1
W3
S2
W2
F79
W4
N5
W3
F84
L90
N5
E2
F48
E1
L180
E4
L90
W4
E4
S4
W4
F36
F93
L180
W5
S1
E5
F96
N3
E3
N2
R270
W5
L180
F24
W5
S5
R180
W1
N5
F6
R90
E1
F52
F77
W4
F34
S3
R90
E1
E5
N5
E1
S5
R90
W5
N4
E3
W3
L90
E2
L90
W3
W5
F49
N1
F48
W3
N4
E4
F100
E1
R90
F25
S1
W2
N2
W1
F25
L90
E2
F96
W2
S1
S4
F91
N2
R90
W4
L90
E4
F78
L90
S1
W3
F56
R90
W1
E4
L90
N5
E1
R90
F53
E5
L90
E2
F82
E4
L90
W2
L180
F51
R270
F37
N5
F15
E4
F16
E2
S1
E4
F91
N4
E5
N5
L90
F9
W2
F64
S4
F72
W2
F31
S4
R90
F40
W3
R90
F50
S1
F61
W3
F90
N5
F76
S1
L90
E3
R180
F19
L90
W3
F70
E3
F35
R90
L90
N1
W5
R180
E2
N5
F34
W4
S1
E1
N5
E1
N2
R90
W4
S1
L180
E5
F59
E1
R90
S2
L90
S4
R90
W2
N5
F60
W1
R90
F35
R270
W5
F100
W2
R90
N2
S5
S3
E1
S2
F36
W1
F90
R90
S3
E3
F5
S4
R90
E3
R90
N3
L90
S1
F74
S2
R180
E4
S5
F13
S3
E2
F92
N5
F2
N4
F3
E2
L180
W3
N3
L90
E4
F21
W1
F76
W5
F56
E4
R180
F100
E1
F29
L90
F96
N2
F43
R90
F26
N3
F15
L180
E3
R180
N3
E3
R90
F7
L90
W2
F33
R90
E5
S4
E2
E3
F34
F66
N4
F14
W3
N2
R270
F66
E4
S5
W5
R90
S5
W5
L90
S4
L90
F69
E5
R90
W5
S5
W4
R90
N3
E4
F14
W3
F24
S3
F48
L180
E1
R90
F36
N4
L90
F68
E4
F59
E5
R90
N2
E4
N5
F56
R90
R90
F91
W3
F24
L90
F56
S5
F59
S4
F36
N1
W3
R270
L90
F86
L180
F33
N5
E4
L90
F14
S3
L90
N5
L270
E5
S4
L180
W5
N2
L90
E3
F69
R90
S5
R270
N3
F70
E2
N2
F3
R90
S5
L180
F59
W3
F67
R180
F74
E4
F4
L90
N4
R90
S5
F6
S1
E3
N4
W3
F24
E1
S1
E4
S2
F82
N3
L90
E1
S2
R270
N4
E1
N3
F32
R270
W4
R90
E4
F33
N5
W3
F34
E2
S1
W3
W4
E2
L90
N5
W3
S1
F86
E4
F99
S1
L90
S2
E2
L90
F100
N5
F19
L180
W1
F25
N3
F25
R90
W4
N4
R180
N2
E5
R90
F66
N5
E2
L180
L90
E1
S2
R90
W3
S1
S2
L90
F93
L90
W2
R270
F73
N4
L90
F44
R90
N1
W3
R90
F69
N5
L90
N1
R90
F35
F89
E4
F31
W3
R270
W1
N2
E5
L90
W4
W1
F93
E4
F18
N4
F31
W5
N4
L90
N1
E2
R270
F34
N5
W2
L270
W3
F44
S3
F47
W2
F86
N4
R90
S5
R90
F4
E3
L180
W5
R180
F89
L180
F46
N3
F76
R270
S2
F62
R90
S2
F28
R180
F47
E4
N4
R90
S4
E3
R180
N1
F92
R180
F86
N3
R270
F47
E4
S4
W2
F67
N5
W3
N1
F98
S1
E4
N3
F97
E3
F69
E3
F38
E3
S4
E5
F81
E3
F5
E3
R90
W2
N4
W3
F94
L180
F30
N1
F91
S3
F89
E1
F68
N5
E5
F89
L90
W1
N5
F79
R90
F44
E4
R90
S1
L90
E5
N3
R90
W3
N4
F83
E5
S4
F82
S2
F29
R90
S1
R180
F49
E5
N1
L180
R180
S3
L180
S3
F55
S3
F70
W5
N2
W2
R90
W1
F93
L180
L90
R90
L90
E3
L90
S3
R90
W5
N4
R90
S1
R90
W5
F100
W4
N2
F84
F76
E5
L180
S4
F85
R90
L90
F68
R90
S4
W2
L90
E1
F19
N2
L90
N4
E5
N1
L90
F75
F42
R90
S5
E4
N1
E4
F7
N5
L180
N4
E5
L270
F6
R180
W5
F93
L180
S1
R90
F66
N4
F83
N1
F10
S2
L90
F80
W1
R180
E2
L90
S4
F53'''
'''
list_of_directions = string_of_directions.splitlines()
instructions = [(line[0], int(line[1:])) for line in list_of_directions]

direction = 90  # east
x, y = 0, 0

for instruction in instructions:
    letter = instruction[0]
    value = instruction[1]

    if letter == "N":
        y += value
    elif letter == "S":
        y -= value
    elif letter == "E":
        x += value
    elif letter == "W":
        x -= value

    elif letter == "R":
        direction += value

    elif letter == "L":
        direction -= value

    elif letter == "F":
        if direction == 0:  # north
            y += value
        elif direction == 90:  # east
            x += value
        elif direction == 180:  # south
            y -= value
        elif direction == 270:  # west
            x -= value

    direction %= 360

print(abs(x) + abs(y))


def rotate(x, y, degs):
    # rotate clockwise
    c = round(math.cos(math.radians(degs)))
    s = round(math.sin(math.radians(degs)))
    return (x*c - y*s, x*s + y*c)

x, y = 0, 0
wp_x, wp_y = 10, 1
for line in list_of_directions:
    match = re.match('^(\w)(\d+)$', line)
    direction = match.group(1)
    mag = int(match.group(2))
    if direction == 'N':
        wp_y += mag
    elif direction == 'S':
        wp_y -= mag
    elif direction == 'E':
        wp_x += mag
    elif direction == 'W':
        wp_x -= mag
    elif direction == 'L' or direction == 'R':
        orientation = mag if direction == 'L' else 360-mag
        wp_x, wp_y = rotate(wp_x, wp_y, orientation)
    elif direction == 'F':
        x += wp_x * mag
        y += wp_y * mag
print(abs(x) + abs(y))'''

# day 13

input_string = '''1000340
13,x,x,x,x,x,x,37,x,x,x,x,x,401,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,613,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41
'''
'''
input_list = input_string.splitlines()
input_list[0] = int(input_list[0])

input_list[1] = [int(i) for i in list(dict.fromkeys(input_list[1].split(","))) if i != "x"]
list1 = [(i - input_list[0] % i, i) for i in input_list[1]]
print(min(list1)[0]*min(list1)[1])


data = [i.strip() for i in input_string.splitlines()]
buses = [(int(value), offset) for offset, value in enumerate(data[1].split(",")) if value.isnumeric()]
part2 = buses[0][0]
increment = 1
def find(ans, bus_value, bus_offset):
    while True:
        if (ans + bus_offset) % bus_value == 0:
            return ans
        ans += increment
for bus in buses:
    part2 = find(part2, bus[0], bus[1])
    increment *= bus[0]


print(part2)'''

# day 14
bitwise_data = '''mask = 11100XX0000X1101X1010100X1010001XX0X
mem[24196] = 465592
mem[17683] = 909049
mem[28999] = 20912603
mem[22864] = 7675
mem[55357] = 6401
mem[47006] = 1087112
mask = 111X000100XX1X01X1X10X01X11101100010
mem[22535] = 42768
mem[3804] = 1432484
mem[5475] = 5972
mem[24585] = 484096364
mem[56009] = 206637948
mem[30917] = 630
mem[28325] = 1467510
mask = 1110X0X0001111011101101011X01000X10X
mem[432] = 23010545
mem[31135] = 250
mem[60949] = 3366
mask = X10101X10X0X100111X11001X0001X11X011
mem[19601] = 169998617
mem[25958] = 295048
mem[277] = 58248
mem[47301] = 2234
mask = 1X101110000001X1101X101X000010101101
mem[27397] = 328720
mem[23718] = 91033
mem[42581] = 1336
mem[39656] = 58221
mask = 101000100011110111X110111011XXX00000
mem[55993] = 21914
mem[8278] = 287934896
mem[7186] = 199312871
mem[35770] = 128786
mem[13001] = 1187
mem[5951] = 34516681
mask = 1110000000101X0X1101100000X11X010001
mem[51573] = 6865197
mem[12594] = 57
mem[43156] = 1988185
mem[194] = 125226832
mem[11055] = 1304
mem[8009] = 15347
mem[39550] = 434
mask = 0100X10X0100X000101001X10X1101001111
mem[4865] = 6399850
mem[54408] = 1063909
mem[37625] = 391570382
mem[15539] = 3309
mask = 1X1000XX0XX01X00110X1101110X0X001110
mem[8011] = 39113
mem[4279] = 54926
mem[24196] = 66470405
mask = 10X0000000X0110X1X01X1X0X001111X1011
mem[9092] = 362810946
mem[47138] = 16850639
mem[41856] = 18821263
mask = 1110000X00X01101X1010XX101010X0XX0X1
mem[50504] = 27298
mem[57026] = 107914
mem[52684] = 127977723
mem[12905] = 3044843
mem[23942] = 34437
mem[18697] = 94002
mask = 1110X010100X11X1110111011101110X1XX0
mem[50504] = 28170
mem[56861] = 48063
mask = 1110101000X001X110110010000X0110XX01
mem[31344] = 15906303
mem[49101] = 18755
mem[50877] = 5126106
mem[27011] = 29112904
mem[11552] = 184372544
mem[27085] = 1711926
mem[57734] = 11
mask = 01X10X000000110110011010X10X000010X0
mem[57703] = 450
mem[55911] = 897776
mem[39593] = 9365920
mem[27918] = 111787
mask = 11100010X0X1110X0X000010X0X00000110X
mem[21285] = 142940
mem[48827] = 1348
mem[47138] = 791004800
mem[17054] = 170726381
mask = 1X1X00X000XX110111010X10XX101X001001
mem[33192] = 5106641
mem[44523] = 205714
mem[2397] = 481
mem[55624] = 3188
mem[26269] = 3891595
mem[14130] = 17865
mem[45278] = 995854
mask = 0101010100011XX1111101000X0X11110000
mem[54355] = 118
mem[37759] = 26260
mem[17076] = 89114435
mem[194] = 1039
mask = 11100001011X1X0X110X100XX1X00000X111
mem[56508] = 5551
mem[24388] = 8654
mask = 1111001010101101110111X10XX0100X1100
mem[54164] = 209
mem[51296] = 377456
mem[17932] = 27062366
mem[6263] = 5509
mask = 00X1010X00001X0X11X101001011X0000000
mem[19882] = 8803576
mem[53384] = 3337517
mem[56996] = 28569
mem[45196] = 176
mem[35228] = 451184
mem[28999] = 1358694
mem[11073] = 106613
mask = 0XX101010X001101110100001XX1101X0000
mem[18074] = 29316
mem[18560] = 6691478
mem[11628] = 29149
mem[17246] = 4374
mem[7371] = 596
mask = X10X01XX00001101X101X10010011X1000XX
mem[20505] = 833
mem[51543] = 514
mem[33874] = 1486233
mask = 01X10101010000011111000101100XXXX111
mem[41142] = 8151
mem[57816] = 850
mem[3408] = 25361551
mem[49742] = 84
mem[533] = 4697
mask = 1100X010X100XXX011010X00XX01000X1010
mem[18925] = 6495
mem[51352] = 2712
mem[35009] = 237034
mem[46199] = 6606255
mem[58066] = 10080453
mem[248] = 176262
mask = 111XX0X0X0X011X11X010001000100X11100
mem[56816] = 26145436
mem[6953] = 387283
mem[50052] = 84
mem[56530] = 141676
mem[60168] = 10908459
mem[17685] = 287
mask = 111000010X1011011X010111X1110111001X
mem[52094] = 1398677
mem[36982] = 4553
mem[24348] = 1001783
mem[28987] = 11213376
mem[14039] = 7011973
mem[52684] = 287185
mask = 11110010X01011XX1XX110X1001110111100
mem[17212] = 36655
mem[24740] = 10507
mem[7497] = 2603
mask = 11X0000100001XX10101X011X0100XX01100
mem[8722] = 1860757
mem[4361] = 9089027
mem[43286] = 764265
mask = 111000X00X00110111110X000101000X0101
mem[21] = 10308359
mem[55077] = 1923265
mask = 11100X001010110111010XX1101X00011X01
mem[51543] = 272
mem[46636] = 41481200
mem[11331] = 16116
mem[4157] = 24217194
mem[39683] = 36276
mem[47837] = 75704
mask = 001XX10100X0011111010X00X11000011010
mem[64404] = 3069125
mem[432] = 42797141
mem[11073] = 655
mem[17402] = 687682
mask = X1111X100000111X100X11X0110X11XX1110
mem[5138] = 3437645
mem[64302] = 10748
mem[22052] = 7646851
mem[57307] = 1846
mem[8556] = 2513
mem[20862] = 2137
mem[47082] = 65210668
mask = 111000X0XX011001011X01110X0X111X0000
mem[24216] = 140969206
mem[64406] = 1006
mem[55744] = 282152566
mem[26368] = 8935044
mem[9525] = 581
mask = X10XXX010X0X00001110101111X0X0010001
mem[37409] = 830
mem[55256] = 1293327
mem[49887] = 10300024
mask = 11100010000111010X0X0X10XX1X1X010010
mem[7371] = 10089034
mem[55184] = 992391
mem[8128] = 2573
mem[16780] = 12198200
mask = X110010X00001101110X1X0X1001X01X1X00
mem[17942] = 3204736
mem[43265] = 160130
mem[54791] = 905
mem[43494] = 31105546
mem[23836] = 5693
mask = 01X10001X100000001000111111X0101X010
mem[52752] = 261536
mem[33121] = 637759448
mem[38648] = 1999
mem[10484] = 4506
mask = X1100001000XX101X1X11010001X1X00X00X
mem[11033] = 303386685
mem[52968] = 76
mem[692] = 80215
mem[32901] = 410
mem[1170] = 1019569
mask = 0100010X000011XX010101001XX0X111X110
mem[33121] = 1004697269
mem[40768] = 9652471
mem[46911] = 51740
mask = 0111010X000011XX100101000100011X1011
mem[31501] = 127217457
mem[8760] = 1331
mem[53277] = 100190787
mem[11055] = 816674979
mem[20322] = 5235075
mask = X1X10X0X000011011X01011X11X1000X110X
mem[34070] = 743
mem[7184] = 550637
mem[19585] = 921346
mem[9587] = 217676716
mask = 111010100000X101X0110000XX1000X10000
mem[28281] = 77
mem[38263] = 1881
mem[28451] = 444240911
mem[43156] = 25309
mem[30888] = 660
mem[2469] = 454
mask = 11X00X100X00110X110100X00001101X01X1
mem[22535] = 480526992
mem[64908] = 1012
mem[18554] = 30457232
mem[7497] = 896738
mem[21289] = 56826187
mem[51296] = 467
mask = 1110001X00X111X1X101010X01010101X001
mem[55693] = 18382
mem[27601] = 41915
mem[22616] = 17257
mem[19492] = 4667
mem[6953] = 40034760
mask = 1X11000000X0X10X1X0X0010110XX1001110
mem[36049] = 431
mem[53464] = 3399
mem[47435] = 3768554
mem[13326] = 10597
mask = 1X10000000011001011001X10000110X01X1
mem[116] = 17770
mem[23833] = 174842
mem[58867] = 3425856
mem[45278] = 118643
mem[44440] = 584704
mask = X1100001000X1X010X011X0X0000XX0X1001
mem[40768] = 85230060
mem[36744] = 690218
mem[23942] = 369155
mem[46690] = 879641338
mem[62388] = 36434630
mem[45788] = 1712
mask = X110X011001111010X010100010000110X01
mem[20289] = 8051
mem[5798] = 64870413
mem[20409] = 12365
mask = 1X1X000X001111XX110100X1001X00X00011
mem[52329] = 9963755
mem[44763] = 911974581
mem[38281] = 1670
mem[30121] = 12169074
mem[60457] = 1795732
mem[59755] = 4148431
mask = 010X0X010100X00X1X1X1X1101101X0X0000
mem[65073] = 19189703
mem[21343] = 199170
mem[31147] = 237218
mem[63870] = 119469
mem[45728] = 7227071
mem[52235] = 232889
mask = 11X0001000011XX101X0001110X110000000
mem[51221] = 414
mem[51296] = 97635
mem[44882] = 597
mem[21580] = 151
mem[62354] = 15729
mem[49238] = 154335
mem[8722] = 6568
mask = 111001010000X10X11001011X00010110X01
mem[10789] = 11719
mem[44455] = 5005
mem[39994] = 1548
mem[2472] = 182989
mem[30152] = 6772910
mem[13360] = 23778
mask = 01X0000101X0X00111110011100X111010X0
mem[40929] = 2617123
mem[24670] = 21298246
mem[19730] = 53122
mem[4453] = 16356635
mem[18167] = 152861
mem[6794] = 109114900
mask = X1010111000X100111X1XXX111X10X110110
mem[60242] = 527195070
mem[9092] = 14828
mem[60561] = 12393
mask = 11X000000000110X110100X0110X01011000
mem[43733] = 3381891
mem[28994] = 102996
mem[34677] = 742154643
mem[56117] = 51070
mem[62864] = 513
mask = 1110XX100000X1X1X0110X0X0X0X10100001
mem[20020] = 102468
mem[54641] = 518248411
mem[42588] = 133137430
mem[49903] = 393777077
mask = 1X100X010XX011011101000X00XXX100011X
mem[59041] = 130847732
mem[55184] = 745
mem[35978] = 1728
mask = 1110101000X011011011101000X110X1X001
mem[32661] = 302743
mem[4437] = 640
mem[8811] = 1334
mem[4453] = 4515
mem[39550] = 598022
mask = 1110X100X0X111010XX11100111110000010
mem[4036] = 120228
mem[35400] = 285627
mem[13330] = 484890
mem[42246] = 9741695
mask = X111X0000010X1001101X100110100000001
mem[4865] = 424
mem[14807] = 2916
mem[9469] = 470087
mem[10170] = 238048
mask = 1110001000X0X101111X110001010010100X
mem[54355] = 114424821
mem[51406] = 899
mem[1515] = 391
mem[38678] = 103708
mem[53982] = 121098
mem[49442] = 9789
mem[35604] = 19583721
mask = 111X000000001101X10111X01101100X1101
mem[43682] = 175571639
mem[3831] = 9455072
mem[44523] = 106569
mem[37257] = 315345859
mem[64406] = 1612
mask = 01XX0001X00X1101X101000X010000001111
mem[19343] = 31345288
mem[8756] = 1677
mem[29688] = 81
mem[52684] = 332229
mem[15099] = 3806446
mem[38338] = 11840
mem[55633] = 116815478
mask = 1110001X00011X01X00X010110X011000010
mem[27344] = 2606
mem[5054] = 810
mask = 1101010X00001X0111010101100X1X10X010
mem[21289] = 4994
mem[16780] = 851612834
mem[18737] = 50882
mem[17717] = 2670
mem[36049] = 578215133
mem[47082] = 496908
mask = X0X101X1X00001111101X1X10111X0X1101X
mem[41026] = 409998
mem[14596] = 704
mem[29771] = 3494643
mem[25660] = 113256355
mem[59154] = 2369
mem[62847] = 2904
mask = 1110000000X111X1110110X011X1000X100X
mem[5769] = 132360
mem[42087] = 3851681
mem[40768] = 1010
mask = 1X100X0X000011011101X10X0100X00000X1
mem[33025] = 1410632
mem[43181] = 2000
mem[24043] = 700
mask = 111000X100001101110100X0X1XX01X00X11
mem[33195] = 1151261
mem[28725] = 6917
mem[21285] = 418795
mask = 1X110X00001X110111010X1XXX0100110X01
mem[1848] = 1543602
mem[20484] = 52183944
mem[24869] = 1750
mem[28451] = 146868
mem[31319] = 3136
mem[49411] = 3378
mem[45914] = 97061
mask = 1X10X000001111X1X1011011111X001X1011
mem[12905] = 145078660
mem[52038] = 2552
mem[34070] = 24245910
mem[11552] = 26334460
mem[769] = 22524
mem[45411] = 162871607
mask = 01110XX101X01X0111X1X0X11100101100X0
mem[34492] = 43083
mem[5855] = 258360838
mem[6147] = 282
mem[63064] = 5211483
mask = 1X10000000111X00110X0X110X1000000011
mem[9866] = 3514
mem[54099] = 14778
mask = X1X1000X0X1X11001101001101000101X0XX
mem[9299] = 24521049
mem[61776] = 292226032
mem[18074] = 19038893
mem[31659] = 114327725
mask = 010X010100001001X101100X0XX011X00X1X
mem[47192] = 499
mem[35562] = 1127803
mem[27862] = 7106662
mask = 1XX000X100101101110X1010010X00001X01
mem[8438] = 44700
mem[45696] = 470154968
mem[41741] = 535
mem[51296] = 550
mem[11976] = 153002786
mem[45322] = 84583483
mem[29651] = 15576
mask = 11100010000011011XX1010XXX010X01X000
mem[1789] = 911
mem[56530] = 115914529
mem[5451] = 142
mem[277] = 933970424
mem[64908] = 5581695
mem[55077] = 199
mask = 1010001X00X111011XX11001X0001000X101
mem[23536] = 53655494
mem[14360] = 754122
mem[15890] = 36708
mem[44816] = 99834802
mem[20566] = 473274604
mask = 111X101000X00X110X1X100001X011110X00
mem[33169] = 51545746
mem[31147] = 2815
mem[16106] = 1393423
mem[8786] = 9878148
mask = 11100010001111X0X0XX0110XX00X0001111
mem[47869] = 330626
mem[10389] = 1173
mask = 111001000000110111010000010X100XX10X
mem[56037] = 3906806
mem[42588] = 6113
mem[27703] = 795872
mem[52731] = 70918735
mem[21662] = 2974689
mem[38094] = 92515
mem[59061] = 75564
mask = 1XX0000X0X10110111X11X100X0X01100111
mem[17179] = 211
mem[25555] = 111231
mem[4258] = 24945299
mem[24124] = 4414744
mem[11003] = 7486
mem[25891] = 496
mask = X1110000X0X0110110001X11X1X10X000X10
mem[4841] = 236728268
mem[420] = 298
mem[34895] = 412844940
mem[9587] = 6377
mask = 1110XX1000001101100100010X01000111X0
mem[20505] = 717616953
mem[55911] = 254
mem[18500] = 12753143
mem[24196] = 2549282
mem[44072] = 370306692
mask = 111X0000001X110X1101X01XX100000X1XX1
mem[42453] = 5827
mem[6953] = 203298
mem[56264] = 375
mem[34887] = 2940099
mem[65469] = 351297914
mem[62106] = 226948
mask = 010X0X010100X00XX1XX1011111X0110100X
mem[6566] = 13861612
mem[62354] = 397490
mem[15192] = 26357463
mem[61353] = 120260489
mem[48329] = 20209615
mask = X1000X100100110111011X10100XX1100000
mem[31626] = 11216
mem[60050] = 922
mem[13079] = 460592139
mem[22864] = 3460
mem[21808] = 427851033
mem[26759] = 747148
mask = 111000X0X00011XX1001X01000011000X0XX
mem[47077] = 21552651
mem[45076] = 4796
mem[59796] = 3055
mem[61256] = 6500
mem[16825] = 980934769
mask = 1110X01101XX1100110X0000X0000X001100
mem[45076] = 584
mem[54926] = 29718
mem[18560] = 3999638
mem[4865] = 1007977570
mask = 01X10X010100X001111110X1X1XX10110XX1
mem[28725] = 172494865
mem[60439] = 7496408
mem[55184] = 111489
mem[15543] = 8109490
mem[25555] = 203769
mask = 101101X00011110111010X1XX011X0110001
mem[40538] = 2820
mem[12808] = 242352332
mem[55693] = 796801
mask = 11100110000X11X11101111X11110X010100
mem[52638] = 130173
mem[41136] = 99225
mem[30981] = 145765
mem[24654] = 23239
mem[56080] = 2600371
mask = 10110X1X000XXXXX1101001X01111011101X
mem[25555] = 35039981
mem[51117] = 899042
mem[28546] = 27200807
mask = 11100X10X00X11011X1111000X0111XX0001
mem[34877] = 19623
mem[32929] = 212201
mem[50492] = 86
mem[25692] = 3967
mem[59620] = 4489
mem[2397] = 167
mem[1613] = 1929
mask = 111001X00000XX0111010X0101X10001X1XX
mem[33026] = 1738730
mem[53181] = 9011944
mem[33688] = 9432725
mem[28325] = 2913917
mem[4760] = 30224638
mem[44900] = 23686766
mask = X010000X0010X100X10001X0X11111001XX0
mem[62904] = 543471105
mem[39372] = 284
mem[54084] = 99353
mem[959] = 565028
mem[41884] = 23617874
mask = 011100001000X1X110X0XXX1X1X1001X0001
mem[62428] = 82
mem[25406] = 1767
mem[9987] = 27303911
mem[45698] = 21354675
mem[33688] = 140290550
mem[11725] = 2764898
mask = 111000100000XX01110X010XX00101010100
mem[41653] = 490
mem[29936] = 361323
mem[61683] = 6863356
mem[19368] = 540
mem[61836] = 4792848
mem[57816] = 984651521
mem[39494] = 141986806
mask = 1X00101011X0X00X11X11110000000000011
mem[6510] = 25364
mem[45411] = 2282830
mem[24451] = 39824
mem[47536] = 125549431
mask = 11X0XX01000X110101010001001100010010
mem[44288] = 998863
mem[29095] = 926329
mem[38956] = 8054373
mem[12846] = 31513
mem[3837] = 14880
mem[44605] = 354763708'''
'''list_bitwise_data = [i.strip(" ").replace("[", " ").replace("]", "").replace("= ", "").split(" ")
                     for i in bitwise_data.splitlines()]
ans14_1 = 0
d = {}
for i in list_bitwise_data:
    if i[0] == "mask":
        mask = i[-1]
    elif i[0] == "mem":
        address = int(i[1])
        value = int(i[-1])
        new_value = list("0"*(36 - len(str(bin(value)).replace("b", ""))) + str(bin(value)).replace("b", ""))
        # noinspection PyUnboundLocalVariable
        for i in range(len(mask)):
            if mask[i] != "X":
                new_value[i] = mask[i]
        new_value = "".join(new_value)
        d[address] = int(new_value, 2)
for i in d:
    ans14_1 += d[i]
print(ans14_1)
d = {}
for command in list_bitwise_data:
    if command[0] == "mask":
        mask = command[1][::-1]

    else:
        address = command[1]
        value = int(command[2])

        new_address = list('0' * 36 + str(bin(int(address)))[2:])[::-1]

        for i, vals in enumerate(zip(mask, new_address)):

            mask_char, address_char = vals

            if mask_char != "0":
                new_address[i] = mask_char

        address_combination = new_address[:]
        for comb in itertools.product((1, 0,), repeat=mask.count("X")):
            address_combination = new_address[:]

            j = 0
            for i, char in enumerate(new_address):
                if char == "X":
                    address_combination[i] = str(comb[j])
                    j += 1

            address_combination = int("".join(address_combination)[::-1], 2)
            d[address_combination] = value
            j = 0
ans14_2 = sum(d.values())
print(ans14_2)'''

# day 15
input_15 = '''8,13,1,0,18,9'''
'''list_input15 = [int(i) for i in input_15.split(",")]
j = True
while 1 < 2:
    if collections.Counter(list_input15)[list_input15[-1]] == 1:
        list_input15.append(0)
    else:
        index = 0
        for i in range(2, len(list_input15) + 1):
            if list_input15[-i] == list_input15[-1]:
                index = - i
                break
        list_input15.append((len(list_input15) - 1) - (len(list_input15) + index))
    print(len(list_input15), end="\r")
    if len(list_input15) == 30000000:
        break

print(list_input15[-1])'''
# day 16
file = '''departure location: 30-828 or 839-971
departure station: 38-339 or 352-958
departure platform: 39-905 or 921-968
departure track: 36-570 or 586-972
departure date: 48-190 or 196-957
departure time: 29-483 or 491-963
arrival location: 28-779 or 803-959
arrival station: 27-221 or 238-966
arrival platform: 28-732 or 741-963
arrival track: 41-752 or 767-967
class: 27-437 or 452-972
duration: 38-93 or 107-958
price: 36-196 or 213-974
route: 48-858 or 880-956
row: 36-59 or 73-974
seat: 39-423 or 431-974
train: 38-499 or 518-958
type: 45-562 or 569-961
wagon: 28-161 or 171-959
zone: 44-75 or 83-964

your ticket:
139,113,127,181,53,149,131,239,137,241,89,151,109,73,157,59,107,83,173,179

nearby tickets:
475,649,830,432,685,476,743,278,558,283,496,337,83,313,153,139,405,522,648,894
888,593,683,820,389,319,405,559,465,948,359,270,811,842,555,704,542,485,255,472
371,457,149,561,468,267,459,849,482,925,281,368,222,809,700,822,612,393,90,108
179,422,138,361,55,597,825,158,395,768,403,158,807,417,282,269,708,780,549,148
731,113,414,421,904,93,133,456,59,616,640,478,521,352,804,238,132,891,568,306
572,806,150,654,768,534,635,621,891,900,56,468,552,673,372,376,463,92,493,390
461,394,305,569,371,825,684,824,187,591,262,363,935,935,730,752,885,104,434,826
834,663,318,632,668,940,670,400,633,354,399,744,630,521,684,821,640,74,748,74
335,637,199,594,687,940,904,530,262,664,642,895,398,642,648,187,372,335,592,480
531,624,844,686,943,541,853,377,731,948,416,267,668,699,182,630,94,339,137,267
468,278,300,267,292,924,386,338,556,671,813,640,448,535,283,607,627,857,363,335
287,810,492,289,313,905,180,296,535,78,363,118,554,148,743,858,881,359,221,812
696,219,221,241,180,778,672,479,320,570,538,707,360,751,273,401,943,226,283,310
147,650,794,291,849,57,182,361,300,452,89,87,804,559,748,744,591,417,107,292
264,247,243,109,541,161,724,15,265,301,528,161,773,746,810,182,378,303,847,721
769,688,172,425,946,90,244,522,173,539,282,744,357,182,691,270,498,559,727,719
741,413,520,902,157,481,937,53,549,828,407,117,681,903,691,565,327,661,824,402
465,141,385,366,520,985,634,526,149,51,539,931,220,725,613,933,161,556,403,377
215,687,634,550,411,388,612,350,245,303,768,307,54,675,770,741,465,617,827,137
632,719,143,854,948,721,609,154,726,186,668,755,246,723,388,355,256,751,727,775
132,418,920,290,691,623,457,925,704,704,676,396,880,88,87,717,329,415,328,182
393,546,388,996,771,322,420,357,312,118,465,400,840,560,636,284,493,312,171,218
649,467,674,897,453,382,633,279,947,378,51,241,565,657,148,352,93,121,923,609
636,13,627,520,778,948,854,942,537,570,948,779,404,221,684,303,687,402,593,629
674,254,773,657,596,609,684,183,948,926,712,541,245,693,518,561,8,527,249,305
888,932,272,295,769,107,894,481,675,708,268,396,541,808,453,77,132,531,89,712
325,921,216,172,183,714,519,374,113,62,924,332,300,482,307,895,421,719,886,745
459,695,712,707,411,943,403,249,904,264,643,148,141,590,470,721,425,51,702,598
358,369,352,617,558,188,494,708,122,903,752,320,744,827,980,628,147,606,109,123
813,477,823,865,651,849,321,180,813,844,372,827,653,845,532,932,220,519,704,779
309,243,851,819,687,768,852,726,247,746,133,57,183,179,888,762,519,660,328,542
340,123,664,945,948,821,319,670,258,849,847,722,808,417,217,431,313,113,692,881
320,682,579,328,546,492,686,555,651,521,905,88,724,292,939,122,307,947,310,825
460,639,467,483,719,406,586,565,657,416,592,651,160,650,710,633,216,531,324,710
889,894,76,243,215,245,298,570,550,320,749,110,518,902,855,853,948,129,819,90
309,282,625,172,777,938,140,290,56,686,266,353,497,671,848,653,130,139,396,735
655,361,332,240,161,219,372,671,680,242,196,998,697,628,667,660,639,550,602,604
552,60,842,744,649,270,661,820,597,254,243,903,603,322,182,652,182,295,652,408
613,607,469,615,614,558,775,597,50,372,5,137,635,703,482,129,146,383,107,824
598,679,897,478,184,243,629,535,654,315,559,15,610,363,181,290,391,621,149,298
221,457,854,468,977,540,527,664,463,722,118,86,323,691,359,744,414,352,709,273
901,569,377,481,774,673,51,90,117,721,637,744,519,75,395,257,733,620,849,458
299,337,174,326,540,423,597,394,852,561,526,677,942,135,739,391,329,360,365,475
561,750,904,415,610,631,155,542,480,283,826,290,244,332,847,342,328,470,253,493
883,622,254,141,459,410,479,156,887,270,452,976,295,598,809,650,744,589,179,85
456,699,372,607,638,855,720,152,528,540,744,595,902,159,650,451,936,609,656,322
565,937,627,308,562,274,238,492,884,291,675,817,882,308,679,261,619,705,409,364
518,623,462,591,126,683,294,650,364,214,640,116,621,553,376,477,411,624,424,148
426,284,270,885,360,85,255,718,89,680,126,272,590,937,605,419,628,469,301,53
275,723,159,636,177,196,668,526,654,732,388,387,272,262,16,926,633,422,117,558
405,151,675,929,928,497,432,428,687,369,727,462,54,129,152,466,295,383,365,630
248,50,526,816,839,227,253,698,180,519,186,852,842,531,160,258,414,385,603,91
523,651,697,562,709,603,21,90,275,479,905,526,381,475,638,278,418,414,611,362
711,274,687,643,709,389,729,225,720,948,675,819,601,412,414,434,375,650,852,377
939,685,627,643,145,275,59,258,524,903,416,635,634,896,834,657,242,466,266,270
296,771,851,676,328,852,357,260,697,52,383,456,774,179,56,905,846,945,15,398
397,412,929,838,279,286,215,845,885,127,715,586,477,930,418,552,459,536,534,292
532,461,404,453,742,269,292,694,437,309,702,56,213,64,187,171,366,661,299,713
747,481,137,520,702,891,534,174,322,946,625,898,592,326,429,852,115,52,178,184
483,936,728,794,888,496,308,256,687,284,588,538,742,296,629,51,603,716,252,890
217,497,948,382,417,327,390,148,701,617,898,529,775,437,916,183,819,676,335,393
937,472,122,288,619,743,660,725,742,313,675,605,383,741,53,69,171,618,125,742
121,376,709,858,710,387,824,468,302,922,884,699,378,582,628,525,890,534,629,459
707,745,410,476,743,307,547,121,482,699,281,309,414,689,728,424,848,140,613,714
880,632,844,627,469,947,399,767,900,185,731,409,826,430,329,50,882,50,405,253
189,922,536,313,385,272,330,932,313,117,132,737,669,182,494,493,702,522,184,609
186,634,287,716,591,55,589,175,306,452,746,694,661,646,855,259,80,221,151,857
477,243,649,546,303,683,285,518,720,367,629,841,371,395,741,333,911,367,750,811
691,693,889,244,461,759,680,932,116,139,654,719,153,260,597,269,627,899,177,883
459,323,125,748,483,370,137,751,991,708,898,149,664,307,392,419,423,256,493,376
882,853,562,694,469,428,219,158,684,587,84,87,464,86,887,712,536,679,700,767
473,623,705,565,470,404,822,409,271,665,87,214,687,880,817,849,213,146,689,190
602,245,713,115,616,639,323,80,176,824,700,240,499,598,810,535,184,187,404,684
938,0,240,433,812,283,673,855,135,156,53,393,727,570,389,216,929,109,416,288
880,401,328,653,694,161,131,747,273,946,647,699,659,309,610,247,807,609,421,69
123,700,841,697,702,279,248,55,592,552,379,185,126,856,803,357,773,568,178,377
325,124,941,826,669,238,636,595,238,934,402,131,188,146,633,436,595,362,191,498
378,632,177,992,177,606,644,626,935,323,332,823,124,380,815,518,619,293,670,821
454,273,118,752,604,526,151,932,294,544,7,462,108,804,407,423,305,134,432,549
143,59,611,463,286,722,132,191,132,712,325,592,548,362,419,108,91,710,359,320
852,905,596,730,532,528,158,116,809,231,570,634,660,681,935,904,401,406,327,695
724,318,660,683,940,635,657,692,366,750,130,463,246,680,24,117,928,608,257,690
123,225,774,336,824,624,267,772,413,180,302,269,179,897,839,596,670,679,295,135
937,291,721,253,665,356,702,292,537,556,804,932,827,695,89,734,108,692,85,708
857,889,149,728,455,461,735,293,643,596,718,274,741,279,881,825,704,298,284,820
395,659,675,588,159,54,296,809,549,707,885,625,723,901,652,677,583,457,811,674
883,238,420,473,664,306,326,650,674,390,627,160,695,196,362,579,703,298,934,287
318,689,777,948,251,530,888,668,612,732,396,604,735,822,925,645,154,613,389,108
266,936,816,376,401,52,518,239,823,732,779,892,602,568,370,897,856,768,331,901
279,622,267,728,771,923,620,417,297,744,646,329,463,545,407,778,345,534,213,399
930,180,624,492,454,380,125,409,312,535,663,132,772,192,817,681,175,704,218,645
379,128,251,902,813,472,84,273,894,273,421,407,251,674,565,555,52,310,303,544
681,180,713,370,248,160,548,718,691,189,978,90,479,676,894,686,262,141,300,639
120,140,686,522,540,131,645,142,554,533,108,59,394,645,841,57,390,762,546,658
311,704,383,750,934,615,608,320,570,724,654,538,714,119,143,252,224,135,660,713
263,633,416,658,925,610,854,887,559,732,627,492,268,21,626,406,470,154,138,298
641,677,827,125,150,552,230,359,405,115,400,749,468,57,672,184,436,659,388,393
437,895,371,529,522,604,751,274,283,399,417,636,71,318,53,186,190,652,472,110
274,673,932,582,325,352,617,883,826,292,882,820,437,124,243,619,547,678,321,216
99,417,938,312,327,337,925,882,594,550,646,128,679,683,590,617,188,682,378,387
271,732,753,561,458,141,461,75,143,935,741,902,728,562,627,218,323,616,559,556
703,703,432,903,846,519,469,391,412,455,527,691,491,710,815,676,171,192,531,547
487,329,86,123,902,547,120,945,116,925,816,271,555,844,667,816,256,217,410,554
115,110,624,559,562,375,262,254,645,414,772,373,307,432,75,458,389,249,81,703
280,256,889,588,536,144,497,113,89,607,852,881,629,617,587,561,983,309,189,180
827,536,118,698,491,898,722,851,467,481,988,855,928,284,261,328,259,175,521,538
315,52,604,656,540,769,424,846,666,930,291,54,58,423,662,140,139,742,720,525
524,890,246,104,663,141,176,73,819,715,570,530,239,255,401,161,671,307,367,87
461,728,660,935,420,805,261,644,255,381,945,637,591,15,902,663,749,846,743,647
150,436,601,269,159,699,675,926,678,416,241,637,482,280,298,526,781,681,778,245
901,530,559,528,620,535,314,141,453,326,778,239,530,148,189,729,808,552,69,334
122,665,283,128,471,270,152,196,246,807,153,109,86,466,125,108,757,714,152,648
707,324,825,587,301,776,822,290,384,824,382,809,930,439,942,181,896,695,279,360
481,678,819,345,275,538,159,710,416,491,297,949,458,385,773,360,895,367,255,945
333,709,741,55,530,455,814,604,292,415,120,149,855,309,573,614,668,404,669,307
435,886,120,410,154,109,147,259,395,669,145,668,306,804,2,499,183,144,691,144
752,424,58,52,241,175,699,638,216,179,807,657,472,547,518,86,902,373,537,768
526,356,355,253,58,921,746,557,708,406,530,998,173,519,555,474,180,469,672,125
694,214,710,390,570,890,689,152,433,644,336,60,881,378,89,692,368,823,491,249
631,665,499,657,389,828,410,255,123,375,53,903,940,754,653,421,253,676,352,173
735,179,690,779,924,54,705,644,847,373,364,547,534,90,529,664,889,358,318,770
723,725,607,321,655,354,421,130,145,949,307,804,600,716,76,437,474,813,692,544
631,685,499,992,922,371,726,374,181,359,688,329,250,406,672,242,882,551,804,122
259,107,642,656,239,604,257,705,386,622,556,946,154,474,56,697,493,439,857,124
437,885,286,111,417,160,82,151,113,711,313,276,160,395,111,560,653,435,683,897
124,382,994,773,177,594,822,300,243,697,615,518,596,453,642,841,495,498,496,296
646,821,364,271,857,492,658,643,699,418,943,364,8,84,636,375,181,922,842,277
857,313,387,932,703,853,314,324,664,769,416,653,498,131,460,881,604,20,171,554
472,533,777,287,626,112,134,608,293,218,54,805,540,326,463,656,175,1,455,143
264,731,620,282,663,646,177,778,749,523,396,124,633,539,492,837,453,881,127,337
303,897,453,213,693,880,743,23,628,595,520,53,221,813,608,184,809,842,613,185
842,547,674,361,382,291,777,302,721,852,519,158,392,537,419,184,142,737,813,630
233,301,677,839,896,545,214,150,461,806,887,148,160,555,727,307,710,142,700,932
83,498,272,693,129,824,710,770,189,855,73,183,729,279,543,23,329,892,670,273
54,664,313,255,645,945,57,496,406,546,180,847,631,542,453,525,845,418,904,999
276,338,55,481,86,274,621,850,623,382,431,273,826,226,458,750,841,275,652,495
556,614,129,769,333,534,276,300,492,190,992,319,491,329,548,142,529,55,397,942
720,218,533,488,943,699,290,609,291,659,298,402,407,325,157,246,157,243,594,611
152,246,483,218,840,449,694,112,700,352,475,773,729,52,108,769,247,534,245,282
187,700,53,939,848,152,133,113,315,729,674,110,494,987,83,589,119,569,540,116
247,114,290,715,646,412,857,921,182,176,607,632,307,773,53,184,683,285,236,562
732,381,244,328,679,775,727,251,619,805,706,827,152,821,551,903,931,702,342,716
401,685,589,389,398,891,813,127,121,420,818,330,523,593,422,87,246,200,319,371
850,856,246,624,462,182,448,335,401,381,681,620,303,645,810,883,569,416,298,594
619,707,309,477,934,624,127,657,57,157,20,196,457,254,292,182,410,742,391,147
817,271,706,467,642,554,695,709,524,596,357,318,777,689,59,223,378,687,352,530
617,935,280,213,637,183,249,332,779,398,905,492,885,455,136,594,306,747,760,693
717,730,410,903,57,92,815,298,522,409,742,680,495,377,266,376,193,126,389,653
282,538,923,654,171,258,743,257,553,628,813,220,156,135,332,529,836,647,302,899
409,73,456,372,534,541,647,354,570,117,56,59,317,807,194,943,558,769,815,431
147,598,490,587,131,779,679,134,536,673,371,419,929,729,854,535,306,927,743,400
354,364,569,717,147,244,654,624,649,700,144,702,188,341,683,647,454,88,299,394
597,751,678,493,899,748,410,479,177,761,521,612,683,536,113,900,895,92,306,658
609,730,722,402,761,731,743,143,365,401,684,897,689,384,411,844,118,359,317,715
379,659,473,399,774,555,291,853,932,587,281,461,142,925,270,602,555,69,600,310
633,674,769,265,694,82,134,180,174,608,378,824,176,56,747,881,108,605,769,885
644,730,589,447,217,522,140,533,900,265,600,613,290,709,408,934,701,216,924,853
338,257,322,123,547,806,188,904,591,381,256,535,594,538,897,940,984,942,388,294
848,663,597,125,287,720,188,87,393,491,171,54,618,221,478,112,438,699,624,378
465,174,640,362,896,718,323,287,398,719,672,606,691,739,724,497,544,803,409,434
761,460,633,263,360,814,731,252,58,752,356,172,928,641,716,374,614,721,558,242
845,324,307,519,127,671,750,709,437,652,219,112,59,682,844,267,653,936,445,561
319,554,716,53,333,422,418,151,149,641,948,186,109,807,405,160,361,424,238,322
545,244,676,311,751,855,704,766,890,532,942,921,359,548,267,264,714,723,895,111
912,308,726,668,238,307,379,619,687,530,275,245,897,369,217,777,614,403,176,940
842,893,238,815,779,407,189,602,605,361,976,927,184,386,606,370,185,921,718,455
148,51,133,250,851,455,191,806,184,846,818,823,284,651,55,51,903,933,709,51
175,607,219,379,527,290,381,529,483,398,884,777,392,452,415,912,334,694,238,295
134,708,622,299,268,452,371,436,893,727,947,498,384,141,520,147,379,630,769,82
359,702,470,918,718,128,892,646,313,695,407,411,729,313,560,58,934,377,189,496
931,464,663,697,160,525,323,317,256,286,678,178,492,422,948,185,355,572,127,316
407,456,568,948,264,949,386,597,393,602,377,924,550,770,311,703,379,327,597,941
495,740,293,407,296,881,431,550,728,625,686,900,596,276,468,127,752,731,467,674
317,644,626,539,274,184,364,395,243,889,333,663,601,83,263,490,338,338,303,528
714,853,279,216,321,769,839,901,922,809,478,940,3,372,771,261,149,267,265,810
150,732,854,684,176,124,266,458,456,738,267,904,678,823,523,602,931,826,363,361
549,742,369,557,774,185,253,21,381,374,390,857,552,896,701,613,596,280,777,588
921,491,492,764,377,891,240,668,404,694,476,381,292,371,395,648,562,821,178,724
694,595,929,522,522,248,942,68,109,625,590,743,50,364,277,273,383,895,324,267
590,326,148,317,747,644,839,397,902,122,669,154,171,365,491,145,50,282,581,394
124,492,84,550,687,181,63,708,461,542,408,569,332,636,730,708,640,436,260,779
593,554,823,369,628,377,177,455,666,557,57,147,678,385,808,475,436,873,471,322
250,723,737,52,778,594,390,187,434,922,654,327,140,244,827,523,532,362,627,724
280,112,471,85,493,59,693,301,180,551,658,318,637,727,926,158,684,397,733,640
382,620,383,81,58,727,805,161,588,476,640,322,596,465,923,274,56,700,124,122
244,821,261,17,722,287,841,814,569,308,286,635,379,903,769,414,885,178,180,649
621,815,593,475,848,668,378,637,135,728,643,496,722,836,589,466,643,544,774,218
176,381,54,368,431,252,253,923,818,728,112,559,761,855,657,528,321,134,809,422
628,946,216,459,217,476,633,391,617,546,377,187,282,825,587,975,709,260,277,714
604,749,462,740,728,893,688,603,182,141,826,374,146,679,311,498,777,523,606,142
109,552,636,215,678,401,306,654,254,941,404,274,427,814,710,266,283,466,809,279
901,670,94,304,644,672,325,900,50,693,880,493,670,622,812,946,888,239,408,625
779,263,560,134,404,407,108,188,526,635,570,112,437,313,846,628,488,380,935,322
441,713,942,379,117,702,569,473,518,653,894,839,818,495,616,142,670,288,116,559
569,308,826,465,539,539,849,248,467,716,478,221,887,811,225,173,142,240,310,842
148,406,883,195,615,362,536,253,393,177,616,562,295,415,523,896,650,846,243,548
320,188,840,189,523,247,158,447,607,394,776,842,718,117,725,747,110,73,75,465
949,180,181,475,588,496,933,700,416,305,18,714,779,682,770,335,657,602,472,945
246,77,590,697,810,491,158,670,936,296,724,633,402,745,929,367,273,361,549,73
929,943,712,386,882,666,743,360,140,821,472,745,551,303,132,86,846,20,618,842
421,238,11,817,111,545,695,651,654,840,634,296,50,632,385,642,146,549,89,675
356,650,240,202,216,253,851,556,697,111,546,293,663,818,828,719,366,849,274,851
615,397,402,590,629,694,541,932,178,311,335,534,721,928,678,118,770,917,689,718
713,593,390,534,188,295,365,621,844,153,382,547,641,720,520,355,659,889,157,996
69,245,479,255,494,618,818,158,83,853,603,929,189,130,242,525,57,360,431,716
73,289,458,611,69,134,704,145,415,127,397,811,599,935,648,743,418,466,310,587
844,597,338,477,400,742,895,659,902,464,895,218,521,772,110,54,149,838,315,562
769,399,706,130,856,312,566,465,810,238,592,807,848,433,136,354,92,174,929,52
219,499,278,562,537,63,779,240,364,775,628,435,74,843,905,547,176,54,120,297
658,248,155,556,213,196,541,641,382,933,238,368,775,79,338,629,686,266,86,400
409,741,554,284,492,537,91,132,848,113,840,302,855,413,439,665,172,542,322,252
819,122,685,935,414,387,624,53,746,637,338,245,114,256,387,596,10,120,770,817
664,846,181,150,413,283,766,466,724,929,257,188,558,366,925,523,273,656,654,483
620,397,229,287,184,454,647,327,216,776,310,719,125,183,459,594,433,279,155,142
112,648,644,155,394,924,189,406,154,405,171,726,364,569,749,529,550,513,307,840
662,240,468,235,452,289,329,806,179,588,414,824,51,621,643,273,817,53,715,128
179,807,537,53,242,740,213,555,751,528,160,680,184,435,356,258,675,433,419,528
771,499,594,635,938,940,810,354,55,644,548,690,133,364,68,727,247,90,823,693
849,748,358,638,899,357,435,329,83,419,629,847,731,352,238,526,243,79,51,196
542,308,428,637,718,410,93,240,481,722,287,93,692,807,923,176,149,310,550,552
306,975,900,315,216,479,743,494,901,535,597,924,239,186,925,124,491,750,588,323
76,929,694,844,114,410,842,941,307,377,553,528,481,858,243,771,818,614,535,749
899,143,342,888,256,750,465,173,855,887,312,827,714,452,550,776,845,242,839,250
525,387,844,731,185,261,935,895,331,840,928,726,821,709,896,891,680,340,172,742
153,93,639,469,947,776,336,362,75,387,310,711,630,282,402,469,567,538,455,695
817,395,849,456,275,645,310,382,240,255,296,926,267,354,760,219,529,810,813,559
610,118,495,624,493,119,628,491,715,266,420,690,586,411,16,496,902,405,841,146
221,375,534,309,390,616,521,704,853,645,353,221,497,493,395,939,752,3,544,844
823,302,638,522,157,616,178,339,705,988,610,467,84,466,886,898,650,814,940,300
191,189,59,329,596,884,728,921,214,679,335,308,752,136,534,494,475,937,551,606
852,633,407,371,608,645,627,59,813,189,586,708,522,598,59,353,71,888,325,174
805,840,110,69,923,294,658,608,86,693,903,253,181,155,420,688,55,55,750,904
396,454,155,431,894,178,473,312,937,295,24,75,498,339,818,676,161,270,244,138
365,597,419,818,216,729,707,464,371,383,772,189,217,367,295,819,990,805,391,586
93,278,65,161,469,701,601,714,849,274,569,196,75,544,57,57,411,418,413,147
646,270,632,405,303,676,499,478,559,410,709,395,81,321,647,609,247,153,816,126
769,466,193,602,529,327,335,215,930,121,743,609,306,288,332,725,217,399,619,819
827,296,445,618,778,897,238,691,474,723,679,215,934,179,528,645,620,359,499,890
401,812,352,813,533,274,675,698,121,175,409,774,411,402,348,626,481,898,589,298
745,819,605,815,87,276,352,821,301,171,937,710,525,327,305,749,930,904,635,753
646,56,534,523,287,271,713,738,115,889,92,750,700,655,113,946,110,747,615,545
806,288,122,176,52,466,453,539,757,218,337,453,383,474,939,660,892,384,115,383
437,803,570,466,458,284,687,405,279,374,393,297,634,369,317,192,494,690,689,260
359,759,606,108,544,300,239,856,550,117,933,401,660,624,457,728,688,685,605,57
616,125,698,214,934,115,182,299,5,276,244,822,688,295,559,261,770,903,357,724'''
'''data = [line.strip() for line in file.splitlines()]

fields = {}
tickets = []
line_breaks = 0

for line in data:

    if line == "":
        line_breaks += 1
        continue

    if line_breaks == 0:  # Fields part
        line = line.split(":")
        intervals = line[1].strip().split(" or ")
        intervals = (tuple(map(int, intervals[0].split("-"))), tuple(map(int, intervals[1].split("-"))))
        fields[line[0]] = intervals

    elif line_breaks == 1:  # My ticket part
        if "your ticket" in line:
            continue

        my_ticket = tuple(map(int, line.split(",")))

    elif line_breaks == 2:  # Nearby tickets part
        if "nearby tickets" in line:
            continue

        tickets.append(tuple(map(int, line.split(","))))

ticket_size = len(fields)


part1 = 0
invalid_tickets = set()

for ticket in tickets:
    for value in ticket:

        found = False

        for field in fields.values():

            first = field[0][0] <= value <= field[0][1]
            second = field[1][0] <= value <= field[1][1]

            if first or second:
                found = True
                break

        if not found:
            invalid_tickets.add(ticket)
            part1 += value
tickets = [ticket for ticket in tickets if ticket not in invalid_tickets]  # Filter out invalid tickets
fields_candidate_positions = {field: set() for field in fields}  # Candidate positions for each field
tickets.append(my_ticket)  # Add my ticket to the batch

for i in range(ticket_size):  # Check each position of ticket values

    values_on_position = [ticket[i] for ticket in tickets]  #

    # Check each field
    for field in fields.items():

        fits = True

        field_name = field[0]
        field_intervals = field[1]

        # Check if all values fit
        for value in values_on_position:
            first = field_intervals[0][0] <= value <= field_intervals[0][1]
            second = field_intervals[1][0] <= value <= field_intervals[1][1]

            if not (first or second):
                fits = False
                break

        if fits:
            fields_candidate_positions[field_name].add(i)

field_to_position = {}
removed = set()

for i in range(ticket_size):  # For each ticket position
    for field_name, candidates in fields_candidate_positions.items():

        candidates -= removed

        if len(candidates) == 1:  # Just one candidate - this position has no dispute and has to be assigned to them
            selected_position = candidates.pop()
            field_to_position[field_name] = selected_position
            removed.add(selected_position)  # We want to remove this position from all other fields - already assigned
            break

part2 = 1
for field_name in field_to_position:  # Calculate product of all departure fields
    if field_name.startswith("departure"):
        part2 *= my_ticket[field_to_position[field_name]]


print(part1)
print(part2)'''

# day 17
input_17 = '''.#.
..#
###'''
'''
data = input_15.splitlines()
def neighbours_active3D(x, y, z):

    active = 0
    for x_ in range(x-1, x+2):
        for y_ in range(y-1, y+2):
            for z_ in range(z-1, z+2):
                if any((x_ >= X, y_ >= Y, z_ >= Z, x_ < 0, y_ < 0, z_ < 0, (x_ == x and y_ == y and z_ == z))):
                    continue

                if plane[z_][y_][x_] in {"#", "I"}:
                    active += 1
    return active


def neighbours_active4D(x, y, z, w):

    active = 0
    for x_ in range(x-1, x+2):
        for y_ in range(y-1, y+2):
            for z_ in range(z-1, z+2):
                for w_ in range(w-1, w+2):
                    if any((x_ >= X, y_ >= Y, z_ >= Z, w_ >= W, x_ < 0, y_ < 0, z_ < 0, w_ < 0, (x_ == x and y_ == y and z_ == z and w_ == w))):
                        continue

                    if plane[w_][z_][y_][x_] in {"#", "I"}:
                        active += 1
    return active


# Part 1 ===
X, Y, Z = 26, 26, 15
plane = [[["." for k in range(X)] for j in range(Y)] for i in range(Z)]
middle = ((X-1)//2, (Y-1)//2, (Z-1)//2)

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            plane[middle[2]][y+middle[1]][x+middle[0]] = data[y][x]

for cycle in range(6):

    for z in range(Z):
        for y in range(Y):
            for x in range(X):

                if plane[z][y][x] in {"#", "I"}:  # Also consider changed in this cycle, because they all look at the same time
                    if not (neighbours_active3D(x, y, z) in (2, 3)):
                        plane[z][y][x] = "I"

                elif plane[z][y][x] in {".", "A"}:
                    if neighbours_active3D(x, y, z) == 3:
                        plane[z][y][x] = "A"

    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if plane[z][y][x] == "I":
                    plane[z][y][x] = "."
                elif plane[z][y][x] == "A":
                    plane[z][y][x] = "#"

part1 = 0
for z in range(Z):
    for y in range(Y):
        for x in range(X):
            if plane[z][y][x] == "#":
                part1 += 1


# Part 2 ===
X, Y, Z, W = 26, 26, 15, 15
plane = [[[["." for l in range(X)] for k in range(Y)] for j in range(Z)] for i in range(W)]
middle = ((X-1)//2, (Y-1)//2, (Z-1)//2, (W-1)//2)

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            plane[middle[3]][middle[2]][y+middle[1]][x+middle[0]] = data[y][x]

for cycle in range(6):

    for w in range(W):
        for z in range(Z):
            for y in range(Y):
                for x in range(X):

                    if plane[w][z][y][x] in {"#", "I"}:  # Also consider changed in this cycle, because they all look at the same time
                        if not (neighbours_active4D(x, y, z, w) in (2, 3)):
                            plane[w][z][y][x] = "I"

                    elif plane[w][z][y][x] in {".", "A"}:
                        if neighbours_active4D(x, y, z, w) == 3:
                            plane[w][z][y][x] = "A"

    for w in range(W):
        for z in range(Z):
            for y in range(Y):
                for x in range(X):
                    if plane[w][z][y][x] == "I":
                        plane[w][z][y][x] = "."
                    elif plane[w][z][y][x] == "A":
                        plane[w][z][y][x] = "#"

part2 = 0
for w in range(W):
    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if plane[w][z][y][x] == "#":
                    part2 += 1


print("Part 1:", part1)
print("Part 2:", part2)'''

# day 18
input_18 = '''(3 + 8 * 9 * (4 * 6 + 3 + 4)) * 9 + 9 * 7 * ((9 * 7) + 4)
(9 + (9 * 3 + 2 * 2 + 6 * 2) + 7 + 9) + 5
8 * 7 * (3 + (2 * 5 + 8)) + 6 + 8 + 6
(4 * 6 + 7 + 7 * 4 + 7) * (5 + 6 * 6 * 6 * 8) * 8 * (5 * 4 * 9 + 4 + 3 * 9) * 3
(8 + 8 * 2) * 9 * 5 + (2 + 2 + 3 * 7 * 5 + 6) + 5
(4 * (2 + 4) + 3 + (7 * 5 * 6 * 5 + 2 + 9)) + 8 * ((6 * 6 + 2 + 7 + 2) * (4 * 9 * 7 * 4 * 7)) + 8 * 2 * 4
(5 + 4 + 6) * (6 * 7 + 5 * 9 * 6) * 6 + ((4 + 5 + 3 * 5 + 6) * 6 + 2)
(4 * 7) * 2 * (2 * 9 * 6 + 8)
7 * (3 * 4 * 5 * 8)
(8 * (9 + 5 * 5 + 9 + 5 + 2) * 6) * (4 + 5 * 9 + (7 + 2 + 8) + 5 * 7) + 3
(2 * 4 * (3 * 4 * 5) + 5) * 2 + (6 * 4) + ((4 * 4) * 3 + 2 * 6) + 9 * ((7 * 6 * 8 + 2 + 7 + 9) * 7 + 3 * (8 + 7) * 6)
6 * 3 * (9 * 2 + 8)
2 + (6 * 4) * 7 * 7
2 + (9 + (9 + 7 + 3 * 4 + 6 * 7) * 9) * (7 * (5 * 8 + 8 + 6 + 6) * 7)
(2 + (5 + 5 + 9 * 4) + 3) * 2 + 2 * 6 * 4
5 * 3 * ((8 + 8 + 7 + 3 + 2) + 9)
((9 * 4 + 5 + 7) * 8 * 3 * 6 * (7 + 8 + 8 * 7 * 5)) + 5 + 8 * 9
(5 * 7 * 5 + (8 * 3 * 9 * 3)) * (8 + 7 + 8) + (2 + (3 * 7 + 4 * 8 + 4 * 3) * 3)
7 + 4 * (3 + 9 * 5 + 3 * 3) * (5 * 7 + 5 + 3)
(7 * 9 * 3 + (2 * 7 * 4 * 5 + 8 + 8)) * ((9 + 6 * 3) + 8 + (3 + 4) * 6 * 8 * 6) + 6 * 4
4 * (3 * 4 + 3 + 4 * 4 + 9) + 5 + 8
3 + 7 * (4 * (6 * 9 * 3 * 2 + 5 + 3) + 5) + 4 + 9
5 + 6 * 2 * 5 + (9 + 6)
4 * (4 * 6) + 7 * (3 * 3 + 6) * 8
((8 + 8) + (7 + 4) + 5 * (9 * 2 * 9 * 8) * 5 * (2 + 3 * 3 + 2 * 5)) + 5 * 7 * (4 * 7 + (3 + 3 * 5 * 5 + 5 + 2) + 8 * (2 + 2 + 9 + 6 + 3)) + 2
6 + 8 + (3 * (8 * 2 + 3) + 9 * 6 + (7 + 9 + 3 * 6) + (7 * 3 * 7))
7 + (5 * 7 * 6 * 3) + 5
7 + 5 + (3 + 8 * (6 + 8 * 3))
9 + (9 + 2 * 3 + 8 * 7) + 6 + (4 + 2)
(4 + 8 * 7 * 9 + 7 + (4 + 7 + 2 * 3)) + (2 + 7) * 6 * 6 * 6 + 9
2 + 5 + 8
6 + ((4 * 8) * 9 * 2 + 7)
6 + 9 + 6 + 4 * 5 + (8 * 9 + 9 + 4 + (5 * 3 + 8 * 7 * 4 * 7) + 5)
9 + (8 * 2 * 5 * 5 + 6)
(4 * 3 + (2 + 3 * 6 + 2) * (9 + 8 + 2 + 8 * 6 * 2)) + 9 + 3
((5 * 9) * (7 + 7) * 8 + 6 + 9 * 3) + (2 + 7 + 7 * 9 + 4)
((5 + 5 * 2 + 8 + 2) * (7 + 4 + 5) * (3 + 2 + 5 + 5 + 6) * 2) * 4 * 5 + 9 * 6 * 9
8 + (4 + (5 + 9 * 9) + 7) + ((7 * 3) + 7 * (4 + 7 * 5 + 8 + 7 + 9) * 3 * 5 + 3) + 4 * 3 * 4
((8 * 5 * 7 + 4) + 5) + 2 + (4 + (7 * 9 + 2 * 9 + 5 + 6) + 3 + 8 * (3 + 9 * 8 + 5 + 6 + 2)) * 7
6 * 9 * (3 + 9 + 9) + 7
4 + 4
(2 + (3 * 8 + 6 * 6 * 8) * 3) + ((3 + 6 + 2 * 6 * 6 + 4) * (7 * 4 + 4 * 9) + 3 + 5 * (7 * 3 * 9 * 4 + 3 + 2)) + 3
(2 + (7 * 3 + 4 * 8)) + 5 + 2
(3 + (8 + 9 * 2 + 4) * (9 * 7 * 8)) + (3 * 2) * 7 * 5
5 + 7 + 3 + ((2 * 9 + 8) + 9) * 7 + 7
(4 * 4 * 2 + (2 + 2) * 8 * 2) * 4 + (5 + 6 + 3 * 6 + 2 * 2) * 9 + 6 + 9
9 + 9 + ((8 * 5 * 6) * 3 + 2 * 2 + (2 * 4 + 7 + 6 + 7) * 3)
((6 * 9 + 6 * 3) * (5 * 7) + 2) + (2 + 6 + 6 + (6 * 3 * 3 * 5 * 5) * 4)
2 * 4 + 2 + 3 + 3
9 * 2 + 6 * 6 * 4 + 7
3 * (4 + (6 * 5 * 7 + 7 + 4) + 6 + 8) * 8 * 3 * 6 * 2
5 * (7 + (4 * 3 * 9) * 8 * 6) * 2
3 + 6 + (5 + 4) * 7 * 2
7 + (6 * 6 * 4) * 9 + 9 + 3
9 + ((2 * 5 * 7 * 9 + 2) * (2 + 6 + 7) + 8 * 2 * 9 + 8) * (2 + 2 + 6 * 8 + (8 * 6 + 3 * 6) * 3) * 6 + 8
(5 + 2 + 6) * (7 * 7 * 8)
(6 * 2 + 9) + 9 * (3 + 9 * 5 + 3)
5 + 2 + (6 + (9 + 2 + 5 * 5 * 8 + 5)) + 3 * 2 + (4 + 4 * 2 * 6)
6 + 4 * (8 * 5 + 4 * 2) + 8
9 * 6 * 6 + 2
7 * (6 + 2 + 4 * 5 + 6) * 6 * (6 + (8 + 9 * 9 + 9) * 8) + 8 + (3 + 2)
5 * 2 * (4 + 8) + 8 * 3 + (2 + 8 + 8 * 6 * 9)
3 + 6 * (8 + (2 + 9 + 5 + 2 * 6) + 3 * 9 * 7 + 2) + 3 + 5
(6 + 9 + 5 + 7 * (5 * 5 + 6 * 5) + 3) * 9 + 4
4 * (3 * 9 + (9 + 9 + 6 + 7)) * 8 + (2 * 8 + 2 * (2 * 8) * 4 * (4 + 6)) * (4 * 6 * (9 * 5 + 9 * 3 * 6) * 2) + 7
4 * 3 + (4 + 8 + 4) * 7 * 3 + 9
4 * 8 * 3 * (3 * (9 + 9 * 8 + 3 + 4) + 8 * 6 + 6)
2 + 8 * (5 * 4 + 3 + 9) * 2 * 8
3 * 8 + 4 * 6 + (5 * 8 * 3 * 8)
2 + 7 * (3 + 5 + 2 + 5) * 7 + 9 * 4
2 * 4 + 5 * (6 * 7 + 3 * 8 + 4) + (2 * (4 + 6 + 7 + 5 * 2 * 2) + (6 * 4 * 4 + 3 + 7) + 6 + 8)
3 + ((6 + 9 + 7) * (2 + 3) * 6) * 2 * (3 * 3 + (9 * 2 + 8) * 7) * 4 + 7
8 * (2 + 9) * (6 + (3 * 5 + 7 * 8 + 5 + 9) * 6 * 9) * 6
6 + 9 * 8 * 5 + (8 + 5 + 7 * (6 * 6 * 5) * 5 * 7) + (4 + 6 * 2 * 9 * 5)
2 * 8 + 3 * 4 * (2 * 8 + 7 + (6 + 9 * 7 + 2 * 9)) * 2
5 * (9 + (9 * 6 * 2 + 2) + 6 * 6) + (5 * 4) * 7 * 6
((9 + 8 * 7 * 4 * 2) + 3 + 3 * 5) * 8 + 5 + 9 * 4 * 5
9 + ((9 + 9) + 4 + 4 + 3 + 6 + (3 + 6)) + 6 * 9 + ((6 + 2 + 3) * 4)
6 + ((3 * 5 * 4 + 6) + 6 * 5 + 4 * 9 + (3 + 9 * 2))
3 + 3 + (7 + 8) + 8 * (4 * 9 + 8 * 9 + 9 * 9)
(5 * 9 * 7 * 4) + 6 + 3 * 5
(7 * 8 * 3 + 4 + (8 + 7) * 4) * 2 + 8 + 5 + 4 * 4
9 + (8 * 6 + 2 * (8 * 6 + 4 + 2 * 5 + 2) + 4)
(7 + 5 + (2 + 4 + 6)) + 9 + 5
(4 + 2 * 5 * 6 + 3) * 2 + 2
((7 * 8 * 8 + 8 + 5 * 6) * 6 * 8) * 5 * 4 * (7 + 3 * (8 + 6 + 5 + 8) * 8 + 9) * 3 * 9
3 + 9 * 8 * (7 + 8) + (9 + 6 + 5 + (8 + 4 + 6 * 5 * 9 * 7))
5 + 2 + 6
(9 + 2 * 7 + (9 + 3 + 6 * 7) * (9 + 3 * 4)) + 8 * 6 + ((3 * 6 + 8 * 6) + 4 * 4 * 8) + 6 * 6
3 + 7 * (8 + 7 * (7 * 2 + 6 + 4 + 3 * 9) + 8 * 7) * ((4 + 7) + 8 + 9 + 5) * 3 + ((2 * 8 + 2 * 3) + 3 + 8)
8 + 5 * 9 * (5 + 3 * 4 * 8 * 8) * 7 + (2 + 9 * 4 + 4 + 3 + 8)
6 + (9 + 4) + 4 + ((7 + 8 * 3 * 6) * 2 + 6 + 9 * 6) + ((2 + 2 + 3 + 3 + 5) * 5 + 5 + 8 + 7 + 4)
(4 + 6 + 7 + (7 * 4 + 7 + 2 + 2)) + 4 * ((9 * 9 + 8) + 3 * 3) + 4
5 * (4 + (6 * 9) * 2 + 5 * 8)
(7 * 5 + (6 + 2 * 3 + 3 + 2 + 7) * 6 + 5 + 8) + 3 + 5
(6 + 4 * 8 + 8 * (7 + 4 + 3 + 9 + 3)) * 5 + (3 + 7 + 4 + (2 + 6 + 5 * 2 + 2) + 7) * 8 + 4
8 * ((5 * 9 * 7 * 6) * 5 + 3) * 9 * (6 * 6 * 8 * 2)
((4 * 4) + 2) * 5 + 8
6 * (4 + (8 + 7 + 8 + 6)) + (9 + 5 * 5 * 6 + 9)
((5 + 9 * 6 * 7 + 7 * 3) + 8 + 2 * 8 + 9 * 5) * 2 * 9 * 4 * 6
(7 * 5 * 9 + 4) * 3 + 5
(5 + 5) + 8 * 9 + 2 * 8 + (7 + 4)
8 + (4 * 7 * (7 + 5 * 3 + 7) * 9) * 8
2 * (7 * 8 + (7 + 5 + 9 + 8)) * 9 + 9 + 9
9 + 8 + (2 + 6 * (9 * 2 * 7 * 7) + 5 + 2 * 5) + 4 + 5
(9 + 3 * 4 + 2 * 9) + (7 + 4 + 9)
2 * (5 * 5 * 6 * (5 * 6 + 2 + 9 + 5 * 3)) * ((2 * 5 * 6 + 5 + 8) + 8 * 2 + 7 * 9 * 2) + 7 * 2
9 * 2 + 7 + 3 + ((9 * 9 * 3 + 7 * 2) + 2 * 2 * (5 * 8 * 3 + 2 * 9 + 6) * 3)
4 + (4 * 9 * 2 + 9 + 9 + 2) + 6 * 2 * (7 + 9)
2 + 4 + (5 * 9 * 4 + (2 * 4 * 2) * (5 + 8 + 5 * 8 * 4 + 6) + 2) + 9 + 6
(7 + 9 * 7 + 8 + 3) * 7 * 6 + (2 + 9 * 7 + 5 * 5) + 2 * ((4 + 3 * 5 + 8) + 7 * 3 * 6 * 9 * 6)
(4 * 8 + 8 * 2) + 5 + (5 * 7 + 6 + 2 + 7 + 2) + 3
9 * (5 * (2 + 3 + 4 * 3)) * 5 + 9 + 9 * 9
9 * 5
5 + (9 * 6)
7 + 7
3 * 4 + 3 + (7 + 3 + 4 + 8 * 4)
8 * (5 + 3 + 3 + 2 * (4 + 6)) + (8 + 5 * 9) * 6
5 + (2 + (6 * 2)) + 5 + 8 * 9 * 3
(9 * 4 * 6 * (4 + 8 * 5) * 5 + 6) + 2 * 8 + 6 * (3 * (6 * 2 * 9 * 4 * 2 * 8) + 9 + (8 * 9 + 3 * 4 + 3 + 8) + 4 + 7)
8 * (5 * 8) + (7 + 7 * 5 * 6 * 3 * 4) + (4 * 7) * (3 * 6 + 9 * 4 * 2)
2 + (8 + 7 * 2 * (6 * 4 + 9 + 7 * 8) + 2) + 4 * 4
2 * (7 + 3 + 2 + (9 + 4 + 8 + 9)) * 2
9 * 8 + ((9 * 8) + 8 + 9 * 3 * 6 + 8) + 5 * 6 + (7 + (3 + 5 + 8 + 7) + 2 * (7 * 5 + 5 * 7) * (8 + 3 + 8) * 4)
2 + 5 + 4 * (6 * 2 * (8 + 8 + 7) + 3 * 9 * 9)
(5 * 5) + 4 * 9 + 8 * 8
((4 + 5 * 4 + 2) + (2 * 9)) * (2 + 4 + 3 * 9) * 9 + ((2 + 7) + 9 * (3 + 6 + 2 + 3) * (7 * 8 + 5 * 6) * 9) * 8 * 6
2 * 9 * (8 * 6 + 6) + 4 * (5 * 8 * 6 * 4)
6 * 7 * 2 * 3 + (8 + 8) * 6
(5 * 7) + 3
8 * 2 * (8 + 8)
5 * 7 + (6 + 4 * 3) + 3 + 9
6 * 2 * 6 * 2 + 8 * 4
(2 * 8 + 9 * 6 * (7 + 3 + 4 * 4 + 4 * 9)) + 2 + (6 + 3 * 5 + 4 + 9 + 8) + (3 * 7 + 3 * 2 + 6)
((3 * 8 * 8 * 4 + 6 * 6) * 7) * 6
(2 + 6 * 2 * 8 * (2 + 6 + 5 * 6) * 4) + 9 * 2 + 7
3 + 4 * 4 + 8
((8 * 6 * 8 + 7) * 8 * 7) * 4 + ((5 + 3 * 9 + 2 + 3 * 4) + 2 + 6 + 4 + (4 + 3 + 2)) * 7
((6 * 9 * 4 + 5) * 5) * 7 * 3 * 7
2 * 5 + 8 * ((6 + 5 * 6 * 5 * 3 * 2) * (7 * 7) * (8 * 3 * 3 * 3 * 8) * (6 + 8 * 9 + 9 * 4)) * 5 * 6
6 * ((6 * 7) + 9)
8 + 2 + 5 * 3 * ((4 + 3 + 8) + 7 + 5 * 6 * (2 * 6 * 2)) * 9
(5 * 5 + (2 * 9 + 8) + 8 * 8 * (3 * 6)) * 9 * 3 * 2
(9 * 8 * 7) * 7 + 7 * 4 + 8 * 7
((3 + 8 + 2 * 7) + 3 + 7 * 2) + 4 + 3
6 * 5 + 3 + (4 + 6 * 2 + (2 * 7)) + 2 * 2
7 * (4 * 9 + 3 + 4 * 2 * 5) * 9 + 7 * (9 + 6 * 7 * 8) * 3
((2 + 2) + 8 * 7 + (5 + 6 * 7 * 9 * 3) + 6 + 4) * 9
((6 * 5 * 2 * 4) * 6 * 6 + 2 + 7 + 6) + 2
7 * 4 + 3 * 3 * 9
5 * ((3 + 9 * 2) * 6 * 3 * (5 * 3) * 6 + 6) * 4
(3 * 7 * 9 + 9 * 6) * 5
6 + (8 + 5 * 3 * (7 * 6 + 5 + 4 * 7 + 8))
4 * 2 * 4 * (7 + 8 * (7 * 5 + 3 * 3))
((5 + 9 + 4 * 2) * 2 * (7 * 3 + 7 + 3 * 8 + 6) + 9 + (2 + 6 + 7 * 2 * 9) * 8) + 7 * (4 + 4)
9 + (7 * (8 * 2 + 5 * 8 + 7) * 7 + 6 + 6 * 2) * 2
(2 * 4) + 6 + (8 * 7 + 8 * 2 + (5 * 7 + 9 + 8 * 8))
3 + (3 + 2 * (5 * 4)) * 2 + (4 + 2 + 6 * (4 + 7 + 2)) * 3
(9 * 6 + 9) + (9 * 8 * (4 * 6 + 5 * 6 * 4)) + 3 + 2 * (9 + 3 + 5 + 5 + (4 + 8 + 8 + 2 * 5))
(8 + 7 * 3 + 2 * 5 * 4) * 4 * 9 + (2 + 5)
6 * 5 + 6 * 9 + 2
(3 * 3 + 5 * 6) + 2 * 5 * 3 + 8 * 7
(8 + 9) * 5 * 7
7 + (2 * 8 + (6 + 5 + 2 + 3 * 8 + 3)) * 8 * 3 * 4
(6 + 9 * 2 * 2 + 4 * 7) + 2 * (9 + 9 + 8 + 9 + 7) + (2 + 5 * 6 * 3 + 3 + 3)
3 + 3 + ((2 + 2 + 9 * 8 * 9) + 4 * 8 + 6 + 8 + 6) * 9 * (4 + (8 * 8 + 5 * 9 * 9 * 9) + (3 + 4) + 6 + 9) * 7
9 + (3 + (4 + 6 + 9 * 2 * 7 * 4) * 9) + 9
7 + (4 + 8) * 2 * 9 * 9
6 + (9 * (5 * 4 * 3 * 5) * 4)
3 * 8 + 4 + 2 + 5 * (4 * (8 * 6 + 2 * 5 + 8 * 4))
(4 + 9 * 3) * 2
5 + 3 * ((9 + 6) * 5 * (3 + 8 + 4))
((9 + 5 * 2 + 9) + 7 + 6 + 9 * (3 + 9 + 6)) + 4 + (3 + (9 * 3 + 7 * 9) * 6 + 9 + 9)
(9 + 6 + 6) + 3 + ((6 + 5) * 6 + 9 * 7) * (8 * (5 * 5 * 3 + 8 + 5 * 4) + (7 + 8 + 3 * 2 * 3 * 8) * 8 + 8) * (7 * (8 + 6 + 9 + 8) + 4 + 3 * 6) * 3
6 + 2 + 4 * (5 + 6 * 6) + 6 + 5
(2 * 7 + 5 + (4 * 4 + 8 * 5) * 4) * 6 * (4 + 2 * 2 * 3)
9 + (8 * 8 * 8 * 2) + 8 * 5 + 5 + (3 + 6 + 4 + 6 + 6)
(3 * (2 * 5) * 6 * 9 * 9 * (7 + 5 + 3)) + 6 + (4 + 2 * 9) * (2 * 6 + 7 + 6 + 3) + 4
3 + 7 + 6 * 6 * (4 * (6 * 6)) + 5
(7 + 2) + 4 * 3 * (5 + 9 + 6)
4 * 7 * (6 * 8 * 3 * 6 + 5) + (8 * 8 * 4 + 5) * 4
9 * 3 * 8 + 7
3 + 7 + 3 + (6 * (2 * 2 + 7 * 4)) + 8
5 * 6 * (7 * 9 * (4 + 8) + (5 * 3 + 7 * 4 * 7))
3 + 4 + 2 + ((6 + 5 * 7 * 8) * 9 * 8 * 8)
(5 + 5 * 2) * 6 + 3 * (4 * 5 + 5 * 5 * 2) + 4
(4 + 4 + 9 * 7 * 9) * 3 + (3 * 4) + 5 * 6 + 7
6 * (4 * 5 + 6 * 3 + 3 * 3) * 8 + 2 * 8
3 * (3 * (4 + 3 * 2 * 5) * (2 + 4 * 5 + 8) * 5 + 3 * 8) * 6
6 + (2 * 3 * 7 * 8 + 7) * 4
4 * 9 * (7 + 6 + 5 * 6 * (8 * 9) + 9) + 8 * (9 * 2 + 9) + 6
9 * 5 + 4 * ((3 + 6 * 4 + 4) + 8 + 4 + (7 + 4 * 3 + 7 * 5 + 9))
3 + ((9 * 4 * 6 + 4) * 4 * (7 + 3 + 8 + 7 + 3 * 4)) + 7 * 4 + 5 * 6
(8 + 2) * ((4 + 8 * 8) * 8) * 5
2 + 8 * 8 + (5 * 7 + 3 * 4) * 4 + 4
5 * 5 + 3 * 8 + ((7 + 5) * 3)
(5 + 8) * (4 * 3 * 9 * 8) * 7
(3 + 4 * (5 + 4) + 7) + (7 * 9 * 3) + 2 * 4
2 * 3 * ((6 * 2 + 8 + 2 * 9 + 5) * 3 * (4 + 4 * 3 + 2) + 8 * (7 * 3 * 5 * 9 + 3) * 8)
3 * 4 * (7 * 4 + 5 + 8 * 5) + ((9 * 5 * 5) + 4 + (6 * 6 + 8 * 2 + 9) * 2) + (3 + 4 + 7 * 7 + 9 * 5)
6 * 2 + 8 * 4 * (9 * 4 + (5 * 3 + 8) + 3 + 9) + 2
5 + (9 * 4 + 4) + (5 * 8 * 6 + 7 + 2 + 2) * 3 + (3 * (4 * 4 + 6) + 4)
5 + 8 * (5 * 7 * 8 * 4 + 6)
8 * 3 + 4
6 + 2 + 5 + 4 * (9 + 2 * 9) + 5
5 + 2 + 6 * (4 * (8 + 7 * 6 * 7) + (4 * 4 + 7) + (2 * 3 + 3 * 4 + 6 + 3) * 4 + 4) * 3
((5 * 4 * 2 * 4 + 9) * 4 + 3 + 4 * 7 + 8) * 3 * 6 + 4 * 2
(9 + 7) * 7 * 7 * ((6 * 3 * 4 * 8) + 9) + (7 + 4 * (3 * 3 + 6 * 2 + 7) * 9)
9 * (7 * 4 + 9) * (8 * 2 * 5 * 7 * (8 * 3 + 9 + 3 * 4) + 6) * 2 * 3 + 3
8 + ((3 * 5 + 3) + 5 * 7 * 8 * 8) + 3
((9 + 3 * 5 + 2) * 6) + 9 * (5 * 5) * 6
5 + (5 * (5 * 8) * 9 + 2) * (8 + (7 + 4 + 9 * 6 * 6 + 8)) * (4 + 8 * (6 + 6) + 7) * 3
5 * (2 + (6 + 9 * 4) + 4 * (8 * 2 + 7) * 8 * 2) * 6 * (7 + (6 + 8 * 6 * 8) * 6)
(7 * 7 * 5 + 8 + 2 + 3) * 3
5 + 3 + 3 + (6 + (3 + 7)) * (4 + 6 + 9) * 8
4 + 3 * (9 + (5 * 8 * 8 * 5 + 3) + 4 + 2 + 9)
2 + 7 + 5 * 6 + ((4 * 6 * 9 * 2 + 2 + 5) * (7 + 2 * 4 * 7 + 8) + 8)
(9 + 7 * 8 * (6 * 5 + 7 * 3)) + 4 * 7 + 5 * 9 + 9
((7 * 7 + 7 + 2) + 9 + 5 + (8 + 6 * 3 * 6 + 9) * (6 * 2 + 4 * 7) * 9) + 6
(3 + (3 * 4 * 6 + 4)) * 7
(6 * 2 * (5 + 5 + 4 + 7 + 8)) * 6 + 4 * 4
4 * 8 + (5 + 8) + 3
3 + 8 + 3 * (9 + (5 * 4 * 9) * 5) * (8 + (6 * 7 * 3 + 7 * 6) * 2) * 8
3 + 8 * (2 * 8 * 5 + 2) + 2 * ((8 + 7 * 6 + 5 + 2) * 6 * 3 * 3 * 5) * (7 * (5 + 5 + 3 * 6 * 3) * (5 * 4 + 4 * 9 + 4) + (9 + 9 + 9 * 5) + 7 * 3)
5 + (9 + 5 + 9 + 7 + (3 + 4 + 3 * 8)) * 8
4 * (9 + 4) + 4 + 3 + 6 + 9
((5 * 4 * 8 * 8 + 8 + 7) + 4) + (5 * 8 + 2) * (8 * 7 * 4 + 9 * 4 + (4 * 2 * 7 + 6)) + 3 + 6
5 * (8 + (9 * 9 * 5 * 2 + 8 + 4) * 6 + 6) + (7 * 5 * 7 * (9 * 2 * 8 + 5 * 7) * (5 + 4 + 2 * 8 * 8 * 9) * 4) + 6 + 9
((4 * 4 * 8) + 8) * 7 * 3 + 8 * 7
5 + 4 * 2 + 8 * (7 + 2 + 9 * 2) + 4
5 * (4 + 9 + (3 * 4 * 5) * 9)
4 + 2 + 3 * 3 + 9 * (9 + 4 * 9)
5 * 4 + 3 * 8
(8 + 4 * 6) * (8 * 3 + 4 * 8 * 9 * 2)
(9 + (8 + 4)) * 6
(9 + 5 * 5 * 8 + 7 * (9 * 6 * 6)) + 2 + 4 * 2 * (3 * 8 * (5 * 5 + 5 * 7) + 8 + (3 + 7 * 5 + 4 * 5) + 5) + 9
3 * 9 + 2 * (7 + 8 + (9 * 6 + 4) * (4 + 8 * 9 + 2 + 3) + 3)
(4 + 7) * 3 + 7 * 5
6 * (4 * 5 + (2 + 7 * 8 + 9 + 5) * 7 + 9 * 2) + 8
8 * (8 * 3 * (3 * 3 + 2) + 9) * 5 + (7 * 3 * 2 * 4)
9 + 3 + 4 * (8 + 4 * (2 * 8 * 3) * (5 * 4) * 7 + 5) * 8
8 * 9 + 6 * (3 * (6 * 8 * 6) + 7 + 9 * 5 * 7) * (7 * 3 + 3 * 6 * 8)
8 + (8 * 6 + 7 + 2 * (4 * 6 * 3))
4 + 2 * 7 * ((7 + 6 + 7) * 8 * 6) * (2 * 7 * (2 + 4 + 9 + 2) * (4 + 3 + 6 + 2 + 6) + 6 + 7)
(3 + 9) * 7 + 5 * (3 + 3 * 2 * 6) * 3 * 2
(5 * (8 * 3 + 6 + 5 * 9) * 8 * 6 + 9 * 9) + 8 + 5
8 + ((9 + 3 + 2) * (7 + 9 * 6 * 3) + (4 + 6 * 5 + 8 + 3) * (6 + 9)) + 9 * 7 * 7
2 + 9 * 3 * ((6 + 3 + 3 + 6 * 7 + 9) + 8 + (5 * 5) * (4 * 8 * 5) * 3)
8 + 6 + 4 * 2 * ((5 * 8 + 9 * 2 * 3) * 3 * 9 + 4 * 9 + (3 + 5 * 9)) + 2
7 * ((6 + 8 + 5) + 9) * 4 + 4
9 + 3 * 4 * (6 + (9 * 3 + 7 * 3 + 7 + 3)) * (4 * (4 * 3 + 4))
7 * (5 + 7 * 5) + 2 + ((7 + 6 * 7 * 9) + 5 + 3 + 9 + 6) * (7 + 4) * 2
2 + 4 * 5 + 6 * 3
2 * 9 * ((9 * 5 * 8) + (8 + 3 * 8)) + (7 * 8)
7 * 6 + 5 + (5 * 4) + 9 * 2
4 * 5 + 2 + (4 * 4 * 7) + 4
5 + 5 + 2 * (8 * (3 + 5 + 9 + 4) + 7) * 3
3 + ((2 * 8 + 7 * 3 * 3 * 4) * 3 + 9) + ((6 * 9 * 4) + 4) * 8 * 6
((2 * 5 + 4) * 2 + (3 + 4) * 8) * 7 * 9 + 2 + (9 * 7 * 8 + 5 + 9) + 8
7 * (9 * (5 * 3 * 2) * 7 * 5 + 3 + 7) + 7 * 9 * 3 + 6
((3 * 3) * 7 + 9 * 7) * 6 * 8 + (4 * 3 + (7 + 4 * 2) * (5 * 9 * 6 + 4 + 6 + 4)) * 2
3 * 6 * 2 + ((4 * 9 + 7) + 6) * 3
9 * (3 + 8) * 6 * 3 * 7 * (4 * 3 + 7 * 2 + (8 + 7 * 6 * 2 * 8 + 3) * 3)
((5 * 4 * 5 * 6) * 8 * 8) + 8
((2 * 9 + 2 + 6 * 5) * 4 * 2 * (4 + 4 * 9 + 3 * 2 * 8)) * 4 * 7 * 3 + 4 + 7
6 * 3 + 5 * 4 + 8 + 9
8 * 2 + (7 + (6 + 4) * (6 * 5) * 3 * 7 * 8) * 2 * 9 + 5
6 + (3 * 2 * 9 * 8 * 5) * 2 + 6 + ((6 * 8 * 7 + 5 * 9) + 3 * 3) * 5
(8 + 3) + 3 * (3 * 3 * 7) + 8 * 8 + 3
6 + 2 * (2 + 2 + 9 * 2)
(7 * 2 * 6 * 3 * 4 + (7 + 6 + 6 + 3 + 2 * 7)) * 8
(7 + 2 + 2 + (9 + 8) + 3) + (4 + (5 + 7 * 6 * 2) + 7 + 9 + (2 * 8 * 4 * 3 + 6)) * (6 * (9 * 6 + 4 + 7) + 8) * 6 + 2 * 6
6 + 5
(9 * (6 * 9 * 2 + 3 + 5) + 7 + 2 + 4) + 8 * (6 + 5 * 9)
8 * (5 * 8) + 5
9 * 2 * 9 * 9 + 7
(8 + 9 + (8 + 7 * 4 + 4) + 4 + 2) + 6 * ((9 + 4 * 9 * 3 + 5 + 2) * 8 * 3 * 8 * 3) + 8
5 + (8 * 4 * 5)
(3 * 7 * 4) + 6 * 8 * (5 + 4 + 8 + 5) * (4 + 8 + 9 * 8 + 7 * 7) + (4 * 8 + (5 + 4 + 2 * 2))
9 + 6 * 7 + 2 * (9 * (3 + 2 + 7 * 9) * 3 * 4 * (6 * 6 * 9 + 4)) + 9
7 + (8 * (5 + 7 * 6) * 8 + (2 * 4 + 5 * 4 + 6 * 7) + 3) + 9
5 + 7 * (3 + 8 + 2 * 8 * 5 + 4) * 7 * 8 + 8
9 * 4 * 4
(9 * 3) * ((5 * 7) * 8 * 2 + 4) + 5 + 9 * 3 + 5
((2 * 5) + 2 + (7 * 5 * 9) * 2 + 5) + 7 + (5 + 2 + (8 + 4 * 4 + 6))
((5 + 4 + 9) * 4 * 4 * 6) * 4 * 6 + 5
4 * 8 + 3 * ((8 + 8) * 5 * 7 + 9)
8 * 6 + 5 + (5 * 9 + 5 * 7 * (9 + 8 * 7) * 5)
7 * (3 + 4 * (3 + 6) + 6 + (3 * 8) * 9) + ((8 * 5 + 3 * 8) + 2 + 3) + (9 + 6 * (6 + 8 + 6 * 8 + 8 + 6)) * 2 * 7
8 + ((6 + 6 + 5 + 3 * 3) * 5 * 8 + 9) + 2
((9 + 8 * 8) * 8 + (6 + 2 + 7 + 3 * 3 + 6) + 2) * ((2 + 3 * 7 + 6) + 3 * 7 + 8 + 6 * 6) * 3 * 8 + 9
5 + (8 * (4 * 2) * 2 + 9) * 2 * 6
(4 + 4 * 9) + (6 + 5 * (4 + 2 * 2 * 4 * 8) * 2 + 4)
6 + 7 + 5 + (6 * (2 + 6 * 2 + 5 + 9)) * 6
5 * 3 + 2 + 2 * ((7 + 6 * 8 + 6 * 7 + 5) * 4)
6 * (7 * 8) * (6 + 6 + 2 + 4 + 6 + 6)
((7 + 3 * 7 * 4) + 7 + 9 * 4) + 4 * (2 * 9 * 7 + (3 + 9 * 3)) + 8 * 9
2 * 3 * 2 * 5 + 9 * 6
((3 * 7 * 9 + 4 + 5 + 3) * 8 + (4 + 5 + 8 + 3) + 2 * 2) * 7 * 5
3 + ((8 * 2) + 8 * 4 + 2) * 4 + 9 * 5 + 5
3 + 9 + (6 * 9 * 8) * ((8 * 3 + 9) * 4 + 5 * 7 + 6) + 7
9 + (8 * 4 + 2 * 6 * 4 * 4) * 9
5 + 3 + 5 * 3 + 4 * 3
(5 * 3 * 4) + 7 + 8 + 6 + 5
(6 * (9 * 7 + 5) + 7 * 4) * 2 * 9 + (7 + 5 * 4 + 7 + 3 * 6)
6 * 9 + 2 * 2 + (6 + (6 * 6 + 2 * 4 + 8) + 7 * 5)
((5 * 9 + 3 * 6) + (5 + 2 + 3 * 4) + 3 + 8) * (9 * 2 + 7 * (8 * 5)) * 6 * 2 + 5
(9 + (5 + 7 + 2 * 9) * 4 * 2) * 5 * 5 + 7 + 7 + 9
9 + 7 + 4 + (9 * 7 + 2 * (5 + 4 + 3 * 4))
6 + (3 + 5 * 4 * 8 + (7 + 4 * 3 * 4)) * 7 * 4
9 * ((7 + 6 * 3 * 6) * 7 + (4 * 5 * 3)) + 9 + (7 * 6 + 8 * 5) + 9
4 + 7 * 6 + 6 + (7 + (7 + 8 * 7 + 8 * 4 * 9) + 3 * 9) + 7
(9 + 7 + 2) * 3 + (7 * 8 + 9)
2 + 4 * (2 * 8 + (7 + 5) * 6) + 4 + 4 + (3 + 2)
(5 + (2 * 4 + 9 * 6) * 9 + 3 * 7 * 3) + (5 + (2 * 4 + 7 + 6) * 4 + 3 + 2) * (7 + 9 + (6 * 9 + 6 * 9) + (2 * 2 + 5 + 5) * 4 + 7)
(8 * 6 * 8 * 7 + 7 + 6) + 8 + 9
6 + (3 * 4 + 6) + 9
5 * 2 * 6 + 2 + (4 * 8 * 2 + (4 + 7 + 3 * 8 + 2)) * (4 + 8)
(4 + 2 + 7) + (7 * 2 * 3 * 8)
(9 * 6 * 2 * 9 * 7) * 4 + 4 * 4 + 4 * 8
9 * 3 * (9 + (5 + 3 + 2 + 6)) + (8 * 6 * 4) * 8
8 + (6 + 3 * 6) * 2 * 8
5 * 4 * 3 + (9 * 8 + 6)
(2 + 4 * 8 * 9 * 9 * 2) + 7 + 7 + 3 * 8
(2 * (4 + 7 + 8 * 4) * 4 * 6 * 7 + 4) * 6 + 5 * (6 + 4 * (6 + 9 * 2 + 2) + 2 + 5) * 4 * 5
(9 + 4 * 8 * 8) * 8 * (6 + (8 * 5) * (2 * 7 * 4 + 4 * 6) + 3 + 4 + 9) + 9 * 9 + 4
(7 * 4 + 3) + 4 + 7 * 9 * 7 + (6 * 3)
4 * 2 + 8 + (3 * 2 * (4 * 8) + 3)
6 + 6 * 3 + (9 * 5 * 5 + 4 + 9 * 9) * 3
2 + 8 * (2 + 8 + 2) + (8 * 6 * (3 * 6 * 4 + 8 * 6 * 6) + (3 + 5 + 7 * 8)) * 9 * (4 * 9 * 5 * 6 * 5 * 7)
4 + ((8 + 9 * 5 * 6) + 3 + 9)
(5 + 5 + 5 * 6 * (6 * 5)) * 7 * 2
4 + 6 + (7 * 2 * (9 * 7 * 5 + 5) + 4 * 2) + 9 * 9 * 2
6 + 9 * 8 * 3 + 9 * (3 * (3 * 2 + 2 + 9 + 7) * 2 + 2 + 3 * 8)
8 * 6 * (9 + 7 * (8 * 9 + 7)) + 8 * (3 + 3 + (4 * 2) + 4 * 7 + 4) * 4
9 * 2 + 2 * 4
(6 + (6 + 9 + 3 + 5 + 6)) * 8 + 8 + 3 * 8 * 9
(8 + 2) + 3 * ((2 + 2 * 5 * 2 + 9 + 6) * 6 * 6 + 3 + 3 + (5 + 9 + 7 + 5 + 9)) * 2 * ((4 * 7 + 4) * 6)
(4 + 8 * (9 + 8) + 2 + 4 * 2) + (7 + 5 + 3 + 9 * 4)
8 * 5 + 8 + (7 + 2 + 8 + 7 + 8) * (9 * 7)
7 + (9 * (9 * 4 * 8)) + (8 + 8 * (2 + 6 + 2 + 6) + (7 * 9 * 2 + 3 + 8 + 7)) * ((5 + 4) + 6 + 3) * 2 + 7
6 + ((4 + 2 * 5) + 3 * 7) * 2 + (4 + 9) * 3 + 3
9 * 4 + 7
((5 + 6 + 6 * 3 * 5 * 8) + 8 + 4) * 6 * 5 * 4
6 + ((4 + 7 * 6 * 4) + 8 * 2 + 6)
7 + 4 * 8 * 8 * 3 * (7 * 6 + 6 + (8 * 6 * 9))
((8 * 5 + 7 + 3 + 7) + 3 + 7 * (4 + 2 * 9)) + (7 * 6 + 2 + 5 + 6) + 2 * 6
(9 + 4) + 2 + 8 * (6 + (7 + 8 * 9 + 6 * 8) + 6) + 3
6 + (6 * 7 + 3 * 7 * (2 + 2 * 2 * 2) * 8) * (2 * 6 * 7 + 4 * (9 + 9 * 3 + 4) + 4) * 6
(6 + 9 + 6 + 8 * 5) * 8 * ((4 * 9 + 2 + 7 * 6 + 4) + (7 + 2 * 4 + 5)) * 3
((9 * 8 + 9 + 8 * 2 * 3) + 7 * (4 * 6 + 7 * 3 + 2 * 3) + 9) * 7 * 9
(3 + 6 + 7 + 9) * (2 + (4 * 7 * 6 + 9 + 3 + 5) + 9 + (2 + 3 + 7 + 4 + 3) + 9) + 8
(6 + 8 * 2) + 3 + 7 * 5
7 * (5 + 4 * 5 + 9 + 6 * (3 + 4 + 4 + 8 + 4))
(4 + 7 * 5 + 4 + 6) + (3 + (5 + 4)) * 3 * (2 * 4) + 2 + 6
(6 * 4) + 8 * (4 * (8 + 7 + 3)) + 4
5 + 6 * 8 + 3 + (7 * 5 + 5)
7 + 2 * 5 * ((8 + 4 * 8 + 3 * 5) + (8 + 4) * 6 + 4 + 9 * 4) * 8
(3 * 3 * (7 + 7 * 7 + 7) * 5 * 9 * 9) * 4 * (5 * 2 * 9 + 8 * (4 + 2) * 7) * 9 + 8 * 4
5 * 7 + (7 * (2 * 4))
3 + (9 + (5 * 9)) + 8 * 4
9 * 5 * 3 + 3 + 3 * (9 * 6 * 6 + 2 * 4)
2 + ((2 * 7 + 4 * 4) + 8 * 6 * (9 + 4))
9 + (8 + (7 * 5 * 7 * 5 * 7)) + 2
(4 * 5 * 6 * 3) + 9
6 + (2 * 5 * 9 + 8 + 2) * (2 * 8 * 3 * 2)
3 * (5 * (3 * 5 + 3) + 5 + (2 + 6 * 8 * 2 + 4 + 6) * 2) * 9 * (6 + 6 + 3) * 2
(2 + 5 + 8) + (2 + 8 + 3 * 7 + 4) * 3 + 3 * 9
6 * 6
5 * 9 * ((6 * 5 + 9 + 9) * 6) * 4
5 + 5 * 6 + (3 * 5) + 5
3 + (8 + 8 * (6 + 9 * 4 + 8 * 6) + 6 + 7 * 3) + 2 + 8 * 6 * 7
(3 * 2 + 6 * 3) * 7 * 6 * 9 + 5
2 + ((6 + 4 + 7 + 5 * 3 * 8) * 3 * 5)
(3 * 9 * 5 + 3 + 2) * 4 + 8 + (6 + 3 * 8 * 8) * (7 + 5 + 8) + (8 + 9)
5 * 2 + 2 * 8 * 5 * (2 * 5)'''

'''
def evaluate(s):
    while len(s) > 1:
        d = eval(s[0] + s[1] + s[2])
        if len(s) > 3:
            s.remove(s[0])
            s.remove(s[0])
            s.remove(s[0])
            s.insert(0, str(d))
        if len(s) == 3:
            return str(eval(s[0] + s[1] + s[2]))

t = input_18.strip().replace(" ", "").splitlines()
part1 = []
for s in t:
    s = list(s)
    while "(" in s:
        for i in range(len(s)):
            if "(" not in s[i + 1:]:
                s[(i):(s[i + 1:].index(")") + 2 + i)] = [evaluate(s[(i + 1):(s[i + 1:].index(")") + 1 + i)])]
                break
            else:
                if s[i] == "(" and s[i + 1:].index(")") < s[i + 1:].index("("):
                    s[(i):(s[i + 1:].index(")") + 2 + i)] = [evaluate(s[(i + 1):(s[i + 1:].index(")") + 1 + i)])]
    part1.append(eval("".join(s)))
print(sum(part1))


data = [line.strip().replace(" ", "") for line in input_18.splitlines()]

#  Not the prettiest solution, will improve later.

# Part 1 ===
part1 = 0

for line in data:

    stack = [0]
    operation_stack = []
    operation = "+"

    for char in line:

        if char.isnumeric():
            if operation == "+":
                stack[-1] += int(char)

            elif operation == "*":
                stack[-1] *= int(char)

        elif char in {"+", "*"}:
            operation = char

        elif char == "(":
            operation_stack.append(operation)
            stack.append(0)
            operation = "+"

        elif char == ")":
            answer = stack.pop()
            operation = operation_stack.pop()

            if operation == "+":
                stack[-1] += answer
            elif operation == "*":
                stack[-1] *= answer

    part1 += stack[0]


# Part 2 ===
part2 = 0

for line in data:

    stack = [0]
    operation_stack = [None]
    operation = "+"

    for char in line:

        if char.isnumeric():
            if operation == "+":
                stack[-1] += int(char)

        elif char == "*":
            if operation_stack[-1] == "*":  # End * group
                operation_stack.pop()
                answer = stack.pop()
                stack[-1] *= answer

            operation_stack.append("*")  # Start new * group
            operation = "+"
            stack.append(0)

        elif char == "+":
            operation = "+"

        elif char == "(":
            operation_stack.append(operation)
            operation = "+"
            stack.append(0)

        elif char == ")":
            answer = stack.pop()
            operation = operation_stack.pop()

            if operation == "+":
                stack[-1] += answer
            elif operation == "*":
                stack[-1] *= answer

                # Do it again if we have multiplication ending just before a closing parenthesis
                answer = stack.pop()
                operation = operation_stack.pop()

                if operation == "+":
                    stack[-1] += answer
                elif operation == "*":
                    stack[-1] *= answer

    if len(stack) > 1:  # Finish everything up if some numbers left in the stack
        for i in stack:
            answer = stack.pop()
            operation = operation_stack.pop()

            if operation == "+":
                stack[-1] += answer

            elif operation == "*":
                stack[-1] *= answer

    part2 += stack[0]


print("Part 1:", part1)
print("Part 2:", part2)'''

# day 19
input_19 = '''0: 4 1 5
1: 2 3 | 3 2
3: 4 5 | 5 4
2: 4 4 | 5 5
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''
'''j = sorted(input_19.split("\n\n")[0].split("\n"))
dict_of_rules = dict((i.split(": ")[0], i.replace("\"", "").split(": ")[1].split(" | ")) for i in j)


checklist = {}
for i in dict_of_rules:
    if len(dict_of_rules[i]) == 1 and dict_of_rules[i][0] == "a" or dict_of_rules[i][0] == 'b':
        checklist[i] = True
        dict_of_rules[i] = dict_of_rules[i][0]
    else:
        checklist[i] = False
print(dict_of_rules)
print(checklist)
aes = 1
d = []
while False in checklist.values():
    for i in dict_of_rules:
        if type(dict_of_rules[i]) == list:
            for f in dict_of_rules[i]:
                k = f
                f = f.replace(" ", "")
                for j in f:
                    if j != "a" and j != "b":
                        if checklist[j]:
                            # print(">>>", j, dict_of_rules[j], type(dict_of_rules[j]))
                            if type(dict_of_rules[j]) == str:
                                f = f.replace(j, dict_of_rules[j])
                            elif type(dict_of_rules[j]) == list:
                                for iterator in dict_of_rules[j]:
                                    for item in range(len(dict_of_rules[j])):
                                        dict_of_rules[i].append(dict_of_rules[i][1])
                                    for item in range(len(dict_of_rules[j])):
                                        print(dict_of_rules[j][item])
                                        dict_of_rules[j][item] = dict_of_rules[j][item].replace(j, dict_of_rules[j][item])
                if len(f.replace("a", "").replace("b", "")) != 0:
                    thing = False
                elif len(f.replace("a", "").replace("b", "")) == 0:
                    thing = True

                dict_of_rules[i][dict_of_rules[i].index(k)] = f
                print(f)
                if thing:
                    checklist[i] = True
                print(dict_of_rules)
    print("-----", checklist)
    print(dict_of_rules)




print(checklist)'''

# day 20

