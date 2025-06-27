#加载playLA里的Vector类
from playLA.Vector import Vector

if __name__ == '__main__':
    vec=Vector([1,2,3])
    print(vec)
    #vec的len长度
    print(len(vec))
    #vec元素索引
    print(vec[0])
    
    #向量相加
    vec2=Vector([4,5,6])
    vec3=vec+vec2
    print(f"{vec} + {vec2} = {vec3}")
    
    #零向量
    zero3=Vector.zero(3)
    print(zero3)
    print(vec+zero3)