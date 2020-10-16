#include "Container.h"
#include "Cube.h"
#include "Cylinder.h"
#include "Tetrahedron.h"

#include <iostream>
#include <cassert>

using namespace std;

Container::Container(int size) {
	this->size = size;
	this->container = new Figure* [this->size];
}

void Container::push_back(Figure* figure) {
	Figure** tempContainer = new Figure * [this->size + 1];

	for (int i = 0; i < this->size; i++) {
		tempContainer[i] = this->container[i];
	}

	tempContainer[this->size] = figure;

	this->size++;

	delete[] this->container;

	this->container = tempContainer;
	
}

void Container::insert(Figure* figure, int index) {
	Figure** tempContainer = new Figure * [this->size + 1];

	for (int i = 0; i < index; i++) {
		tempContainer[i] = this->container[i];
	}

	tempContainer[index] = figure;

	for (int i = index + 1; i < this->size + 1; i++) {
		tempContainer[i] = this->container[i - 1];
	}

	this->size++;

	delete[] this->container;

	this->container = tempContainer;

}

void Container::index_delete(int index) {
	Figure** tempContainer = new Figure * [this->size - 1];

	for (int i = 0; i < index; i++) {
		tempContainer[i] = this->container[i];
	}

	for (int i = index; i < this->size; i++) {
		tempContainer[i] = this->container[i + 1];
	}

	this->size--;

	delete[] this->container;

	this->container = tempContainer;

}

void Container::delete_back() {

	Figure** tempContainer = new Figure * [this->size - 1];

	for (int i = 0; i < this->size - 1; i++) {
		tempContainer[i] = this->container[i];
	}

	this->size--;

	delete[] this->container;

	this->container = tempContainer;
}

Container* Container::containerInitialize() {
	cout << "\nВведите размер контейнера >>> ";
	int size;
	cin >> size;
	Container* container = new Container(0);
	cout << "\nВВОДИТЕ ДАННЫЕ\n";

	for (int i = 0; i < size; i++) {
		cout << endl;
		cout << "1 - КУБ\n";
		cout << "2 - ЦИЛИНДР\n";
		cout << "3 - ТЕТРАЕДР\n";
		cout << "\nВыберите фигуру >>> ";

		int figure;
		cin >> figure;

		switch (figure) {
		case 1:
			cout << "\nВведите длину ребра куба >>> ";
			float edgeLength;
			cin >> edgeLength;

			container->push_back(new Cube(edgeLength));

			break;

		case 2:
			cout << "\nВведите высоту цилиндра >>> ";
			float height;
			cin >> height;

			cout << "\nВведите радиус основания цилиндра >>> ";
			float baseRadius;
			cin >> baseRadius;

			container->push_back(new Cylinder(height, baseRadius));

			break;

		case 3:
			cout << "\nВведите длину ребра тетраедра >>> ";
			float edgeLength2;
			cin >> edgeLength2;

			container->push_back(new Tetrahedron(edgeLength2));

			break;

		default:
			cout << "\n НЕВЕРНЫЙ ВВОД!!! \n";
			i--;

			break;
		}

	}

	return container;
}

void Container::containerOutput() {
	for (int i = 0; i < this->size; i++) {
		if (this->container[i] != nullptr) {
			this->container[i]->infoOutput();
		}
	}
}

int Container::getSize() {
	return this->size;
}

Figure*& Container::operator [] (const int index) {
	assert(index >= 0 && index < this->size);

	return this->container[index];
}

Container::~Container() {
	for (int i = 0; i < this->size; i++) {
		if (this->container[i] != nullptr) {
			delete this->container[i];
		}
	}

	delete[] this->container;
}