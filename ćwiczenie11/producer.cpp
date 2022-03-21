#include <windows.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include "config.h"

int main()
{

    std::ifstream inFile;
    inFile.open("in.txt");
    std::ofstream bufFile;
    bufFile.open("buf.txt");
    std::string buf;
    if (inFile.is_open())
    {
        while (std::getline(inFile, buf))
        {
            std::cout << "[PRODUCENT]: " << buf << '\n';
            bufFile << buf << '\n';
            flag_is_buf_full = true;
            Sleep(1);
        }
    }
    inFile.close();
    bufFile.close();

    return 0;
}