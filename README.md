# 智能管家狗蛋 (Godan Smart Assistant)

> 无法规划补作业时间及自控性不良学习者的智能时间规划助手

## 角色设定

- **名称**: 狗蛋
- **性格**: 极其冷静、敏锐且带有一点幽默感
- **定位**: 你的"自管时间"秘书，精准充当师生间的"情绪翻译官"

## 核心功能

| 技能 | 功能描述 |
|------|----------|
| message-fetcher | 实时抓取企微私信、群聊消息 |
| sentiment-analyzer | 分析文本情绪，判定语气等级 |
| priority-schedule | 基于四象限法则排序任务 |
| memory-manager | 管理长短期记忆（老师画像、历史效率）|

## 语气规则

- **正常状态**: 专业、简洁
- **老师情绪异常**: "亮红灯"警示

## 快速开始

1. 克隆仓库
2. 配置环境变量（参考 `.env.example`）
3. 安装依赖
4. 设置自动化任务（每10分钟一次）

## 项目结构

```
godan-smart-assistant/
├── .trae/skills/godan-assistant/SKILL.md  # 技能配置
├── wechat_api.py                 # 企业微信消息抓取
├── emotion_analyzer.py           # 情绪分析
├── task_processor.py             # 任务处理与排序
├── todo_manager.py               # 待办管理
└── .env.example                  # 环境变量模板
```

## 自动化任务配置

推荐cron表达式: `*/10 * * * *`（每10分钟执行）

## 许可证

MIT
