#!/bin/sh

dnsmasq_file=dnsmasq.conf.add
nat_file=nat-start
ip_file=ips.list
ip_filter=ips.filter
site_fiile=sites.list.merge
dns_server=`cat dns.server`

cd /home/pi/asus
rm -f $dnsmasq_file
rm -f $nat_file
rm -f $ip_file
#rm -f dnsmasq.conf.tmp

#wget -q https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/dnsmasq.conf -O dnsmasq.conf.tmp

sites=`cat $site_fiile|grep -v "^$"|grep -v "#"`

for site in $sites
do
    echo "-->" $site
    echo "server=/$site/127.0.0.1#65053" >> $dnsmasq_file
    ips=`dig +short $site @$dns_server|grep -v -e "[a-zA-Z]"`
    for ip in $ips
    do
        echo "   " $ip
        echo $ip >> $ip_file
    done
done

cat nat-start.header > $nat_file

cat nat-start.basic >> $nat_file
if [ -e $ip_file ]
then
    ips_except=""
    if [ -e $ip_filter ]
    then
        ips_except=`cat $ip_filter`
    fi
    ips=`cat $ip_file|sort|uniq`
    for ip in $ips
    do
        ip_match=`echo $ips_except|grep $ip`
        if [ -z "$ip_match" ]
        then
            echo "iptables -t nat -A SHADOWSOCKS -p tcp -d $ip/32 -j REDIRECT --to-ports 1080" >> $nat_file
        fi
    done
fi

cat nat-start.tail >> $nat_file
