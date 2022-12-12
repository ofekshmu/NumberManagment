#ifndef Stack_H
#define Stack_H

#include <vector>

template <typename T>
class Stack
{
    public:

        /**
         * @brief Construct a new Stack object
         * 
         */
        Stack();

        ~Stack();


        /**
         * @brief push an element to the top of the stack
         * 
         * @param element 
         */
        void push(T element);

        /**
         * @brief return the top element in the stack and removes it
         * 
         * @return returns the removes element 
         */
        T pop();

        /**
         * @brief Returns the top element in the stack
         * 
         * @return T 
         */
        T top();

        /**
         * @brief Returns the number of elements in the stack
         * 
         * @return int 
         */
        int len();

        /**
         * @brief Check if the stack is empty
         * 
         * @return true if the stack is empty
         * @return false if the stack has atleast one element
         */
        bool is_empty();

        /**
         * @brief ToString function
         * 
         * @return std::string which describes the stack
         */
        std::string repr();

    private:
    // A vector to store the elements of the stack
    std::vector<T> elements;
}

#endif // Stack_H