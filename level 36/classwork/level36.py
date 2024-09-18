def hero(bullets, dragons):
    return bullets >= dragons * 2

def grow(arr):
    product = 1
    for number in arr:
        product *= number
    return product



def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_positives = sum(1 for x in arr if x > 0)
    sum_negatives = sum(x for x in arr if x < 0)
    return [count_positives, sum_negatives]




def count_by(x, n):
    return [x * i for i in range(1, n + 1)]