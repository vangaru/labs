#pragma once

#include "Document.h"

class Waybill : public Document
{
private:
	int organizationSize;
	int itemSize;
	int destinationSize;

protected:
	char* organization;
	char* item;
	char* destination;
	float itemPrice;

public:
	void infoOutput() override;

	void setOrganziation(char* organization);
	void setItem(char* item);
	void setDestination(char* destination);
	void setItemPrice(float itemPrice);

	char* getOrganization();
	char* getItem();
	char* getDestination();
	float getItemPrice();

	Waybill(float date, char* organization, char* item, char* destination, float itemPrice);
	Waybill();
	
	virtual ~Waybill();
};

