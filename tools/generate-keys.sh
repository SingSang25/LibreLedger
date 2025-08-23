#!/usr/bin/env sh

if [[ ! -f secrets/private.pem ]]; then
    echo "Generating public / private keys for JWT"
    mkdir -p secrets
    echo "" | openssl genpkey -out secrets/private.pem -pass stdin -algorithm rsa -pkeyopt rsa_keygen_bits:4096
    echo "" | openssl pkey -in secrets/private.pem -passin stdin -out secrets/public.pem -pubout
fi