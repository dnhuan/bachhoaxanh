import requests
import json

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Access-Control-Allow-Origin': '*',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://www.bachhoaxanh.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.bachhoaxanh.com/he-thong-sieu-thi',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'authorization': 'Bearer 4795427F3368A982A3A704DD2A705F7B',
    'deviceid': '96235302-b3e3-4f5c-b532-66452a3cdb32',
    'platform': 'webnew',
    'referer-url': 'https://www.bachhoaxanh.com/he-thong-sieu-thi',
    'reversehost': 'http://bhxapi.live',
    'sec-ch-ua': '"Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'xapikey': 'bhx-api-core-2022',
}


def fetch_all_stores(provinceId, headers):
    all_stores = []
    total_items = None
    page_index = 0
    page_size = 50
    pages_needed = None

    while True:
        params = {
            'provinceId': str(provinceId),
            'districtId': '0',
            'wardId': '0',
            'pageSize': str(page_size),
            'pageIndex': str(page_index),
        }
        print("Getting page" + str(page_index))
        print("size" + str(len(all_stores)))
        response = requests.get('https://apibhx.tgdd.vn/Location/V2/GetStoresByLocation', params=params, headers=headers)
        response_data = response.json()

        # Extract stores and add to the list
        stores = response_data["data"]["stores"]
        all_stores.extend(stores)

        # Set total_items if not already done
        if total_items is None:
            total_items = response_data["data"]["total"]
            pages_needed = total_items // page_size + 2

        # Check if we have reached the last page
        if page_index + 1 >= pages_needed:
            break

        # Move to the next page
        page_index += 1

    return all_stores


tatCaStores = []
allProvinces = [3, 82, 102, 105, 107, 109, 110, 111, 81, 7, 9, 6, 113, 8, 115, 122, 125, 126, 129, 132, 136, 140, 141, 144, 146, 151, 152, 154]
for province in allProvinces:
    print("Fetching stores for province " + str(province))
    tatCaStores.extend(fetch_all_stores(province, headers))

print(len(tatCaStores))

with open("allProvinces.json", "w") as outfile:
    outfile.write(json.dumps(tatCaStores))
