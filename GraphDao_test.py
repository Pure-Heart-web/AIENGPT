# -*- coding: utf-8 -*-
# @Time    : 2024/1/26 21:52
# @Author  : nongbin
# @FileName: zhipu_chat.py
# @Software: PyCharm
# @Affiliation: tfswufe.edu.cn
import httpx

from typing import List, Dict

from zhipuai.core._sse_client import StreamResponse

from lang_chain.client import get_ai_client

from qa.answer import get_answer

from lang_chain.zhipu_chat import chat_with_ai

__client = get_ai_client()



print(chat_with_ai("我想了解一下python的基础知识"))