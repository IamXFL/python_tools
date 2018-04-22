#-*-coding:utf-8-*
#!/usr/bin/python

dict = {'add11':'页面地址',
          'bit':'位地址',
          'rel':'相对偏移量，带符号8位偏移字节',
          'direct':'直接地址单元（RAM-SFR-I0)',
          '#data':'立即数','Rn':'工作寄存器',
          '(Rn)':'工作寄存器的内容',
          'A':'累加器',
          '(A)':'累加器的内容',
          '((Ri))':'Ri指出的单元的内容',
          '(X)':'某一寄存器的内容',
          'X':'某一寄存器',
          'ADD':'ADD A,Rn  FUNCTION A <-(A)+(Rn)',
          'ADDC':'ADDC Rn  FUNCTION A <- (A) + (Rn) + (Cy)',
          'SUBB':'SUBB A,Rn  FUNCTION A <- (A) - (Rn) - (Cy)',
          'INC':'INC A   FUNCTION A <--(A) + 1',
          'DPTR':'数据指针，可用作16位数据寄存器',
          'DEC':'DEC A  FUNCTION A <--(A) - 1',
          'MUL':'MUL AB  FUNCTION AB <-- (A) * (B)',
          'DIV':'DIV AB  FUNCTION  AB <-- (A)除以(B),商放在(A)中，余数放在(B)中',
          'DA':'DA A   FUNCTION 对A进行十进制调整',
          'ANL':'ANL A,Rn  FUNCTION A <-- (A)与(Rn)按位与',
          'ORL':'ORL A,Rn  FUNCTION A <-- (A)与(Rn)按位或',
          'XRL':'XRL A,Rn  FUNCTION A <-- (A)与(Rn)按位异或',
          'CLR':'CLR A   FUNCTION A <--0',
          'CPL':'CPL A   FUNCTION 按位取反',
          'RL':'RL A    FUNCTION A循环左移一位',
          'RLC':'RLC A  FUNCTION A带进位循环左移一位',
          'RR':'RR A   FUNCTION A 循环右移一位',
          'RRC':'RRC A   FUNCTION A 带进位循环右移一位',
          'SWAP':'SWAP A  FUNCTION A 半字节交换',
          'MOV':'MOV A,Rn   FUNCTION A <-- (Rn)',
          'MOVC':'MOVC A,@A + DPTR   FUNCTION A <-- ((A) + (DPTR))',
          'MOVX':'MOVX A,@Ri   FUNCTION A <--((Ri) + (P2)); MOVX A,@DPTR   FUNCTION A <--((DPTR)); MOVX A,@A+PC FUNCTION A <-- ((A)+(PC))',
          'PUSH':'PUSH direct  FUNCTION SP <--(SP)+1, (SP) <-- (direct)',
          'POP':'POP direct   FUNCTION direct <-- (SP) , (SP) <--(SP) - 1',
          'XCH':'XCH A,Rn   FUNCTION A <--> Rn 指向的单元VALUE',
          'XCHD':'XCHD A,@Ri   FUNCTION (A)0~3  <--> ((Ri))0~3 交换值',
          'SETB':'SETB C  FUNCTION Cy <-- 1; SETB bit  FUNCTION bit <-- 1',
          'ACALL':'ACALL addr11  FUNCTION PC <-- (PC) +2,SP<--(SP)+1,(SP)<--(PC)L,SP<--(SP)+1,(SP)<--(PC)H,PC10~PC0<--addr11',
          'LCALL':'LCALL addr16  FUNCTION PC <-- (PC) +3,SP<--(SP)+1,(SP)<--(PC)L,SP<--(SP)+1,(SP)<--(PC)H,PC<--addr16',
          'RET':'RET  FUNCTION PCH(此处H为下标) <--((SP)),SP<--(SP)-1,PCL(此处的L为下标)<--((SP)),SP<--(SP)-1',
          'RETI':'RETI FUNCTION PCH(此处H为下标) <--((SP)),SP<--(SP)-1,PCL(此处的L为下标)<--((SP)),SP<--(SP)-1,从中断返回',
          'AJMP':'AJMP addr11 FUNCTION PC10~PC0 <--addr11',
          'LJMP':'LJMP addr16 FUNCTION PC <-- addr16',
          'SJMP':'SJMP rel  FUNCTION PC <--(PC) + rel',
          'JMP':'JMP @A + DPTR  FUNCTION PC <--(A)+(DPTR)',
          'JZ':'JZ rel  FUNCTION PC <-- (PC) +2;若(A)=0,PC <--PC + rel  累加器内容为0时跳转',
          'JNZ':'JNZ rel FUNCTION PC <--(PC) + 2;若(A)！!0，PC <--PC + rel, 累加器内容不为0时跳转',
          'JC':'JC rel  FUNCTION PC <-- (PC) + 2;若Cy = 1, PC <-- (PC) + 2, Cy 为进位位',
          'JNC':'JNC rel FUNCTION PC <---(PC) +2;若Cy = 0, PC <-- (PC) + 2,Cy 为进位位',
          'JB':'JB bit,rel FUNCTION PC <-- (PC) +3; 若(bit) =1,则 PC <--(PC) +rel',
          'JNB':'JNB bit,rel FUNCTION PC <-- (PC) +3; 若（bit) = 0， 则PC<--(PC) +rel',
          'CJNE':'CJNE A,direct,rel   FUNCTION PC <--(PC)+3; 比较指令，若不相等，PC <--(PC)+rel;若(A)<direct,则Cy <-- 1，之后可通过判断Cy是否为1建立新的分支结构',
          'DJNZ':'DJNE Rn,rel   FUNCTION PC<--(PC) + 2, Rn <-- (Rn) -1;若(Rn) ！= 0， PC <--(PC) + rel,常用于判断循环标志是否为0',
          'NOP':'NOP   FUNCTION 空操作'};
COMMAND = 'LANXIANFENG';
while(COMMAND!='0'):
        COMMAND = raw_input("INPUT THE COMMAND YOU WANT TO SEARCH,USE MAJUSCULE(大写字母):")
        print 
        print "EXAMPLE MNEMONIC,FUNCTION EXPLAIN\n";
        if COMMAND in dict.keys():
              print dict[COMMAND];
              print 
        else:
             print "sorry,cannot find the command.";
             print 
print "SEARCH FINISHED";


    
