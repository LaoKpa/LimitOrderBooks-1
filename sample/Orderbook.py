"""
    Aim:
        Create an order book class to read in order book data

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

__author__ = "Awais Talib"
__project__ = "Limit Order Books"
__maintainer__ = "Awais Talib"
__license__ = ""
__version__ = "0.1"
__all__ = ['unpack_orders', 'unpack_data']

class OrderBook:

    def __init__(self, file):
        self.file = file
        self.time = {}
        self.buy_orders = {}
        self.sell_orders = {}
        self.order_id = {}
        self.hidden_orders = {}

    def __str__(self):
        time = "Current order book time: " + str(0.0)
        index = "Message Index: " + str(0.0)
        return time + "\n" + index

    def read(self, number_of_orders):
        order_file = pd.read_csv(self.file)
        order_file.as_matrix()  # convert into matrix
        rows, cols = np.size(order_file)
        output = np.matrix(number_of_orders. cols)

        for i in range(0,number_of_orders):
            for j in range(0, cols):
                output[i, j] = order_file[i, j]

        return output

    def summary(self):
        time = "Current order book time: " + str(0.0)
        index = "Message Index: " + str(0.0)
        bid_orders = "Bid Orders: " + str(0.0)
        ask_orders = "Ask Orders: " + str(0.0)
        total_orders = "Total Orders: " + str(0.0)
        return time + "\n" + index + "\n" + bid_orders + "\n" + ask_orders + "\n" + total_orders

    def display(self):
        pass

    def plot(self):
        pass