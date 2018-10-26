# AdalUsrPwd - Python method to get an access token by using AD username/password

There are many ways of acquiring a token. Here is the possible method (but not recommended) to acquire an access token by using an Active Directory username and password. This method will consist in:
- Getting user credentials and consent to permissions
- Requesting OAuth bearer token providing an access token
- Calling Azure application via API URL with the valid access token in Authorization header
- Verifying the call status
- Fetching API data from the application

## Installation

AD Authentication Library (ADAL) for Python must be installed to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.

```
pip install adal
```

## How to use it

As a prerequisite, retrieve information from Azure portal and fill it into `config.py` file with  to run `AdalUsrPwd.py` properly. For example, Go to 'Azure Active Directory >  Properties' to retrieve the Directory ID. It will be required to build the `authority_url` variable with the [Tenant ID](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#get-tenant-id).

You will be prompted to enter your username and password by using the [getpass module](https://docs.python.org/2/library/getpass.html), which are used to request a security token from Microsoft. Then, the OAuth protocol is needed to retrieve authentication tokens from Azure Active Directory, by using [ADAL AuthenticationContext class](https://docs.microsoft.com/en-us/python/api/adal/adal.authentication_context.authenticationcontext?view=azure-python).

It is now possible to call the Azure application via API URL for which we are authorized, by using the [requests module](http://docs.python-requests.org/en/master/) with the valid authentication token. The status of API call can be also verified, as well as the API data content.

# Useful reading

- Azure Active Directory Library for Python: [azure-activedirectory-library-for-python](https://github.com/AzureAD/azure-activedirectory-library-for-python)
- Azure Active Directory Library for Dotnet: [azure-activedirectory-library-for-dotnet](https://github.com/AzureAD/azure-activedirectory-library-for-dotnet)

## Licence

This software is distributed under the MIT License. Copyright 2016-2018 Fabrice Radja.


## Credits

1. The authentication method used here is based on the [answer](https://stackoverflow.com/questions/45244998/azure-ad-authentication-python-web-api) provided by Philippe Signoret to the Stack Overflow issue about 'Azure AD Authentication Python Web API'.

