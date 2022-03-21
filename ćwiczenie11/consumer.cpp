#include <windows.h>
#include <iostream>
#include <fstream>
#include "config.h"

int main()
{
    std::ofstream outFile;
    outFile.open("out.txt");
    std::ifstream bufFile;
    bufFile.open("buf.txt");
    std::string line;
    if (bufFile.is_open())
    {
        while (!flag_is_buf_full)
        {
            //czekaj
        }

        while (getline(bufFile, line))
        {
            std::cout << "[KONSUMENT]: " << line << '\n';
            outFile << line << '\n';
            Sleep(1);
        }

        outFile.close();
        bufFile.close();
    }

    return 0;
}