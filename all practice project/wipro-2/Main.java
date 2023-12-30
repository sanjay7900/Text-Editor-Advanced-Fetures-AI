/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
public class Main
{
	public static void main(String[] args) {
		System.out.println("Hello World");
		int n=3521,s=0,i=0,min=100000;
		while(i<4)
		{
		     
		    s=n%10;
		    n/=10;
		    if(s<min){
		        min=s;
		    }
		    else{
		        
		    }
		    i++;
		    System.out.println(s);
		}
		System.out.println(min);
	}
}
