#pragma once

class Figure
{
protected:
	float area;
	float volume;

	virtual void calculateArea() = 0;
	virtual void calculateVolume() = 0;
	
public:

	virtual float getArea() = 0;
	virtual float getVolume() = 0;

	virtual void infoOutput() = 0;

	virtual ~Figure() {};
};

