s=input("请输入字符串");
lens=len(s);
cnt=0;
vowels="aeiou"
for i in s:
    if i in vowels:
        cnt+=1;
print(cnt);
