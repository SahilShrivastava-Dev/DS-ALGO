#include<iostream>
using namespace std;

int main(){
    int n ;
    double fact;
    fact=1;
    cout << "enter the number for factorial : ";
    cin>>n;
    for (int i=1;i<=n;i++){
        fact *= i;
    }
    cout<<fact << " is the factorial of "<< n;
    return 0;
}