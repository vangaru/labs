#pragma once

#include "Document.h"

class Check : public Document
{
protected:
	float sum;

public:
	void infoOutput() override;
	void setSum(float sum);

	float getSum();

	Check(float date, int number, float sum);
	Check();

	virtual ~Check() {};
};

