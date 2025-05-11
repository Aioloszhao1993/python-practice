def merge_batches(orders, MAX_WEIGHT=100, MAX_VOLUME=2):
    # 按user_id, address, timestamp排序
    orders.sort(key=lambda x: (x['user_id'], x['address'], x['timestamp']))
    print(f'orders"{orders}')

    merged_orders = []
    current_batch = None

    for order in orders:
        if current_batch is None or \
                order['user_id'] != current_batch['user_id'] or \
                order['address'] != current_batch['address'] or \
                order['timestamp'] - current_batch['end'] > 30 or \
                current_batch['total_weight'] + order['weight'] > MAX_WEIGHT or \
                current_batch['total_volume'] + order['volume'] > MAX_VOLUME:
            # 开始新批次
            if current_batch is not None:
                merged_orders.append(current_batch)
            current_batch = {
                'user_id': order['user_id'],
                'address': order['address'],
                'start': order['timestamp'],
                'end': order['timestamp'],
                'total_weight': order['weight'],
                'total_volume': order['volume'],
                'count': 1
            }
        else:
            # 更新当前批次
            current_batch['end'] = order['timestamp']
            current_batch['total_weight'] += order['weight']
            current_batch['total_volume'] += order['volume']
            current_batch['count'] += 1

    # 添加最后一个批次
    if current_batch is not None:
        merged_orders.append(current_batch)

    return merged_orders


# 测试样例
orders = [
    {"user_id": 1, "address": "A", "timestamp": 100, "weight": 30, "volume": 0.5},
    {"user_id": 1, "address": "A", "timestamp": 130, "weight": 40, "volume": 0.8},
    {"user_id": 1, "address": "A", "timestamp": 160, "weight": 50, "volume": 1.0},
    {"user_id": 1, "address": "A", "timestamp": 200, "weight": 20, "volume": 0.3},
    {"user_id": 2, "address": "B", "timestamp": 300, "weight": 90, "volume": 1.5},
]

print(merge_batches(orders))