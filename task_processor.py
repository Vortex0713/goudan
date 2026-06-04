#!/usr/bin/env python3
import re
from datetime import datetime, timedelta

class TaskProcessor:
    def __init__(self):
        self.subjects = {
            '数学': ['数学', 'math', '算数', '代数', '几何'],
            '语文': ['语文', 'chinese', '作文', '阅读', '古诗'],
            '英语': ['英语', 'english', '英文', '单词', '语法'],
            '物理': ['物理', 'physics', '力学', '电学'],
            '化学': ['化学', 'chemistry', '实验', '方程式'],
            '生物': ['生物', 'biology'],
            '历史': ['历史', 'history'],
            '地理': ['地理', 'geography'],
            '政治': ['政治', 'politics', '道法']
        }
        
        self.deadline_patterns = [
            r'(\d+)月(\d+)日',
            r'(\d+)-(\d+)-(\d+)',
            r'(\d+)/(\d+)/(\d+)',
            r'明天\s*(\d+)\s*点',
            r'明天\s*(\d+)\s*:\s*(\d+)',
            r'后天\s*(\d+)\s*点',
            r'后天\s*(\d+)\s*:\s*(\d+)',
            r'下周[一二三四五六日]',
            r'下周一',
            r'下周二',
            r'下周三',
            r'下周四',
            r'下周五',
            r'下周六',
            r'下周日',
            r'今晚\s*(\d+)\s*点',
            r'今晚\s*(\d+)\s*:\s*(\d+)',
            r'(\d+)\s*点前',
            r'(\d+)\s*:\s*(\d+)\s*前'
        ]
    
    def generate_reply(self, emotion_result):
        if emotion_result['urgent']:
            if emotion_result['emotion'] == 'angry':
                return "老师您好！我已收到消息，马上处理，非常抱歉让您生气了！"
            else:
                return "老师您好！我已收到消息，立即着手处理，保证按时完成！"
        else:
            return "老师您好！消息已收到，我会认真完成作业的，谢谢老师！"
    
    def extract_task(self, text):
        task_info = {
            'subject': self._extract_subject(text),
            'deadline': self._extract_deadline(text)
        }
        return task_info
    
    def _extract_subject(self, text):
        text_lower = text.lower()
        for subject, keywords in self.subjects.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    return subject
        return '未识别'
    
    def _extract_deadline(self, text):
        today = datetime.now()
        
        match = re.search(r'(\d+)月(\d+)日', text)
        if match:
            month = int(match.group(1))
            day = int(match.group(2))
            year = today.year
            if month < today.month:
                year += 1
            return f"{year}年{month}月{day}日"
        
        match = re.search(r'(\d+)-(\d+)-(\d+)', text)
        if match:
            return f"{match.group(1)}年{match.group(2)}月{match.group(3)}日"
        
        match = re.search(r'(\d+)/(\d+)/(\d+)', text)
        if match:
            return f"{match.group(1)}年{match.group(2)}月{match.group(3)}日"
        
        match = re.search(r'明天\s*(\d+)\s*点', text)
        if match:
            tomorrow = today + timedelta(days=1)
            return f"{tomorrow.strftime('%Y年%m月%d日')} {match.group(1)}点"
        
        match = re.search(r'明天\s*(\d+)\s*:\s*(\d+)', text)
        if match:
            tomorrow = today + timedelta(days=1)
            return f"{tomorrow.strftime('%Y年%m月%d日')} {match.group(1)}:{match.group(2)}"
        
        match = re.search(r'后天\s*(\d+)\s*点', text)
        if match:
            day_after = today + timedelta(days=2)
            return f"{day_after.strftime('%Y年%m月%d日')} {match.group(1)}点"
        
        if '下周一' in text:
            days_ahead = (7 - today.weekday()) % 7 + 1
            next_monday = today + timedelta(days=days_ahead)
            return f"{next_monday.strftime('%Y年%m月%d日')}"
        
        if '下周二' in text:
            days_ahead = (7 - today.weekday()) % 7 + 2
            next_tuesday = today + timedelta(days=days_ahead)
            return f"{next_tuesday.strftime('%Y年%m月%d日')}"
        
        if '今晚' in text:
            return f"{today.strftime('%Y年%m月%d日')} 今晚"
        
        return '未识别'
