import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    """ n が素数かどうかを判定する関数 """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(limit):
    """ 指定した数の素数を生成するジェネレーター """
    n = 2
    primes = []
    while len(primes) < limit:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes

def plot_primes(primes):
    """ 素数を棒グラフで表示する関数 """
    # 百の区切りで分ける
    bins = [i for i in range(0, max(primes) + 100, 100)]
    counts, _ = np.histogram(primes, bins=bins)

    # 棒グラフを描画
    plt.bar([f"{b}-{b+99}" for b in bins[:-1]], counts, width=0.8, color='blue')
    plt.xlabel('素数の範囲')
    plt.ylabel('素数の個数')
    plt.title('素数の分布')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    limit = 100000  # 生成する素数の個数
    primes = generate_primes(limit)
    plot_primes(primes)
