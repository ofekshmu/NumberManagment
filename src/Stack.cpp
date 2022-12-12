#include "Stack.h"
#include <sstream>
#include <iostream>

Stack::Stack<bitset>():
{
    this->
}

Stack::~Stack()
{
    // No specific actions are required for the destructor
}


void push(bitset element)
{
    elements.push_back(element);
}

bitset pop()
{
    return elements.pop_back();
}

bitset top()
{
    return elements.back();
}

int len()
{
    // Might need to return a size_t here
    return elements.size();
}

bool is_empty()
{
    return elements.empty();
}

std::string repr()
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
