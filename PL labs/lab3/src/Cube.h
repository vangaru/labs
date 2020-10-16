#pragma once

#include "Figure.h"

class Cube : public Figure
{
private:
	float edgeLength;

protected:
	void calculateArea() override;
	void calculateVolume() override;

public:

	Cube(float edgeLength);
	Cube();

	float getArea() override;
	float getVolume() override;

	float getEdgeLength();

	void infoOutput() override;

	Cube& operator = (const Cube& other);
	
	bool operator == (const Cube& other);

	bool operator != (const Cube& other);

	~Cube() {};
};

