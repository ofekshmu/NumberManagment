#ifndef Nums_Managment_H
#define Nums_Managment_H

// Include any necessary standard or third-party libraries
#include <string>
#include <generator>
#include <bitset>

// Define the MyClass class
class NumsManagment
{
public:


    // Constructor
    NumsManagment(std::string& file_name);

    // Destructor
    ~NumsManagment();


    /**
     * @brief 
     * The function yields the next 
     * @return std::generator<bitset> 
     */
    std::generator<bitset> read_from_file_gen();


private:

    /**
     * @brief 
     * Checks if st - a line in the file, represents a positive integer
     * @param st 
     * @return True is @param st represent a positive integer and falase otherwise. 
     */
    bool is_line_pos_int(const std::string& st);

    std::string file_name;
};

#endif // Nums_Managment_H