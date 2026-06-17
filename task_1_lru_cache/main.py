import random
import time

#generate requests
def make_queries(n,q, hot_pool=30, p_hot=0.95, p_update=0.03):
    hot = [(random.randint(0, n //2), random.randint(n//2, n-1))
           for _ in range(hot_pool)]
    queries= []
    for _ in range(q):
        if random.random() < p_update:
            idx = random.randint(0, n-1)
            val = random.randint(1, 100)
            queries.append(("Update", idx, val))
        else:
            if random.random() < p_hot:
                left, right = random.choice(hot)
            else:
                left = random.randint(0, n-1)
                right = random.randint(left, n-1)
            queries.append(("Range", left, right))
    return queries

class LRUCache:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.cache = {}
    
    def get(self, key):
        if key in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache[key]= value
            return value
    def put(self, key, value):
        if key in self.cashe:
            self.cashe.pop(key)
        elif len(self.cashe) >= self.capacity:
            first_key = next(iter(self.cache))
            self.cashe.pop(first_key)
        self.cashe[key] = value
    def invalidate_index(self, index: int):
        keys_to_remove = [key for key in self.cache.keys() if key[0] <= index <= key[1]]
        for key in keys_to_remove:
            self.cache.pop(key) 

cache_sysrtem = LRUCache(capacity=1000)  

        

def range_sum_no_cache(array, left, right):
    return sum(array[left : right + 1])

def update_no_cache(array, index, value):
    array[index] = value

def range_sum_with_cache(array, left, right):
    key = (left, right)
    cached_result = cache_system.get(key)
    if cached_result != -1:
        return cached_result
    result = sum(array[left : right +1])
    cache_system.put(key, result)
    return result
def update_with_cache(array, index, value):
    array[index] = value
    cache_system.invalidate_index(index)
    
if __name__ == "__main__":
        test_queries = make_queries(100000, 50000)
        print("--- Перевірка запуску скрипта ---")
        test_array = [1, 2, 3, 4, 5]
        print(f"Масив: {test_array}")
        print(f"Сума елементів з 1 по 3 індекс: {range_sum_no_cache(test_array, 1, 3)}")
        update_no_cache(test_array, 2, 10)
        print(f"Масив після оновлення індексу 2 на значення 10: {test_array}")

