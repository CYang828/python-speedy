# Review the Code

Created by Caihao Cui on 2023-Mar-18.


## Environment
- VS Code 1.76.2
- Base Env Python 3.9.16
- g++ --version Apple clang version 14.0.0 (clang-1400.0.29.202) Target: x86_64-apple-darwin22.3.0
- Docker version 20.10.23, build 7155243

## Review Report

The Review report about the Image:

![Python-vs-C++](assets/3_extrapolated.png)


### Python Experimental Result

```bash

```bash
❯ python run_main_test.py
CompletedProcess(args=['docker', 'run', '-it', '--rm', '-v', '/Users/USERNAME/Documents/GitHub/python-speedy/single_test_run.py:/single_test_run.py', 'python:3.11-slim', 'python3', '/single_test_run.py', '--k_mer', '13'], returncode=0, stdout='开始\n生成 k-mers 的数量: 67108864\n完成!\n37.0328秒\n', stderr='')
新版本 Python 3.11 花费了 37.0328 秒.

CompletedProcess(args=['docker', 'run', '-it', '--rm', '-v', '/Users/USERNAME/Documents/GitHub/python-speedy/single_test_run.py:/single_test_run.py', 'python:3.5-slim', 'python3', '/single_test_run.py', '--k_mer', '13'], returncode=0, stdout='开始\n生成 k-mers 的数量: 67108864\n完成!\n50.1815秒\n', stderr='')
Python 3.5 花费了 50.1815 秒.(Python 3.11 比它快 35.5% )
CompletedProcess(args=['docker', 'run', '-it', '--rm', '-v', '/Users/USERNAME/Documents/GitHub/python-speedy/single_test_run.py:/single_test_run.py', 'python:3.6-slim', 'python3', '/single_test_run.py', '--k_mer', '13'], returncode=0, stdout='开始\n生成 k-mers 的数量: 67108864\n完成!\n51.0515秒\n', stderr="Unable to find image 'python:3.6-slim' locally\n3.6-slim: Pulling from library/python\na2abf6c4d29d: Pulling fs layer\n625294dad115: Pulling fs layer\n838e3a5a04bf: Pulling fs layer\ne93b4e59b689: Pulling fs layer\nc4401b8c7f9e: Pulling fs layer\ne93b4e59b689: Waiting\nc4401b8c7f9e: Waiting\n625294dad115: Verifying Checksum\n625294dad115: Download complete\ne93b4e59b689: Verifying Checksum\ne93b4e59b689: Download complete\nc4401b8c7f9e: Verifying Checksum\nc4401b8c7f9e: Download complete\n838e3a5a04bf: Verifying Checksum\n838e3a5a04bf: Download complete\na2abf6c4d29d: Verifying Checksum\na2abf6c4d29d: Download complete\na2abf6c4d29d: Pull complete\n625294dad115: Pull complete\n838e3a5a04bf: Pull complete\ne93b4e59b689: Pull complete\nc4401b8c7f9e: Pull complete\nDigest: sha256:2cfebc27956e6a55f78606864d91fe527696f9e32a724e6f9702b5f9602d0474\nStatus: Downloaded newer image for python:3.6-slim\n")
Python 3.6 花费了 51.0515 秒.(Python 3.11 比它快 37.9% )
CompletedProcess(args=['docker', 'run', '-it', '--rm', '-v', '/Users/USERNAME/Documents/GitHub/python-speedy/single_test_run.py:/single_test_run.py', 'python:3.7-slim', 'python3', '/single_test_run.py', '--k_mer', '13'], returncode=0, stdout='开始\n生成 k-mers 的数量: 67108864\n完成!\n50.4755秒\n', stderr="Unable to find image 'python:3.7-slim' locally\n3.7-slim: Pulling from library/python\n3f9582a2cbe7: Already exists\n57d9937f91c0: Already exists\na09893073b59: Pulling fs layer\n00457f9c7d41: Pulling fs layer\n0850f6fed9e0: Pulling fs layer\n00457f9c7d41: Verifying Checksum\n00457f9c7d41: Download complete\n0850f6fed9e0: Verifying Checksum\n0850f6fed9e0: Download complete\na09893073b59: Verifying Checksum\na09893073b59: Download complete\na09893073b59: Pull complete\n00457f9c7d41: Pull complete\n0850f6fed9e0: Pull complete\nDigest: sha256:27d5f7c2d108b7c97b9a7829f441c529df1e2866d94037e42f20e052a5ebdd01\nStatus: Downloaded newer image for python:3.7-slim\n")
Python 3.7 花费了 50.4755 秒.(Python 3.11 比它快 36.3% )
CompletedProcess(args=['docker', 'run', '-it', '--rm', '-v', '/Users/USERNAME/Documents/GitHub/python-speedy/single_test_run.py:/single_test_run.py', 'python:3.8-slim', 'python3', '/single_test_run.py', '--k_mer', '13'], returncode=0, stdout='开始\n生成 k-mers 的数量: 67108864\n完成!\n51.6387秒\n', stderr="Unable to find image 'python:3.8-slim' locally\n3.8-slim: Pulling from library/python\n3f9582a2cbe7: Already exists\n57d9937f91c0: Already exists\n828b5d400b8f: Pulling fs layer\ncef6a4978288: Pulling fs layer\n359e410c1c75: Pulling fs layer\ncef6a4978288: Verifying Checksum\ncef6a4978288: Download complete\n359e410c1c75: Verifying Checksum\n828b5d400b8f: Verifying Checksum\n828b5d400b8f: Download complete\n828b5d400b8f: Pull complete\ncef6a4978288: Pull complete\n359e410c1c75: Pull complete\nDigest: sha256:54ece633a6094e4eb66f6f8bcdff20355c4cc60c63a4f7787a2e3a46f2f39e6f\nStatus: Downloaded newer image for python:3.8-slim\n")
Python 3.8 花费了 51.6387 秒.(Python 3.11 比它快 39.4% )
CompletedProcess(args=['docker', 'run', '-it', '--rm', '-v', '/Users/USERNAME/Documents/GitHub/python-speedy/single_test_run.py:/single_test_run.py', 'python:3.9-slim', 'python3', '/single_test_run.py', '--k_mer', '13'], returncode=0, stdout='开始\n生成 k-mers 的数量: 67108864\n完成!\n47.9749秒\n', stderr="Unable to find image 'python:3.9-slim' locally\n3.9-slim: Pulling from library/python\n3f9582a2cbe7: Already exists\n57d9937f91c0: Already exists\n448f85f51b17: Pulling fs layer\n6c153184ac51: Pulling fs layer\n6c37649d3f36: Pulling fs layer\n6c153184ac51: Verifying Checksum\n6c153184ac51: Download complete\n6c37649d3f36: Verifying Checksum\n6c37649d3f36: Download complete\n448f85f51b17: Download complete\n448f85f51b17: Pull complete\n6c153184ac51: Pull complete\n6c37649d3f36: Pull complete\nDigest: sha256:50554b007c60cfc0406278504ce8ab3695b117739905e864ebc4a884931f5c98\nStatus: Downloaded newer image for python:3.9-slim\n")
Python 3.9 花费了 47.9749 秒.(Python 3.11 比它快 29.5% )
CompletedProcess(args=['docker', 'run', '-it', '--rm', '-v', '/Users/USERNAME/Documents/GitHub/python-speedy/single_test_run.py:/single_test_run.py', 'python:3.10-slim', 'python3', '/single_test_run.py', '--k_mer', '13'], returncode=0, stdout='开始\n生成 k-mers 的数量: 67108864\n完成!\n46.3438秒\n', stderr="Unable to find image 'python:3.10-slim' locally\n3.10-slim: Pulling from library/python\n3f9582a2cbe7: Already exists\n57d9937f91c0: Already exists\n0ccda17ba6b6: Pulling fs layer\ne8b7950ca30e: Pulling fs layer\n3e3b4b76fb2b: Pulling fs layer\ne8b7950ca30e: Verifying Checksum\ne8b7950ca30e: Download complete\n3e3b4b76fb2b: Verifying Checksum\n3e3b4b76fb2b: Download complete\n0ccda17ba6b6: Verifying Checksum\n0ccda17ba6b6: Download complete\n0ccda17ba6b6: Pull complete\ne8b7950ca30e: Pull complete\n3e3b4b76fb2b: Pull complete\nDigest: sha256:c35f011718a64510d819052464072753cfe20eb9b19e34c0f10cba04f6d1c9f8\nStatus: Downloaded newer image for python:3.10-slim\n")
Python 3.10 花费了 46.3438 秒.(Python 3.11 比它快 25.1% )
```

### C++ 

```bash
❯ g++ -o k_mer_review k_mer.c
```
```
❯ ./k_mer_review 
开始
生成 k-mers 的数量: 67108864    花费时间: 11.1364 秒
完成!
```

---

**END**