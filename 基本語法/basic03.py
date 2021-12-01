"""
股票交易成本計算
小明在股價 10 元時買了 Hero 公司股票 10 張，於 11 元全數賣出，
請問小明賺了多少？
提示：
1張 = 1000股
交易成本(台股)
手續費：股票價值 * 1.425(‰) 買賣股票時都要扣除(不足 20 元者以 20 元計算。)
證交稅：股票價值 * 3(‰) 賣出股票時才扣除
"""
import math
amount = 1  # 張數
cost = 10 * amount * 1000  # 買進成本
fee_buy = cost * 0.001425  # 買進手續費
fee_buy = math.floor(fee_buy)  # 無條件捨去
fee_buy = 20 if fee_buy < 20 else fee_buy  # 判斷手續費是否小於20元
cost_add_fee_buy = cost + fee_buy  # 買進成本 + 買進手續費
print(cost, fee_buy, cost_add_fee_buy)
# ------------------------------------------------------
price = 11 * amount * 1000  # 賣出價值
fee_sell = math.floor(price * 0.001425)  # 賣出手續費(無條件捨去)
fee_sell = 20 if fee_sell < 20 else fee_sell  # 判斷手續費是否小於20元
tax_sell = math.ceil(price * 0.003)  # 賣出交易稅(無條件進入)
price_sub_fee_sell_tax_sell = price - \
                              fee_sell - tax_sell  # 賣出價值 - 賣出手續費與交易稅
print(price, fee_sell, tax_sell, price_sub_fee_sell_tax_sell)
# ------------------------------------------------------
profit = price_sub_fee_sell_tax_sell - cost_add_fee_buy
print('profit=', profit, ((price - cost) - profit))
