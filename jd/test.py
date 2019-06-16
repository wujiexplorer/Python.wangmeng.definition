import requests
from lxml.html import etree
import time
import csv


# 定义函数抓取每页前30条商品信息
def crow_first(n):
    # 构造每一页的url变化
    url = 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&' \
          'enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=' + str(
        2 * n - 1)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=2&s=29&scrolling=y&log_id=1560410274.34680&tpl=3_M&show_items=100003344497,100000177756,100003395445,100005702200,100000651175,7437786,8735304,100002642218,100000773875,3133811,100004245926,100004404954,100003242371,100002425279,100000287145,100005228558,100002795955,100001467225,100003138763,100000650837,7283905,7299782,100003062377,7437710,100003475378,100003464635,100000822981,8485229,100003884564,7437788',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&pvid=829a8faa9f3e43a8a213dc695e6a8dd4',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': '__jdc=122270672; __jdv=122270672|direct|-|none|-|1560404473161; areaId=15; __jdu=15604044731381234785254; PCSYCityID=1213; shshshfpa=0622183f-a931-2db0-748b-17f5474e432b-1560404474; shshshfpb=qI3hc6X7VgMzrypf%2FSMAnFw%3D%3D; xtest=374.cf6b6759; ipLoc-djd=1-72-2799-0; rkv=V0200; __jda=122270672.15604044731381234785254.1560404473.1560404473.1560409742.2; shshshfp=fafa3644970f4f4759fba440e1007e57; qrsc=3; 3AB9D23F7A4B3C9B=GL5EO3YGIQLZW45BQUEE3CPAZ4PSWOL7OL2F3VLFRKPAHP33N2Q3TVKMURWQ5SG5YGZ2MEQHIUJ7GCQSATHOXLSUHY; __jdb=122270672.7.15604044731381234785254|2.1560409742; shshshsID=15004e2abfde605efb7757c545b7f0ee_7_1560410275352'
            }
    r = requests.get(url, headers=head)
    # 指定编码方式，不然会出现乱码
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    # 定位到每一个商品标签li
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    # 将抓取的结果保存到本地CSV文件中
    i = 0
    with open('JD_Phone.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        for data in datas:
            psku = data.xpath('//li/@data-sku')[i]
            pspu = data.xpath('//li/@data-spu')[i]
            pid = data.xpath('//li/@data-pid')[i]
            p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')
            # 这个if判断用来处理那些价格可以动态切换的商品，比如上文提到的小米MIX2，他们的价格位置在属性中放了一个最低价
            if len(p_price) == 0:
                p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
                # xpath('string(.)')用来解析混夹在几个标签中的文本
            write.writerow([pspu, psku, pid, p_name, p_price])
            i += 1
    f.close()


# 定义函数抓取每页后30条商品信息
def crow_last(n):
    # 获取当前的Unix时间戳，并且保留小数点后5位
    a = time.time()
    b = '%.5f' % a
    url = 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=' + str(
        2 * n) + '&scrolling=y&log_id=' + str(b)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=2&s=30&scrolling=y&log_id=1560477410.86775&tpl=3_M&show_items=100003344497,100003395445,100005702200,100000651175,100000177756,8735304,100003242371,100002642218,7437786,100002425279,100004245926,100000773875,100002795955,3133811,100005228558,100000287145,7437710,100001467225,4120319,100004404954,100000650837,100003464635,7299782,7283905,100003062377,100000400128,100000993265,8485229,7652029,100003884564',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&pvid=264b4c2a2572442a9051878a2c3d6932',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': '__jdc=122270672; __jdv=122270672|direct|-|none|-|1560404473161; areaId=15; __jdu=15604044731381234785254; PCSYCityID=1213; shshshfpa=0622183f-a931-2db0-748b-17f5474e432b-1560404474; shshshfpb=qI3hc6X7VgMzrypf%2FSMAnFw%3D%3D; xtest=374.cf6b6759; ipLoc-djd=1-72-2799-0; rkv=V0200; qrsc=3; __jda=122270672.15604044731381234785254.1560404473.1560409742.1560476146.3; 3AB9D23F7A4B3C9B=GL5EO3YGIQLZW45BQUEE3CPAZ4PSWOL7OL2F3VLFRKPAHP33N2Q3TVKMURWQ5SG5YGZ2MEQHIUJ7GCQSATHOXLSUHY; __jdb=122270672.7.15604044731381234785254|3.1560476146; shshshfp=fafa3644970f4f4759fba440e1007e57; shshshsID=85e9dea4f68824dbe1be1cb68a470ba9_3_1560477410686'

            }
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    i=0
    with open('JD_Phone.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        for data in datas:
            psku = data.xpath('//li/@data-sku')[i]
            pspu = data.xpath('//li/@data-spu')[i]
            pid = data.xpath('//li/@data-pid')[i]
            p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')
            if len(p_price) == 0:
                p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
            write.writerow([pspu, psku, pid, p_name, p_price])
            i+=1
    f.close()


if __name__ == '__main__':
    with open('JD_Phone.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        write.writerow(['spu', 'sku', 'pid', 'pname', 'price'])
        f.close()
    for i in range(1, 101):
        # 下面的print函数主要是为了方便查看当前抓到第几页了
        print('***************************************************')
        try:
            print('   First_Page:   ' + str(i))
            crow_first(i)
            print('   Finish')
        except Exception as e:
            print(e)
        print('------------------')
        try:
            print('   Last_Page:   ' + str(i))
            crow_last(i)
            print('   Finish')
        except Exception as e:
            print(e)