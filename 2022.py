import re
from collections import defaultdict
import time
from math import sqrt

start = time.time()
# day_1
input_1 = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
'''list_1 = [sum(list(map(int, i.splitlines()))) for i in input_1.split("\n\n")]
list_1.sort()
ans_1_1 = list_1[-1]
ans_1_2 = list_1[-3] + list_1[-2] + list_1[-1]
print(list_1, "\n", ans_1_1, "\n", ans_1_2)'''
# day_2
input_2 = '''A Y
B X
C Z'''
'''list_2 = [i.split(" ") for i in input_2.splitlines()]
scores_2 = []
guide = {"Draw": [["A", "X"], ["B", "Y"], ["C", "Z"]], "Win": [["A", "Y"], ["B", "Z"], ["C", "X"]], "Lose": [["A", "Z"], ["B", "X"], ["C", "Y"]]}
guide_2 = {"X":1, "Y":2, "Z":3}
for i in list_2:
    score_i = guide_2[i[1]]
    if i in guide["Draw"]:
        score_i += 3
    elif i in guide["Win"]:
        score_i += 6
    scores_2.append(score_i)
ans_2_1 = sum(scores_2)
for i in list_2:
    if i[1] == "Z":
        for j in guide["Win"]:
            if j[0] == i[0]:
                i[1] = j[1]
                break
    elif i[1] == "X":
        for j in guide["Lose"]:
            if j[0] == i[0]:
                i[1] = j[1]
                break
    elif i[1] == "Y":
        for j in guide["Draw"]:
            if j[0] == i[0]:
                i[1] = j[1]
                break

scores_2 = []
for i in list_2:
    score_i = guide_2[i[1]]
    if i in guide["Draw"]:
        score_i += 3
    elif i in guide["Win"]:
        score_i += 6
    scores_2.append(score_i)
ans_2_2 = sum(scores_2)'''
# day_3
input_3 = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
'''list_3_1 = [list(set(i[len(i) // 2:]).intersection(set(i[:len(i) // 2]))) for i in input_3.splitlines()]
guide_3 = {}
for i in range(97, 123):
    guide_3[chr(i)] = i - 96
for i in range(65, 91):
    guide_3[chr(i)] = i - 38
ans_3_1 = sum(guide_3[i[0]] for i in list_3_1)
list_3_2 = []
j = 0
t = []
for i in input_3.splitlines():
    if j < 2:
        t.append(i)
        j += 1
    elif j == 2:
        t.append(i)
        list_3_2.append(t)
        t = []
        j = 0
t = []
for i in list_3_2:
    t.append(list(set(i[0]).intersection(set(i[1])).intersection(set(i[2]))))
ans_3_2 = sum(guide_3[i[0]] for i in t)
print(ans_3_2)'''
# day_4
input_4 = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
'''
list_4 = [x.strip() for x in input_4.splitlines()]

ans_4_1 = 0
ans_4_2 = 0
for i in list_4:
    a, b, c, d = map(int, re.findall(r"\d+", i))
    x = set(range(a, b + 1))
    y = set(range(c, d + 1))
    if x - y == set() or y - x == set():
        ans_4_1 += 1
    if x & y != set():
        ans_4_2 += 1

print(ans_4_1, ans_4_2)'''
# day_5 : broken if stack 1 is not max size (compared to other stacks); EXTREMELY shitty and hardcoded parsing
input_5 = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
'''list_5 = [i.splitlines() for i in input_5.split("\n\n")]
list_5[0] = list(map(list, list_5[0]))
list_5[0][-1] = "".join(list_5[0][-1])
copier = []
for i in iter(list_5[0][:-1]):
    count = 0
    t = []
    i = iter(i)
    for j in i:
        if j == '[':
            if count != 0:
                print(count)
                blanks = (count-1)//4
                for blank in range(blanks):
                    t.append("")
                count = 0
            t.append(j + next(i) + next(i))
        if j == " ":
            count += 1
    print(t)
    copier.append(t)
copier.append(re.split(r'\s+', list_5[0][-1][1:-1]))
print(copier)
list_5[0] = copier
print(list_5[0])
stacks_5 = {int(i): [] for i in list_5[0][-1]}
list_5[1] = [[int(i.split()[1]), int(i.split()[3]), int(i.split()[5])] for i in list_5[1]]
print(list_5[1])
print(list_5[0])
for i in range(0, len(list_5[0]) - 1):
    print(i)
    for j in range(len(list_5[0][i])):
        stacks_5[j + 1].append(list_5[0][i][j])

for i in stacks_5:
    stacks_5[i] = list(filter(lambda a: a != '', stacks_5[i]))
for instance in list_5[1]:
    print(instance, stacks_5[instance[1]], stacks_5[instance[2]])
    for i in range(instance[0]):
        stacks_5[instance[2]].insert(0, stacks_5[instance[1]].pop(0))
    print("STACK     :", stacks_5)
ans_5_1 = ''
for i in stacks_5:
    ans_5_1+=stacks_5[i][0][1]
print(ans_5_1)
# day 5_2
for instance in list_5[1]:
    print(instance, stacks_5[instance[1]], stacks_5[instance[2]])
    list_5_2 = []
    for i in range(instance[0]):
        list_5_2.insert(0, stacks_5[instance[1]].pop(0))
    for i in list_5_2:
        stacks_5[instance[2]].insert(0, i)
    print("STACK     :", stacks_5)
ans_5_2 = ''
for i in stacks_5:
    ans_5_2+=stacks_5[i][0][1]
print(ans_5_2)'''
# day_6
input_6 = ''
'''for i in range(len(input_6)-3):
    var = ''
    for j in range(4):
        var += input_6[i+j]
    if len(set(var)) == 4:
        print(i+4)
        break
        
for i in range(len(input_6)-13):
    var = ''
    for j in range(14):
        var += input_6[i+j]
    if len(set(var)) == 14:
        print(i+14)
        break'''
