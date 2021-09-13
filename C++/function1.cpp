#include<iostream>
using namespace std;
int sum(int A){
    int i ,Sum;
    Sum=0;

    for(i=0;i<=A;i++){
        Sum+=i;
        
    }
    //cout <<Sum;
    return Sum;
}
int main(){
    int n;
    cout<<"enter any number : ";
    cin>> n;
    sum(n);
    return 0;
}
