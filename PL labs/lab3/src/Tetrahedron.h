#pragma once

#include "Figure.h"

class Tetrahedron : public Figure
{
private:
	float edgeLength;
	float height;

protected:
	void calculateArea() override;
	void calculateVolume() override;
	
	void calculateHeight();

public:
	Tetrahedron();
	Tetrahedron(float edgeLength);

	float getArea() override;
	float getVolume() override;

	float getEdgeLength();
	float getHeight();

	void infoOutput() override;

	Tetrahedron& operator = (const Tetrahedron& other);

	bool operator == (const Tetrahedron& other);
	
	bool operator != (const Tetrahedron& other);

	~Tetrahedron() {};
};

