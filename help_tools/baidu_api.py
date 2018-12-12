# 此文件是百度AI的api封装
from django.conf import settings

from aip import AipOcr

class BDApi:
    '''
    百度Api接口类
    文档地址:https://ai.baidu.com/docs#/OCR-Python-SDK/top
    @author: wxk
    @time: 2018-12-12
    '''
    def __init__(self):
        self.client = AipOcr(settings.BAIDU_APP_ID, settings.BAIDU_APP_KEY, settings.BAIDU_SECRET_KEY)

    @staticmethod
    def read_pic_file(file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()

    def common_text_recognize(self, path, type=1, language_type='CHN_ENG'):
        '''
        通用文字识别
        :param path: 图片地址参数
        :param type: 1. 远程url 2.本地文件
        :param language_type: 选择语言 默认中英 其他有 ENG：英文, POR：葡萄牙语, FRE：法语, GER：德语, ITA：意大利语, SPA：西班牙语, RUS：俄语, JAP：日语, KOR：韩语
        :return:
        '''
        # 参数配置
        options = {}
        options['language_type'] = language_type
        options["detect_direction"] = "true"

        if type == 1:
            res = self.client.basicGeneralUrl(path, options)
        else:
            file = BDApi.read_pic_file(path)
            res = self.client.basicGeneral(file, options)

        return res

    def common_text_loc_recognize(self, path, type=1, language_type='CHN_ENG'):
        '''
        通用文字识别(含位置信息)
        :param path: 图片地址
        :param type: 1. 远程url 2.本地文件
        :param language_type: 选择语言 默认中英 其他有 ENG：英文, POR：葡萄牙语, FRE：法语, GER：德语, ITA：意大利语, SPA：西班牙语, RUS：俄语, JAP：日语, KOR：韩语
        :return:
        '''
        options = {}
        options["recognize_granularity"] = "big"
        options["language_type"] = language_type
        options["detect_direction"] = "true"

        if type == 1:
            res = self.client.generalUrl(path, options)
        else:
            file = BDApi.read_pic_file(path)
            res = self.client.general(file, options)

        return res

    def web_text_recognize(self, path, type=1):
        '''
        网络图片文字识别（背景复杂的，比如验证码）
        :param path: 图片地址
        :param type: 1. 远程url 2.本地文件
        :return:
        '''
        if type == 1:
            res = self.client.webImageUrl(path)
        else:
            file = BDApi.read_pic_file(path)
            res = self.client.webImage(file)

        return res

    def idCard_recognize(self, path, id_card_side):
        '''
        身份证识别
        :param path: 图片地址
        :param id_card_side: front - 身份证含照片的一面  back - 身份证带国徽的一面
        :return:
        '''
        options = {}
        options["detect_direction"] = "true"
        options["detect_risk"] = "false"
        image = BDApi.read_pic_file(path)
        res = self.client.idcard(image, id_card_side, options)

        return res

    def bankcard_recognize(self, path):
        '''
        银行卡识别
        :param path: 图片地址
        :return:
        '''
        image = BDApi.read_pic_file(path)
        res = self.client.backcard(image)
        return res

    def driving_recognize(self, path):
        '''
        驾驶证识别
        :param path: 图片地址
        :return:
        '''
        image = BDApi.read_pic_file(path)
        res = self.client.drivingLicense(image)
        return res

    def vehicleLicense_recognize(self, path):
        '''
        行驶证识别
        :param path: 图片地址
        :return:
        '''
        image = BDApi.read_pic_file(path)
        res = self.client.vehicleLicense(image)
        return res

    def plate_recognize(self, path, multi='false'):
        '''
        车牌识别
        :param path: 图片地址
        :param multi: 多车牌 'false' 否 'true' 是
        :return:
        '''
        options = {}
        options['multi_detect'] = multi

        image = BDApi.read_pic_file(path)
        res = self.client.licensePlate(image, options)
        return res

    def table_text_recognize(self, path):
        '''
        表格同步识别
        :param path:
        :return:
        '''
        image = BDApi.read_pic_file(path)
        res = self.client.tableRecognition(
            image,
            {
                'result_type': 'json',
            },
        )
        return res