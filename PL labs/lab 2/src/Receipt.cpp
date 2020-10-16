#define _CRT_SECURE_NO_WARNINGS
#include "Receipt.h"
#include "string.h"
#include <iostream>

using namespace std;

void Receipt::setBank(char* bank) {
	this->size = strlen(bank);
	this->bank = new char[this->size];
	strcpy(this->bank, bank);
}

char* Receipt::getBank() {
	return this->bank;
}

void Receipt::infoOutput() {
	cout << endl << "КВИТАНЦИЯ:" << endl;
	cout << "Номер документа: " << this->getNumber() << endl; 
	cout << "Дата: " << this->getDate() << endl;
	cout << "Сумма: " << this->getSum() << endl;
	cout << "Банк: " << this->getBank() << endl;
}

Receipt::Receipt(float date, int number, float sum, char* bank){
	this->date = date;
	this->number = number;
	this->sum = sum;
	this->size = strlen(bank);
	this->bank = new char[this->size];
	strcpy(this->bank, bank);
}

Receipt::Receipt() {
	this->date = 1;
	this->number = 1;
	this->sum = 9999;
	this->size = strlen("N/A");
	this->bank = new char[this->size];
	strcpy(this->bank, "N/A");
}

Receipt::~Receipt() {
	delete[] bank;
}
