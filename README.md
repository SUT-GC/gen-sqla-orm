# Generate Sqlalchemy Orm
> 自动生成Sqlalchemy所需要的ORM文件

## 使用姿势

### 1 安装
`pip install gensqlalorm`

### 2 运行
在终端内输入 `gensqlalorm`

当你看到如下的文字，说明开始执行:     

```text
----------------------------------- welcome -----------------------------------

    step 1 select mode:
        c: config mode, read db config from config file. you can read README.md to get the file layout
        u: url mode, read db config from url. like localhost:3306/gc?username=root&password=gc
    step 2 input the path where to output:
        the path use to output orm class file, like '/gc/orm/'
```

### 3 根据引导进行输入
`gensqlalorm` 提供了两种配置文件装载模式:     
* 第一种`u` 模式: 该模式为连接串模式，需要输入数据库的连接串，连接串格式为`{地址}:{端口}/{数据库}?username={用户名}&password={密码}` 如 `localhost:3306/gc?username=root&password=gc`    
`u` 模式需要输入 `orm文件输出路径` ,该路径必须是当前用户可写的文件目录, 必须存在, 如 `/Users/gc`

* 第二种`c` 模式: 该模式为配置文件模式，需要输入数据库的配置文件地址，如`/Users/gc/db_config.yml` , `/Users/gc/gen_config.yml` 
配置文件为两个，都是yml文件格式，一个是数据库的链接文件，一个是配置输出目录的文件，配置文件格式如下:     

**数据库链接文件 db_config.yml**
```yaml
#项目1名:
#   dbName:数据库名
#   dbPort:数据库端口
#   hostName:数据库地址
#   passWord:密码
#   userName:用户名
#项目2名:
#   dbName:数据库名
#   dbPort:数据库端口
#   hostName:数据库地址
#   passWord:密码
#   userName:用户名

project1Name:
  dbName: gc1
  dbPort: '3306'
  hostName: localhost
  passWord: gc
  userName: root
project2Name:
  dbName: gc2
  dbPort: '3306'
  hostName: localhost
  passWord: gc
  userName: root
```
> 数据库配置文件可以配置多个链接地址，以项目名区分

**数据目录文件 gen_config.yml**    
```yaml
# genProjectNames
# - 项目1名
# - 项目2名
# rootPath: 生成文件放置的目录
genProjectNames:
- gc
rootPath: /Users/gc
```
> 数据目录文件里面填写要生成的项目名，`gensqlalorm`只会生成这里配置的项目，比如db_config.yml里面配置了项目1和项目2，gen_config.yml里面只配置了项目1，则只会生成项目1

### 4 开始生成

```text
set url/config success...
if you want gen orm class now ? ( y / n ) :
```
当你看到上面的话，说明你已经完成配置文件的设置，并且询问你是否要生成orm的class，输入`y`则开始进行生成     
最终会在您配置的生成目录下，生成一个`generate`的目录，里面有个`__init__.py` 和 `models`, `models`里面则是以你**项目名**改为驼峰只会的orm文件

### 说明

* `u`模式，项目名默认为数据库名

## RELEASE
[https://pypi.org/project/gensqlalorm/](https://pypi.org/project/gensqlalorm/)
