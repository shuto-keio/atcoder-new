# 各種ソフトのinstall
##  online-judge-toolsのinstall
```
pip install online-judge-tools
```

## Node.jsのinstall
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
nvm install node
```
[Node Version Manager](https://github.com/nvm-sh/nvm)

## atcoder-cliのinstall
```
npm install -g atcoder-cli
```

# 設定
## atcoder-cliのインストール確認
```
acc -h
```
## online-judge-toolsとの連携確認
```
acc check-oj
```
## Atcoderへのlogin
```
acc login
oj login https://atcoder.jp
```
## templateのcopy
```
cp ./config/python `acc config-dir`
```
## config設定
```
acc config default-task-choice all
acc config default-template python
acc config default-test-dirname-format test
```