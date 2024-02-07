import http.client, json, requests, time

webhook = "https://discord.com/api/webhooks/1204590660888432710/DsJEJS4q1Nrt18Zbzpyx4iH99alNc39s4NL_V1KFxN40goRCCPB8SnMjtTZ_fM2rge7I"
time_sleep_every_loop = 5
# DONT REMOVE OR IT WONT WORK
made_by = "coxy.57"
ping = "None"

def active():
   conn = http.client.HTTPSConnection("api.bloxflip.com")
   made_by = "coxy.57"
   headers = {
        "Referer": "https://bloxflip.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/117.0.5938.108 Mobile/15E148 Safari/604.1"
   }
   conn.request("GET",url="/chat/history",headers=headers)
   return json.loads(conn.getresponse().read().decode())['rain']

while True:
   rain_ = active()
   if rain_['active']:
      getd = rain_['duration']
      c = rain_['created']
      addx = getd + c
      dur = addx/1000
      duration = round(dur)
      conv = (duration/(1000*60))%60
      time_to_slp = (conv*60+10)
      usdid = requests.post(f"https://users.roblox.com/v1/usernames/users", json={"usernames": [rain_['host']]}).json()['data'][0]['id']
      data = {
         "content": "<@1153035380824743966>",
         "username": "Rain Notifier | made by coxy57"
      }
      data["embeds"] = [
        {
            "description" : f" {ping} A rain has been started!\n**Host**: {rain_['host']}\n**Rain Amount**: {rain_['prize']}\n**Expiration**: <t:{duration}:R>",
            "title" : "Rain Notifier",
            "thumbnail": {
                "url": requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={usdid}&size=50x50&format=Png&isCircular=false").json()['data'][0]['imageUrl']
            }
        }
      ]
      r = requests.post(webhook,json=data)
      time.sleep(time_to_slp)
   time.sleep(time_sleep_every_loop)


# made by coxy
