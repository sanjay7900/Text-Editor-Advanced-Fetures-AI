/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include<iostream>
using namespace std;
 struct Employee
       {
              int Id;
              char Name[25];
              int Age;
              long Salary;
       };
int main()
       {
              int i;
              Employee Emp[3];         //Statement   1

              for(i=0;i<3;i++)
              {

                    cout<<"\nEnter details of " << i+1 << " Employee";

                    cout<<"\n\tEnter Employee Id : ";
                    cin>>Emp[i].Id;

                    cout<<"\n\tEnter Employee Name : ";
                    cin>>Emp[i].Name;

                    cout<<"\n\tEnter Employee Age : ";
                    cin>>Emp[i].Age;

                    cout<<"\n\tEnter Employee Salary : ";
                    cin>>Emp[i].Salary;
              }
                cout<<"\nDetails of Employees";
              for(i=0;i<3;i++)
              cout<<"\n"<<Emp[i].Id<<"\t"<<Emp[i].Name<<"\t"<<Emp[i].Age<<"\t"<<Emp[i].Salary;
       }
