# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re
Ap_Header = ApplicationType._VALUES_TO_NAMES[304]
Ap_Version = '8.11.0'
class Config(object):
    LINE_HOST_DOMAIN            = 'https://gd2.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gd2.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gd2.line.naver.jp/mh'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_TYPE    = Ap_Header
    APP_VER     = Ap_Version
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = '✯ͥ ͣ ͫ͢ŚhÀH•ŹÀ!η༼༻'
    SYSTEM_VER  = '8.22.17'
    IP_ADDR     = '1.1.1.1'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self):
        self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        self.USER_AGENT = 'Line/%s' % self.APP_VER
