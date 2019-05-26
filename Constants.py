prefix = '!'

Chiru_bot_token = 'NTY3NTc1NjE3Mzg2ODQwMDc0.XL_txg.huFZuB7fCUU8vMX5Bzpawx-NhQE'

help_info = { 'help' : ( 'short-info' , 'long-info' ),
            'say' : ( 'short-info' , 'long-info' ), 
            'play' : ( 'short-info' , 'long-info' ) }

rps_round_overview_channel = 568332019520503829
rps_round_results_channel = 568332113238294538

bot_spam_channel = 567573421983268884

timeout_in_secs = 10
is_executing = [ False ]
is_disallow_reactions = [ False ]

tictactoe_res = r'C:\Users\coolb\Desktop\Discord Bots\Chiru Bot\Tic_Tac_Toe_Res'

class improper_function_arguments( Exception ) : pass
            
import discord
client = discord.Client()
