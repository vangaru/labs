#pragma once

#include <iostream>

using namespace std;

class Receipt{

private:
	// ����������� ���� 
	int number;
	int date;
	float price;

public:
	// ������ set
	void setNumber(int setNumber);
	void setDate(int setDate);
	void setPrice(float setPrice);

	// ������ get
	int getNumber();
	int getDate();
	float getPrice();

	// ����� ��� ������ �������� ����� �������
	void output();

	// ������������
	Receipt();                                  // ����������� �� ���������
	Receipt(int number, int date, float price); // ����������� � �����������
	Receipt(const Receipt& receipt);            // ����������� �����������

	~Receipt() { cout << "\n���������� ��������� " << this << endl; } // ����������
};

