"""This is a module for learning Python documentation

This module will do a few disconnected functions. It will calculate
a average GPA given a list of GPAs from each of the student's classes.
Then, it will also hold information for a hypothetical bank account
that raises ValueError exceptions if data does not match ranges & 
other criteria. We will also install pylint as well as build functionality
to work with python's help() function.

Extra Information:

  Author: Vincenzo Meschi
  Date: 2024-01-16
  Version: Python 3.10.12 (python3 --version)

  To convert the number 010001 from base 2 to base 10 using the int()
  function, you can use the base param to assign a base to convert
  from. This will return the base 10 version of the number.

  int("010001", base=2) == 17
"""


def class_average_gpa(classes: list) -> float:
    """Calculates a student's average GPA from each class GPA.

    Args:
        classes: A list of class GPA's to be averaged

    Returns:
        Average GPA for the student from the provided class
        informaiton in the classes param.

    Raises:
        ValueError: If the param's children are not type int or float.
    """
    total = 0
    for gpa in classes:
        if isinstance(gpa) == float or isinstance(gpa) == int:
            total += gpa
        else:
            raise ValueError(
                "List parameter contains a value that is not either type int or float."
            )

    return f"{total / len(classes):.2f}"


class BankAccount:
    """Hypothetical bank account.

    It will contain an account id, account name, as well as a dollar amount.
    This will be complete with getters and setters to modify said information.

    Attributes:
        id: 100,000 - 999,999 (inclusive).
        first_name: First name of the account. Cannot be blank or include numbers.
        last_name: Last name of the account. Cannot be blank or include numbers.
        amount: Dollar amount that is in the account.
    """

    def __init__(
        self, account_id: int, first_name: str, last_name: str, amount: float
    ) -> None:
        """Initializes the instance based on user information

        Args:
          account_id: Bank account ID associated with the account.
          first_name: First name of the user.
          last_name: Last name of the user.
          amount: Dollar amount that is to be stored in the account.

        """
        if account_id >= 100000 and account_id < 1000000:
            self.account_id = account_id
        else:
            raise ValueError(
                "Variable account_id is out of bounds. It must be between 100000 and 1000000 (exclusive)"
            )
        if isinstance(first_name) == str and len(first_name) != 0:
            self.first_name = first_name
        else:
            raise ValueError(
                "Variable first_name must be type str and cannot be empty."
            )
        if isinstance(last_name) == str and len(last_name) != 0:
            self.last_name = last_name
        else:
            raise ValueError("Variable last_name must be type str and cannot be empty.")
        if amount >= 999999999.99:
            self.amount = amount
        else:
            raise ValueError(
                "We are a small bank. Amount must be less than 999,999,999.99"
            )
