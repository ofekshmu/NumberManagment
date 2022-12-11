#include "NumsManagment.h"
#include <string>
#include <fstream>
#include <iostream>

// Constructor
NumsManagment::NumsManagment(std::string& file_name)
{
    // Open the file for reading
    std::ifstream file(file_name);

    // Check if the file was successfully opened
    if (!file.is_open())
    {
        throw std::ios_base::failure("Error: failed to open file for reading.");
        return 1;
    }
    // Initialize the file name to an empty string
    this->file_name = file_name;
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

std::generator<bitset> read_from_file_gen()
{
    // Read the file line by line
    std::string line;
    while (std::getline(this->file, line))
    {
        if (this->is_line_pos_int(line))
            yield binary_number(std::stoi(line))
    }
    throw std::ios_base::failure("Error: No more lines to read!");

}