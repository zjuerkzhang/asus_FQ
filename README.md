# Asus-Merlin路由器科学上网设置生成工具

## Introduction
- 本工具主要用于基于梅林固件的华硕路由器的科学上网配置，主要是生成dnsmasq的DNS配置和shadowsocks的iptables配置。dnsmasq的DNS配置用于防止DNS污染，shadowsocks的iptables配置用于根据目标IP地址，分流国内和国外的路由。
- 配置中需要的域名信息来自于[googlehosts/hosts](https://github.com/googlehosts/hosts)，在此感谢。

## Pre-condition
#### 路由器端
- dnscrypt-proxy: 为dnsmasq提供无污染的DNS查询。其对应服务器可以使用现有的，也可以在VPS上配置dnscrypt-wrapper来提供服务。
- ss-redir: 为路由器下属的局域网提供透明代理，由iptables的规则表决定哪些IP地址使用该透明代理。
- dig: 虽然本工具内的nat-start.basic已经内置了google, facebook等主要网站的iptables配置列表，但是对于一些域名地址，仍然需要通过dig来获取IP地址，然后生成iptables配置。

## Configuration
- dns.server: 用于设置dig查询域名的DNS服务器。
- ips.filter: 用于设置不需要走透明代理的IP地址。

## Usage
`./net_utils.sh`

