class UserCredentials:
    """
        Represents user login credentials for authentication purposes.

        Purpose:
            This class encapsulates user login information, providing a structured way to store and manage user credentials securely.
            It's designed to enhance code readability, maintainability, and security by centralizing the handling of sensitive login data.

        Attributes:
            username (str): The username used for authentication. It should be unique to each user.
            password (str): The corresponding password associated with the provided username.
                            It should be kept confidential and not exposed in code or logs.

        Note:
            - User credentials should be handled securely and not hardcoded in scripts for production applications.
                Consider using environment variables or secure vaults for storing sensitive information.
            - Always follow security best practices when dealing with user credentials to prevent unauthorized access and data breaches.
    """
    def __init__(self, username, password):
        """
            Initialize user credentials with the provided username and password.

            Args:
                username (str): The username used for authentication.
                password (str): The corresponding password associated with the username.
        """
        self.username = username
        self.password = password


# URLs
signInUrl = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon" \
            ".com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess" \
            "%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode" \
            "=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

mainPageUrl = "https://www.amazon.com/"

# User credentials
loginDataValid = UserCredentials("jorjmargaryann@mail.ru", "Jorj905888")
loginDataInvalidLogin = UserCredentials("invalidlogin@mail.ru", "Jorj905888")
loginDataInvalidPassword = UserCredentials("jorjmargaryann@mail.ru", "invalidpassword")

# Zip codes are used when changing the delivery location
zipCodeData = {"validZipCode": 90001, "otherValidZipCode": 90002, "invalidZipCode": 10000}

# Search keywords
searchTextData = {"validText": "Agv pista GP RR", "invalidText": "@#$%^&*"}


# This is used when a captcha check occurs when going to the login page.
captchaElementTextSignIn = "Enter the characters you see below"

# This is used when a captcha check occurs on the login page after entering a password.
captchaElementTextPassword = {"firstCaptchaText": "Solve this puzzle to protect your account",
                              "secondCaptchaText": "Enter the characters you see"}

# This is used to check when an incorrect username or password has been entered on the login page
invalidLoginAlert = {"title": "There was a problem", "text": "We cannot find an account with that email address"}
invalidPasswordAlert = {"title": "There was a problem", "text": "Your password is incorrect"}

profileNameUpdateTooltipText = "Name is updated"

addToCartConfirmationMessage = "Added to Cart"



