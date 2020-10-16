#include "Cube.h"

#include <iostream>
#include <cmath>

using namespace std;

Cube::Cube() {
	this->edgeLength = 1;
	this->calculateArea();
	this->calculateVolume();
}

Cube::Cube(float edgeLength) {
	this->edgeLength = edgeLength;
	this->calculateArea();
	this->calculateVolume();
}

void Cube::calculateArea() {
	this->area = 6 * pow(this->edgeLength, 2);
}

void Cube::calculateVolume() {
	this->volume = pow(this->edgeLength, 3);
}

float Cube::getArea() {
	return this->area;
}

float Cube::getVolume() {
	return this->volume;
}

float Cube::getEdgeLength() {
	return this->edgeLength;
}

void Cube::infoOutput() {
	cout << endl << "дкхмю пеапю йсаю: " << this->getEdgeLength() << endl;
	cout << "окныюдэ йсаю: " << this->getArea() << endl;
	cout << "назел йсаю: " << this->getVolume() << endl;
}

Cube& Cube::operator = (const Cube& other) {
	this->edgeLength = other.edgeLength;
	this->area = other.area;
	this->volume = other.volume;

	return *this;
}

bool Cube::operator == (const Cube& other) {
	
	return this->edgeLength == other.edgeLength;
}

bool Cube::operator != (const Cube& other) {

	return this->edgeLength != other.edgeLength;
}