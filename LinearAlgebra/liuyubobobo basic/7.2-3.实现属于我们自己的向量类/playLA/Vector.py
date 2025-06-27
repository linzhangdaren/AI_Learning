class Vector:
    def __init__(self,lst):
        self.values=lst
        
    #取元素索引
    def __getitem__(self,index):
        return self.values[index]
    
    #长度len
    def __len__(self):
        return len(self.values)
        
    def __repr__(self):#官方详细->Vector([1,2,3])
        return f"Vector({self.values})"
    def __str__(self):#非正式用户调用:print(对象)->(1,2,3)
        return f"({','.join(str(i) for i in self.values)})"