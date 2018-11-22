import xml.dom.minidom
from src.util import config


class Data:
    """
    path:子目录 file:文件
    """
    def __init__(self, path, file_name):
        conf = config.Config()
        data_path = conf.get_config('system', 'data_path')
        # 获取文本
        xml_file = xml.dom.minidom.parse(data_path + path + file_name)
        self.xml_doc = xml_file.documentElement

    """
    #读取数据
    tag:标签
    """
    def get_data_by_tag(self, tag):
        mtag = self.xml_doc.getElementsByTagName(tag)
        return mtag[0].firstChild.data
