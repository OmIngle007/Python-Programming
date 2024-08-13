def count(string,sub_string,flag):
	count=0
	start=0
	if flag==True:
		while True:
	   		start=string.find(sub_string,start)
	   		if start==-1:
	        		break
	   		count+=1
	   		start+=1
		return count	
		
	else:
	   flag==False
	   return string.count(sub_string)
	   		

print(count("suuuuuunidhi","uu",True))
	
