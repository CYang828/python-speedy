# C++ Run DNA K-mers

[中文](README-CHS.md)

## Depndencies
- g++ compiler

## Build
```bash
g++ -o k_mer k_mer.c
```

## Run
```bash
❯ ./k_mer
开始
生成 k-mers 的数量: 67108864    花费时间: 11.1504 秒
完成!
```

## Build with O3 optimization
```bash
❯ g++ -O3 -o k_mer_v2 k_mer.c
```

## Run
```bash
❯ ./k_mer_v2  
开始
生成 k-mers 的数量: 67108864    花费时间: 0.336514 秒
完成!
```
