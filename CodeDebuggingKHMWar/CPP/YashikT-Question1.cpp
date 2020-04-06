#include <iostream>
#include <string.h>					// string typo fixed
using namespace std;					// to use std as a common namespace, to avoid std::cin, etc
int getLIndex(char *string,char c);			// to use getLIndex in main, string is changed to *string
int getFIndex(char *string,char c);			// to use getFIndex in main, added datatypes, I is capitalised in 
							// getFindex, changed string to *string
int main()
{
        char str[100];
        char ch; 
        int Lindex,Findex; 
        cin>>str;					// added semicolon
        cin>>ch;
        Lindex = getLIndex(str,ch);
        Findex= getFIndex(str,ch);
        if(Lindex!=-1)
                cout<<Lindex<<endl<<Findex;		// Positions of Lindex and Findex changed
        else
                cout<<"NOT FOUND"<<endl;
        return 0;
}
int getLIndex(char *string,char  c)			//string is changed to *string
{
        int size = strlen(string),i=0;			//len changed to strlen
        while(i<size)
        {

                if(string[i]==c){			// Equal sign added
                    return i;
                   //break;				// No need of break
                }
                i++; 
        }
	return i;

}
int getFIndex(char *string, char c)			// added datatypes and string to *string, capitalised I in getFindex
{
        int size = strlen(string);			//len changed to strlen
        int i=size; 
        while( i>=0)					// removed semicolon
{
                if(string[i]==c){
                    return i;
		    //break;				// No need of break
                }
        i--;
}
	return i;

}

