#ifndef GROUPE_H
#define GROUPE_H

#include <string>

class Groupe
{
public:
    // Konstruktor
    Groupe(std::string name, std::string description);

    // Getter
    std::string getName() const;
    std::string getDescription() const;

    // Setter
    void setName(const std::string &name);
    void setDescription(const std::string &description);

private:
    std::string name;
    std::string description;
};

#endif