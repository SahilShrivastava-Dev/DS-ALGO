# include <iostream>
using namespace std;
void add(int num1, int num2);
void sub(int num1, int num2);
void multiply(int num1, int num2);
void divide(int num1, int num2);

int main() {
    char optr;
    float num1, num2;

    cout << "Enter two operands(seperated by space !!dont use commas!!) : ";
    cin >> num1 >> num2;

    cout << "Enter operator: +, -, *, /: ";
    cin >> optr;

    

    switch(optr) {
        case '+':
            add(num1,num2);
            break;

        case '-':
            sub(num1,num2);
            break;

        case '*':
            multiply(num1,num2);
            break;

        case '/':
            divide(num1,num2);
            break;

        default:
            
            cout << "INVALID OPERATOR";
            break;
    }

    return 0;
}
void add(int num1, int num2){
    cout<<"the addition is : "<< num1+num2 ;
}
void sub(int num1, int num2){
    cout<<"the subtraction is : "<< num1-num2 ;
}
void multiply(int num1, int num2){
    cout<<"the multiplication is : "<< num1*num2 ;
}
void divide(int num1, int num2){
    cout<<"the division is : "<< num1/num2 ;
}