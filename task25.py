a="divya supermarket"
print(a.center(100, ).title())
name="kavya"
address="1-4/3,gandhi chowk"
phno="12345"
print('name:'+name,'address:'+address,'phno:'+phno, sep="\n" )

print("s.no","items","qty","price",sep="\t")
n=["salt","sugar","flour"]
s=0
for sno in range(0,3):
    items=n[sno]
    Sno=sno+1
    quantity=sno+1
    if items=="sugar":
        price=20*quantity
    elif items=="salt":
        price=5*quantity
    elif items=="flour":
        price=25*quantity
    print(Sno,items,quantity,price,sep="\t")
    s+=price
print("\t""\t""total",s)
b="thank you visit again"
print(b.center(100, ).title())

    
'''
                                         Divya Supermarket
name:kavya
address:1-4/3,gandhi chowk
phno:12345
s.no    items   qty     price
1       salt    1       5
2       sugar   2       40
3       flour   3       75
                total 120
                                       Thank You Visit Again

'''

