# include <iostream>
using namespace std;

int main() {
    char optr;
    float num1, num2;

    cout << "Enter two operands: ";
    cin >> num1 >> num2;

    cout << "Enter operator: +, -, *, /: ";
    cin >> optr;

    

    switch(optr) {
        case '+':
            cout << num1 << " + " << num2 << " = " << num1 + num2;
            break;

        case '-':
            cout << num1 << " - " << num2 << " = " << num1 - num2;
            break;

        case '*':
            cout << num1 << " * " << num2 << " = " << num1 * num2;
            break;

        case '/':
            cout << num1 << " / " << num2 << " = " << num1 / num2;
            break;

        default:
            
            cout << "INVALID OPERATOR";
            break;
    }

    return 0;
}