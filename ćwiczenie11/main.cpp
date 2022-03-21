/* autor: Klaudia Korczak
Problem Producent-Konsument dla Windows*/

#include <windows.h>
#include <iostream>
#include "config.h"

int main(int argc, char *argv[])
{

    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    STARTUPINFO si2;
    PROCESS_INFORMATION pi2;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    ZeroMemory(&si2, sizeof(si2));
    si2.cb = sizeof(si2);
    ZeroMemory(&pi2, sizeof(pi2));

    flag_is_buf_full = false;

    if (!CreateProcess(NULL, NULL, NULL, NULL,
                       FALSE, //uchwyty nie sa dziedziczone
                       0,     // priorytet
                       NULL,  // srodowisko
                       NULL, &si, &pi))
    {
        std::cout << "Create process failed: "
                  << GetLastError() << '\n';
    }
    WinExec("./producer.exe", SW_SHOWNORMAL);

    if (!CreateProcess(NULL, NULL, NULL, NULL,
                       FALSE, //uchwyty nie sa dziedziczone
                       0,     // priorytet
                       NULL,  // srodowisko
                       NULL, &si2, &pi2))
    {
        std::cout << "Create process failed: "
                  << GetLastError() << '\n';
    }
    WinExec("./consumer.exe", SW_SHOWNORMAL);

    WaitForSingleObject(pi.hProcess, INFINITE);
    WaitForSingleObject(pi2.hProcess, INFINITE);
    CloseHandle(pi.hProcess);
    CloseHandle(pi2.hProcess);

    return 0;
}
