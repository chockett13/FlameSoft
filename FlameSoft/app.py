from os import getcwd, path, mkdir
from pathlib import Path
from sys import argv, exit
from sys import path as path_

from PyQt5 import QtWidgets
from cv2 import VideoCapture

folder_path = str(Path(__file__).parent.absolute())
package_path = str(Path(folder_path).parent.absolute())
file_path = str(Path(__file__).absolute())

path_.append(file_path)
path_.append(folder_path)
path_.append(package_path)

import FlameSoft.fs as fs
from FlameSoft.gui import Ui_MainWindow
from FlameSoft.validator import IntVal, FloatVal

# call("pyuic5 gui.ui -o gui.py")


class Form(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.funcs = GuiFuncs()
        self.cls = None
        self.show()

    @property
    def set_default_values(self):
        self.ui.outpath.setText(getcwd())
        self.ui.videopath.setText(getcwd())
        # self.ui.outpath.setText('E:\Github\Flame-Speed-Tool')
        # self.ui.videopath.setText('E:/Github/Flame-Speed-Tool/bin/video1.wmv')
        self.ui.slices.setText('4')
        self.ui.filter.setText('25, 25, 25, 25')
        self.ui.thresh_data.setText('10, 10, 10, 10')
        self.ui.length.setText('10')
        self.ui.speed.setText('300')
        self.ui.ratio.setText('1.1')

    @property
    def link_buttons(self):
        self.ui.b_out.clicked.connect(lambda: self.funcs.open_file(caption='Browse the out path for Data',
                                                                   lineedit=self.ui.outpath,
                                                                   file=False))

        self.ui.b_video.clicked.connect(lambda: self.funcs.open_file(caption='Browse the path for Video',
                                                                     lineedit=self.ui.videopath,
                                                                     file=True))

        # Note here I am not using property designation cause i am not passing any arguments to function for connect
        self.ui.b_process.clicked.connect(self.process)

        self.ui.b_whiten.clicked.connect(self.whiten)

        self.ui.b_blacken.clicked.connect(self.blacken)

        self.ui.b_detect.clicked.connect(self.detect)

        self.ui.b_data.clicked.connect(self.df)

        self.ui.b_thresh.clicked.connect(self.view_image)

    @property
    def validation(self):
        self.ui.slices.setValidator(IntVal())
        self.ui.speed.setValidator(IntVal())
        self.ui.length.setValidator(FloatVal(int_lim=2, fl_lim=2))
        self.ui.ratio.setValidator(FloatVal())

    def error_check(self):

        e1 = self.funcs.check_filter(text=self.ui.filter.text(), length=int(self.ui.slices.text()),
                                     edit_field='filter data')
        e2 = self.funcs.check_filter(text=self.ui.thresh_data.text(), length=int(self.ui.slices.text()),
                                     edit_field='thresh data')
        e3 = self.video_check()

        if e1 and e2 and e3:
            return 1
        else:
            return 0

    def process(self):

        proceed = self.error_check()

        if proceed:

            try:
                # Make directory if not exists already
                self.make_directory()
                # Index 0 = Right for direction
                if self.ui.useprevious.currentIndex() == 0:
                    # Try to laod the poinst from the file
                    try:
                        points = self.funcs.read_txt(str(self.ui.outpath.text()) + r'\bin' + r'\points.txt')
                    # If no file exists raise an error
                    except Exception as _:
                        self.funcs.error('Please Crop again', 'No stored Data in Directory')
                        points = fs.Crop(path=str(self.ui.videopath.text()),
                                         out=str(self.ui.outpath.text())).crop_video()

                else:
                    points = fs.Crop(path=str(self.ui.videopath.text()), out=str(self.ui.outpath.text())).crop_video()

                self.create_object()
                self.cls.process(breaks=int(self.ui.slices.text()),
                                 filter_size=self.funcs.string_to_list(self.ui.filter.text()),
                                 thresh_val=self.funcs.string_to_list(self.ui.thresh_data.text()),
                                 crop_points=points,
                                 flow_right=int(self.ui.direction.currentIndex()),
                                 height=float(self.ui.ratio.text()),
                                 sub_frame=int(self.ui.subframe.currentIndex())
                                 )
            except Exception as _:
                self.funcs.error('Runtime Error', str(_))

    def whiten(self):
        if self.cls is None:
            self.funcs.error('Video Not Processed', 'Please Process the video frirst')
        self.cls.whiten_image()

    def blacken(self):
        if self.cls is None:
            self.funcs.error('Video Not Processed', 'Please Process the video frirst')
        self.cls.blacken_image()

    def detect(self):
        if self.cls is None:
            self.funcs.error('Video Not Processed', 'Please Process the video frirst')
        self.cls.get_data()

    def view_image(self):
        if self.cls is None:
            self.funcs.error('Video Not Processed', 'Please Process the video frirst')
        self.cls.view_pimage()

    def df(self):
        if self.cls is None:
            self.funcs.error('Video Not Processed', 'Please Process the video frirst')
        self.cls.Dataframe(length=float(self.ui.length.text()),
                           fps=int(self.ui.speed.text()))

    def create_object(self):

        if self.cls is None:
            self.cls = fs.Flame(path_=str(self.ui.videopath.text()), out=str(self.ui.outpath.text()))

    def make_directory(self):
        directory = str(self.ui.outpath.text())
        if path.exists(directory + '/bin'):
            pass
        else:
            mkdir(directory + '/bin')

    def video_check(self):

        cap = VideoCapture(self.ui.videopath.text())
        success, frame = cap.read()
        if not success:
            self.funcs.error('Video Input Error', 'Please check the video path')
            return 0
        return 1


class GuiFuncs(object):
    """Class linking functions to existing gui"""

    @staticmethod
    def open_file(caption, lineedit: QtWidgets.QLineEdit, display_container: QtWidgets.QTextEdit or None = None,
                  file: bool = True):
        """
        Method to open the dialog box to browse files or folder
        :param caption: Caption of the browsing window
        :param lineedit: Linedit in which the data will be filled
        :param display_container: if the text need to be displayed
        :param file: if true browse files else folders
        :return:
        """
        # Return the filename from browse input box and fill corressponding lineedit with filename
        if file:
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(caption=caption, directory=getcwd(),
                                                                initialFilter="Text Files (*.txt)")
        else:
            filename = QtWidgets.QFileDialog.getExistingDirectory(caption=caption, directory=getcwd())
        # Set the lineedit text to filename
        lineedit.setText(filename)

        if display_container:
            # Display the loaded data in the QtextEdit
            GuiFuncs.display_load_data(load_file=filename, display_container=display_container)

    @staticmethod
    def read_txt(path: str):
        """Function to read the points.txt and output list of points"""
        ans = []
        with open(path, 'r') as file:
            for line in file:
                ans.append(line.strip())
        ans = [int(i) for i in ans]

        x1, y1, x2, y2 = ans
        ans = [(x1, y1), (x2, y2)]
        return ans

    @staticmethod
    def display_load_data(load_file: str, display_container: QtWidgets.QTextEdit):
        """Method to display the text of the file in QTextEdit"""
        # Open the file
        with open(load_file, 'r+') as file:
            text = file.read()
            # Display the text in display container
            display_container.setText(text)

    @staticmethod
    def error(title, message):
        """Pop up a error box"""
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    @staticmethod
    def string_to_list(var: str):
        """Convert the excel input to list"""
        try:
            ans = [int(num) for num in var.split(',')]
        except Exception as _:
            ans = []
        return ans

    @staticmethod
    def check_filter(text: str, length: int, edit_field: str):
        ans = 1

        statement = f'Please edit the {edit_field} field'
        text_length = len(text.split(','))
        # Check the length of the split string
        if text_length < length:
            ans = 0
        # Get the text to be free of spaces
        text = [val.strip() for val in text.split(',')]

        for val in text:
            try:
                int(val)
            except Exception as _:
                print(_, val)
                ans = 0
            break

        if ans == 0:
            GuiFuncs.error('Input Error', statement)
        return ans


if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    window = Form()
    exit(app.exec_())
