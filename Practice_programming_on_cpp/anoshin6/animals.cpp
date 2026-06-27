#include <iostream>

using ui = unsigned int;

class IAnimal {
	ui satiety = 0;

public:
    virtual ~IAnimal() {
        std::cout << "Destructor IANIMAL" << std::endl;
    }
	void Eat(ui food) {
		satiety += food;
	}

	virtual void Sound() const = 0;
};

class Cat : public IAnimal {
public:
    ~Cat(){
        //
    };
	void Sound() const override {
		std::cout << "Purr" << std::endl;
	}
};

class Pig : public IAnimal {
public:
    ~Pig(){
        //
    };
	void Sound() const override {
		std::cout << "Oink" << std::endl;
	}
};

int main() {

	IAnimal* animal = new Cat;
	animal->Sound();
	delete animal;			// Something wrong here

	animal = new Pig;
	animal->Sound();
	delete animal;			// And here

	return 0;
}