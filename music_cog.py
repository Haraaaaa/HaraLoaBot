import discord
import random
from discord.ext import commands

from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""

     #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            #try to connect to voice channel if you are not already connected

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            print(self.music_queue)
            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name="play")
    async def p(self, ctx, *args):
        query = " ".join(args)
        
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            #you need to be connected so that the bot knows where to go
            await ctx.send("목림의 방으로 들어오라규!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("노래를 못찾겠어요! 왔다한테 노래 불러달라하세요")
            else:

                            
#                @bot.command()
#                async def 안녕(ctx):
                random_message = ['목림이 노래 부른다~ 동구밭 과수원길..', '샹트햄이 노래 부른다~ 숙제가 제일 좋아~', '나날이 노래 부른다~ 이게 기공이지', '왔다가 노래부른다~ 여어~~','워로드가 노래부른다~ 카운터요?']  
                random_message_number = random.randint(0, len(random_message) - 1)
                embed = discord.Embed(title = random_message[random_message_number], color = 0x62c1cc)                
               # embed.add_field(name=retval, inline=True)
                await ctx.send(embed = embed)



#                random_message = ['목림이 노래부른다~ 몽몽몽', '샹트햄이 노래부른다~ 숙제가 제일 좋아~', '나날이 노래부른다~ 이게기공이지', '왔다가 노래부른다~ 여어~~','워로드가 노래부른다~ 카운터요?']  
#                random_message_number = random.randint(0, len(random_message) - 1)
#                await ctx.send(random_message[random_message_number]) 

                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="queue")
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("노래 좀 추가해주세요 ㅠ")

    @commands.command(name="skip")
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music()
            
    @commands.command(name="disconnect")
    async def dc(self, ctx):
        await self.vc.disconnect()
