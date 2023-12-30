/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int solve(vector<int> &v){
    if(v[0]==0)
        v[0]=-1;
    for(int i=1;i<v.size();i++){
        if(v[i]==0){
            v[i]=-1;
        }
        v[i]+=v[i-1];
    }
    int cnt=0;
    unordered_map<int,int> mp;
    for(int i=0;i<v.size();i++){
        if(mp[v[i]]>0){
            cnt+=mp[v[i]];
        }
        if(v[i]==0)
            cnt++;
        mp[v[i]]++;
    }
    
    return cnt;
}
int main() {
    
	//code
	int t;
	cin>>t;
	while(t--){
	    
	    int k;
	    cin>>k;
	    vector<int> v;
	    while(k--){
	        int i;
	        cin>>i;
	        v.push_back(i);
	    }
	    cout<<solve(v)<<endl;
	}
	return 0;
}