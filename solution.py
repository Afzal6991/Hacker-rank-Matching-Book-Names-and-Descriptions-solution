from nltk.stem.porter import PorterStemmer


porter = PorterStemmer()



stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
            "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", 
            "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
            "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", 
            "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", 
            "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", 
            "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
            "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", 
            "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", 
            "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor",
            "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", 
            "now"];


ll=int(input())

tt=[]
tt1=[]
dd=[]
dd1=[]
for t in range(ll):
    tt.append(input().split(' '))
    
    
for d in range(ll+1):
    dd.append(input().split('.'))
    

dd.remove(['*****'])
des=[]
for i in range(ll):
    des.append(dd[i][0])
    dd1.append(dd[i][0].split(' '))
    

dd11=[]
tt0=[]
for e in range(ll):
    for q in range(len(dd1[e])):
        w=str(dd1[e][q])
        if w not in stop_words:
            tt0.append(porter.stem(dd1[e][q]))
    dd11.append(tt0)
    tt0=[]
    
rr=[]
tt0=[]
for e in range(ll):
    for q in range(len(tt[e])):
        w=str(tt[e][q])
        if w not in stop_words:
            tt0.append(porter.stem(tt[e][q]))
    rr.append(tt0)
    tt0=[]
    
    
#print(dd11)
#print(rr)

temp=[]
ml=int(0)
i=int(0)
for u in range(ll):
    i=int(0)
    ml=int(0)
    for y in range(ll):
        temp=list((set(dd11[u])& set(rr[y])))
        #print(temp)
        if(len(temp)>ml):
            ml=len(temp)
            #print(ml)
            i=y
    print(i+1)
        
        

