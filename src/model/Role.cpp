#include "model/Role.h"

Role::Role(std::string name, std::string description)
    : name(name), description(description) {}

std::string Role::getName() const { return name; }
void Role::setName(const std::string &name) { this->name = name; }
std::string Role::getDescription() const { return description; }
void Role::setDescription(const std::string &description) { this->description = description; }