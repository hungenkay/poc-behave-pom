## Installation

- Run `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` to install HomeBrew

- Run `brew install python3` to install Python3

- Run `pip3 install -r requirements` to install required dependencies

- Run `brew cask install chromedriver` to install chromedriver

## Execution
```bash

# Login Test With The Valid Account
python3 -m behave --tags=loginWithValidAccount --no-skipped

# Login Test With The Blocked Account
python3 -m behave --tags=loginWithLockedAccount --no-skipped

# Add To Cart Test In Case Of Using The Valid Account
python3 -m behave --tags=addToCardUsingValidAccount --no-skipped