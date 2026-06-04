#!/usr/bin/env python3
import os
import requests
from datetime import datetime

class WeChatAPI:
    def __init__(self):
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin"
        self.corpid = os.getenv("WECHAT_CORPID")
        self.corpsecret = os.getenv("WECHAT_CORPSECRET")
        self.agentid = os.getenv("WECHAT_AGENTID")
        self.access_token = None
        self.token_expires = 0
        self.simulated_messages = []
        
        if not self.corpid or not self.corpsecret:
            print("⚠️  警告: 未配置企业微信API凭证，将使用模拟模式")
            self._setup_simulated_data()
    
    def _setup_simulated_data(self):
        self.simulated_messages = [
            {
                'id': '1',
                'sender': '张老师',
                'content': '同学们，今天的数学作业必须在明天晚上8点前完成！否则后果自负！',
                'type': 'group',
                'time': datetime.now().isoformat()
            },
            {
                'id': '2',
                'sender': '李老师',
                'content': '大家好，今天的语文作业是写一篇作文，题目自拟，下周一交。',
                'type': 'group',
                'time': datetime.now().isoformat()
            }
        ]
    
    def get_access_token(self):
        if not self.corpid or not self.corpsecret:
            return 'simulated_token'
        
        if self.access_token and datetime.now().timestamp() < self.token_expires:
            return self.access_token
        
        url = f"{self.base_url}/gettoken"
        params = {
            'corpid': self.corpid,
            'corpsecret': self.corpsecret
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get('errcode') == 0:
            self.access_token = data['access_token']
            self.token_expires = datetime.now().timestamp() + data['expires_in'] - 300
            return self.access_token
        else:
            raise Exception(f"获取access_token失败: {data}")
    
    def get_latest_messages(self):
        if not self.corpid or not self.corpsecret:
            return self._get_simulated_messages()
        
        try:
            token = self.get_access_token()
            messages = []
            
            messages.extend(self._get_private_messages(token))
            messages.extend(self._get_group_messages(token))
            messages.extend(self._get_emails(token))
            
            return messages
        except Exception as e:
            print(f"获取消息失败: {e}")
            return self._get_simulated_messages()
    
    def _get_simulated_messages(self):
        if self.simulated_messages:
            msg = self.simulated_messages.pop(0)
            return [msg]
        return []
    
    def _get_private_messages(self, token):
        return []
    
    def _get_group_messages(self, token):
        return []
    
    def _get_emails(self, token):
        return []
    
    def send_message(self, to_user, content):
        if not self.corpid or not self.corpsecret:
            print(f"📤 [模拟] 发送消息给 {to_user}: {content}")
            return True
        
        try:
            token = self.get_access_token()
            url = f"{self.base_url}/message/send"
            
            data = {
                'touser': to_user,
                'msgtype': 'text',
                'agentid': int(self.agentid) if self.agentid else 1,
                'text': {
                    'content': content
                }
            }
            
            response = requests.post(url, params={'access_token': token}, json=data)
            result = response.json()
            
            if result.get('errcode') == 0:
                print(f"📤 消息发送成功: {to_user}")
                return True
            else:
                print(f"❌ 消息发送失败: {result}")
                return False
        except Exception as e:
            print(f"❌ 发送消息异常: {e}")
            return False
    
    def send_to_file_helper(self, content):
        return self.send_message('filehelper', content)
    
    def create_todo(self, title, content, priority='normal', due_date=None):
        if not self.corpid or not self.corpsecret:
            print(f"✅ [模拟] 创建待办: {title} (优先级: {priority})")
            return True
        
        try:
            token = self.get_access_token()
            url = f"{self.base_url}/oa/todo/add"
            
            data = {
                'userid': '@all',
                'todo': {
                    'title': title,
                    'content': content,
                    'priority': priority,
                }
            }
            
            if due_date:
                data['todo']['due_date'] = due_date
            
            response = requests.post(url, params={'access_token': token}, json=data)
            result = response.json()
            
            if result.get('errcode') == 0:
                print(f"✅ 待办创建成功: {title}")
                return True
            else:
                print(f"❌ 待办创建失败: {result}")
                return False
        except Exception as e:
            print(f"❌ 创建待办异常: {e}")
            return False
