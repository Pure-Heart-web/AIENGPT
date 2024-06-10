from py2neo import Graph
# -*- coding: utf-8 -*-
# @Time    : 2024/1/28 21:41
# @Author  : nongbin
# @FileName: graph_dao.py
# @Software: PyCharm
# @Affiliation: tfswufe.edu.cn
from datetime import datetime
from pathlib import Path
from typing import Sequence, Set

from py2neo import Graph, Node, NodeMatcher, RelationshipMatcher, ConnectionUnavailable

from config.config import Config
from logger import Logger


# 编写一个GraphDao类，该类包含与图相关的数据库操作方法。
class GraphDao(object):
    """
    连接图数据库neo4j
    """
    _logger: Logger = Logger(Path(__file__).name)

    def __init__(self):
        # 读取yaml配置
        self.__url = Config.get_instance().get_with_nested_params("database", "neo4j", "url")
        self.__username = Config.get_instance().get_with_nested_params("database", "neo4j", "username")
        self.__password = Config.get_instance().get_with_nested_params("database", "neo4j", "password")
        self.__connect_graph()
        self.__meta_node_id = 'meta-001'

        # 创建节点匹配器
        self.__node_matcher = NodeMatcher(self.__graph) if self.__graph else None

        # 创建关系匹配器
        self.__relationship_matcher = RelationshipMatcher(self.__graph) if  self.__graph else None

    def printConfig(self):
        print(self.__url)
        print(self.__username)
        print(self.__password)
        print(self.__meta_node_id)


    def __connect_graph(self):
        self.__graph = Graph("bolt://localhost:7689", auth=("neo4j", "12345678"))
        self.__graph.run("MATCH p=()-[r:`李白得罪高力士`]->() RETURN p LIMIT 25").data()
        print(self.__graph.run("MATCH p=()-[r:`李白得罪高力士`]->() RETURN p LIMIT 25").data())

#graph = Graph("bolt://localhost:7689", auth=("neo4j", "12345678"))
#print(graph.run("MATCH p=()-[r:`李白得罪高力士`]->() RETURN p LIMIT 25").data())

if __name__ == "__main__":
    graphDao = GraphDao()
    graphDao.printConfig()

