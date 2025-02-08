#include <Address.h>

Address::Address(const std::string &street, const std::string &city, const std::string &postalCode, const std::string &country)
    : street(street), city(city), postalCode(postalCode), country(country) {}

std::string Address::getStreet() const { return street; }
void Address::setStreet(const std::string &street) { this->street = street; }
std::string Address::getCity() const { return city; }
void Address::setCity(const std::string &city) { this->city = city; }
std::string Address::getPostalCode() const { return postalCode; }
void Address::setPostalCode(const std::string &postalCode) { this->postalCode = postalCode; }
std::string Address::getCountry() const { return country; }
void Address::setCountry(const std::string &country) { this->country = country; }