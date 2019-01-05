k=0;
hcf=0;
num1=3
num2=10
if(num1>num2){
    k=num1;
    num1=num2;
    num2=k;
}
if(num1==0){
 process.abort();
}
if(num2%num1==0){
    hcf=num1;
}
while(hcf==0){
    
    if(num2%num1==0){
        hcf=num1;
    }
    else{
        j=num1;
        num1=num2%num1;
        num2=j;
    }
}

