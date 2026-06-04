#!/usr/bin/env python3
from wechat_api import WeChatAPI

class TodoManager:
    def __init__(self):
        self.wechat = WeChatAPI()
    
    def create_todos(self, task_info, is_urgent):
        priority = 'high' if is_urgent else 'normal'
        subject = task_info.get('subject', '未识别')
        deadline = task_info.get('deadline', '未识别')
        
        steps = [
            {
                'title': f'【{subject}】步骤1：仔细阅读要求',
                'content': f'科目: {subject}\n截止时间: {deadline}\n请仔细阅读老师布置的作业要求，确保理解所有细节。'
            },
            {
                'title': f'【{subject}】步骤2：制定计划',
                'content': f'科目: {subject}\n截止时间: {deadline}\n根据作业要求制定详细的完成计划，合理安排时间。'
            },
            {
                'title': f'【{subject}】步骤3：开始执行',
                'content': f'科目: {subject}\n截止时间: {deadline}\n按照计划开始执行作业任务，认真完成每一部分。'
            },
            {
                'title': f'【{subject}】步骤4：检查提交',
                'content': f'科目: {subject}\n截止时间: {deadline}\n完成后仔细检查作业内容，确保无误后按时提交。'
            }
        ]
        
        for i, step in enumerate(steps):
            self.wechat.create_todo(
                step['title'],
                step['content'],
                priority=priority
            )
