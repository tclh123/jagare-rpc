# Jagare

> Seines Herzen an wie sind die Jageer!

`Jagare` 是一个 git service，依赖于 `ellen`。

## 搭建开发环境

- clone代码到本地
- `dae sync`
- `dae service serve`
- 测试服务 `dae service call Jagare get '.'`

*更多内容请参照[DAE Service 文档](http://code.dapps.douban.com/dae/docs/userdoc/backend/service/)*

## 运行测试

`dae venv py.test tests`

Or,

`dae test -p tests`
