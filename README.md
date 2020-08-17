# ansible-role-postfix [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-postfix.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-postfix)

CentOS 7 に postfix（送信専用）を導入する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

| 項目名           | デフォルト値     | 説明                       |
| ---------------- | ---------------- | -------------------------- |
| postfix_hostname | mail.example.com | FQDN                       |
| postfix_networks | 127.0.0.0/8      | 接続許可するネットワーク   |
