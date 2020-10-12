#include "Receipt.h"

Receipt NoName(Receipt& receipt);
void View(Receipt a);

int main() {
	setlocale(0, "");

	Receipt receipt;
	void(Receipt::*funcPointer)() = &Receipt::output; // Указатель на компоненту-функцию
	(receipt.*funcPointer)();

	Receipt a = receipt;
	a.output();
	Receipt b;
	View(b);
	Receipt c = NoName(receipt);
	c.output();

	Receipt receipt2(10, 10, 1.2);
	receipt2.output();
	
	Receipt receipt3(receipt2);
	receipt3.output();

	Receipt receipt_arr[2];     // Статический массив объектов
	receipt_arr[0].setNumber(1);
	receipt_arr[0].setDate(1);
	receipt_arr[0].setPrice(1);
	receipt_arr[0].output();

	receipt_arr[1].setNumber(2);
	receipt_arr[1].setDate(2);
	receipt_arr[1].setPrice(2);
	receipt_arr[1].output();

	Receipt* receipt_dyn_arr = new Receipt[2];   // Динамический массив объектов
	receipt_dyn_arr[0].setNumber(3);
	receipt_dyn_arr[0].setDate(3);
	receipt_dyn_arr[0].setPrice(3);
	receipt_dyn_arr[0].output();
	Receipt* pointer = &receipt_dyn_arr[0]; // Указатель на экземпляр класса
	pointer->output();

	receipt_dyn_arr[1].setNumber(4);
	receipt_dyn_arr[1].setDate(4);
	receipt_dyn_arr[1].setPrice(4);
	receipt_dyn_arr[1].output();

	delete[] receipt_dyn_arr;
}

Receipt NoName(Receipt& receipt) {
	Receipt temp(receipt);
	temp.setNumber(15);
	return temp;
}

void View(Receipt a) {
	a.output();
}