/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;
String anagram(string s1,string s2)
{
    int len=s1.length();
    int bool;
    int temp[len]={0};
    if(s1.length()!=s2.length())
    {
        return "not anagram";
        
    }
    else
    {
        for(int i=0;i<len;i++)
        {
            char c=s[i];
            bool=0;
            for(int j=0;j<len;i++)
            {
                if(s2[j]==c && temp[j]!=1)
                {
                    temp[j]=1;
                    bool=1;
                    
                    
                }
            }
            if(bool!=0)
        }
    }
    
}

int main()
{
    cout<<"Hello World";

    return 0;
}
