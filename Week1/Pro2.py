s=input("请输入字符串");
sub="abba"#sub="bob";
start=0;
len_sub=len(sub);
num=0;
len_s=len(s);
while(start+len_sub-1<len_s):
    num+=s.count(sub,start,start+len_sub);
    start+=1; 
print("Number of times bob occurs is:")
print(num);
