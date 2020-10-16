#include "Document.h"
#include "Check.h"
#include "Receipt.h"
#include "Waybill.h"

//#include <vector>
#include <iostream>

using namespace std;

int main() {
	setlocale(0, "");
	
	cout << "Введите название банка >>> ";

	char* bank = new char(20);
	cin.getline(bank, 20);

	cout << "Введите название организации >>> ";
	char* organization = new char(20);
	cin.getline(organization, 20);

	cout << "Введите имя адресата >>> ";
	char* destination = new char(20);
	cin.getline(destination, 20);

	cout << "Введите наименование товара >>> ";
	char* item = new char[20];
	cin.getline(item, 20);

	//Document* document = new Document(10, 12);
	Document* check = new Check(13, 14, 16);
	Document* receipt = new Receipt(20, 21, 22, bank);
	Document* waybill = new Waybill(1, organization, item, destination, 2);

	Document::listOutput();
	

	//vector<Document*> v;
	//v.push_back(document);
	//v.push_back(check);
	//v.push_back(waybill);
	//v.push_back(receipt);
	//v.at(2)->infoOutput();
}