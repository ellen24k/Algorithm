#include <vector>
#include <set>

using namespace std;

int solution(vector<int> elements) {
    set<int> elem_set;
    int elem_size = elements.size();
    for (int idx = 0; idx < elem_size; idx++){
        int sum = 0;
        for (int len = 0; len < elem_size; len++){
            sum += elements[(idx + len) % elem_size];
            elem_set.insert(sum);
        }
    }
    return elem_set.size();
}