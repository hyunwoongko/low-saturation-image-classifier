# Author : Hyunwoong
# When : 2019-06-24
# Homepage : github.com/gusdnd852
import os

from src.gray_classifier import GrayscaleClassifier

classifier = GrayscaleClassifier()
good_root = 'good_example/'
wrong_root = 'wrong_example/'

good = os.listdir(good_root)
wrong = os.listdir(wrong_root)
length = len(good) + len(wrong)

accuracy = 0

for i in good:
    if not classifier.is_gray(good_root + i):
        accuracy += 1

for i in wrong:
    if classifier.is_gray(wrong_root + i):
        accuracy += 1

print('\ntest accuracy is ' + str(accuracy / length))
