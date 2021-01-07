# -*- coding: utf-8 -*-

# @{PROJECT_NAME}
# @Author ：TLQ
# @Time ：2021/1/7 12:56

import json
import commands
import sys
import xlwt
import prettytable as pt
from prettytable import PrettyTable


reload(sys)
sys.setdefaultencoding('utf-8')

data_dir = ''

def load_json_service_dict():
    load_json = open(data_dir + 'a.json', 'r')
    all_server_json = json.load(load_json)
    return all_server_json

def get_aws_route53_data(hosted_zone_id,profile):
    aws_cli_cmd = "aws route53 list-resource-record-sets --hosted-zone-id "+ hosted_zone_id +" --profile "+ profile +" --output json"
    data_json = commands.getoutput(aws_cli_cmd)
    return json.loads(data_json)

def get_aws_route53_list(all_data):
    route53_list = []
    for i in all_data.get("ResourceRecordSets"):
        route53_list.append(str(i.get("Name"))[:-1])
    route53_list = list(set(route53_list))
    return route53_list


def get_DomainName_value(all_data,route53_list):
    datas = {}
    for j in route53_list:
        domainname_value_list = []
        domainname_value_dict = {}
        for i in all_data.get("ResourceRecordSets"):
            if str(i.get("Name"))[:-1] == j:
                value = []
                domainname_value_dict["Type"] =str(i.get("Type"))
                if i.get("ResourceRecords"):
                    for x in i.get("ResourceRecords"):
                        value.append(str(x.get("Value")))
                else:
                    value.append(str(i.get("AliasTarget").get("DNSName")))
                domainname_value_dict["value"] = value
        domainname_value_list.append(domainname_value_dict)
        datas[j]=domainname_value_list

    return datas

def get_domain_value_secrets(route53_list,datas):
    for i in route53_list:
        get_secrets_cmd = 'curl -Iv  --connect-timeout 5 https://'+ i + ' 2>&1 |grep subject|grep -oE CN=.*$|awk -F  \',\' \'{print $1}\''
        secrets = commands.getoutput(get_secrets_cmd)
        secrets_expire_date_cmd = 'curl -Iv  --connect-timeout 5 https://'+ i + ' 2>&1 | grep "expire date"|sed \'s/expire date://g\'| sed \'s/*//\'|tr -d "\t"'
        expire_date = commands.getoutput(secrets_expire_date_cmd)
        domain_secrets = {}
        for j in datas.keys():
            if i == j:
                domain_secrets["secrets"]=str(secrets)
                domain_secrets["expire_date"]=str(expire_date)
                datas.get(j).append(domain_secrets)
    return datas



def get_data_table(success_data):

    table = PrettyTable(["域名","记录类型","记录值","证书","证书过期时间"])
    for i in success_data.keys():
        table.add_row([i,str(success_data[i][0].get("Type")), str(success_data[i][0].get("value")), str(success_data[i][1].get("secrets")),str(success_data[i][1].get("expire_date"))])
    table.padding_width = 3
    table.align["域名"] = 'l'
    table.align["记录类型"] = 'l'
    table.align["记录值"] = 'l'
    table.align["证书"] = 'l'
    table.align["证书过期时间"] = 'l'
    #print(table)

def out_data_excel(success_data):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    header=["Domain","Type","Value","Secrets","expire_date"]

    for i in range(len(header)):
        sheet.write(0,i,header[i])#第0行第一列写入内容
    for j in range(len(success_data)):
        how = j+1
        sheet.write(how,0,success_data.keys()[j])
        sheet.write(how,1,success_data[success_data.keys()[j]][0].get('Type'))
        sheet.write(how,2,str(success_data[success_data.keys()[j]][0].get('value')).replace("'","").replace("[","").replace("]",""))
        sheet.write(how,3,success_data[success_data.keys()[j]][1].get('secrets'))
        sheet.write(how,4,success_data[success_data.keys()[j]][1].get('expire_date'))

    wbk.save('Domains.xls')


def main():
    hosted_zone_id = raw_input("请输入域名ID,可以从AWS管理控制台-Route53-托管区域-托管区 ID获取:")   #域名ID，可以从AWS管理控制台-Route53-托管区域-托管区 ID获取
    profile = raw_input("请输入AWS配置文件,(eg:9391):")    #AWS配置文件
    all_data= get_aws_route53_data(hosted_zone_id,profile)
    route53_list= get_aws_route53_list(all_data)
    datas = get_DomainName_value(all_data,route53_list)
    success_data = get_domain_value_secrets(route53_list,datas)
    out_data_excel(success_data)
if __name__ == '__main__':
    main()