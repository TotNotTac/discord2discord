#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import sys
import time
import pprint
import json

client = discord.Client()
				
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	log = message.content
	await client.send_message(discord.Object(id='Channel_ID'), log)
	
async def on_message(message):
	
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')
