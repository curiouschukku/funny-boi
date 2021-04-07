import praw
import discord
from discord.ext import commands
#praw api

reddit = praw.Reddit(
                    client_id = "Your scripts ID",
                    client_secret = "Your scripts tokeen",
                    username = "Your reddit username",
                    password = "Your Reddit account password",
                    user_agent = "Could be anything, but i reccomend 'pythonagent'"
)


client = commands.Bot(command_prefix='*')
client.remove_command('help')

#

@client.event
async def on_ready():
    print('Logged in')

@client.command()
async def help(ctx):
  em = discord.Embed(title="Help Prompt", description="Gives all help needed with any command (type *help_categoryname for more)", color =discord.Colour.blue())
  em.add_field(name="Games", value="say")
  em.add_field(name = "Images", value = "reddit")
  em.add_field(name = "Other", value = "youtube, duckduckgo, animefinder")
  em.add_field(name =  "Get more info of commands on my website", value = url)
  await ctx.send(embed=em)



@client.command()
async def meme(ctx):
  subreddit = reddit.subreddit('meme')
  all_subs = []
# the limit is the limit to the amount of posts bot can show once booted
  top = subreddit.top(limit = "100000")
  for submission in top:
    all_subs.append(submission)
  
  randomsub = random.choice(all_subs)

  name = random_sub.title
  url = random_sub.url
  em = discord.Embed(title=title, color =discord.Colour.yellow())
  em.set_image(url=url)
  await ctx.send(embed=em)

@client.command()
async def doggo(ctx):
  subreddit = reddit.subreddit('dogs')
  all_subs = []
  top = subreddit.top(limit = "100000")
  for submission in top:
    all_subs.append(submission)
  
  randomsub = random.choice(all_subs)

  name = random_sub.title
  url = random_sub.url
  em = discord.Embed(title=title, color =discord.Colour.yellow())
  em.set_image(url=url)
  await ctx.send(embed=em)

@client.command()
async def cat(ctx):
  subreddit = reddit.subreddit('cats')
  all_subs = []
  top = subreddit.top(limit = "100000")
  for submission in top:
    all_subs.append(submission)
  
  randomsub = random.choice(all_subs)

  name = random_sub.title
  url = random_sub.url
  em = discord.Embed(title=title, color =discord.Colour.yellow())
  em.set_image(url=url)
  await ctx.send(embed=em)


@client.command()
async def duckduckgo(ctx,*, question):
  question = question.replace(" " "+")
  em = discord.Embed(title = "connecting to servers", description = "Connected!")
  em.add_field(name = "DuckDuckGo results:", value = f"And duck duck go says!:https://duckduckgo.com/?q={question}&ia=web")
  await ctx.send(embed=em)

@client.command()
async def animefinder(ctx,*,anime):
  anime = anime.replace(" " "+")
  em = discord.Embed(title = "connecting to servers", description = "Connected!")
  em.add_field(name = "Animenet results:", value = f"https://animenetwork.net/search/?q={anime}&t=anime")
  await ctx.send(embed=em)

@client.command()
async def youtube(ctx,*,yt):
  yt = yt.replace(" " "+")
  em = discord.Embed(title = "connecting to servers", description = "Connected!")
  em.add_field(name = "Youtube results:", value = f"https://www.youtube.com/results?search_query={yt}")
  await ctx.send(embed=em)

client.run('Token')
