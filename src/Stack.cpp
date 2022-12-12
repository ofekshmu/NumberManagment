#include "Stack.hpp"
#include <sstream>
#include <iostream>
#include <string>


template <typename T>
Stack<T>::Stack()
{
    // Do i need to initialize the vector?
}

template <typename T>
Stack<T>::~Stack()
{
    // No specific actions are required for the destructor?
    // is this even needed?
}

template <typename T>
void Stack<T>::push(T element)
{
    elements.push_back(element);
}

template <typename T>
T Stack<T>::pop()
{
    return elements.pop_back();
}

template <typename T>
T Stack<T>::top()
{
    return elements.back();
}

template <typename T>
int Stack<T>::len()
{
    // Might need to return a size_t here
    return elements.size();
}

template <typename T>
bool Stack<T>::is_empty()
{
    return elements.empty();
}

template <typename T>
std::string Stack<T>::repr()
{
    std::stringstream ss;
    ss << "Stack (size = " << elements.size() << "): [";
    for (auto it = elements.begin(); it != elements.end(); ++it) {
        ss << *it;
        if (std::next(it) != elements.end()) {
            ss << ", ";
        }
    }
    ss << "]";
    return ss.str();
}
