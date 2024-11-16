import sys,time
from tkinter import Tk, Label, Button, Entry, INSERT



def main():
    def getTable(exp, avar):
        dexp = exp
        rem = len(avar)
        l_val = []
        for ii in range(len(avar)):
            st = "0" * int((2 ** rem) / 2)
            st += "1" * int((2 ** rem) / 2)
            rem -= 1
            st *= int(2 ** (len(avar) - rem) / 2)
            l_val.append(st)

        def finalres(dexp):
            cc = 0
            res = []
            fers = []
            for ii in range(int(2 ** len(avar))):
                adexp = dexp
                for jj in range(len(avar)):
                    adexp = adexp.replace(avar[jj], l_val[jj][ii])
                res.append(eval(adexp))
                cc += 1
            for i in res:
                if i == -1:
                    fers.append(0)
                    continue
                elif i == -2:
                    fers.append(1)
                    continue
                fers.append(i)
            return fers

        return(finalres(dexp))

        Tableres = finalres(dexp)
        print(finalres(dexp), len(finalres(dexp)))
        return Tableres

        pass

    def getVars(exp):
        vars=[]
        st = ""
        dup = exp
        dup = list(dup.split(" "))
        for ii in dup:
            if ii in [" ", "and", "or", "not"] :
                dup.remove(ii)
        for ii in dup:
            st+=ii
        lst = set(list(st))
        for ii in lst:
            if ord(ii) in range(97,123):
                vars.append(ii)
        vars.sort()
        return vars

    def expConv(stexp):
        stexp = "0 + " + stexp
        oexp = ''
        for i in range(len(stexp)):
            if stexp[i].isdigit():
                oexp += stexp[i]
            if ord(stexp[i]) in range(97, 123) or stexp[i] in ['(', ')'," "]:
                oexp += ""+stexp[i]+""
            if stexp[i] in ['*', "."]:
                oexp += " and "
            if stexp[i] in ['+']:
                oexp += " or "
            if stexp[i] == "'":
                if ord(oexp[-1]) in range(97, 123):
                    t = oexp[-1]
                    oexp = oexp[:len(oexp) - 1] + " not " + t
                if oexp[-1] == ')':
                    c = 0
                    j = len(oexp) - 1
                    while j > 0:
                        if oexp[j] == ')':
                            c += 1
                        if oexp[j] == '(':
                            c -= 1
                        if oexp[j] == '(' and c == 0:
                            t = oexp[j:]
                            oexp = oexp[:j] + " not " + t
                            break
                        j -= 1;
        oexp = oexp.replace('and', '&')
        oexp = oexp.replace('or', '|')
        oexp = oexp.replace('not', '~')
        return oexp[5:]

    def fAnd():

        if str(top.focus_get()) == ".!entry":
            Eexp1.insert(Eexp1.index(INSERT), "*")
        elif str(top.focus_get()) == ".!entry2":
            Eexp2.insert(Eexp2.index(INSERT), "*")

    def fOr():
        if str(top.focus_get()) == ".!entry":
            Eexp1.insert(Eexp1.index(INSERT), "+")
        elif str(top.focus_get()) == ".!entry2":
            Eexp2.insert(Eexp2.index(INSERT), "+")

    def fNot():
        if str(top.focus_get()) == ".!entry":
            if ord(Eexp1.get()[-1]) in range(65,91) or ord(Eexp1.get()[-1]) in range(97,123):
                Eexp1.insert(Eexp1.index(INSERT)-1, "(")
                Eexp1.insert(Eexp1.index(INSERT) + 1, ")")
            Eexp1.insert(Eexp1.index(INSERT), "'")
        elif str(top.focus_get()) == ".!entry2":
            if ord(Eexp2.get()[-1]) in range(65,91) or ord(Eexp2.get()[-1]) in range(97,123):
                Eexp2.insert(Eexp2.index(INSERT)-1, "(")
                Eexp2.insert(Eexp2.index(INSERT) + 1, ")")
            Eexp2.insert(Eexp2.index(INSERT), "'")

    def fOpar():
        if str(top.focus_get()) == ".!entry":
            Eexp1.insert(Eexp1.index(INSERT), "(")
        elif str(top.focus_get()) == ".!entry2":
            Eexp2.insert(Eexp2.index(INSERT), "(")

    def fCpar():
        if str(top.focus_get()) == ".!entry":
            Eexp1.insert(Eexp1.index(INSERT), ")")
        elif str(top.focus_get()) == ".!entry2":
            Eexp2.insert(Eexp2.index(INSERT), ")")

    def fCalc():
        Stexp1 = Eexp1.get().lower()
        Stexp2 = Eexp2.get().lower()
        Oexp1, Oexp2 = expConv(Stexp1), expConv(Stexp2)

        print(Oexp1,'++++',Oexp2)
        avar1 = getVars(Oexp1)
        avar2 = getVars(Oexp2)
        print(avar1,'+++', avar2)
        t1 = getTable(Oexp1, avar1) if Oexp1 not in '   ' else []
        t2 = getTable(Oexp2, avar2) if Oexp2 not in '   ' else []
        print(t1,'\n',t2)

        ans1 = ''
        for i in t1:
            ans1 += '\n'+" "*10+str(i)+'-'*20
        Lout1.config(text="Truth Table (Exp 1)" + ans1)
        ans2 = ''
        for i in t2:
            ans2 += '\n' + '-'*20+str(i)+' '*10
        Lout2.config(text="Truth Table (Exp 2)" + ans2)

        if t1 == t2 :
            Lres.config(text="EQUAL", fg='green')
        else:
            Lres.config(text="NOT EQUAL", fg='red')




    top = Tk()
    top.title("Truth Table Calculator")
    top.resizable(0,0)
    top.geometry("600x700")

    Lexp1 = Label(top, text="Expression 1")
    Lexp1.place(x=20, y=40)
    Eexp1 = Entry(top, font="Helvetica 12 ", width=40)
    Eexp1.place(x=150, y=40)
    Lexp2 = Label(top, text="Expression 2")
    Lexp2.place(x=20, y=80)
    Eexp2 = Entry(top, font="Helvetica 12 ", width=40)
    Eexp2.place(x=150, y=80)

    Band = Button(top, text="AND",command=fAnd, width=4)
    Band.place(x=20, y=150)
    Bor = Button(top, text="OR",command=fOr, width=4)
    Bor.place(x=80, y=150)
    Bnot = Button(top, text="NOT", command=fNot, width=4)
    Bnot.place(x=140, y=150)
    BOpar = Button(top, text="(", command=fOpar, width=2)
    BOpar.place(x=200, y=150)
    BOpar = Button(top, text=")", command=fCpar, width=2)
    BOpar.place(x=225, y=150)

    BCalc = Button(top, text="Calculate", command=fCalc, width=10)
    BCalc.place(x=280, y=150)

    Lout1 = Label(top, font="Helvetica 10 ", text="Truth Table (Exp 1)")
    Lout1.place(x=40, y=200)

    Lout2 = Label(top, font="Helvetica 10  ", text="Truth Table (Exp 2)")
    Lout2.place(x=160, y=200)

    Lres = Label(top, font="Helvetica 15")
    Lres.place(x=300, y = 250)

    top.mainloop()

main()