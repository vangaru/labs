#include "Receipt.h"

void Receipt::setNumber(int setNumber) {
	number = setNumber;
}

void Receipt::setDate(int setDate) {
	date = setDate;
}

void Receipt::setPrice(float setPrice) {
	price = setPrice;
}

int Receipt::getNumber() { return number; }

int Receipt::getDate() { return date; }

float Receipt::getPrice() { return price; }

Receipt::Receipt() {
	setNumber(1);
	setDate(1);
	setPrice(9.9);
	cout << "\n����������� �� ��������� ��������� " << this << endl;
}

Receipt::Receipt(int number, int date, float price) {
	setNumber(number);
	setDate(date);
	setPrice(price);
	cout << "\n����������� ��������� " << this << endl;
}

Receipt::Receipt(const Receipt& receipt) {
	setNumber(receipt.number);
	setDate(receipt.date);
	setPrice(receipt.price);
	cout << "\n����������� ����������� ��������� " << this << endl;
}

void Receipt::output() {
	cout << "����� ���������: " << getNumber() << endl;
	cout << "����: " << getDate() << endl;
	cout << "����: " << getPrice() << endl;
}

