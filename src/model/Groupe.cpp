#include "model/Groupe.h"

Groupe::Groupe(std::string name, std::string description)
    : name(name), description(description) {}

std::string Groupe::getName() const { return name; }
void Groupe::setName(const std::string &name) { this->name = name; }
std::string Groupe::getDescription() const { return description; }
void Groupe::setDescription(const std::string &description) { this->description = description; }