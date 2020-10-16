#include "Tetrahedron.h"

#include <iostream>
#include <cmath>

using namespace std;

Tetrahedron::Tetrahedron() {
	this->edgeLength = 1;
	this->calculateHeight();
	this->calculateArea();
	this->calculateVolume();
}

Tetrahedron::Tetrahedron(float edgeLength) {
	this->edgeLength = edgeLength;
	this->calculateHeight();
	this->calculateArea();
	this->calculateVolume();
}

void Tetrahedron::calculateHeight() {
	this->height = (this->edgeLength * sqrt(6)) / 2;
}

void Tetrahedron::calculateArea() {
	this->area = pow(this->edgeLength, 2) * sqrt(6);
}

void Tetrahedron::calculateVolume() {
	this->volume = (pow(this->edgeLength, 3) * sqrt(2)) / 12;
}

float Tetrahedron::getEdgeLength() {
	return this->edgeLength;
}

float Tetrahedron::getHeight() {
	return this->height;
}

float Tetrahedron::getArea() {
	return this->area;
}

float Tetrahedron::getVolume() {
	return this->volume;
}

void Tetrahedron::infoOutput() {
	cout << endl << "ÄËÈÍÀ ÐÅÁÐÀ ÒÅÒÐÀÝÄÐÀ: " << this->getEdgeLength() << endl;
	cout << "ÂÛÑÎÒÀ ÒÅÒÐÀÝÄÐÀ: " << this->getHeight() << endl;
	cout << "ÏËÎÙÀÄÜ ÒÅÒÐÀÝÄÐÀ: " << this->getArea() << endl;
	cout << "ÎÁÚÅÌ ÒÅÒÐÀÝÄÐÀ: " << this->getVolume() << endl;
}

Tetrahedron& Tetrahedron::operator = (const Tetrahedron& other) {
	this->edgeLength = other.edgeLength;
	this->height = other.height;
	this->area = other.area;
	this->volume = other.volume;

	return *this;
}

bool Tetrahedron::operator == (const Tetrahedron& other) {
	return this->height == other.height;
}

bool Tetrahedron::operator != (const Tetrahedron& other) {
	return this->height != other.height;
}