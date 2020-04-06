#include<iostream>
#include<math.h>				// to use pow function
using namespace std;
int main(){
  int num,d=0,n,r,p=0,a=1;
  char choice;
  cin>>num;					//changed insertion operator (<<) to get from operator (>>)
  cin>>choice;					//changed insertion operator (<<) to get from operator (>>)
  switch(choice)				//switch typo fixed
	{
	case 'a':				// added colon, case value should be constant changed it to 'a'
		n=num;
		while(n!=0)
		{
			n=n/10;
			d++;
		}
		n=num;
		while(n!=0)
		{
			r=n%10;
			a=a*pow(r,d);		// sqr changed to pow, removed Equal sign to make it assign
			n=n/10;
		}
		cout<<a<<"\n";  
		break;				// added break
	case 'p':				// added colon, case value should be constant changed it to 'p'
		n=num;
		while(n!=0)
		{
			r=n%10;
			p=(p*10)+r;		// removed Equal sign, changed p+10+r to (p*10)+r
			n=n/10;
		}
		cout<<p<<"\n";
		//continue;			// No need of continue
	}
}

