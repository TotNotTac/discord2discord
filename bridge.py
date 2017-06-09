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
	if message.channel.id == 'Channel:_ID1':
		await client.send_message(discord.Object(id='Channel_ID2'), message.content)
		
	if message.channel.id == 'Channel_ID2':
		await client.send_message(discord.Object(id='Channel_ID1'), message.content)
	
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')
