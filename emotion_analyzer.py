#!/usr/bin/env python3
import re

class EmotionAnalyzer:
    def __init__(self):
        self.urgent_keywords = [
            '必须', '立刻', '马上', '赶紧', '否则', '后果', '严肃',
            '严厉', '警告', '注意', '重要', '紧急', '抓紧', '尽快',
            ' deadline', 'asap', 'urgent', 'important'
        ]
        
        self.angry_keywords = [
            '怎么回事', '为什么', '搞什么', '不像话', '太过分', '生气',
            '愤怒', '恼火', '火大', '可恶', '讨厌', '混蛋', '废物',
            '没用', '差劲', '失望', '愤怒', 'angry', 'mad', 'furious'
        ]
        
        self.exclamation_pattern = re.compile(r'[!！]{2,}')
        self.question_pattern = re.compile(r'[?？]{2,}')
    
    def analyze(self, text):
        urgent_score = 0
        angry_score = 0
        
        text_lower = text.lower()
        
        for keyword in self.urgent_keywords:
            if keyword in text_lower:
                urgent_score += 1
        
        for keyword in self.angry_keywords:
            if keyword in text_lower:
                angry_score += 1
        
        if self.exclamation_pattern.search(text):
            urgent_score += 1
            angry_score += 1
        
        if self.question_pattern.search(text):
            angry_score += 1
        
        is_urgent = urgent_score > 0 or angry_score > 0
        
        emotion = 'normal'
        if angry_score > 0:
            emotion = 'angry'
        elif urgent_score > 0:
            emotion = 'serious'
        
        return {
            'urgent': is_urgent,
            'emotion': emotion,
            'urgent_score': urgent_score,
            'angry_score': angry_score
        }
