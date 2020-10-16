#pragma once

#include "Figure.h"

class Cylinder : public Figure
{
private:
	float height;
	float baseRadius;

protected:
	void calculateArea() override;
	void calculateVolume() override;

public:
	Cylinder();
	Cylinder(float height, float baseRadius);

	float getArea() override;
	float getVolume() override;

	float getHeight();
	float getBaseRadius();

	void infoOutput() override;

	Cylinder& operator = (const Cylinder& other);

	bool operator == (const Cylinder& other);

	bool operator != (const Cylinder& other);

	~Cylinder() {};
};

