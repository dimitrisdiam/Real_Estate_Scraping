
from autosite import ZillowScraper

FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSeRNrvCLuWmde4OV4Mj7rs1dLfBSiGutdhe381zhwWKi3ilBg/viewform?usp=sf_link'
ZILLOW_PAGELINK = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.67022170019531%2C%22east%22%3A-122.19643629980469%2C%22south%22%3A37.682425048476226%2C%22north%22%3A37.86804135353387%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

HEADERS = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en,el;q=0.9",
            "cache-control": "max-age=0",
            "cookie": 'zguid=23|%245c172ede-4e94-4136-80b2-11261effb224; _ga=GA1.2.460028284.1642935887; _gid=GA1.2.444621028.1642935887; zjs_user_id=null; zjs_anonymous_id=%225c172ede-4e94-4136-80b2-11261effb224%22; _pxvid=47c4bf2a-7c3c-11ec-a6ba-776e6e51466e; _gcl_au=1.1.1553019129.1642935898; KruxPixel=true; _fbp=fb.1.1642935900348.1947643502; __gads=ID=5fe69a75c8066ab3:T=1642935900:S=ALNI_MZxUeg1hIAhQ0FV0KMKZI1e0ounRQ; __pdst=ace3effb2b1c442db5a74f9d3b3ca94e; _pin_unauth=dWlkPU1EaGhObVZqTnprdFl6SXpNaTAwWWprNUxUZ3pZVGt0Tm1VMk5UQTJZekk0T1RSaQ; KruxAddition=true; FSsampler=1899646412; JSESSIONID=AD825FA6C57C331251DC9809D389655A; zgsession=1|9e0a0ace-d6ba-4d73-b11f-acf27c092535; DoubleClickSession=true; utag_main=v_id:017e869c560e0021cb8b48ba7a680507802f007000942$_sn:2$_se:1$_ss:1$_st:1643014365900$dc_visit:2$ses_id:1643012565900%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:eu-central-1%3Bexp-session$ttd_uuid:742d032a-c7be-4320-817c-517f1825df40%3Bexp-session; g_state={"i_p":1643019860342,"i_l":1}; _gat=1; _pxff_bsco=1; search=6|1645606410974%7Crect%3D38.06238242908446%252C-121.48575819921875%252C37.48708129572077%252C-123.38089980078125%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D0%26beds%3D1-%26price%3D0-872627%26mp%3D0-3000%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%09%09831687%09%09%09%09%09%09; _px3=b9a52a35eb5376ab4973ebed17c9b8c9c44d232c86fe8a5cef4c2ac2ef5ab1e5:6ZFbsTu1C3t41bXATcuIGpVouKGVGbRmu7e/plIRpio2Y3JxLr4kGYIuR/7TIcKFZpvrU9S/DO2qDNE5MNTMCA==:1000:laZT75v53Q4M9tn51XUBpcWU8n9dVa8EJ4ZVYgDcFFyZlj68Irs6PvTP4TO9pyRdUfGvEzDISr4zYIBf/+UgQIFCJIw4Xj36axgzvZQzMWLZkzabl0F9vpVDRBPJmqk15Krd0f9PLo3rGxQooaTLTeWIHveoYuMa/ytY8RQ6sVr4/a/MPRxSlMbUx8FQSsVTqb3VhHJSfuwRO/KeoHFn+Q==; AWSALB=nDJhSTzdepHY45BagusY9E5/6GWuR9F4sA0BgubaCSqQu5ndCcHTbJEDQ1pWdoXPAY9yrP8rTDe+VdpXoIoWLsQZp4M2RImU/Yj9wLZ/8ELp8FG4UfZQq9HgwdEa; AWSALBCORS=nDJhSTzdepHY45BagusY9E5/6GWuR9F4sA0BgubaCSqQu5ndCcHTbJEDQ1pWdoXPAY9yrP8rTDe+VdpXoIoWLsQZp4M2RImU/Yj9wLZ/8ELp8FG4UfZQq9HgwdEa; _uetsid=4ea3bbd07c3c11ec91fe653fb68e18c7; _uetvid=4ea3c1d07c3c11ec963573838984bf0a',
            "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "macOS",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "cross-site",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
}
# PARAMS = {'searchQueryState': '{"pagination":{},"mapBounds":{"west":-122.67022170019531,"east":-122.19643629980469,"south":37.703343724016136,"north":37.847169233586946},"mapZoom":11,"isMapVisible":true,"filterState":{"price":{"max":872627},"beds":{"min":1},"fore":{"value":false},"mp":{"max":3000},"auc":{"value":false},"nc":{"value":false},"fr":{"value":true},"fsbo":{"value":false},"cmsn":{"value":false},"fsba":{"value":false}},"isListVisible":true}'}

zillow = ZillowScraper()
zillow.bring_the_data(ZILLOW_PAGELINK)
zillow.complete_the_doc(FORM)


