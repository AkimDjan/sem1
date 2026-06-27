#include <iostream>

int main() 
{   
    int n,k;
    std::cin >> n >> k;
    int dayofweek=n;
    for (int i=1; i<n; i++) {
        std::cout << "   "; 
    }

    for (int day=1; day<=k; ++day) {
        if (day <10) {
            std::cout << " ";
        }
        std::cout << day;
        if (dayofweek==7) {
            std::cout << "\n";
            dayofweek=1;
        } else {
            std::cout<< " ";
            dayofweek+=1;
        }

    }
    if (dayofweek!=1) {
        std::cout << "\n";
    }

    return 0;
}
