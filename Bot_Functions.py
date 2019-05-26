import random
import time
import asyncio

from Constants import prefix, improper_function_arguments, timeout_in_secs, client

def pause( no_seconds ):
    time.sleep( no_seconds )

def random_number( lower_bound, higher_bound ):
    return ( random.randint( lower_bound , higher_bound ) )

async def incomplete_command( channel ):
    await channel.send(''"**Missing** command arguments!" )

async def incorrect_command( channel ):
    await channel.send( 'I didn\'t understand you! Perhaps you meant'
        + '"poop"\n**Say !help for list of all commands**' )

async def unavailable_feature( channel ):
    await channel.send( 'Feature currently unavailable!' )

def trim_input ( input_string, command_name ):
    return input_string [ len( prefix ) + len( command_name ) : ].strip()

async def verify_input ( message , input ):
    if ( len( message.content ) == len( prefix ) + len( input ) ):
        await incomplete_command( message.channel )
        return False
        
    if ( message.content[ len( prefix ) + len( input ) ] != ' ' ):
        await incorrect_command( message.channel )
        return False
    
    return True

async def time_out_message( message ):
    await message.channel.send( message.author.mention + 
        ' Did not respond in time, cancelled routine' )

def is_iterable( obj ):
    try:
        iter(obj)
    except TypeError:
        print('not iterable')
        return False
    return True

async def get_answer_with_emoji_options( message, question, *options, 
                            emoji_list = '\U0001F197', timeout = timeout_in_secs, delete = False ):
    sent_messages = [ await message.channel.send( question ) ]

    if ( len( emoji_list ) != 1  and len( emoji_list ) != len( options ) ):
        raise improper_function_arguments("number of emojis != number of options")
    
    if ( len( emoji_list ) == 1 ):
        emoji_list = emoji_list * len ( options )

    if ( is_iterable( emoji_list ) ):
        emoji_list = "".join( emoji_list )

    bot_messages = []

    for emoji, option in zip( emoji_list, options ):
        msg = await message.channel.send( option )
        await msg.add_reaction( emoji )
        bot_messages.append( msg.id )
        sent_messages.append( msg )

    try: 
        reaction = ( await client.wait_for( 'reaction_add' , timeout = timeout ,
            check = lambda  x , y  : ( True if x.message.id in bot_messages else False )
                                        and y == message.author ) ) [ 0 ]
    except asyncio.TimeoutError:
        time_out_message( message )
        if ( delete ):
            for i in sent_messages:
                await i.delete()
        return "timeout"

    if ( delete ):
        for i in sent_messages:
            await i.delete()
    return bot_messages.index( reaction.message.id ) + 1
    # returns which option ( first option = 1 ) was chosen

async def get_user( message , display_message = 'click emoji' , excepted_users = () ,
                        emoji = '\U0001F197' , delete = False):
    msg = await message.channel.send( display_message )
    await msg.add_reaction( emoji )

    def check( reaction , user ):
        if ( user == client.user ):
            return False
        if ( not is_iterable( excepted_users ) ):
            if ( user in excepted_users ):
                return False
            else:
                return True
        elif ( user == excepted_users ):
            return False
        else:
            return True
            
    try:
        user = ( await client.wait_for( 'reaction_add', timeout = timeout_in_secs, 
            check = check ) )[ 1 ]
    except asyncio.TimeoutError:
        time_out_message( message )
        if ( delete ):
            msg.delete()
        time_out_message( message )
        return "timeout"
    if ( delete ):
        msg.delete()
    return user