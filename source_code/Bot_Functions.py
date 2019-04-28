import discord
import asyncio
import random
import time

from Constants import prefix

def pause( no_seconds ):
    time.sleep( no_seconds )

def random_number( lower_bound, higher_bound ):
    return ( random.randint( lower_bound , higher_bound ) )

async def incomplete_call( channel ):
    await channel.send("**Missing** command arguments!")

async def incorrect_call( channel ):
    await channel.send('I didn\'t understand you! Perhaps you meant'
        + '"poop"\n**Say !help for list of all commands**')

async def verify_input ( message , input ):
    if ( len( message.content ) == len( prefix ) + len( input ) ):
        await incomplete_call( message.channel )
        return False
        
    if ( message.content[ len( prefix ) + len( input ) ] != ' ' ):
        await incorrect_call( message.channel )
        return False
    
    return True

def trim_input ( input_string, command_name ):
    return input_string [ len( prefix ) + len( command_name ) : ].strip()