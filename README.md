[中文版本](./README_CN.md)

**我的任务:**

1. 核心分析
   1. 模型构建 : (例子:随机数森林)
   2. 模型评估: (例子:性能指标报告)
   3. 特征重要性分析: (关键因素排序)
   4. 业务解读: (预测结果应用)
   5.
   6. 2.可视化优化
   7. 统计图表美化
   8. 模型结果可视化

step:

1. 首先我需要去理解数据集.
1. 清洗数据集, 标准化处理.
   1. 标准化列名 [全部小写, 下划线连接]
   2. 标准化每一个属性的字段值
      1. 对 `gender` 属性进行标准化处理[Male, Female, Other]
      2. 对 `no_employees` 属性进行标准化处理[1-5, 6-25, 26-100, 100-500, 500-1000, 1000+]
      3. 对`leave`属性进行标准化处理[Easy, Slightly easy,Slightly difficult, Difficult, Don't know]
      4. 对`coworkers`属性进行标准化处理[Yes, No, Some]
      5. 对 `supervisor` 属性进行标准化处理[Yes, No, Some]
      6.
   3. 处理缺失值
      1. 对 `self_employed` 属性的缺失值进行填充[No]
      2. 对 `treatment == 'Yes'` 属性 and `work_interfere` 属性为空的行, 填充众数
      3. 对 `work_interfere` 属性为空的行, `treatment  == 'No'`, 填充 `/` 表示不适用
      4. 对 `country` 不是 `United States` 且 `state` 填充 ·`/`, 填充 `/` 表示不适用
      5. 对 `state` 属性的缺失值进行填充[`/`]
      6. 对 `comments` 属性 drop 整列
