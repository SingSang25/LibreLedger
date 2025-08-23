if (!(Test-Path secrets/private.pem)) {
    Write-Output "Generating public / private keys for JWT"
    mkdir -p secrets
    Write-Output "" | openssl genpkey -out secrets/private.pem -pass stdin -algorithm rsa -pkeyopt rsa_keygen_bits:4096
    Write-Output "" | openssl pkey -in secrets/private.pem -passin stdin -out secrets/public.pem -pubout
}