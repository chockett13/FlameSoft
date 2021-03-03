from PyQt5 import QtCore
from PyQt5 import QtGui


class IntVal(QtGui.QValidator):
    """Class to validate the integers"""

    def validate(self, text, pos):
        # Response for states
        # Important to have the validate function in the class with same var names
        # state = 0 invalid
        # state = 1 Intermediate
        # state = 2 Acceptable

        # QRegExpValidator object
        rval = QtGui.QRegExpValidator(QtCore.QRegExp("[1-9]\\d{0,1}"))

        # if there is text and the ourput is acceptable
        if bool(text) and rval.validate(text, 0)[0] == 2:
            state = QtGui.QIntValidator.Acceptable
        # If there is nothing the state is intermediate
        elif not bool(text.strip()):
            state = QtGui.QIntValidator.Intermediate
        # if there is something else the state is Invalid
        else:
            state = QtGui.QIntValidator.Invalid

        # retuurn the state, text and pos is following order
        return state, text, pos


class FloatVal(QtGui.QValidator):
    """Class to validate the strings with diffeent number of integers and floats"""

    def __init__(self, int_lim=1, fl_lim=2, decimal_only=False):
        """
        :param int_lim: Number of interger digits
        :param fl_lim: Number of float digits
        :param decimal_only: if True only decimals allowed starting with 0. for example 0.1
        """
        # Super command is important to make a class with init work
        # inherits the methods of parent class
        super().__init__()
        self.int_lim = int_lim
        self.fl_lim = fl_lim
        self.decimal_only = decimal_only

    def validate(self, text, pos):
        # Response for states
        # Important to have the validate function in the class with same var names
        # state = 0 invalid
        # state = 1 Intermediate
        # state = 2 Acceptable

        # Regex for integer or floats
        regx = fr"\d{{0,{self.int_lim}}}|\d{{0,{self.int_lim}}}\.\d{{0,{self.fl_lim}}}"

        # if decimal is true then use following regex
        if self.decimal_only:
            regx = fr"""[0]\.\d{{0,{self.fl_lim}}}|a[0]?\.\d{{0,{self.fl_lim}}}|\.\d{{0,{self.fl_lim}}}"""

        # regx2 = r"\d{0,8}|\d{0,8}\.\d{0,3}"
        # QRegExpValidator object
        rval = QtGui.QRegExpValidator(QtCore.QRegExp(regx))

        # if there is text and the ourput is acceptable
        if bool(text) and rval.validate(text, 0)[0] == 2:
            state = QtGui.QValidator.Acceptable
        # If there is nothing the state is intermediate
        elif not bool(text.strip()):
            state = QtGui.QValidator.Intermediate
            # if state if decimal then fdont allow to delete 0.
            if self.decimal_only:
                state = QtGui.QValidator.Invalid
        # if there is something else the state is Invalid
        else:
            state = QtGui.QValidator.Invalid

        # retuurn the state, text and pos is following order

        return (state, text, pos)


if __name__ == '__main__':
    x = FloatVal()
    x.validate('12', 0)
