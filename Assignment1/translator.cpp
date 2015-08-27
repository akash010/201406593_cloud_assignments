#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

string line;

int main()
{
	vector<string> keywords_32, keywords_64;
	keywords_32.push_back("ebp"); 
	keywords_32.push_back("esp");
	keywords_32.push_back("eax");
	keywords_32.push_back("edi");
	keywords_32.push_back("movl");
	keywords_32.push_back("subl");
	keywords_32.push_back("addl");
	keywords_32.push_back("pushl");

	keywords_64.push_back("rbp");
	keywords_64.push_back("rsp");
	keywords_64.push_back("rax");
	keywords_64.push_back("rdi");
	keywords_64.push_back("movq");
	keywords_64.push_back("subq");
	keywords_64.push_back("addq");
	keywords_64.push_back("pushq");

	while( getline(cin, line))
	{
		for (int i = 0; i < keywords_32.size(); ++i)
		{
			if(line.find(keywords_32[i]) != -1)
				line.replace(line.find(keywords_32[i]),keywords_32[i].size(), keywords_64[i] );
		}
		cout << line << endl;
	}
	return 0;
}