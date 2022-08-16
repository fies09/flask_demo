#!/bin/bash
#通过工具创建的数据表生成models脚本文件
sqlacodegen --outfile=models.py mysql://admin:admin123@192.168.1.241:3306/yuntong?charset=utf8mb4