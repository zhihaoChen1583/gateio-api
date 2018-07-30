#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
Provide user specific data and interact with gate.io
'''

from gateAPI import GateIO

## 填写 apiKey APISECRET
apiKey = 'A8528A0D-3DCF-40D2-8A31-7E242231834001'
secretKey = '2fea7692d8fa02e1ceb82cb1b0dddcf9b2889cf30fd92ee3662f6cd40047d53005'
## address
btcAddress = 'your btc address'


## Provide constants

API_QUERY_URL = 'data.gateio.io'
API_TRADE_URL = 'api.gateio.io'

## Create a gate class instance

gate_query = GateIO(API_QUERY_URL, apiKey, secretKey)
gate_trade = GateIO(API_TRADE_URL, apiKey, secretKey)


# Trading Pairs
# 获取所有支持的交易对
# print(gate_query.pairs())


## Below, use general methods that query the exchange

#  Market Info
# 返回所有系统支持的交易市场的参数信息，包括交易费，最小下单量，价格精度等
# print(gate_query.marketinfo())

# Market Details
# 返回所有系统支持的交易市场的详细行情和币种信息，包括币种名，市值，供应量，最新价格，涨跌趋势，价格曲线等。
# print(gate_query.marketlist())

# Tickers
# 返回系统支持的所有交易对的 最新，最高，最低 交易行情和交易量，每10秒钟更新
# print(gate_query.tickers())
# Depth
# 返回系统支持的所有交易对的市场深度（委托挂单），其中 asks 是委卖单, bids 是委买单
# print(gate_query.orderBooks())

# orders
# 获取我的当前挂单列表,可获取到订单编号
print(gate_query.openOrders())


## Below, use methods that make use of the users keys

# Ticker
# 查询指定交易对最新，最高，最低 交易行情和交易量，每10秒钟更新
#print(gate_query.ticker('btc_usdt'))

# Market depth of pair
# 返回指定交易对的市场深度（委托挂单），其中 asks 是委卖单, bids 是委买单
# print(gate_query.orderBook('btc_usdt'))

# Trade History
# 返回指定交易对最新80条历史成交记录
# print(gate_query.tradeHistory('btc_usdt'))

# Get account fund balances
# 获取帐号资金余额
# print(gate_trade.balances())

# get new address
# 获取充值地址
# print(gate_trade.depositAddres('btc'))

# get deposit withdrawal history
# 获取充值提现历史
# print(gate_trade.depositsWithdrawals('1469092370', '1569092370'))

# Place order buy
# 下订单买入
# print(gate_trade.buy('etc_btc', '0.001', '123'))

# Place order sell
# 下定单卖出
# print(gate_trade.sell('etc_btc', '0.001', '123'))

# Cancel order
# 取消指定订单
# print(gate_trade.cancelOrder('267040896', 'etc_btc'))

# Cancel all orders
# 取消所有订单
# print(gate_trade.cancelAllOrders('0', 'etc_btc'))

# Get order status
# 获取指定订单状态
# print(gate_trade.getOrder('267040896', 'eth_btc'))

# Get my last 24h trades
# 获取我的24小时内成交记录
# print(gate_trade.mytradeHistory('etc_btc', '267040896'))

# withdraw
# 提现
# print(gate_trade.withdraw('btc', '88', btcAddress))
