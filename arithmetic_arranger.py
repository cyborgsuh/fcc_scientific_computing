def arithmetic_arranger(expression,solve=False):
    arithmetic_arranger_top=""
    arithmetic_arranger_bottom=""
    arithmetic_line=bottom_line(expression)   #   '-----    -----    -----    -----    '
    exp_breakdown=breakdown(expression)     #  
    line_count=arithmetic_line.split()
    sumx=""
    if len(expression)>5:
        print("Error: Too many problems.")
        exit()
    for count,exxp in enumerate(exp_breakdown):
        if len(exxp[0])>4 or len(exxp[2])>4:
            print("Error: Numbers cannot be more than four digits.")
            exit()
        if exxp[0].isdigit()==False or exxp[2].isdigit()==False:
            print("Error: Numbers must only contain digits.")
            exit()
        if exxp[1]!='+' and exxp[1]!='-':
            print("Error: Operator must be '+' or '-'.")
            exit()
        len_first=len(exxp[0])
        len_second=len(exxp[2])
        space=len(line_count[count])
        first=int(exxp[0])
        second=int(exxp[2])
        operator=exxp[1]
        if len_second>len_first:
            arithmetic_arranger_top+=" "*(space-len_first)+exxp[0]+'    '
            arithmetic_arranger_bottom+=exxp[1]+' '*(space-len_second-1)+exxp[2]+'    '
        elif len_first>len_second:
            arithmetic_arranger_top+=' '*(space-len_first)+exxp[0]+'    '
            arithmetic_arranger_bottom+=exxp[1]+' '*(space-len_second-1)+exxp[2]+'    '
        elif len_first==len_second:
            arithmetic_arranger_top+=' '*(space-len_first)+exxp[0]+'    '
            arithmetic_arranger_bottom+=exxp[1]+' '*(space-len_second-1)+exxp[2]+'    '
        if solve:
            if operator=='+':
                sum=first+second
                l=len(str(sum))
                sumx+=' '*(space-l)+str(sum)+'    '
            else:
                sum=first-second
                l=len(str(sum))
                sumx+=' '*(space-l)+str(sum)+'    '




    
    print(arithmetic_arranger_top)
    print(arithmetic_arranger_bottom)
    print(arithmetic_line)
    print(sumx)
def breakdown(expression):
        for i in expression:
            expression_list=i.split()
            yield expression_list
def bottom_line(the_list):
    line=''
    for exxp in the_list:
        exxps=exxp.split()
        len_first=len(exxps[0])
        len_second=len(exxps[2])
        if len_second>len_first:
            line+='-'*(len_second+2)+'    '
        elif len_first>len_second:
            line+='-'*(len_first+2)+'    '
        elif len_first==len_second:
            line+='-'*(len_first+2)+'    '
    return line


if __name__=="__main__":
    arithmetic_arranger(["3801 - 2", "123 + 49"],True)
