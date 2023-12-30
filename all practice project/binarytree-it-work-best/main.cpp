/******************************************************************************

                              Online C++ Compiler.
        /******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include<stdlib.h>
#include<conio.h>
struct binary
{
  int data;
  struct binary *minadd;
  struct binary *maxadd;
};

void
left_view (struct binary *node, int max)
{

  if (node == NULL)
    {
      return;
    }
  if (max == 0)
    {

      left_view (node->minadd, max + 1);
      printf ("v-%d", node->data);
      max++;


    }
  else
    {

      left_view (node->minadd, max + 1);
      printf ("v-%d", node->data);
      left_view (node->maxadd, max + 1);




    }
}



void
printbinary (struct binary *head)
{
  if (head == NULL)
    {
      return;
    }
  else
    {
      printbinary (head->minadd);
      printf ("\n%d", head->data);
      printbinary (head->maxadd);
    }
}

int
main ()
{
  int i = 0;
  struct binary *start = NULL;
  struct binary *start1, *p, *last;

  while (i == 0)
    {
      p = (struct binary *) malloc (sizeof (struct binary));
      printf ("neter the data in binary tree");
      scanf ("%d", &p->data);

      if (start == NULL)
	{
	  p->maxadd = NULL;
	  p->minadd = NULL;
	  start = p;
	  start1 = p;
	  //last=p;
	}
      else
	{
	  p->minadd = NULL;
	  p->maxadd = NULL;
	  while (start1 != NULL)
	    {
	      last = start1;
	      if (p->data > last->data)
		{
		  start1 = start1->maxadd;
		  printf ("\nbda h");
		}

	      else if (p->data < last->data)
		{
		  start1 = start1->minadd;
		  printf ("\nchotaa h");
		}

	      printf ("yes");
	    }

	  if (last->data < p->data)
	    {
	      last->maxadd = p;
	      printf ("\nbde m gya");
	    }
	  if (last->data > p->data)
	    {
	      last->minadd = p;
	      printf (" chote m gya");
	    }

	}
      //last=start;
      start1 = start;
      //i++;
      printf ("enter the 0 to keep continue");
      scanf ("%d", &i);
    }
  /*  while(last!=NULL)
     {
     printf("\n%d",last->data);
     last=last->minadd;

     }
     last=start;
     while(last!=NULL)
     {
     printf("\n%d",last->data);
     last=last->maxadd;

     } */
  int max = 0;
  printbinary (start);
  left_view (start, max);
}
