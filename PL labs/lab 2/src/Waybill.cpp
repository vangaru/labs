#define _CRT_SECURE_NO_WARNINGS
#include "Waybill.h"
#include "string.h"
#include <iostream>

using namespace std;

void Waybill::setOrganziation(char* organization) {
	this->organizationSize = strlen(organization);
	this->organization = new char[this->organizationSize];
	strcpy(this->organization, organization);
}

void Waybill::setItem(char* item) {
	this->itemSize = strlen(item);
	this->item = new char[this->itemSize];
	strcpy(this->item, item);
}

void Waybill::setDestination(char* destination) {
	this->destinationSize = strlen(destination);
	this->destination = new char[this->destinationSize];
	strcpy(this->destination, destination);
}

void Waybill::setItemPrice(float itemPrice) {
	this->itemPrice = itemPrice;
}

char* Waybill::getOrganization() {
	return this->organization;
}

char* Waybill::getItem() {
	return this->item;
}

char* Waybill::getDestination() {
	return this->destination;
}

float Waybill::getItemPrice() {
	return this->itemPrice;
}

void Waybill::infoOutput() {
	cout << endl << "НАКЛАДНАЯ" << endl;
	cout << "Номер документа: " << this->getNumber() << endl;
	cout << "Дата: " << this->getDate() << endl;
	cout << "Организация: " << this->getOrganization() << endl;
	cout << "Товар: " << this->getItem() << endl;
	cout << "Адресат: " << this->getDestination() << endl;
	cout << "Наименование товара: " << this->getItemPrice() << endl;
}

Waybill::Waybill(float date, char* organization, char* item, char* destination, float itemPrice) {
	this->date = date;
	this->organizationSize = strlen(organization);
	this->organization = new char[this->organizationSize];
	strcpy(this->organization, organization);
	this->itemSize = strlen(item);
	this->item = new char[this->itemSize];
	strcpy(this->item, item);
	this->destinationSize = strlen(destination);
	this->destination = new char[this->destinationSize];
	strcpy(this->destination, destination);
	this->itemPrice = itemPrice;
}

Waybill::Waybill() {
	this->date = 10;
	this->organizationSize = strlen("N/A");
	this->organization = new char[this->organizationSize];
	strcpy(this->organization, "N/A");
	this->itemSize = strlen("N/A");
	this->item = new char[this->itemSize];
	strcpy(this->item, "N/A");
	this->destinationSize = strlen("N/A");
	this->destination = new char[this->destinationSize];
	strcpy(this->destination, "N/A");
	this->itemPrice = 9999;
}

Waybill::~Waybill() {
	delete[] organization;
	delete[] item;
	delete[] destination;
}