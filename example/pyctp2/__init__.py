# -*- coding:utf-8 -*-

import os
import os.path

from .common.base import (check_path,
                          INFO_PATH,
                          CONFIG_PATH,
                          STATE_PATH,DATA_PATH,INTERNAL_PATH,
                          TEST_PATH,TEST_STATE_PATH,
                          SIMULATOR_PATH,SIMULATOR_DATA_PATH,SIMULATOR_STATE_PATH,
                          DYNAMIC_PATH,DYNAMIC_WAITING_PATH,DYNAMIC_FINISHED_PATH,
                         )

#在这里的话,必然是整个pyctp2被作为一个包导入时才执行, 保证当前根路径没有问题
check_path(INFO_PATH)
check_path(CONFIG_PATH)
check_path(STATE_PATH)
check_path(DATA_PATH)
check_path(INTERNAL_PATH)
check_path(TEST_PATH)
check_path(TEST_STATE_PATH)
check_path(SIMULATOR_PATH)
check_path(SIMULATOR_DATA_PATH)
check_path(SIMULATOR_STATE_PATH)
check_path(DYNAMIC_PATH)
check_path(DYNAMIC_WAITING_PATH)
check_path(DYNAMIC_FINISHED_PATH)
