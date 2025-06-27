class Vector:
    def __init__(self,lst):
        self.values=lst
        
    #取元素索引
    def __getitem__(self,index):
        return self.values[index]
    
    #长度len
    def __len__(self):
        return len(self.values)
    
    #向量加法
    def __add__(self,another):
        #assert的语法: assert 语法, 错误信息|如果语法为True,什么都不做,为False,则抛出错误信息
        assert len(self)==len(another), "两个向量的维度必须相同"#如果不成立就报错
        #等价于: 但是不会像assert中断程序
        # if len(self.values)==len(another.values):
        #   print("两个向量的维度必须相同") 
        return Vector([a+b for a,b in zip(self.values,another.values)])
    #等价于:
        #return Vector([self[i]+another[i] for i in range(len(self))])   
        
    #向量减法
    def __sub__(self,another):
        assert len(self)==len(another), "两个向量的维度必须相同"#如果不成立就报错
        return Vector([a-b for a,b in zip(self.values,another.values)])
    
    #向量的乘法 向量*数
    def __mul__(self,k):
        return Vector([k*e for e in self])
    #向量的右乘运算 数*向量
    def __rmul__(self,k):
        return self*k
    
    #向量取正
    def __pos__(self):
        return 1*self
    #向量取负
    def __neg__(self):
        return -1*self
        
        
    def __repr__(self):#官方详细->Vector([1,2,3])
        return f"Vector({self.values})"
    def __str__(self):#非正式用户调用:print(对象)->(1,2,3)
        return f"({','.join(str(i) for i in self.values)})"