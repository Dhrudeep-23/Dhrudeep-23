#add
st={'book1','book2','book3','book4'}
st.add('book5')
print(st)

#update
st.update(['book6','book7'])
print(st)

#clear
st.clear()
print(st)

#remove
st={'book1','book2','book3','book4'}
st.remove('book3')
print(st)

#pop
st.pop()
print(st)

#del
del st
# print(st)

# convert list into set
st={'book1','book2','book3','book4'}
li=['list','set']
st.update(li,st)
li=set(li)
print(li)

# convert tuple into set
st={'book1','book2','book3','book4'}
tp=('tuple','set')
st.update(tp,st)
tp=set(tp)
print(tp)

# convert dictionaries to set
st={'book1','book2','book3','book4'}
dic={'dic','set'}
st.update(dic,st)
dic=set(dic)
print(dic)

#union
car={'BMW','Ferrari','Buggati'}
bike={'Ducati','Harley','NS200'}
print(car|bike)

#difference
car={'BMW','Ferrari','Buggati'}
bike={'Ducati','Harley','NS200'}
print(car-bike)

#intersaction
