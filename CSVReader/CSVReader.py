import csv
from FileUtilities.Absolute_Path import absolute_path
from pprint import pprint


def class_factory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CSVReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        with open(absolute_path(filepath)) as test_data:
            csv_data = csv.DictReader(test_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
                pprint(self.data)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(class_factory(class_name, row))
        return objects
