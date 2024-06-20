import os

Ngrok_token = "2hF4nM18BPxdRnYlIwUw9hae9r3_7uBDMDgctvhhJZb4SEJKu" #@param {type:"string"}
# Put your ngrok token here (obtainable from https://ngrok.com)

Ngrok_domain = "" # optional, leave empty if you don't have a domain

# -------------------------------- #

!pip install pyngrok

from pyngrok import ngrok, conf
import fileinput
import sys

if Ngrok_token!="":
  ngrok.kill()
  srv=ngrok.connect(7860 , pyngrok_config=conf.PyngrokConfig(auth_token=Ngrok_token),
                    bind_tls=True, domain=Ngrok_domain).public_url
  print(srv)
  get_ipython().system("python webUI.py")
else:
  print('An ngrok token is required. You can get one on https://ngrok.com and paste it into the ngrok_token field.')
