import discord
import asyncio

import TicTacToe as ttt
from Constants import client, tictactoe_res, timeout_in_secs, improper_function_arguments
from Bot_Functions import get_answer_with_emoji_options, unavailable_feature, get_user
from Bot_Functions import random_number

async def get_difficulty( message ):
    input = await get_answer_with_emoji_options( message , message.author.mention 
                + ' Choose difficulaty: ', '**Easy**', '**Hard**', delete = True ) 

    if ( input == 'timeout' ):
        return 'timeout'
    elif ( input == 1 ):
        return 'easy'
    else:
        return 'hard'

async def computer_tic_tac_toe( message ):
    difficulty = get_difficulty( message )

async def print_board( channel , Board , players = None ):
    if ( len( players ) != 0 and len( players ) != 2 ):
        raise improper_function_arguments( "Expected 2 element tuple but got " 
                                                + str( len( players ) ) + " elements" )
    await channel.send( file= discord.File( Board.curr_board_direc() ) )

async def get_human_users( message ):
    player = await get_user( message , ( message.author.mention + 
        ' registered\nSecond Player Please Click OK to register' ) , [ message.author ] )
    if ( player == 'timeout' ):
        return 'timeout'
    else:
        return ( message.author, player )
    
async def user_vs_user_tic_tac_toe( message ):
    players = get_human_users( message )
    if ( players == 'timeout' ):
        return 'timeout' 
    else:
        player_one , player_two = players
    player_one_is_x = True if random_number( 1 , 2 ) == 1 else False

    Board = ttt.Board_class( tictactoe_res )
    print_board( message.channel, Board, players)

async def user_or_computer( message ):
    input = await get_answer_with_emoji_options( message , 'Please pick an option',
        '**User** vs **User**', '**User** vs **Computer**', delete = True ) 

    if ( input == 'timeout' ):
        return 'timeout'
    elif ( input == 1 ):
        return False
    else:
        return True

async def tic_tac_toe( message ):
    is_against_computer = await user_or_computer( message )
    if ( is_against_computer == 'timeout' ):
        return
    
    if ( is_against_computer ):
        await computer_tic_tac_toe( message )
    else: 
        await user_vs_user_tic_tac_toe( message )