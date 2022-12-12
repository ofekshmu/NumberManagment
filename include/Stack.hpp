#ifndef Stack_H
#define Stack_H

#include <vector>

template <typename T>
class Stack
{
    public:

        Stack();

        ~Stack();

        void push(T element);

        T pop();

        T top();

        int len();

        bool is_empty();

        std::string repr();

    private:
    // A vector to store the elements of the stack
    std::vector<T> elements;
}

#endif // Stack_H