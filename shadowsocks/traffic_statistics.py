from multiprocessing import Manager
import logging

class TrafficCount:

    def __init__(self):
        manager = Manager()

        self.__traffic_statistics_dict = manager.dict()


    def add_bytes_by_ip(self, address, direct, bytes):
        """
        :param address: the string of the address (ip, port)
        :param direct:  upstream:    from client to server direction
                        downstream:  from server to client direction
        :param bytes: the data length the client request or get
        :return: None
        """
        ip = address[0]
        temp = self.__traffic_statistics_dict.get(ip, [0, 0])  #get ip ,ingnore port
        temp[direct] += bytes
        self.__traffic_statistics_dict[ip] = temp

        logging.info('Traffic_statistics_dict:%s' %
                     (str(self.__traffic_statistics_dict)))

    def get_all_count(self):


        return str(self.__traffic_statistics_dict)


    def get_special_count(self, ip):
        temp = self.__traffic_statistics_dict.get(ip, [0, 0])
        return str(temp)
