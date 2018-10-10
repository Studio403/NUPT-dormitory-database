# NUPT-dormitory-database

NUPT学生宿舍数据库导出工具

## How to use 使用方法

1. Get a copy of student dormitory excel. //获取学生宿舍管理积分表(每年宿舍评优的时候辅导员会公示)，不要修改他们，放在同一个文件夹下即可

2. Put `shit.py` in the same folder. //将py文件放到同一目录下

Eg.

```
\2017年-2018学年第二学期宿舍管理积分汇总表\

三牌楼.xls
兰苑.xlsx
李苑.xlsx
柳苑.xlsx
桂苑.xlsx
桃苑.xlsx
梅苑.xls
竹苑.xlsx
荷苑.xlsx
菊苑.xlsx
shit.py
```

3. `$ python shit.py` //运行程序

    注意：读取xls文件需要较长时间（取决于xls文件的大小），xls文件过大(>1MB)，建议先处理一下，减小体积

4. Now you get the formated txt data.  //现在你获得了格式规整的txt/csv数据：output.txt，将它用在你需要的地方

## Disclaimer 免责声明

作者对由于使用本程序引起的一切后果不承担任何责任

请勿将本程序用于非法用途