// Address.h
#ifndef ADDRESS_H
#define ADDRESS_H

#include <string>

class Address
{
public:
    // Konstruktor
    Address(const std::string &street, const std::string &city, const std::string &postalCode, const std::string &country);

    // Getter
    std::string getStreet() const;
    std::string getCity() const;
    std::string getPostalCode() const;
    std::string getCountry() const;

    // Setters
    void setStreet(const std::string &street);
    void setCity(const std::string &city);
    void setPostalCode(const std::string &postalCode);
    void setCountry(const std::string &country);

private:
    std::string street;
    std::string city;
    std::string postalCode;
    std::string country;
};

#endif
