#include <iostream>
#include <vector>
/*
Learning C++ before taking OOP software design lab. Understanding fundamentals; comments are notes.
*/

/*
Unlike Java, C++ can operate overload such as +, -, *
*/
namespace test{ // categorizes variables so that same name can be used as long as the name space is called
    int test(){
        return 43;
    }
    int b = 0;
    int a = 12;

}

int main()
{    int tests = 54;
    int *ip; // * designated a pointer or how to access the variable
    ip = &tests; // set the pointer to the prexisting memory address of the test
    *ip = 34; // can set the value of tests just through accessing the pointer
    std::cout <<  tests << '\n';
    int **ipp; //This is a pointer to a pointer as the pointer is also an object with a memory
    ipp = &ip; //setting the pointer to the prior pointer's address
    **ipp = 50; //just like changing the val of tests through pointer, it can be done thru two pointers as well
    std::cout <<  tests << '\n';
    std::cout << "Hello World"; //std is a name space, kind of like a way to designate between variables, methods, classes
    // :: is like a dot for java or python to designate whether it is is an object or a method
    // << is like the method
    for(int i = 0; i < 3; i++){
        if(i==2) continue; //skips over the action if conditional is true otherwise it doesn't skip over
        std::cout <<  i << '\n';
    } 
    using test :: b;
    std :: cout << b;
    std :: cout << test::test();
}

class Chemical
{
private:
    /* data */
    int uniqueid;


public:
    virtual int getAtomicNumber(); // =0 makes this a pure virtual function
    virtual int getAtomicMass();
    virtual int getNeutrons();
    virtual int getBonds();
}; //need semi colon after class declaration

class Hydrogen : public Chemical{
private: //categorized into private and public instead of just declaring it individually, can also have protected
    int uniqueid;
    int atomicnumber;
    int atomicmass;
    std::vector<Chemical> bonds;
public:
    Hydrogen(int a , int b){ //Defining constructor here, all constructors must be public. Can also be declared outside
        this->atomicnumber = a; //instead of using this.variable or function, C++ uses this->
        this -> atomicmass = b;
    }
    int getAtomic(){
        return this->atomicnumber;
    }
    int getAtomicMass(){
        return this->atomicmass;
    }
    void setAtomicMass(){
        this->atomicmass = 0;
    }
    void formBonds(Chemical c){
        int valencec = (c.getAtomicNumber()-2)%2;
        int valencecur = this->getAtomicNumber();
        if(valencecur+valencec==8){
            bonds.push_back(c);
            std::cout <<"This is a covalent bond";
        }
    }
};

class Storage{

public:
    std::vector <Chemical> bunker;    // pure virtual functions cannot be objects
    void add(Chemical c){
        bunker.push_back(c);
    }
};
