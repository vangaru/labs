#pragma once

#include "Check.h"

class Receipt : public Check
{
private:
	int size;

protected:
	char* bank;

public:
	void infoOutput() override;

	void setBank(char* bank);
	
	char* getBank();

	Receipt(float date, int number, float sum, char* bank);
	Receipt();

	~Receipt();
};