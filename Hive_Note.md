# HiveQL独有的特性
- 多表查询
- 支持create table as select
- 集成MapReduce脚本

# HQL常用语法
- 系统执行语句的顺序如下所示
    - select [ALL|DISTINCT] 字段列表(字段1 别名，...) 
    - from 表1别名，表2别名
    - where 条件
    - group by 分组字段 having(组约束条件)
    - order by 排序字段1 Asc|Desc，字段2 Asc|Desc，...
    - [cluster by 字段 |[distribute by 字段][sort by 字段]]
    - limit M,N 限制输出个数
  

- ALL DISTINCT 关键字
    - distinct 后面可跟单个或多个字段
    - distinct 可用于分组函数中

- HQL内置函数
    - 常用内置函数有max(),min(),avg(),sum(),count(),concat(),substr(),round()函数
    - concat()为字符串连接函数，例如，concat('hello,','world')='hello,world'
    - substr()为字符串截取函数，substr(STRINGs，开始下标，截取长度)
    - round()为格式化函数，round(num,n),num为数字，n为保留n位小数

- group by用法
    - 按其后的字段进行分组，配合having使用，having是对分组的约束条件
    - select avg(sal), deptno from emp group by deptno having avg(sal)>2000;

- join on用法
    - join on子句主要用于表的连接，用法是：JOIN表ON条件，即按某个条件关联两个表，与where子句作用相同
    - 使用JOIN ON子句：查询emp表薪水大于2500的员工姓名及所在部门名称。
        - select a.ename,b.dname from emp a join dept b on a.deptno=b.deptno where a.sal>2500

- HQL子查询
    - 查询中嵌套查询
    - 在emp表中，查询工资最高的员工姓名，薪水
        - select ename，sal from emp a,(select max(sal) max_sal from emp) b where a.sal = b.max_sal
    - 在emp表中，查询工资高于平均工资最高的员工姓名，薪水
    select ename, sal from emp a,(select avg(sal) avg_sal from emp) b where a.sal>b.avg_sal
    

    
