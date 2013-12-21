# Jagare

> Seines Herzen an wie sind die Jageer!

`Jagare` 是一个 git service，依赖于 `ellen`。

## 搭建开发环境

- clone代码到本地
- `dae sync`
- `dae service serve`
- 测试服务 `dae service call Jagare get '.'`

*更多内容请参照 [DAE Service 文档](http://code.dapps.douban.com/dae/docs/userdoc/backend/service/)*

## 运行服务

`make service`

## 运行测试

`make test`

## 运行测试

当修改了 `thrift` 文件后，应当执行 `make service_gen` 来重新生成 `client/` 及 `service_gen/`。
