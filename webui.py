# -*- coding: utf-8 -*-
# @Time    : 2024/2/19 11:07
# @Author  : nongbin
# @FileName: webui.py
# @Software: PyCharm
# @Affiliation: tfswufe.edu.cn
import os

import gradio as gr

from config.config import Config
from env import get_app_root
from qa.interaction import chat_libai

__AVATAR = (os.path.join(get_app_root(), "resource/avatar/user.png"),
            os.path.join(get_app_root(), "resource/avatar/user.png"),)


def run_webui():
    chat_app = gr.ChatInterface(
        chat_libai,
        chatbot=gr.Chatbot(height=400, avatar_images=__AVATAR),
        textbox=gr.Textbox(placeholder="请输入你的问题", container=False, scale=7),
        title="KXO151编程与问题解决课程教学情景📒",
        description="此为KXO151期末复习的场景demo,用于测试和改良RAG知识图谱问答系统,参考自MeetLibai项目",
        theme="default",
        examples=["您好", "给出期末考试有关Java基础概念的例题，并进行解答","请给出Assessment 3的任务解读以及步骤化教学","帮我检查我的代码，并结合课程要求查看其问题"],# 此处需要额外定义问题类型
        cache_examples=False,
        retry_btn=None,
        submit_btn="发送",
        stop_btn="停止",
        undo_btn="删除当前",
        clear_btn="清除所有",
        concurrency_limit=4,
    )

    chat_app.launch(server_name="127.0.0.1"
                    , server_port=int(Config.get_instance().get_with_nested_params("server", "ui_port"))
                    , share=Config.get_instance().get_with_nested_params("server", "ui_share")
                    , max_threads=10)


if __name__ == "__main__":
    run_webui()
