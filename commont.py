#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


class Commont:
    def filepath(self,dir,filename):
        # print(os.path.dirname(__file__))
        return os.path.join(os.path.dirname(__file__),dir,filename)

# if __name__ == '__main__':
#     com=Commont()
#     print(com.filepath("webSelenium\pages","data.yaml"))