#include<iostream>
#include<cmath>

int main(){
    using std::cout;
    using std::cin;
    using std::string;

    char op ;
    int num1,num2,result;
    string line = "########################\n",line1 = "######";
    cout << line;
    cout << line1 << " Calculator " << line1;
    cout << "\n" << line;

    cout << "Enter First number\n";
    cin >> num1;

    cout << "Enter Second number\n";
    cin >> num2;

    cout << "Enter operator\n";
    cin >> op;
    
    switch (op)
    {
    case '+':
        result = num1 + num2;
        break;
    case '-':
        result = num1 - num2;
        break;
    case '/':
        result = num1 / num2;
        break;
    case '*':
        result = num1 * num2;
        break;
    case '%':
        result = num1%num2;
        break;
    default:
        cout << "insert a valid operator" << "\n";
        break;
    }

    cout << "result = " << result;
    return 0;

}