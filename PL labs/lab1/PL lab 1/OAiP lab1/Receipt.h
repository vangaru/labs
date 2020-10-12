#pragma once

#include <iostream>

using namespace std;

class Receipt{

private:
	// Необходимые поля 
	int number;
	int date;
	float price;

public:
	// Методы set
	void setNumber(int setNumber);
	void setDate(int setDate);
	void setPrice(float setPrice);

	// Методы get
	int getNumber();
	int getDate();
	float getPrice();

	// Метод для вывода значений полей объекта
	void output();

	// Конструкторы
	Receipt();                                  // Конструктор по умолчанию
	Receipt(int number, int date, float price); // Конструктор с параметрами
	Receipt(const Receipt& receipt);            // Конструктор копирования

	~Receipt() { cout << "\nДеструктор отработал " << this << endl; } // Деструктор
};

