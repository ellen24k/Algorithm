#include <set>

using namespace std;

int solution(int a, int b, int c) {
    set<int> s{a, b, c};
    
    switch(s.size()){
        case 1:
            return 27*(a*a*a)*(a*a)*a;
        case 2:
            return (a+b+c)*(a*a+b*b+c*c);
        default:
            return a+b+c;
    }
}