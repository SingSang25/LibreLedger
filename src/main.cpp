#include <iostream>
#include <string>
#include <vector>
#include "model/Address.cpp"
#include "model/Role.cpp"
#include "model/Groupe.cpp"
#include "model/User.cpp"

int main()
{
    Address address("Leimenmàtteliweg 16", "Frenkendorf", "4402", "Schweiz");
    Role role("Admin", "Administrator");
    Groupe groupe("Admins", "Administrator");

    int zahl;

    return 0;
}