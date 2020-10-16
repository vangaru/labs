#pragma once

#include "Figure.h"

class Container
{
private:
	Figure** container;
	int size;

public:
	Container(int size);

	void push_back(Figure* figure);
	void insert(Figure* figure, int index);
	void delete_back();
	void index_delete(int index);
	static Container* containerInitialize();
	void containerOutput();

	int getSize();

	Figure*& operator[](const int index);

	~Container();
};
