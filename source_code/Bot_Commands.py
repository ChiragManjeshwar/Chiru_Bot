import discord
import asyncio

from Bot_Functions import incorrect_call, verify_input, trim_input
from Constants import prefix, help_info

commands = {}

def command_dict( function ):
    commands[function.__name__] = function
    return function

async def help_message( message ):
    embed = discord.Embed( title = '**LIST OF COMMANDS**',
                           description = 'type **!help [command_name]** for a more detailed description',
                           color=0xf7ff28 )

    for i in help_info:
            embed.add_field( name = i,
                            value = (help_info[i])[0],
                            inline = False )
    await message.channel.send( embed = embed )

@command_dict
async def help( message ):
    if ( len(message.content) == len( prefix ) + len( help.__name__ ) ):
         await help_message( message )
         return
    
    if ( not ( await verify_input ( message, help.__name__ ) ) ):
        return

    help_command = trim_input( message.content , help.__name__ )

    try:
        await message.channel.send( (help_info[ help_command ])[1] )
    except:
        await incorrect_call( message.channel )

@command_dict   
async def say( message ):
    if ( not ( await verify_input ( message, say.__name__ ) ) ):
        return

    message_to_say = trim_input( message.content , say.__name__ )

    await message.delete()
    await message.channel.send( message_to_say )

@command_dict
async def terminate( message ):
    if ( len( message.content ) == len( prefix ) + len( terminate.__name__ ) ):
        await message.channel.send( 'Bye!' )
        quit()
