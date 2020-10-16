#include "Check.h"
#include <iostream>

using namespace std;

void Check::setSum(float sum) {
	this->sum = sum;
}

float Check::getSum() {
	return this->sum;
}

void Check::infoOutput() {
	cout << endl << "ЧЕК:" << endl;

	cout << "Номер документа: " << this->getNumber() << endl;
	cout << "Дата: " << this->getDate() << endl;
	cout << "Сумма: " << this->getSum() << endl;
}

Check::Check(float date, int number, float sum) {
	this->date = date;
	this->number = number;
	this->sum = sum;
}

Check::Check() {
	this->date = 1;
	this->number = 1;
	this->sum = 9999;
}