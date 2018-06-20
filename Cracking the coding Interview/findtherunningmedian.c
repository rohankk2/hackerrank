
/* PROBLEM:

Check out the resources on the page's right side to learn more about heaps. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

The median of a dataset of integers is the midpoint value of the dataset for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your dataset of integers in non-decreasing order, then:

If your dataset contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted dataset ,  is the median.
If your dataset contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted dataset ,  is the median.
Given an input stream of  integers, you must perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the list's updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
Input Format

The first line contains a single integer, , denoting the number of integers in the data stream.
Each line  of the  subsequent lines contains an integer, , to be added to your list.

Constraints

Output Format

After each new integer is added to the list, print the list's updated median on a new line as a single double-precision number scaled to  decimal place (i.e.,  format).

*/

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <iomanip>

using namespace std;

class minHeap{
public:
    int parentindex(int n);
    int leftindex(int n);
    int rightindex(int n);
    void push(int n);
    bool haschild(int n);
    float pop();
    void heapifyup(int n);
    void heapifydown(int n);
    int higherpriority(int n);
    int size();
    float removemin();

private:
    vector<float> heap;
};
int minHeap::higherpriority(int n){
    int left= leftindex(n);
    int right=rightindex(n);
    return heap[left]<heap[right] ? left: right;
}
void minHeap::heapifyup(int n){
    if(n!=0){
    int parent=parentindex(n);
    if(heap[n]<heap[parent]){
        std::swap(heap[n],heap[parent]);
        heapifyup(parent);
    }
    }
}
void minHeap::heapifydown(int n){
    if(haschild(n)){
    int childindex= higherpriority(n);
        if(heap[childindex]<heap[n]){
            std::swap(heap[childindex],heap[n]);
            heapifydown(childindex);
        }
    }
}
int minHeap::parentindex(int n){
    return (n-1)/2;
}
int minHeap::leftindex(int n){
    return (2*n+1);
}
int minHeap::rightindex(int n){
    return (2*n+2);
}
void minHeap::push(int n){
    heap.push_back(n);
    heapifyup(heap.size()-1);
}
float minHeap::pop(){
    float temp=heap[0];
    heap[0]=heap[heap.size()-1];
    heap.pop_back();
    heapifydown(0);
    return temp;
}
float minHeap::removemin(){
  return heap[0];
}
bool minHeap::haschild(int n){
    if(leftindex(n)>=heap.size()){
        return false;
    }
    else{
        return true;
    }
}
int minHeap::size(){
    return heap.size();
}

int main(){
    int n;
    cin >> n;
    vector<float> a;
    int flag=0;
    std::cout << std::setprecision(1) << std::fixed;
    minHeap minheap;
    priority_queue<float> maxheap;
    int middleindex;
    float value;
    int balanced;
    for(int a_i = 0;a_i < n;a_i++){
       float curr;
       cin>>curr;
       a.push_back(curr);
        if(a_i==0){
            minheap.push(curr);
            cout<<curr<<"\n";
            continue;
        }



        if(curr>minheap.removemin()){
            minheap.push(curr);
            maxheap.push(minheap.pop());

        }
        else{
            maxheap.push(curr);
        }

      balanced= minheap.size()-maxheap.size();
        if(balanced<0){
            balanced=balanced*-1;
        }
       if(a_i%2==0){

           if(minheap.size()>maxheap.size()){
               value=minheap.removemin();
           }
           else{
               value=maxheap.top();
           }
       }
        else{
            if(balanced>1){
                if(minheap.size()>maxheap.size()){
                    maxheap.push(minheap.pop());
                }
                else{
                    minheap.push(maxheap.top());
                    maxheap.pop();
                }
            }
            value=(minheap.removemin()+maxheap.top())/2.0;
        }

        cout<<value<<"\n";
    }
    return 0;
}



