# voka-backend

#### 启动

python main.py

依赖 `flask pymysql sqlalchemy flask-sqlalchemy flasgger`

#### 介绍

main.py 是入口

采用分层架构：

* controller 层负责接受 restful API 接口
* service 层负责处理业务逻辑
* dao 层负责与数据库交互
* entity 定义数据实体，负责约束数据类型以及规范
* exceptions 定义错误处理函数以及自定义的错误类型
* test 负责做一些测试

#### 写法规范

尽量采用 typing 约束类型

```python
# 变量后加类型用 : ，返回值类型用 ->
def hasUser(self, user: UserEntity) -> bool:
```

当出现异常情况，如数据实体找不到相应 Key，应 raise 错误并添加参数。如果错误不足以描述错误状况，记得添加错误实体。

#### 类型规范

在 controller 层中返回的应该是 Response 类型

#### TODO

使用生产环境部署

## 开发流程

1. 确定前后端对接的接口、做 Swagger OpenAPI
2. 定数据，数据库的格式 SQL
3. 写分层和逻辑、测试


ER 图转换为数据库表：https://blog.csdn.net/maxle/article/details/122006729
解决冗余过多的问题 —— 数据库范式：https://blog.csdn.net/weixin_49343190/article/details/117435819
ORM 实体类读取，参考：http://www.pythondoc.com/flask-sqlalchemy/models.html
业务代码，等待用户访问接口
