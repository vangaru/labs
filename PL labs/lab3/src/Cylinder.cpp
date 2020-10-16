#define _USE_MATH_DEFINES
#include "Cylinder.h"

#include <iostream>
#include "math.h"

using namespace std;

Cylinder::Cylinder() {
	this->height = 1;
	this->baseRadius = 1;
	this->calculateArea();
	this->calculateVolume();
}

Cylinder::Cylinder(float height, float baseRadius) {
	this->height = height;
	this->baseRadius = baseRadius;
	this->calculateArea();
	this->calculateVolume();
}

void Cylinder::calculateArea() {
	this->area = 2 * M_PI * this->baseRadius * (this->baseRadius + this->height);
}

void Cylinder::calculateVolume() {
	this->volume = M_PI * pow(this->baseRadius, 2) * this->height;
}

float Cylinder::getArea() {
	return this->area;
}

float Cylinder::getVolume(){
	return this->volume;
}

float Cylinder::getBaseRadius() {
	return this->baseRadius;
}

float Cylinder::getHeight() {
	return this->height;
}

void Cylinder::infoOutput() {
	cout << endl << "ÂÛÑÎÒÀ ÖÈËÈÍÄÐÀ: " << this->getHeight() << endl;
	cout << "ÐÀÄÈÓÑ ÎÑÍÎÂÀÍÈß ÖÈËÈÍÄÐÀ: " << this->getBaseRadius() << endl;
	cout << "ÏËÎÙÀÄÜ ÖÈËÈÍÄÐÀ: " << this->getArea() << endl;
	cout << "ÎÁÚÅÌ ÖÈËÈÍÄÐÀ: " << this->getVolume() << endl;
}

Cylinder& Cylinder::operator = (const Cylinder& other) {
	this->height = other.height;
	this->baseRadius = other.baseRadius;
	this->area = other.area;
	this->volume = other.volume;

	return *this;
}

bool Cylinder::operator == (const Cylinder& other) {

	return (this->height == other.height && this->baseRadius == other.baseRadius);
}

bool Cylinder::operator != (const Cylinder& other) {

	return (this->height != other.height || this->baseRadius != other.baseRadius);
}