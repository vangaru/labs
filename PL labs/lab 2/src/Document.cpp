#include "Document.h"
#include <iostream>

using namespace std;

Document::Node* Document::head = NULL;

void Document::setDate(float date) {
	this->date = date;
}

void Document::setNumber(int number) {
	this->number = number;
}

float Document::getDate() {
	return this->date;
}

int Document::getNumber() {
	return this->number;
}

void Document::infoOutput() {
	cout << endl << "ДОКУМЕНТ:" << endl;

	cout << "Номер документа: " << this->getNumber() << endl;
	cout << "Дата: " << this->getDate() << endl;
}

void Document::push() {
	Node* node = new Node;
	node->document = this;
	node->next = head;
	head = node;
}

void Document::listOutput() {
	Node* pointer = head;
	while (pointer != NULL) {
		pointer->document->infoOutput();
		pointer = pointer->next;
	}
}

Document::Document(float date, int number) {
	this->date = date;
	this->number = number;
	this->push();
}

Document::Document() {
	this->date = 1;
	this->number = 1;
	this->push();
}
          