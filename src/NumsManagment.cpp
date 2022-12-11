#include "NumsManagment.h"
#include <string>

// Constructor
NumsManagment::NumsManagment(std::string& file_name)
{
    // Initialize the file name to an empty string
    file_name = file_name;
}

// Destructor
NumsManagment::~NumsManagment()
{
    // No specific actions are required for the destructor
}

bool is_line_pos_int(const std::string& st)
{
    if (str.empty())
        return false;

    if (str[0] == '-')
        return false;

    for (char c : str)
        if (!isdigit(c))
            return false;

    return true;
}
