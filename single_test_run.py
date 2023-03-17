import time
import argparse


def K_mer(k: int) -> None:
    def convert(c):
        if c == "A":
            return "C"
        if c == "C":
            return "G"
        if c == "G":
            return "T"
        if c == "T":
            return "A"

    print("开始")

    opt = "ACGT"
    s = ""
    s_last = ""
    len_str = k

    for i in range(len_str):
        s += opt[0]

    for i in range(len_str):
        s_last += opt[-1]

    pos = 0
    counter = 1
    while s != s_last:
        counter += 1
        # 你可以取消下一行的注释来查看所有的 k-mers.
        # print(s)
        change_next = True
        for i in range(len_str):
            if change_next:
                if s[i] == opt[-1]:
                    s = s[:i] + convert(s[i]) + s[i + 1 :]  # type: ignore
                    change_next = True
                else:
                    s = s[:i] + convert(s[i]) + s[i + 1 :]  # type: ignore
                    break

    # 你可以取消下一行的注释来查看所有的 k-mers.
    # print(s)
    print("生成 k-mers 的数量: {}".format(counter))
    print("完成!")


def run_test(k: int) -> None:
    start_time = time.time()
    K_mer(k)
    # print(f"{(time.time() - start_time):.4f}秒")
    print("{:.4f}秒".format(time.time() - start_time))


def main():
    """Main loop in arg parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-k",
        "--k_mer",
        help="DNA 序列长度",
        type=int,
        default=13,
    )

    args = parser.parse_args()

    run_test(args.k_mer)

if __name__ == "__main__":
    main()