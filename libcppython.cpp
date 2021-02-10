#include "libcppython.h"

int Function(int num) {
    std::cout << "Num = " << num << std::endl;
    return 0;
}

extern "C" {
    int My_Function(int a){
        return Function(a);
    }
}
