from numpy.random import random
from pyds import isEqual, loadJSON, makeKey, saveJSON
import os
import shutil
import unittest


class SaveJSONTestCase(unittest.TestCase):
    def setUp(self):
        obj = {}
        temp = obj

        for i in range(0, 100):
            key = makeKey(8)

            if random() < 0.25:
                temp[key] = {}
                temp = temp[key]
            else:
                temp[key] = random()

        self.filename = makeKey(8)

        try:
            os.mkdir("temp")
        except:
            pass

        saveJSON("temp/" + self.filename, obj)
        self.obj = obj

    def tearDown(self):
        shutil.rmtree("temp")

    def test(self):
        pred = loadJSON("temp/" + self.filename)
        self.assertTrue(isEqual(self.obj, pred), msg="Failed to load JSON!")

    def testCyclicObjects(self):
        # This makes sure that we can serialize objects with cyclic references.
        x = {}
        x["me"] = x
        failed = False

        try:
            saveJSON("temp/" + makeKey(8), x)

        except:
            failed = True

        self.assertFalse(failed, "Failed to serialize a cyclic object!")
