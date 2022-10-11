#! /usr/bin/env bash
# linux 下启动测试
# Let the DB start 测试数据库链接
python ./app/db_pre_start/backend_pre_start.py

# Run migrations  迁移数据库表
alembic revision --autogenerate -m "first commit"

alembic upgrade head

# Create initial data in DB  初始化数据库内容
python ./app/initial_data.py
