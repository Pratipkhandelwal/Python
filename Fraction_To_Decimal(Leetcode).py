def fractionToDecimal(numerator,denominator):
        val = numerator / denominator
        first = str(val)[:2]
        sec = str(val)[2:]
        print(first,sec)
        v = ""
        z = int(sec)
        if(len(sec)>1):
            for i in range(0,len(sec)-1):
                if(sec[i]!=sec[i+1]):
                    v+=sec[i]
                else:
                    v+="(" + str(sec[i]) + ")"
                    break
            final = first + v
            print(str(final))
        else:
            print(first + sec)
                
        
numerator = int(input())
denominator = int(input())
fractionToDecimal(numerator,denominator)
