#include <iostream>
#include <string>
#include <ctime>
#include <windows.h>

using namespace std;

string input(string dialog);
void runCommand(string command);
string ddNum(int inputInt);
string getDateAsString();

int main() {
	string customMessage = "New commit";
	string inputString = input("Custom message? Y/N: ");
	if (inputString.find('Y') != string::npos || inputString.find('y') != string::npos) {
		system("cls");
		customMessage = input("Enter custom message:\n\n> ");
		
	}
	time_t rawTime = time(0);
	string command1 = "git add .";
	string command2 = "git commit -m \"" + customMessage + " (" + getDateAsString() + ")\"";
	string command3 = "git push origin main";
	system("cls");
	cout << "Commands:\n\n" << command1 << endl << command2 << endl << command3 << "\n\n";
	system("pause");
	system("cls");
	command2 = "git commit -m \"" + customMessage + " (" + getDateAsString() + ")\"";
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

string input(string dialog) {
	cout << dialog;
	string userInput, table;
	cin >> userInput;
	getline(cin, table);
	return userInput + table;
}

string getDateAsString() {
	time_t rawTime = time(0);
	string outputString = ddNum(localtime(&rawTime)->tm_mday) + "-";
	switch (localtime(&rawTime)->tm_mon) {
		case 0:
			outputString += "Jan-";
			break;
		case 1:
			outputString += "Feb-";
			break;
		case 2:
			outputString += "Mar-";
			break;
		case 3:
			outputString += "Apr-";
			break;
		case 4:
			outputString += "May-";
			break;
		case 5:
			outputString += "Jun-";
			break;
		case 6:
			outputString += "Jul-";
			break;
		case 7:
			outputString += "Aug-";
			break;
		case 8:
			outputString += "Sept-";
			break;
		case 9:
			outputString += "Oct-";
			break;
		case 10:
			outputString += "Nov-";
			break;
		case 11:
			outputString += "Dec-";
			break;
	}
	outputString += to_string(localtime(&rawTime)->tm_year + 1900) + "-" + ddNum(localtime(&rawTime)->tm_hour) + ":" + ddNum(localtime(&rawTime)->tm_min) + ":" + ddNum(localtime(&rawTime)->tm_sec);
	return outputString;
}