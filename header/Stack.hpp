#ifndef Stack_H
#define Stack_H

#include <string>

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

    // add variables
}

#endif // Stack_H