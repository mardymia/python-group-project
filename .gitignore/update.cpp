#include <iostream>
#include <string>
#include <ctime>
#include <windows.h>

using namespace std;

void runCommand(string command);
string ddNum(int inputInt);

int main() {
	time_t rawTime = time(0);
	string command2 = "git commit -m \"New commit (" + ddNum(localtime(&rawTime)->tm_mday) + "-";
	switch (localtime(&rawTime)->tm_mon) {
		case 0:
			command2 += "Jan-";
			break;
		case 1:
			command2 += "Feb-";
			break;
		case 2:
			command2 += "Mar-";
			break;
		case 3:
			command2 += "Apr-";
			break;
		case 4:
			command2 += "May-";
			break;
		case 5:
			command2 += "Jun-";
			break;
		case 6:
			command2 += "Jul-";
			break;
		case 7:
			command2 += "Aug-";
			break;
		case 8:
			command2 += "Sept-";
			break;
		case 9:
			command2 += "Oct-";
			break;
		case 10:
			command2 += "Nov-";
			break;
		case 11:
			command2 += "Dec-";
			break;
	}
	command2 += to_string(localtime(&rawTime)->tm_year + 1900) + "-" + ddNum(localtime(&rawTime)->tm_hour) + ":" + ddNum(localtime(&rawTime)->tm_min) + ":" + ddNum(localtime(&rawTime)->tm_sec) + ")\"";
	string command1 = "git add .";
	string command3 = "git push origin main";
	runCommand(command1);
	runCommand(command2);
	runCommand(command3);
	//cout << command1 << endl << command2 << endl << command3 << endl;
	system("pause");
	return 0;
}

void runCommand(string command) {
	system(command.c_str());
}

string ddNum(int inputInt) {
	if (inputInt < 10)
		return "0" + to_string(inputInt);
	else
		return to_string(inputInt);
}