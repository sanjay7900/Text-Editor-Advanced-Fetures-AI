/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.


*******************************************************************************/
import java.util.*;
class string_rotate{
    int i,j,k,n;
    char s;
    String a,b;
    void my_string(String a,String b)
    { 
        this.a=a;
        this.b=b;
        n=b.length();
        for(j=0;j<2;j++){
        s=b.charAt(j);
        for(i=j;i<b.length();i++)
        {
            b.charAt(i)=b.charAt(i+1);
            
            
        }
        b.charAt(n-1)=s;
        
        
    }
    

        System.out.println("yes"+a+b);
    }
    
}
public class Main
{
	public static void main(String[] args) {
		System.out.println("Hello World");
		string_rotate a1=new string_rotate();
		a1.my_string("amazon","azonam");
	}
}
