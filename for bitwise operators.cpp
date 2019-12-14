#include<iostream>
using namespace std;
int main()
{
	int a=5;
	int b=7;
	cout<<"The bitwise left shift operator:"<<(b<<1)<<endl;
	cout<<"The bitwise right shift operator:"<<(b>>1)<<endl;
	cout<<"The bitwise not operator:"<<~a<<endl;
	cout<<"The bitwise AND operator:"<<(a&b)<<endl;
	cout<<"The bitwise OR operator:"<<(a|b)<<endl;
	cout<<"The bitwise XOR operator:"<<(a^b)<<endl;
	return 0;
}



