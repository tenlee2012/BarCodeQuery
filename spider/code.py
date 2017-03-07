#!/bin/env python3
# coding = utf-8

import requests
from bs4 import BeautifulSoup

__all__ = ['good_detail_code']


def get_all_attr():
    url = "http://www.anccnet.com/goods.aspx?base_id=F25F56A9F703ED747E0E167C9EA1642400D316346D26AB36181D28494198D235C33030361735CD16"
    req = requests.get(url)
    content = req.text
    table = BeautifulSoup(content, "html.parser")
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        name = cells[0].text
        spans = cells[1].findAll("span")

        if len(spans) == 1:
            print("'': ('" + spans[0]['id'] + "'),  # " + name)
        else:
            ids = "("
            for span in spans:
                ids += "'" + span['id'] + "',"

            print("'': " + ids.strip(',') + "),  #" + name)


good_detail_code = {
    'name': ('Att_Sys_zh-cn_141_G'),  # 产品名称
    'ename': ('Att_Sys_en-us_141_G'),  # 产品名称(英文)
    'unspsc': ('Att_Sys_zh-cn_22_G'),  # UNSPSC分类
    'brand': ('Att_Sys_zh-cn_304_G'),  # 品牌名称
    'type': ('Att_Sys_zh-cn_332_G'),  # 规格型号
    'width': ('Att_Sys_zh-cn_101_G', 'Att_Sys_zh-cn_104_G'),  # 宽度
    'height': ('Att_Sys_zh-cn_106_G', 'Att_Sys_zh-cn_326_G'),  # 高度
    'depth': ('Att_Sys_zh-cn_118_G', 'Att_Sys_zh-cn_331_G'),  # 深度
    'origincountry': ('Att_Sys_zh-cn_74_G'),  # 原产国
    'originplace': ('Att_Sys_zh-cn_405_G'),  # 产地
    'assemblycountry': ('Att_Sys_zh-cn_171_G'),  # 装配国
    'barcodetype': ('Att_Sys_zh-cn_167_G'),  # 条码类型
    # '': ('Att_Sys_zh-cn_122_G'),  # 产品所处层级
    'isbasicunit': ('Att_Sys_zh-cn_107_G'),  # 是否为基本单元
    # '': ('Att_Sys_zh-cn_204_G'),  # 是否为零售单元
    # '': ('Att_Sys_zh-cn_312_G'),  # 是否为变量单元
    # '': ('Att_Sys_zh-cn_151_G'),  # 二级品牌
    # '': ('Att_Sys_zh-cn_11_G'),  # 关键字
    # '': ('Att_Sys_zh-cn_90_L'),  # 供货开始日期
    # '': ('Att_Sys_zh-cn_51_G'),  # 包装材料
    'packagetype': ('Att_Sys_zh-cn_31_G'),  # 包装类型
    # '': ('Att_Sys_zh-cn_43_G', 'Att_Sys_zh-cn_66_G'),  # 包装材料计量
    # '': ('Att_Sys_zh-cn_271_G'),  # 包装上是否有可退还标记
    # '': ('Att_Sys_zh-cn_188_G'),  # 包装上是否标明成分
    # '': ('Att_Sys_zh-cn_32_G'),  # 包装上优惠信息
    # '': ('Att_Sys_zh-cn_44_G', 'Att_Sys_zh-cn_242_G'),  # 包装上零售价格
    # '': ('Att_Sys_zh-cn_68_G'),  # 包装上环保标记
    # '': ('Att_Sys_zh-cn_111_G'),  # 包装上循环再生标记
    # '': ('Att_Sys_zh-cn_308_G'),  # 包装上民族标记
    # '': ('Att_Sys_zh-cn_161_G'),  # 包装上不含成份的标记
    # '': ('Att_Sys_zh-cn_30_G'),  # 包装上的有效期类型
    # '': ('Att_Sys_zh-cn_230_G'),  # 包装上食物规定和过敏原
    # '': ('Att_Sys_zh-cn_53_L', 'Att_Sys_zh-cn_193_L'),  # 可退包装押金总计
    # '': ('Att_Sys_zh-cn_157_L'),  # 可退包装押金代码
    # '': ('Att_Sys_zh-cn_38_L'),  # 最早可退押金日期
    # '': ('Att_Sys_zh-cn_147_L'),  # 最迟可退押金日期
    # '': ('Att_Sys_zh-cn_322_G'),  # 包装使用条款
    # '': ('Att_Sys_zh-cn_286_G'),  # 钉子孔编号
    # '': ('Att_Sys_zh-cn_103_G', 'Att_Sys_zh-cn_328_G'),  # 钉子孔水平距离
    # '': ('Att_Sys_zh-cn_126_G', 'Att_Sys_zh-cn_245_G'),  # 钉子孔垂直距离
    # '': ('Att_Sys_zh-cn_33_G', 'Att_Sys_zh-cn_40_G'),  # 直径
    # '': ('Att_Sys_zh-cn_293_G', 'Att_Sys_zh-cn_310_G'),  # 固形物重量
    'grossweight': ('Att_Sys_zh-cn_54_G', 'Att_Sys_zh-cn_84_G'),  # 毛重
    'netcontent': ('Att_Sys_zh-cn_148_G', 'Att_Sys_zh-cn_162_G'),  # 净含量
    'netweight': ('Att_Sys_zh-cn_10_G', 'Att_Sys_zh-cn_189_G'),  # 净重
    # '': ('Att_Sys_zh-cn_314_G'),  # 包装上是否标明净含量
    # '': ('Att_Sys_zh-cn_254_G'),  # 计价类型
    # '': ('Att_Sys_zh-cn_173_G', 'Att_Sys_zh-cn_277_G'),  # 计价量
    # '': ('Att_Sys_zh-cn_274_G', 'Att_Sys_zh-cn_281_G'),  # 排面宽度
    # '': ('Att_Sys_zh-cn_89_G'),  # 普通成分
    # '': ('Att_Sys_zh-cn_79_G', 'Att_Sys_zh-cn_313_G'),  # 普通成分浓度
    # '': ('Att_Sys_zh-cn_15_G'),  # 成分浓度
    # '': ('Att_Sys_zh-cn_18_G'),  # 尺寸标准
    # '': ('Att_Sys_zh-cn_266_G'),  # 尺寸类型
    # '': ('Att_Sys_zh-cn_26_G', 'Att_Sys_zh-cn_105_G'),  # 尺寸
    # '': ('Att_Sys_zh-cn_198_G'),  # 尺寸描述
    # '': ('Att_Sys_zh-cn_298_G'),  # 尺寸分组
    # '': ('Att_Sys_zh-cn_81_L', 'Att_Sys_zh-cn_227_L'),  # 价单价格
    # '': ('Att_Sys_zh-cn_196_G', 'Att_Sys_zh-cn_225_G'),  # 建议零售价
    # '': ('Att_Sys_zh-cn_5_L', 'Att_Sys_zh-cn_75_L'),  # 订单至装运的时间
    # '': ('Att_Sys_zh-cn_209_L'),  # 订购基数
    # '': ('Att_Sys_zh-cn_140_L', 'Att_Sys_zh-cn_142_L'),  # 订购尺寸因素
    # '': ('Att_Sys_zh-cn_17_L'),  # 税种代码
    # '': ('Att_Sys_zh-cn_27_L'),  # 税种描述
    # '': ('Att_Sys_zh-cn_233_L'),  # 税率
    # '': ('Att_Sys_zh-cn_180_L'),  # 税额
    # '': ('Att_Sys_zh-cn_156_L'),  # 发票名称
    'description': ('Att_Sys_zh-cn_4_G'),  # 附加描述
    # '': ('Att_Sys_zh-cn_36_G'),  # 形态描述
    # '': ('Att_Sys_zh-cn_205_G'),  # 外部描述链接
    'catena': ('Att_Sys_zh-cn_181_G'),  # 产品系列
    # '': ('Att_Sys_zh-cn_6_G'),  # 产品组代码
    # '': ('Att_Sys_zh-cn_52_G'),  # 产品组描述
    # '': ('Att_Sys_zh-cn_48_G'),  # 变体
    # '': ('Att_Sys_zh-cn_97_L'),  # 供货截止日期
    # '': ('Att_Sys_zh-cn_45_G'),  # 取消日期
    # '': ('Att_Sys_zh-cn_325_G'),  # 停产日期
    # '': ('Att_Sys_zh-cn_117_L'),  # 上市时间
    # '': ('Att_Sys_zh-cn_135_L'),  # 最早订单日期
    # '': ('Att_Sys_zh-cn_163_L'),  # 最晚订单日期
    # '': ('Att_Sys_zh-cn_1_L'),  # 最早发货日期
    # '': ('Att_Sys_zh-cn_21_L'),  # 最晚发货日期
    # '': ('Att_Sys_zh-cn_128_G'),  # 目标消费者年龄
    # '': ('Att_Sys_zh-cn_210_G'),  # 目标消费者性别
    # '': ('Att_Sys_zh-cn_127_L'),  # 产品的特征或优势
    # '': ('Att_Sys_zh-cn_219_L'),  # 销售广告词
    # '': ('Att_Sys_zh-cn_239_L'),  # 特殊产品类别
    # '': ('Att_Sys_zh-cn_307_L'),  # 季节性供应年份
    # '': ('Att_Sys_zh-cn_185_L'),  # 可供应季节
    # '': ('Att_Sys_zh-cn_16_L'),  # 季节名称
    # '': ('Att_Sys_zh-cn_65_L'),  # 季节性供应结束日期
    # '': ('Att_Sys_zh-cn_83_L'),  # 同币种优惠券代码
    # '': ('Att_Sys_zh-cn_42_L'),  # 促销活动名称
    # '': ('Att_Sys_zh-cn_72_L'),  # 促销活动开始日期
    # '': ('Att_Sys_zh-cn_296_L'),  # 促销活动截止日期
    # '': ('Att_Sys_zh-cn_13_G'),  # 危险品规则
    # '': ('Att_Sys_zh-cn_164_G'),  # 危险品运输名称
    # '': ('Att_Sys_zh-cn_24_G'),  # 危险品专业名称
    # '': ('Att_Sys_zh-cn_265_G'),  # 危险品分类
    # '': ('Att_Sys_zh-cn_136_G'),  # 危险品极限数量
    # '': ('Att_Sys_zh-cn_94_G'),  # 危险品代码
    # '': ('Att_Sys_zh-cn_297_G'),  # 危险品包装级别
    # '': ('Att_Sys_zh-cn_23_G'),  # 联合国危险品代码
    # '': ('Att_Sys_zh-cn_252_G'),  # 原料成分代码
    # '': ('Att_Sys_zh-cn_217_G', 'Att_Sys_zh-cn_226_G'),  # 燃点
    # '': ('Att_Sys_zh-cn_246_G'),  # 内包装数
    # '': ('Att_Sys_zh-cn_208_G'),  # 内包装中次级贸易项目数量
    # '': ('Att_Sys_zh-cn_186_L'),  # 完整层数（Hi）
    # '': ('Att_Sys_zh-cn_85_L'),  # 完整层中的贸易项目数（Ti）
    # '': ('Att_Sys_zh-cn_145_L'),  # 每托盘层数
    # '': ('Att_Sys_zh-cn_264_L'),  # 每托盘层贸易项目数
    # '': ('Att_Sys_zh-cn_259_L'),  # 每托盘贸易项目数
    # '': ('Att_Sys_zh-cn_152_G'),  # 操作说明
    # '': ('Att_Sys_zh-cn_149_G'),  # 堆放层数
    # '': ('Att_Sys_zh-cn_37_G', 'Att_Sys_zh-cn_201_G'),  # 堆放最大承重
    # '': ('Att_Sys_zh-cn_159_L'),  # 到货后有效期
    # '': ('Att_Sys_zh-cn_261_G', 'Att_Sys_zh-cn_317_G'),  # 贮藏最高温度
    # '': ('Att_Sys_zh-cn_262_G', 'Att_Sys_zh-cn_270_G'),  # 贮藏最低温度
    # '': ('Att_Sys_zh-cn_100_G', 'Att_Sys_zh-cn_330_G'),  # 贮藏最大湿度
    # '': ('Att_Sys_zh-cn_28_G', 'Att_Sys_zh-cn_195_G'),  # 贮藏最小湿度
    # '': ('Att_Sys_zh-cn_29_G', 'Att_Sys_zh-cn_253_G'),  # 送达配送中心最高温度
    # '': ('Att_Sys_zh-cn_57_G', 'Att_Sys_zh-cn_324_G'),  # 送达配送中心最低温度
    # '': ('Att_Sys_zh-cn_158_G', 'Att_Sys_zh-cn_257_G'),  # 送达市场最高温度
    # '': ('Att_Sys_zh-cn_7_G', 'Att_Sys_zh-cn_251_G'),  # 送达市场最低温度
    # '': ('Att_Sys_zh-cn_222_G'),  # 托盘类型
    # '': ('Att_Sys_zh-cn_99_G'),  # 托盘使用条款
    'licensenum': ('Att_Sys_zh-cn_337_G'),  # 生产许可证号
    'healthpermitnum': ('Att_Sys_zh-cn_338_G'),  # 卫生许可证号
    # '': ('Att_Sys_zh-cn_430_G'),  # 产品执行标准代号
    # '': ('Att_Sys_zh-cn_339_G'),  # 绿色食品证号
    # '': ('Att_Sys_zh-cn_340_G'),  # 保健食品证号
    # '': ('Att_Sys_zh-cn_406_G'),  # 特殊用途化妆品批准文号
    # '': ('Att_Sys_zh-cn_408_G'),  # 进口化妆品批准文号
    # '': ('Att_Sys_zh-cn_355_L'),  # 其他包装类型
    # '': ('Att_Sys_zh-cn_356_L'),  # 保质期(天)
    # '': ('Att_Sys_zh-cn_362_L'),  # 其他包装材料
    # '': ('Att_Sys_zh-cn_409_G'),  # 产地代码
    # '': ('Att_Sys_zh-cn_410_G'),  # 税号
    # '': ('Att_Sys_zh-cn_411_G'),  # 配料
    # '': ('Att_Sys_zh-cn_412_G'),  # 年份
    # '': ('Att_Sys_zh-cn_413_G'),  # 质量等级
    # '': ('Att_Sys_zh-cn_414_G'),  # 啤酒类型
    # '': ('Att_Sys_zh-cn_415_G'),  # 糖度/总糖量
    # '': ('Att_Sys_zh-cn_416_G'),  # 进口酒类经营许可证代码
    # '': ('Att_Sys_zh-cn_417_G'),  # 产品标准名称
    # '': ('Att_Sys_zh-cn_418_G'),  # 香型
    # '': ('Att_Sys_zh-cn_419_G'),  # 产品添加剂
    # '': ('Att_Sys_zh-cn_420_G'),  # 加工方式
    # '': ('Att_Sys_zh-cn_421_G'),  # 地理标志产品名称
    # '': ('Att_Sys_zh-cn_422_G'),  # 是否具有防伪标识
    # '': ('Att_Sys_zh-cn_424_G'),  # QS分类
    # '': ('Att_Sys_zh-cn_425_G'),  # 产品执行标准名称
    # '': ('Att_Sys_zh-cn_426_G'),  # 防伪方式描述
    # '': ('Att_Sys_zh-cn_427_G'),  # 防伪类型
    # '': ('Att_Sys_zh-cn_428_G'),  # 防伪供应商名称
    # '': ('Att_Sys_zh-cn_429_G'),  # 防伪供应商组织机构代码
    # '': ('Att_Sys_zh-cn_434_G'),  # 3C认证
    # '': ('Att_Sys_zh-cn_435_G'),  # 适用车型
    # '': ('Att_Sys_zh-cn_436_G'),  # 使用寿命
    # '': ('Att_Sys_zh-cn_437_G'),  # 主要下游企业信息
    # '': ('Att_Sys_zh-cn_95_L'),  # 其它产品编码
    # '': ('Att_Sys_zh-cn_78_G'),  # 商标所有者GLN
    # '': ('Att_Sys_zh-cn_329_G'),  # 商标所有者名称
    # '': ('Att_Sys_zh-cn_155_L'),  # 附加分类类别代码
    # '': ('Att_Sys_zh-cn_194_L'),  # 附加分类类别描述
    # '': ('Att_Sys_zh-cn_327_L'),  # 附加分类机构名称
    # '': ('Att_Sys_zh-cn_386_L'),  # 必需配件
    # '': ('Att_Sys_zh-cn_382_L'),  # 直送消费者
    # '': ('Att_Sys_zh-cn_404_G'),  # eanucc代码
    # '': ('Att_Sys_zh-cn_403_G'),  # eanucc类型
    # '': ('Att_Sys_zh-cn_383_L'),  # 环保标识
    # '': ('Att_Sys_zh-cn_357_G'),  # 是否被辐照
    # '': ('Att_Sys_zh-cn_358_G'),  # 是否为转基因
    # '': ('Att_Sys_zh-cn_359_G'),  # 酒精含量
    # '': ('Att_Sys_zh-cn_360_G'),  # 干货脂肪含量
    # '': ('Att_Sys_zh-cn_361_G'),  # 原麦汁浓度
    # '': ('Att_Sys_zh-cn_402_G'),  # GPC分类类别代码
    # '': ('Att_Sys_zh-cn_384_L'),  # 危险品分类
    # '': ('Att_Sys_zh-cn_398_L'),  # 是否有防盗标签
    # '': ('Att_Sys_zh-cn_380_L'),  # 是否提供特殊订货
    # '': ('Att_Sys_zh-cn_374_L'),  # 是否可召回
    # '': ('Att_Sys_zh-cn_381_L'),  # 是否包含木料
    # '': ('Att_Sys_zh-cn_199_G'),  # 制造商GLN
    # '': ('Att_Sys_zh-cn_294_G'),  # 制造商名称
    # '': ('Att_Sys_zh-cn_134_G'),  # 原料成分
    # '': ('Att_Sys_zh-cn_215_G'),  # 原料百分比
    # '': ('Att_Sys_zh-cn_150_G'),  # 原料安全数据表号码
    # '': ('Att_Sys_zh-cn_377_G'),  # 型号
    # '': ('Att_Sys_zh-cn_363_L', 'Att_Sys_zh-cn_365_L'),  # 嵌套增量
    # '': ('Att_Sys_zh-cn_109_G'),  # 描述性尺寸
    # '': ('Att_Sys_zh-cn_432_G'),  # 防伪样张（图片）
    # '': ('Att_Sys_zh-cn_433_G'),  # 防伪生产许可证
    # '': ('Att_Sys_zh-cn_35_L'),  # 销售单位
    # '': ('Att_Sys_zh-cn_88_L'),  # 定购单位
    # '': ('Att_Sys_zh-cn_176_G'),  # 有机产品标准主管机构
    # '': ('Att_Sys_zh-cn_247_G'),  # 有机状况
    # '': ('Att_Sys_zh-cn_368_G', 'Att_Sys_zh-cn_370_G'),  # 净深
    # '': ('Att_Sys_zh-cn_371_G', 'Att_Sys_zh-cn_372_G'),  # 净高
    # '': ('Att_Sys_zh-cn_373_G', 'Att_Sys_zh-cn_399_G'),  # 净宽
    # '': ('Att_Sys_zh-cn_385_L'),  # Point Value
    # '': ('Att_Sys_zh-cn_376_L'),  # 退货政策
    # '': ('Att_Sys_zh-cn_63_L'),  # 季节性供应开始日期
    # '': ('Att_Sys_zh-cn_389_L'),  # 防盗标签提交日期
    # '': ('Att_Sys_zh-cn_144_G'),  # 防盗标签位置
    # '': ('Att_Sys_zh-cn_305_G'),  # 防盗标签类型
    # '': ('Att_Sys_zh-cn_387_L', 'Att_Sys_zh-cn_388_L'),  # 建议货架展示数
    # '': ('Att_Sys_zh-cn_390_L'),  # 特殊订货生产周期（天）
    # '': ('Att_Sys_zh-cn_392_L'),  # 特殊订货最小订购数
    # '': ('Att_Sys_zh-cn_393_L'),  # 特殊订购增量
    # '': ('Att_Sys_zh-cn_396_L'),  # 是否涉及美国专利
    # '': ('Att_Sys_zh-cn_223_L'),  # 目标市场细分代码
    # '': ('Att_Sys_zh-cn_123_L'),  # 税机构代码
    # '': ('Att_Sys_zh-cn_70_L'),  # 被替代产品的其它产品编码
    # '': ('Att_Sys_zh-cn_323_G'),  # 被替代产品的GTIN
    # '': ('Att_Sys_zh-cn_9_G'),  # 颜色代码表管理机构
    # '': ('Att_Sys_zh-cn_177_G'),  # 颜色代码
    # '': ('Att_Sys_zh-cn_182_G'),  # 颜色描述
    # '': ('Att_Sys_zh-cn_131_L'),  # 专卖权结束日期/时间
    # '': ('Att_Sys_zh-cn_203_L'),  # 最小订购数量开始日期
    # '': ('Att_Sys_zh-cn_207_L'),  # 最小订购数量截止日期
    # '': ('Att_Sys_zh-cn_237_L'),  # 最大订购数量开始日期
    # '': ('Att_Sys_zh-cn_279_L'),  # 最大订购数量截止日期
    # '': ('Att_Sys_zh-cn_132_G'),  # 简短描述
    # '': ('Att_Sys_zh-cn_61_G'),  # 外观描述
    # '': ('Att_Sys_zh-cn_55_L'),  # 进口分类代码
    # '': ('Att_Sys_zh-cn_212_L'),  # 进口分类类型
    # '': ('Att_Sys_zh-cn_3_G'),  # 未售出是否可退回
    # '': ('Att_Sys_zh-cn_47_G'),  # 是否标明可再生利用
    # '': ('Att_Sys_zh-cn_58_G'),  # 是否有批号
    # '': ('Att_Sys_zh-cn_102_G'),  # 织数
    # '': ('Att_Sys_zh-cn_224_G', 'Att_Sys_zh-cn_289_G'),  # 原料重量
    # '': ('Att_Sys_zh-cn_14_L'),  # 最少订购数量
    # '': ('Att_Sys_zh-cn_46_L', 'Att_Sys_zh-cn_218_L'),  # 订货至交货的时间
    # '': ('Att_Sys_zh-cn_124_L'),  # 可否再次订购
    # '': ('Att_Sys_zh-cn_153_L'),  # 最早送达日期/时间
    # '': ('Att_Sys_zh-cn_154_L'),  # 协议最大购买量
    # '': ('Att_Sys_zh-cn_229_L'),  # 是否依据数量定价
    # '': ('Att_Sys_zh-cn_256_L'),  # 最大订购数量
    # '': ('Att_Sys_zh-cn_272_L'),  # 协议最小购买量
    # '': ('Att_Sys_zh-cn_166_G'),  # 尺寸代码表机构
    # '': ('Att_Sys_zh-cn_316_G'),  # 尺寸代码
    # '': ('Att_Sys_zh-cn_56_G'),  # 变量贸易项目类型
    # '': ('Att_Sys_zh-cn_82_L'),  # 是否为物流单元
    # '': ('Att_Sys_zh-cn_87_L'),  # 是否为可订购单元
    # '': ('Att_Sys_zh-cn_139_L'),  # 是否为发票单元
    # '': ('Att_Sys_zh-cn_258_L'),  # 定价依据
    # '': ('Att_Sys_zh-cn_92_G'),  # 遵从法规
    # '': ('Att_Sys_zh-cn_394_L', 'Att_Sys_zh-cn_395_L'),  # 整车数量
    # '': ('Att_Sys_zh-cn_366_L', 'Att_Sys_zh-cn_367_L'),  # 组件数目
    # '': ('Att_Sys_zh-cn_379_G'),  # 保修说明的URL
    # '': ('Att_Sys_zh-cn_378_G'),  # 保修说明
    # '': ('Att_Sys_zh-cn_431_G'),  # 营业执照
}

if __name__ == '__main__':
    get_all_attr();