# day_7
input_7 = '''$ cd /
$ ls
dir dscbfp
283653 fsdfddfv
dir mjzqq
241330 rcm.psp
dir sjbpgc
dir zfsbvs
$ cd dscbfp
$ ls
dir fgtvzpl
dir hgfrgbv
dir hmwqgjnl
dir jvr
dir lcvdgm
dir mmhtpz
dir wqc
dir znl
dir zph
dir zwlpm
$ cd fgtvzpl
$ ls
dir fvrghzfg
28513 lbbg.rhq
$ cd fvrghzfg
$ ls
212295 cjb.nwg
dir ftqs
$ cd ftqs
$ ls
250415 mmhtpz
$ cd ..
$ cd ..
$ cd ..
$ cd hgfrgbv
$ ls
86365 cdrgnzrz.hwf
175318 wqtmwb
$ cd ..
$ cd hmwqgjnl
$ ls
dir dscbfp
dir dwtfrgj
130223 fnl.whg
66339 mtcv
dir rgvvz
$ cd dscbfp
$ ls
146043 wpzr
$ cd ..
$ cd dwtfrgj
$ ls
dir jwmw
dir pntqg
$ cd jwmw
$ ls
dir dscbfp
243410 lbbg.phv
dir mmhtpz
$ cd dscbfp
$ ls
dir mmhtpz
$ cd mmhtpz
$ ls
dir mdrddz
$ cd mdrddz
$ ls
167704 fgjsq.bpb
$ cd ..
$ cd ..
$ cd ..
$ cd mmhtpz
$ ls
233626 dtcmsq.pdl
163642 jczs.rgg
111667 msfmjd.vlr
23137 ndhvh.jbq
$ cd ..
$ cd ..
$ cd pntqg
$ ls
68578 lnjvpcgq.zqs
62492 rcm.psp
$ cd ..
$ cd ..
$ cd rgvvz
$ ls
dir hmwqgjnl
dir jrjgnch
110656 lnjvpcgq.zqs
206537 mmhtpz.wgd
198736 msfmjd.vlr
110172 rrl.wqz
dir wrb
$ cd hmwqgjnl
$ ls
141962 bsgljmww.whq
dir hsmr
123313 msfmjd.vlr
223573 rcm.psp
$ cd hsmr
$ ls
229737 fzptbrzb.lqv
$ cd ..
$ cd ..
$ cd jrjgnch
$ ls
4426 lbbg.fzh
dir zbnp
$ cd zbnp
$ ls
65658 cjqbfv.fjf
270282 pwv.bcz
$ cd ..
$ cd ..
$ cd wrb
$ ls
dir fgwnpp
249291 lbbg
dir mbd
dir rdnf
dir rgvvz
dir rnrr
dir vzjh
$ cd fgwnpp
$ ls
dir gdfrtgl
230060 lbbg.qfm
275250 rbd.fqj
dir zlgpdb
$ cd gdfrtgl
$ ls
dir gvw
dir rgvvz
$ cd gvw
$ ls
123285 mmhtpz.vbl
167405 qhfqz
$ cd ..
$ cd rgvvz
$ ls
254625 rcm.psp
$ cd ..
$ cd ..
$ cd zlgpdb
$ ls
72966 cjjl.wzp
217828 ndhvh.jbq
141199 wbnl.qdc
$ cd ..
$ cd ..
$ cd mbd
$ ls
dir hmwqgjnl
$ cd hmwqgjnl
$ ls
13420 mmhtpz.snz
$ cd ..
$ cd ..
$ cd rdnf
$ ls
dir frqb
dir jjjzcjdh
dir mwpd
dir nvz
152893 rcm.psp
$ cd frqb
$ ls
dir dscbfp
231903 gwlj.lgn
dir mmhtpz
298674 nhc.hpl
193867 rfmv.dzd
dir sqt
$ cd dscbfp
$ ls
280820 rgvvz.glj
$ cd ..
$ cd mmhtpz
$ ls
137192 jczs.rgg
273426 rcm.psp
$ cd ..
$ cd sqt
$ ls
dir fwvgbgbs
245416 rgvvz.cgh
12489 wnjgq
$ cd fwvgbgbs
$ ls
dir mfpd
170052 msfmjd.vlr
278273 mwr.stv
177661 vgwstqlt.zml
$ cd mfpd
$ ls
264130 gmwhsj.jvp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jjjzcjdh
$ ls
dir cnjnnzw
dir flprjhlm
266398 fqclzm.mfw
dir gftmlvmh
113237 jgnmbml.rnr
148723 ljfg.vmc
237722 rrzvq.cqr
$ cd cnjnnzw
$ ls
231497 ldqdwn.bvf
$ cd ..
$ cd flprjhlm
$ ls
185486 hmwqgjnl.jdn
$ cd ..
$ cd gftmlvmh
$ ls
dir blpt
41840 qbr.tjw
$ cd blpt
$ ls
dir sbtg
$ cd sbtg
$ ls
7518 wsh.vrp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd mwpd
$ ls
35589 flgh
$ cd ..
$ cd nvz
$ ls
147018 mpmcpwnl.hqg
$ cd ..
$ cd ..
$ cd rgvvz
$ ls
280057 dhwzlmgn
156280 gmzvl.gtg
dir hmwqgjnl
dir pfcjgrgp
dir prhzdjqv
132543 qlwqmd.wmj
223249 rcm.psp
124899 zvzjh.sbg
$ cd hmwqgjnl
$ ls
99756 mvdpfcvs.wft
$ cd ..
$ cd pfcjgrgp
$ ls
dir lbbg
dir nlgf
130799 wtrdvzhs
$ cd lbbg
$ ls
193125 lnjvpcgq.zqs
dir vnlmr
$ cd vnlmr
$ ls
39935 lgd.hzz
$ cd ..
$ cd ..
$ cd nlgf
$ ls
106563 jfr
$ cd ..
$ cd ..
$ cd prhzdjqv
$ ls
dir jhhq
$ cd jhhq
$ ls
135155 mzjdptfm.fln
$ cd ..
$ cd ..
$ cd ..
$ cd rnrr
$ ls
249039 jczs.rgg
154853 whlwl
$ cd ..
$ cd vzjh
$ ls
dir hjrs
$ cd hjrs
$ ls
146991 mmhtpz
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jvr
$ ls
13268 gwsldhjc.vbf
dir hbpwd
34369 mjtwr.rpv
dir tfvztnb
$ cd hbpwd
$ ls
253823 bzqc
dir dscbfp
237051 ggvvcpg.gmj
23097 mhl
211524 ndhvh.jbq
133936 qzslmmz.fzp
$ cd dscbfp
$ ls
184190 msfmjd.vlr
238872 ndhvh.jbq
dir pfsq
dir pljsm
dir tlgtcb
$ cd pfsq
$ ls
dir hmwqgjnl
249351 mmhtpz
$ cd hmwqgjnl
$ ls
301132 rcm.psp
$ cd ..
$ cd ..
$ cd pljsm
$ ls
263279 bqh.vhl
$ cd ..
$ cd tlgtcb
$ ls
50558 bgzrlnzz.rfm
83169 gtrjzl.hhh
212764 mgf.zlg
210599 mmhtpz.dqm
dir tqsvhc
$ cd tqsvhc
$ ls
264513 lnjvpcgq.zqs
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd tfvztnb
$ ls
dir mdz
$ cd mdz
$ ls
209155 dqjh
$ cd ..
$ cd ..
$ cd ..
$ cd lcvdgm
$ ls
135165 lbbg.gsz
282211 vlbwsps.plg
$ cd ..
$ cd mmhtpz
$ ls
dir dscbfp
dir mmhtpz
70564 msfmjd.vlr
dir nzdvqb
59232 rgvvz
dir ztbht
$ cd dscbfp
$ ls
dir cddzd
dir dscbfp
dir hmwqgjnl
142689 qnnc
dir whbjm
$ cd cddzd
$ ls
255928 dtnn.hzf
$ cd ..
$ cd dscbfp
$ ls
dir brvf
182587 fhmzbc.nlb
129514 lbbg
177841 ngw.tlj
dir qttp
dir zdmb
269964 zqn.htj
$ cd brvf
$ ls
24071 tzsvg.pwc
174118 vtdntn
$ cd ..
$ cd qttp
$ ls
54613 ccdnjnwz
131277 zzppc
$ cd ..
$ cd zdmb
$ ls
117682 bwjhr.gvw
dir hmwqgjnl
138816 jczs.rgg
273129 mmhtpz
89710 rcm.psp
dir rgvvz
$ cd hmwqgjnl
$ ls
102907 mmhtpz.dnp
235885 ndhvh.jbq
239856 rcm.psp
$ cd ..
$ cd rgvvz
$ ls
dir fpzzfc
292842 lbbg
70603 msfmjd.vlr
157797 qjs.zlm
dir zgn
$ cd fpzzfc
$ ls
dir rgvvz
$ cd rgvvz
$ ls
222407 crrwlp.zcd
$ cd ..
$ cd ..
$ cd zgn
$ ls
70915 hmwqgjnl.zdg
276918 lbbg.wlg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd hmwqgjnl
$ ls
207726 cqn.rds
$ cd ..
$ cd whbjm
$ ls
44954 ndhvh.jbq
136649 pphznj
dir ptq
215264 rmpbqgrl.mqt
276795 tbtv
292696 vddnpnp
dir wnqgpj
$ cd ptq
$ ls
191976 jczs.rgg
59747 ncbs.mjc
77874 njqmf
dir zss
$ cd zss
$ ls
209276 vnv.nvm
$ cd ..
$ cd ..
$ cd wnqgpj
$ ls
211738 jczs.rgg
$ cd ..
$ cd ..
$ cd ..
$ cd mmhtpz
$ ls
dir hmwqgjnl
$ cd hmwqgjnl
$ ls
dir jzb
dir mmhtpz
$ cd jzb
$ ls
138393 drqp.ttd
250098 jczs.rgg
dir mfq
$ cd mfq
$ ls
dir nfn
$ cd nfn
$ ls
239922 rcm.psp
$ cd ..
$ cd ..
$ cd ..
$ cd mmhtpz
$ ls
158815 jvwqttqn
72929 jvzfccm
18353 lwz.clt
144822 rnvfllt.fwn
$ cd ..
$ cd ..
$ cd ..
$ cd nzdvqb
$ ls
226139 rcm.psp
$ cd ..
$ cd ztbht
$ ls
279766 jczs.rgg
222685 msfmjd.vlr
$ cd ..
$ cd ..
$ cd wqc
$ ls
dir cndf
dir hmwqgjnl
dir lbbg
$ cd cndf
$ ls
dir hmwqgjnl
284014 qsr.pjg
$ cd hmwqgjnl
$ ls
91921 zrsp.qwd
$ cd ..
$ cd ..
$ cd hmwqgjnl
$ ls
dir fccbrtcn
23864 msfmjd.vlr
286035 nrbmbpm
dir pwvgqth
91650 rgvvz
dir wllwhm
$ cd fccbrtcn
$ ls
87931 bmjdngzq.zbv
dir cwr
dir djngvdp
266568 lnjvpcgq.zqs
dir zdwhqb
$ cd cwr
$ ls
dir cmnv
$ cd cmnv
$ ls
dir dscbfp
dir dwdnwdz
291794 rcm.psp
$ cd dscbfp
$ ls
dir gtcg
$ cd gtcg
$ ls
73017 pgzcm.qbz
$ cd ..
$ cd ..
$ cd dwdnwdz
$ ls
dir hvgwfj
$ cd hvgwfj
$ ls
235064 rnjjh.qnp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd djngvdp
$ ls
264940 jczs.rgg
162343 rgvvz
$ cd ..
$ cd zdwhqb
$ ls
233875 ggd
230766 ggqrt.pqn
$ cd ..
$ cd ..
$ cd pwvgqth
$ ls
dir nrm
dir rgvvz
289164 sgdsg.fbs
$ cd nrm
$ ls
135745 hmwqgjnl.fwb
$ cd ..
$ cd rgvvz
$ ls
269675 rcm.psp
$ cd ..
$ cd ..
$ cd wllwhm
$ ls
14033 rptrszg.lfh
$ cd ..
$ cd ..
$ cd lbbg
$ ls
dir fsz
dir hmwqgjnl
2856 jpmw.tsp
156026 ndhvh.jbq
dir rgmmpm
dir vzg
$ cd fsz
$ ls
29744 cdsr
dir frjzv
dir hmwqgjnl
75723 hmwqgjnl.jcj
222555 jczs.rgg
dir lbbg
dir pplp
184370 vzb
$ cd frjzv
$ ls
87553 lnjvpcgq.zqs
$ cd ..
$ cd hmwqgjnl
$ ls
94991 hsjmzpq
$ cd ..
$ cd lbbg
$ ls
177441 dscbfp
9637 lnjvpcgq.zqs
$ cd ..
$ cd pplp
$ ls
230787 gcjfcbg.sds
54478 twnslqqv.gtw
54723 wzwcw.pfj
$ cd ..
$ cd ..
$ cd hmwqgjnl
$ ls
dir drpt
dir dscbfp
18560 jczs.rgg
dir tpt
$ cd drpt
$ ls
dir gmcpd
10052 jczs.rgg
87927 mmhtpz.jdt
dir rgvvz
$ cd gmcpd
$ ls
dir rgvvz
$ cd rgvvz
$ ls
dir tjqcj
$ cd tjqcj
$ ls
273175 bgsjwb
$ cd ..
$ cd ..
$ cd ..
$ cd rgvvz
$ ls
104452 fbv
$ cd ..
$ cd ..
$ cd dscbfp
$ ls
dir bjn
dir rvm
$ cd bjn
$ ls
119619 mmhtpz.slf
$ cd ..
$ cd rvm
$ ls
dir hgl
$ cd hgl
$ ls
9146 jczs.rgg
294696 rcm.psp
$ cd ..
$ cd ..
$ cd ..
$ cd tpt
$ ls
102194 tmlbnm
$ cd ..
$ cd ..
$ cd rgmmpm
$ ls
25462 dcp.zfg
99756 frmlbqp
71786 msfmjd.vlr
275455 mvrszdhp.jbr
$ cd ..
$ cd vzg
$ ls
dir hmwqgjnl
160612 msfmjd.vlr
103726 pprnm.rmw
$ cd hmwqgjnl
$ ls
130188 ndhvh.jbq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd znl
$ ls
256149 qcd
dir rgrhdq
dir wfhcc
$ cd rgrhdq
$ ls
dir nqpz
17930 rglm.wrj
$ cd nqpz
$ ls
253269 rcm.psp
$ cd ..
$ cd ..
$ cd wfhcc
$ ls
dir dpds
dir hmwqgjnl
82595 rcm.psp
dir rgvvz
$ cd dpds
$ ls
143467 bljj.ddw
283261 rcm.psp
$ cd ..
$ cd hmwqgjnl
$ ls
dir fnmqpt
$ cd fnmqpt
$ ls
288739 dscbfp
$ cd ..
$ cd ..
$ cd rgvvz
$ ls
41475 srcnvmj.tqb
$ cd ..
$ cd ..
$ cd ..
$ cd zph
$ ls
dir hmwqgjnl
dir tbwhzrtt
$ cd hmwqgjnl
$ ls
67069 rcm.psp
219165 rgvvz
$ cd ..
$ cd tbwhzrtt
$ ls
198892 gwlw.hbb
94996 mmhtpz
dir wwwj
$ cd wwwj
$ ls
dir lcttc
14000 lnjvpcgq.zqs
$ cd lcttc
$ ls
141874 jhlrtbjw.thr
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd zwlpm
$ ls
206595 ctvmprqd.nwz
292861 dscbfp.bpv
171719 ldmrl.zhz
23134 lnjvpcgq.zqs
dir mmhtpz
283001 msfmjd.vlr
dir pwrfgjdg
dir qdztzhl
$ cd mmhtpz
$ ls
90712 lzv.smr
102181 mcntll.fgt
260630 nhn.fll
219684 tlws
dir tpsvqmgb
$ cd tpsvqmgb
$ ls
dir bpmqlq
$ cd bpmqlq
$ ls
67400 lnjvpcgq.zqs
$ cd ..
$ cd ..
$ cd ..
$ cd pwrfgjdg
$ ls
30612 fflm
174894 jczs.rgg
$ cd ..
$ cd qdztzhl
$ ls
dir dscbfp
dir gcpjnrb
dir nlffhf
dir vnrgqg
dir zrpgb
$ cd dscbfp
$ ls
dir gdjvclf
dir mbhdvsq
dir tqb
dir vlqqslp
$ cd gdjvclf
$ ls
104663 hwwlf.mhv
$ cd ..
$ cd mbhdvsq
$ ls
98749 gqsjtd.rbv
200237 lbbg.nwb
$ cd ..
$ cd tqb
$ ls
101550 cqjmfvd.grg
dir hmwqgjnl
$ cd hmwqgjnl
$ ls
dir mlmmr
$ cd mlmmr
$ ls
dir rgvvz
$ cd rgvvz
$ ls
188297 gprgzd.rjf
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd vlqqslp
$ ls
191754 lbbg
$ cd ..
$ cd ..
$ cd gcpjnrb
$ ls
254902 nzzsg.bds
$ cd ..
$ cd nlffhf
$ ls
295353 hhjqvqnc
dir mmhb
58446 rgvvz.hsj
120084 rvgctqpr.qpp
302397 wtmlrm
$ cd mmhb
$ ls
57621 ndhvh.jbq
$ cd ..
$ cd ..
$ cd vnrgqg
$ ls
dir fpmpzvj
dir gtqwbhc
213709 hmwqgjnl
283893 hmwqgjnl.bbc
dir lnw
dir mmhtpz
177958 rcm.psp
68642 vzr.gwd
297210 zqcvpgfm.sgv
$ cd fpmpzvj
$ ls
62127 mmhtpz.mwv
$ cd ..
$ cd gtqwbhc
$ ls
174559 rgvvz
$ cd ..
$ cd lnw
$ ls
dir lbbg
162886 mlsb
dir rgvvz
dir szgmtgb
253283 zpvqj.crr
$ cd lbbg
$ ls
dir jgwj
dir ndljhbv
dir smhzdbn
68451 sznhpr
$ cd jgwj
$ ls
290222 fnpmb
148122 lnjvpcgq.zqs
dir ptwrtdcf
4669 rcm.psp
76708 thgtnwhq
$ cd ptwrtdcf
$ ls
dir gcjpt
$ cd gcjpt
$ ls
dir hmwqgjnl
$ cd hmwqgjnl
$ ls
259660 lnjvpcgq.zqs
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ndljhbv
$ ls
226511 qmtttllc.wgt
$ cd ..
$ cd smhzdbn
$ ls
161029 mjwqn.bfs
49691 msfmjd.vlr
77941 ncwrv.fjc
12615 ndhvh.jbq
19222 rlrnrcqw.cgh
$ cd ..
$ cd ..
$ cd rgvvz
$ ls
270852 msfmjd.vlr
$ cd ..
$ cd szgmtgb
$ ls
167819 ndhvh.jbq
$ cd ..
$ cd ..
$ cd mmhtpz
$ ls
6153 msfmjd.vlr
$ cd ..
$ cd ..
$ cd zrpgb
$ ls
dir dgcrgg
dir dscbfp
dir gcdtbrnj
dir hmwqgjnl
284848 hnfqrh.nll
dir jsjrg
16735 lbbg.lpg
274897 vrp.fvm
$ cd dgcrgg
$ ls
dir gpvhhh
210466 lbbg
161257 tqc.qgg
dir zggnvwcb
$ cd gpvhhh
$ ls
100124 msfmjd.vlr
$ cd ..
$ cd zggnvwcb
$ ls
76550 dsmvrsp.hht
106682 swj.pnq
$ cd ..
$ cd ..
$ cd dscbfp
$ ls
297842 msfmjd.vlr
$ cd ..
$ cd gcdtbrnj
$ ls
78674 jmc.sst
$ cd ..
$ cd hmwqgjnl
$ ls
280262 hmwqgjnl
dir hrl
dir mmhtpz
159812 rcm.psp
$ cd hrl
$ ls
dir cqwbgn
dir nlqd
dir wmgqpt
$ cd cqwbgn
$ ls
91489 msfmjd.vlr
$ cd ..
$ cd nlqd
$ ls
1982 jczs.rgg
172223 rcm.psp
$ cd ..
$ cd wmgqpt
$ ls
dir hmwqgjnl
91172 jczs.rgg
125726 lbbg
147883 rgvvz
99929 rhzwrpw.jml
145844 tzzqwr
$ cd hmwqgjnl
$ ls
198790 mlccths
284058 mmhtpz.dvb
$ cd ..
$ cd ..
$ cd ..
$ cd mmhtpz
$ ls
60918 hmwqgjnl.jhw
220709 lnjvpcgq.zqs
$ cd ..
$ cd ..
$ cd jsjrg
$ ls
230757 czg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd mjzqq
$ ls
33792 fsrws.tdp
dir lbbg
50734 lnz.fwp
268057 wbgjwnb
$ cd lbbg
$ ls
207413 cqf
$ cd ..
$ cd ..
$ cd sjbpgc
$ ls
73862 lbbg.ddv
$ cd ..
$ cd zfsbvs
$ ls
dir lbbg
10390 lqgh.fpl
147426 mqw.fmr
273227 rcm.psp
$ cd lbbg
$ ls
dir mmhtpz
$ cd mmhtpz
$ ls
25218 dtdt'''
'''input = input_7.splitlines()
input.append('$ EOF')

def process_commands(commands):
    filesystem = []
    cur_dir = -1
    directory = ''
    inode = -1
    for l, command_line in enumerate(commands):
        token = command_line.split()
        if token[0] == '$':
            if directory != '':
                inode += 1
                filesystem.append(directory)
                cur_dir = inode
                directory = ''
            command = token[1]
            if command == 'cd':
                argument = token[2]
                if argument == '..':
                    cur_dir = filesystem[cur_dir]['parent']
                    dir_name = filesystem[cur_dir]['dir_name']
                else:
                    parent_dir = cur_dir
                    dir_name = argument
            elif command == 'ls':
                directory = {'dir_name': dir_name, 'parent': parent_dir, 'files': [], 'dirs': [], 'total_size': 0}
        elif token[0] == 'dir':
            subdir = token[1]
            directory['dirs'].append(subdir)
        else:
            size = int(token[0])
            file = token[1]
            directory['files'].append((file, size))
            directory['total_size'] += size
            # percolate file size up the tree
            pdir = directory['parent']
            while True:
                if pdir == -1: break
                filesystem[pdir]['total_size'] += size
                pdir = filesystem[pdir]['parent']
    print(filesystem)
    return filesystem


# -----------------------------------------------------------------------------------------
filesystem = process_commands(input)

directory_sum = 0

total_disk_space = 70000000
used_space = filesystem[0]['total_size']
unused_space = total_disk_space - used_space

required_unused = 30000000
space_to_free = required_unused - unused_space

best_delete_size = total_disk_space
delete_dir = ''

for directory_inode, directory in enumerate(filesystem):
    dir_size = directory['total_size']
    if dir_size <= 100000:
        directory_sum += dir_size
    if dir_size >= space_to_free:
        if dir_size < best_delete_size:
            best_delete_size = dir_size
            delete_dir = directory['dir_name']

print('Part 1 answer:', directory_sum)
print('Part 2 answer: delete dir', delete_dir, 'to free', best_delete_size)'''
# day 8
input_8 = '''30373
25512
65332
33549
35390'''
'''list_8 = [list(map(int, list(i))) for i in input_8.splitlines()]
visible = 0


def is_visible(i, j):
    if i == 0 or i == len(list_8) - 1:
        return True
    if j == 0 or j == t - 1:
        return True
    if max(list_8[i][j + 1:]) < list_8[i][j] or \
            max(list_8[i][:j]) < list_8[i][j] or \
            max(x[j] for x in list_8[i + 1:]) < list_8[i][j] or \
            max(x[j] for x in list_8[:i]) < list_8[i][j]:
        return True
    else:
        return False
def scenic_score(i, j):
    if i == 0 or i == len(list_8) - 1:
        return 0
    if j == 0 or j == t - 1:
        return 0
    l = {'score': 0, 'max': 0}
    u = {'score': 0, 'max': 0}
    d = {'score': 0, 'max': 0}
    r = {'score': 0, 'max': 0}
    column = [col[j] for col in list_8]
    for x in range(1, j+1):  # left
        if list_8[i][:j][-x] >= l['max']:
            l['max'] = list_8[i][:j][-x]
            l['score'] += 1
    for x in list_8[i][j+1:]:  # right
        if x >= r['max']:
            r['max'] = x
            r['score'] += 1
    for x in range(1, i+1):  # up
        if column[:i][-x] >= u['max']:
            u['max'] = column[:i][-x]
            u['score'] += 1
    for x in column[i+1:]:
        if x >= d['max']:
            d['max'] = x
            d['score'] += 1
    return l['score']*r['score']*u['score']*d['score']

t = len(list_8[0])
ans_8_2 = 0
for i in range(len(list_8)):
    for j in range(t):
        u = scenic_score(i, j)
        if u > ans_8_2:
            print(i, j, list_8[i][j], u)
            ans_8_2 = u
        if is_visible(i, j):
            visible += 1
print(visible)
print(ans_8_2)'''
# day 9
input_9 = '''R 1
D 1
L 1
D 1
L 2
U 2
D 2
R 1
D 1
L 2
R 1
L 2
R 2
L 1
R 2
D 1
R 1
D 2
U 1
R 1
D 2
R 2
L 1
D 1
R 2
D 2
R 1
L 2
D 1
L 2
D 2
R 2
D 2
L 1
D 1
L 1
D 1
R 2
L 2
R 2
D 2
R 2
D 2
R 2
L 2
R 2
U 1
R 1
D 2
R 1
L 1
U 1
L 2
U 1
D 1
R 1
U 1
R 2
D 2
U 2
D 2
R 1
L 1
U 2
L 2
D 2
L 1
R 2
D 1
R 1
L 2
U 2
R 1
D 1
U 2
L 1
U 2
L 1
R 2
D 2
R 1
D 2
R 1
D 1
R 1
D 1
L 2
D 2
R 2
D 2
R 1
D 1
R 2
L 1
U 2
R 2
D 1
L 2
U 1
D 2
L 2
D 2
L 2
D 1
R 1
L 1
U 2
L 2
D 1
L 2
U 1
L 3
D 1
R 1
U 3
L 2
U 1
D 3
L 1
D 2
R 1
L 3
D 2
L 2
D 1
L 1
R 2
L 3
D 2
L 1
U 3
L 1
R 3
U 1
R 3
U 3
D 1
L 2
U 2
D 2
U 3
D 3
L 1
U 3
D 3
L 3
R 1
D 1
U 2
R 1
U 3
L 3
D 2
L 3
D 1
R 2
U 1
D 2
L 3
D 2
U 2
R 1
L 3
R 2
L 2
U 2
R 2
L 1
D 1
U 3
D 1
R 2
L 1
U 1
R 1
L 1
D 2
L 1
D 1
L 1
D 3
U 3
D 3
R 3
D 2
L 1
R 1
L 1
D 3
L 2
D 1
R 1
D 3
U 3
L 2
D 1
U 1
D 1
U 3
R 2
L 1
D 3
U 3
D 3
U 2
L 1
R 1
U 1
D 3
R 2
U 1
L 2
U 1
L 2
U 2
D 1
L 3
U 1
R 1
L 2
U 1
D 2
L 1
D 4
L 3
D 4
R 2
D 2
L 3
U 2
L 3
D 1
L 4
R 2
D 1
U 4
L 3
D 1
R 1
D 4
R 4
U 3
D 3
L 3
D 3
U 1
R 4
L 2
D 1
R 3
L 4
D 1
R 2
L 4
U 3
L 4
R 1
L 3
D 1
U 4
L 4
R 3
U 4
D 3
U 2
R 3
D 1
R 3
L 3
D 2
U 4
R 3
U 4
L 4
R 4
L 2
R 2
D 3
L 2
U 1
L 4
U 3
R 3
L 4
U 1
L 1
U 1
D 2
R 1
U 1
L 3
R 4
L 2
D 4
R 3
L 2
R 1
L 4
R 1
D 2
R 4
L 3
U 3
L 3
D 1
R 2
L 4
D 2
R 3
U 2
D 3
R 2
U 4
L 1
U 2
D 2
L 1
D 4
R 3
L 3
R 4
D 1
U 2
R 2
D 1
L 3
U 2
L 3
R 1
D 1
R 4
L 4
R 1
U 3
R 4
L 3
D 3
L 4
R 4
D 5
R 2
U 5
L 1
D 5
L 5
R 1
L 5
U 5
L 3
D 3
L 2
D 1
L 1
U 1
L 1
D 2
L 3
U 2
D 3
L 4
R 5
U 2
L 3
D 3
R 4
U 3
D 5
U 1
R 3
L 3
D 1
U 2
L 3
R 5
D 2
R 2
U 4
L 2
R 4
D 5
R 2
U 2
D 5
L 3
R 2
D 2
L 1
U 2
R 1
D 2
U 1
L 2
U 5
R 1
U 4
D 1
R 4
U 4
R 3
D 1
U 2
L 5
U 1
L 3
D 1
U 5
D 5
U 1
L 3
D 1
R 2
L 4
R 4
L 2
U 2
R 5
U 1
R 5
L 1
D 1
R 3
D 2
R 4
L 5
D 3
L 3
U 5
R 2
D 5
L 1
U 2
D 2
U 4
R 4
L 4
U 1
D 1
U 4
R 4
D 3
L 4
R 2
D 3
R 5
U 4
L 4
R 4
L 2
U 4
R 4
D 1
R 3
D 6
U 6
D 5
L 4
R 2
D 5
R 5
D 3
R 3
U 3
D 3
U 2
L 2
R 6
L 6
D 1
L 4
R 6
D 5
L 2
R 4
U 2
L 5
R 6
U 6
D 1
U 3
D 3
R 1
L 4
D 2
U 1
L 2
R 1
D 3
U 5
R 1
D 2
U 5
D 5
R 3
U 2
D 4
U 2
R 5
U 4
R 2
L 4
U 5
L 3
D 1
R 3
U 3
L 1
U 1
L 2
R 5
U 2
D 4
R 1
D 5
L 6
R 6
U 2
D 4
R 4
D 4
L 6
D 3
U 1
L 4
U 5
R 3
D 3
R 6
D 3
R 6
D 1
L 3
R 4
D 5
R 4
D 6
R 3
U 6
R 4
U 1
D 4
L 2
D 4
L 2
U 2
R 4
D 4
L 1
D 4
U 4
D 6
U 3
D 1
L 2
D 5
R 2
D 2
L 5
R 4
L 5
R 5
U 6
L 1
R 3
U 5
D 1
U 2
R 2
D 4
R 4
D 6
R 4
L 4
D 2
R 6
L 1
D 1
U 3
R 1
D 4
L 1
D 3
U 5
R 2
U 2
D 6
L 5
U 4
L 5
R 3
U 7
R 2
D 1
R 6
D 6
U 6
R 5
D 5
R 6
D 6
R 6
D 5
U 5
D 7
L 4
U 3
D 3
U 2
L 2
U 4
D 1
R 7
U 4
L 1
D 4
L 3
R 6
L 1
R 2
L 4
R 5
U 6
D 6
U 2
R 5
U 4
L 5
U 3
D 1
L 6
R 2
D 2
L 3
U 5
R 6
U 7
R 1
L 7
D 5
U 5
D 2
R 4
U 2
L 7
R 4
D 7
U 4
D 3
R 2
D 3
L 3
U 6
R 2
L 6
D 2
R 6
L 3
R 4
U 1
D 3
U 2
L 4
D 6
U 7
D 4
L 3
R 1
U 6
L 3
R 3
U 7
R 7
U 6
L 1
U 8
L 1
D 8
L 6
R 3
L 7
D 5
U 8
R 5
L 4
U 8
L 3
D 2
U 1
R 8
D 8
R 7
U 1
D 2
R 6
L 8
D 5
L 6
U 1
R 2
U 6
L 3
D 6
U 2
R 2
D 1
U 4
L 8
D 8
R 1
L 2
R 2
D 7
U 5
D 8
L 1
R 7
L 8
D 2
R 8
D 7
U 3
R 3
U 3
D 1
L 2
U 6
D 7
U 8
R 6
D 6
R 5
U 7
R 8
L 1
U 7
D 2
R 6
U 7
R 3
D 3
R 3
U 4
D 8
L 7
R 5
U 1
L 6
R 8
D 6
R 4
L 4
D 1
U 5
L 6
U 1
D 8
U 2
R 4
L 2
R 8
D 1
R 1
L 4
R 7
U 7
D 8
R 8
L 6
U 7
L 4
D 2
R 2
U 5
D 1
R 5
L 6
U 8
L 1
R 7
D 8
L 3
D 2
U 3
D 3
L 1
R 3
L 7
D 6
R 4
D 1
U 8
L 3
D 6
L 7
U 5
R 6
D 2
L 4
R 9
D 2
R 4
D 6
R 5
L 7
R 5
U 7
R 1
L 5
U 6
R 4
D 8
U 5
L 4
U 1
D 8
U 9
D 4
U 7
L 4
R 8
D 4
R 4
D 8
R 1
D 3
R 5
D 7
U 8
D 2
R 2
U 1
L 1
U 2
L 9
R 9
D 1
U 1
D 8
R 3
L 8
D 7
U 9
R 6
L 4
U 8
D 4
U 2
L 3
D 8
L 2
R 5
U 4
D 6
U 6
L 8
R 7
D 2
R 3
L 8
U 9
R 2
U 4
L 9
R 5
D 5
R 4
D 6
R 3
D 3
R 8
D 3
R 4
D 1
U 2
D 6
R 4
D 7
U 5
D 2
R 6
D 3
U 3
R 4
U 5
L 3
U 5
L 8
D 3
L 8
D 5
R 4
L 8
R 5
U 8
R 10
D 2
U 10
R 1
D 1
L 4
D 9
L 6
U 2
R 3
D 2
L 6
R 2
L 10
D 2
L 10
U 3
L 2
D 8
U 10
R 5
L 1
U 8
R 9
D 8
U 2
R 4
U 3
D 2
U 4
D 2
R 3
L 2
U 4
D 1
U 9
R 2
U 1
R 3
D 3
L 3
R 2
D 1
U 8
D 1
L 5
R 4
L 8
D 3
L 1
U 10
R 9
D 9
U 9
D 1
R 6
L 6
U 6
L 1
D 5
L 4
U 8
L 10
U 9
R 9
D 5
U 4
D 7
R 5
U 10
D 5
U 1
R 5
L 7
D 9
R 5
L 3
U 2
D 6
R 4
D 7
U 4
R 8
L 5
R 8
L 9
R 8
D 1
R 1
L 9
D 7
L 10
D 6
R 8
U 4
D 4
R 7
L 9
D 9
R 9
L 1
R 6
L 7
R 10
L 1
U 9
D 11
R 4
D 4
U 5
R 8
U 9
L 8
D 8
L 10
U 10
L 4
D 1
L 3
U 7
D 11
U 4
L 7
R 2
U 9
D 4
R 4
U 1
L 5
U 10
R 4
D 3
L 9
R 2
L 3
U 5
D 6
U 2
R 7
D 7
R 4
L 8
U 5
R 1
U 4
D 3
U 5
R 9
D 2
R 4
D 8
U 9
R 7
U 5
D 3
R 6
L 7
U 7
R 10
L 3
U 10
L 8
R 11
L 3
U 10
R 5
D 1
U 7
R 6
U 9
L 3
R 9
L 4
R 9
L 5
R 9
D 5
U 8
R 7
L 7
R 4
L 9
R 9
D 7
R 2
L 3
U 1
L 1
D 11
U 3
D 5
R 3
U 11
L 1
U 7
R 8
D 8
U 7
D 7
R 6
D 3
R 8
L 9
U 10
D 10
L 1
D 9
L 1
R 5
D 6
U 5
L 1
R 10
L 1
U 7
D 11
R 8
U 11
L 6
R 4
U 7
R 3
L 8
D 8
L 12
U 3
D 12
L 6
R 1
U 8
R 3
U 4
L 3
D 10
L 9
D 6
L 12
R 11
D 4
U 4
L 12
R 1
U 1
D 10
L 11
R 3
D 4
R 4
U 4
D 3
U 10
R 9
U 9
L 1
U 10
D 11
U 4
D 3
L 10
R 5
D 8
R 5
U 6
R 12
L 10
U 10
D 2
L 6
U 5
D 3
R 2
D 3
U 7
D 1
L 5
U 9
D 3
U 10
L 10
U 4
L 12
R 11
D 2
L 10
U 6
L 4
D 5
R 3
L 4
D 8
U 7
R 12
D 1
U 5
L 2
D 7
R 3
U 1
L 10
R 9
L 7
R 8
U 9
R 9
U 1
L 7
D 6
L 1
R 11
L 9
U 12
R 8
U 3
R 5
U 5
L 12
R 7
L 8
R 11
L 4
R 10
D 2
L 4
U 12
R 5
D 1
L 12
D 1
L 5
D 3
U 8
L 5
U 5
R 7
D 1
L 3
D 9
L 12
R 5
D 12
U 6
L 7
D 6
L 5
U 6
R 7
U 5
D 8
R 11
D 12
R 10
L 11
R 6
L 13
D 3
L 2
U 4
D 12
U 8
D 6
R 2
D 2
R 13
U 1
D 6
R 8
D 12
L 8
R 4
L 7
R 8
D 9
U 3
L 1
U 3
L 10
R 12
U 13
R 7
U 1
D 13
U 6
L 13
D 11
U 8
L 10
D 13
R 11
L 8
D 5
U 11
R 1
D 9
L 4
D 12
R 13
L 11
D 7
L 9
U 8
L 13
D 11
L 10
R 4
U 4
D 4
L 5
D 7
L 12
U 10
R 3
L 10
U 2
L 2
R 8
L 6
U 11
L 4
D 4
U 9
L 1
R 12
D 12
R 13
D 8
R 8
L 12
U 5
D 8
L 7
D 13
U 12
D 12
R 10
U 10
R 13
D 9
R 3
U 13
L 12
R 6
U 14
D 11
R 14
L 2
R 5
U 6
R 10
U 6
L 3
R 8
U 7
L 3
D 4
R 13
L 10
D 5
U 10
R 13
L 6
R 6
L 1
D 4
U 10
R 14
U 7
L 11
R 14
D 11
R 8
D 2
U 13
L 5
R 10
D 6
U 7
D 7
L 6
U 11
L 4
D 11
L 9
R 6
L 5
U 14
R 2
D 1
U 12
L 3
U 3
D 2
U 3
L 7
U 10
D 2
R 9
L 8
U 10
D 4
R 7
U 4
L 8
R 3
L 6
D 2
R 11
L 2
D 12
U 14
L 1
R 1
U 12
R 3
L 14
U 9
D 7
L 3
U 8
R 9
L 4
U 7
D 4
R 5
D 7
R 11
L 13
R 3
D 10
R 11
U 6
L 4
D 9
R 4
U 5
D 9
R 13
D 6
R 11
L 1
D 1
R 13
U 4
L 9
U 14
L 9
R 2
D 2
L 7
D 13
L 11
D 8
R 4
L 7
R 4
U 12
D 5
R 13
D 14
R 7
U 6
R 2
U 13
L 7
U 14
R 11
U 15
R 8
U 7
D 7
L 5
U 2
D 13
U 11
L 12
R 6
D 13
L 6
U 8
L 3
R 15
L 13
D 1
U 2
L 14
D 8
L 4
U 6
R 11
D 11
R 2
U 13
L 13
R 2
U 15
R 3
D 4
L 7
R 7
D 7
R 7
L 13
R 10
U 8
R 13
L 2
U 13
D 8
U 15
L 4
D 13
R 13
U 8
R 3
L 11
R 12
U 2
L 13
U 1
L 9
U 11
D 14
R 12
D 6
U 6
D 12
U 8
R 3
U 4
R 8
U 2
D 5
L 12
U 14
D 4
R 1
U 10
L 10
R 6
D 13
U 11
D 11
U 11
R 14
D 15
L 11
U 14
D 7
L 12
D 3
L 14
U 7
R 1
U 5
L 1
R 15
U 13
D 7
R 9
L 15
U 15
L 15
D 7
R 15
D 3
U 5
L 8
R 13
L 15
D 8
L 15
D 12
L 5
D 14
U 16
R 11
L 14
R 6
L 10
U 11
R 8
U 16
L 6
U 9
L 13
D 14
R 7
D 10
L 15
D 1
L 10
D 1
R 2
U 15
L 9
U 6
D 3
L 8
D 13
U 16
D 12
R 2
L 1
D 8
L 15
R 14
D 8
L 9
U 12
R 3
U 15
D 10
U 13
R 8
L 15
D 9
R 8
L 9
U 2
R 7
L 11
R 3
D 13
U 16
L 9
U 6
L 7
U 4
L 16
U 16
L 12
U 9
R 8
D 13
L 2
R 15
D 7
U 15
D 16
R 12
L 12
U 8
L 8
D 3
R 16
L 3
U 13
R 1
L 5
R 10
U 13
D 7
R 3
D 10
L 2
R 1
U 4
L 13
U 15
R 4
D 1
R 2
L 5
D 3
L 1
R 4
L 1
U 1
D 7
R 9
L 12
R 13
D 5
R 5
D 9
L 15
R 17
D 4
R 2
U 1
D 1
R 3
L 15
D 10
L 8
U 16
L 14
U 12
R 5
L 13
D 10
L 15
D 12
U 4
D 8
R 9
L 17
D 17
U 3
D 2
L 14
D 12
L 5
D 9
L 3
R 10
U 1
R 9
U 16
L 14
R 13
L 11
R 4
U 2
L 10
D 6
R 5
D 17
L 15
R 12
U 15
L 9
U 9
D 3
R 8
U 6
R 8
U 9
D 14
R 7
U 1
L 3
R 3
D 2
U 4
R 5
L 17
D 16
U 13
D 5
U 6
R 2
U 5
D 7
U 11
R 6
L 17
R 4
L 14
D 3
U 15
L 5
R 4
U 1
D 16
L 16
U 10
L 10
D 17
R 6
D 2
U 10
L 10
D 12
R 15
L 4
R 11
L 17
U 15
L 8
U 8
L 16
D 6
L 7
U 17
L 14
D 6
L 5
R 14
U 5
D 1
U 2
D 17
R 14
L 1
R 4
D 7
L 8
U 7
D 6
L 16
U 5
D 7
R 7
D 17
L 16
R 1
D 5
U 17
L 2
U 7
L 16
U 15
L 17
D 3
L 2
R 7
L 11
R 1
L 16
U 2
L 1
R 18
U 5
L 9
U 4
D 8
U 4
L 18
D 17
L 14
D 2
R 1
U 13
L 9
R 14
D 14
U 12
D 14
L 2
U 10
D 11
R 10
L 9
U 7
D 12
L 4
D 2
R 17
D 1
U 15
R 14
D 16
L 1
R 11
U 9
R 8
U 6
D 7
U 7
L 2
D 10
U 9
D 9
L 11
D 11
L 14
U 16
D 11
L 17
R 5
L 13
U 16
R 16
U 18
D 1
R 1
U 13
R 6
L 7
U 11
D 12
L 8
U 17
D 11
U 8
L 14
U 17
L 4
U 18
D 18
R 8
D 13
L 10
U 3
R 9
L 14
R 7
U 14
R 14
L 9
U 5
R 4
D 13
U 10
D 1
R 10
D 4
R 3
U 14
D 10
U 12
L 11
U 9
L 16
R 5
L 14
D 4
U 11
L 2
R 10
U 8
D 9
L 2
R 16
L 1
R 12
U 7
D 11
U 18
D 4
R 8
U 18
D 5
R 15
U 16
L 2
D 15
U 5
D 10
U 18
L 7
U 4
R 2
U 17
L 2
R 3
D 2
L 2
U 3
R 10
L 8
U 4
L 18
U 6
D 11
R 13
D 9
U 10
L 16
R 15
L 4
D 1
L 5
D 7
U 18
L 5
R 7
L 15
U 4
L 6
U 19
D 19
L 2
R 2
L 19
D 9
L 14
U 18
D 12
R 19
U 15
L 16
U 9
L 11
R 5
L 14
R 16
U 19
D 7
U 8
R 6
U 14
R 17
D 9
L 5
U 3
D 9
U 8
L 4
U 12
D 12
R 13
U 3
R 18
U 5
L 12
U 4
L 1
D 14
R 5
L 19
U 17
R 18
D 11
L 4
U 18
L 9'''
'''UNIT_VECTORS = {"U": 1j, "D": -1j, "L": -1, "R": 1}

def move_tail(moves: list, length: int):
    rope = [0j] * length
    print(rope)
    tail_positions = set()
    for direction, steps in moves:
        for _ in range(int(steps)):
            rope[0] += UNIT_VECTORS[direction]
            for n in range(1, len(rope)):
                diff = rope[n - 1] - rope[n]
                if abs(diff) > sqrt(2):
                    if diff.real != 0:
                        rope[n] += diff.real / abs(diff.real)
                    if diff.imag != 0:
                        rope[n] += complex(0, diff.imag) / abs(diff.imag)
            tail_positions.add(rope[-1])
    return tail_positions


moves = [l.split() for l in input_9.splitlines()]
print(len(move_tail(moves, 2)))
print(len(move_tail(moves, 10)))'''
# day 10
input_10 = '''noop
addx 12
addx -5
addx -1
noop
addx 4
noop
addx 1
addx 4
noop
addx 13
addx -8
noop
addx -19
addx 24
addx 1
noop
addx 4
noop
addx 1
addx 5
addx -1
addx -37
addx 16
addx -13
addx 18
addx -11
addx 2
addx 23
noop
addx -18
addx 9
addx -8
addx 2
addx 5
addx 2
addx -21
addx 26
noop
addx -15
addx 20
noop
addx 3
noop
addx -38
addx 3
noop
addx 26
addx -4
addx -19
addx 3
addx 1
addx 5
addx 3
noop
addx 2
addx 3
noop
addx 2
noop
noop
noop
noop
addx 5
noop
noop
noop
addx 3
noop
addx -30
addx -4
addx 1
addx 18
addx -8
addx -4
addx 2
noop
addx 7
noop
noop
noop
noop
addx 5
noop
noop
addx 5
addx -2
addx -20
addx 27
addx -20
addx 25
addx -2
addx -35
noop
noop
addx 4
addx 3
addx -2
addx 5
addx 2
addx -11
addx 1
addx 13
addx 2
addx 5
addx 6
addx -1
addx -2
noop
addx 7
addx -2
addx 6
addx 1
addx -21
addx 22
addx -38
addx 5
addx 3
addx -1
noop
noop
addx 5
addx 1
addx 4
addx 3
addx -2
addx 2
noop
addx 7
addx -1
addx 2
addx 4
addx -10
addx -19
addx 35
addx -1
noop
noop
noop'''
'''cycle = 0
x = 2
mark = 20
ss = 0
instructions = [[i.split()[0], i.split()[-1]] for i in input_10.splitlines()]
for instruction in instructions:
    if instruction[0] == "noop":
        if cycle == mark:
            ss += mark*x
            mark += 40
        cycle += 1
        if cycle == mark:
            ss += mark*x
            mark += 40

    elif instruction[0] == "addx":
        cycle += 1
        if cycle == mark:
            ss += mark*x
            mark += 40
        cycle += 1
        if cycle == mark:
            ss += mark*x
            mark += 40
        x += int(instruction[1])
    if mark == 260:
        break
print(ss) # part 1
mark_2 = 40
for instruction in instructions:
    if instruction[0] == "noop":
        cycle += 1
        if cycle in [x-1, x, x+1]:
            print("#", end="")
        else:
            print(".", end="")
        if cycle == mark_2:
            mark_2+= 40
            x+= 40
            print()
    elif instruction[0] == "addx":
        cycle += 1
        if cycle in [x-1, x, x+1]:
            print("#", end="")
        else:
            print(".", end="")
        if cycle == mark_2:
            mark_2 += 40
            x += 40
            print()
        cycle += 1
        if cycle in [x-1, x, x+1]:
            print("#", end="")
        else:
            print(".", end="")
        if cycle == mark_2:
            mark_2 += 40
            x += 40
            print()
        x += int(instruction[1])'''
# day 11
input_11 =''''''
