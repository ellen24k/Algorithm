#include <set>

using namespace std;

int solution(int a, int b, int c) {
    set<int> s; 
    s.insert(a);
    s.insert(b);
    s.insert(c);
    
    switch(s.size()){
        case 1:
            return 27*(a*a*a)*(a*a)*a;
        case 2:
            return (a+b+c)*(a*a+b*b+c*c);
        default:
            return a+b+c;
    }
}