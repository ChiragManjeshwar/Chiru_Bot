from PIL import Image
import os

class Board_class:

    board_name = 'Board.png'
    x_name = 'X.png'
    o_name = 'O.png'
    temporary_board_name = 'Temporary_Board.png'
    summary_gif_name = 'Summary.gif'
    summary_gif_dimens = ( 100, 100 )

    __board_list = []

    def __init__( self, direc ):
        self.__directory = direc

        self.__X = Image.open( direc + '\\' + self.x_name )
        self.__O = Image.open( direc + '\\' + self.o_name )
        
        self.__board = Image.open( direc + '\\' + self.board_name )
        self.__board.save( self.__directory + '\\' + self.temporary_board_name)
        self.__board_list.append( self.__board.resize( self.summary_gif_dimens ).copy() )
        self.__board.close()
    
    def __del__( self ):
        self.__X.close()
        self.__O.close()
        os.remove( self.__directory + '\\' + self.temporary_board_name )

        if ( os.path.exists( self.__directory + '\\' + self.summary_gif_name ) ):
            os.remove( self.__directory + '\\' + self.summary_gif_name )

    def curr_board_direc( self ):
        return ( self.__directory + '\\' + self.temporary_board_name )

    def clear_board( self ):
        default_board = Image.open( self.__directory + '\\' + self.board_name )
        default_board.save( self.__directory + '\\' + self.temporary_board_name)
        default_board.close()
        self.__board_list = []
        return ( self.__directory + '\\' + self.temporary_board_name )

    def update_board( self, input_symbol, position ):
        board = Image.open( self.__directory + '\\' + self.temporary_board_name )

        if ( input_symbol.lower() == 'x' ):
            symbol = self.__X
        else:
            symbol = self.__O

        x = ( ( position - 1 ) - (6 if position > 6 else ( 3 if position > 3 else 0 ) ) ) * 100
        x += 1 if x else 0
        y = ( ( position - 1 ) // 3 ) * 100 
        y += 1 if x else 0

        board.paste( symbol , ( x , y ) , symbol )
        board.save( self.__directory + '\\' + self.temporary_board_name )
        self.__board_list.append( board.resize( self.summary_gif_dimens ).copy() ) 
 
        board.close()
        return ( self.__directory + '\\' + self.temporary_board_name )

    def game_summary_gif( self ):
        self.__board_list[0].save( self.__directory + '\\' + self.summary_gif_name, 
            save_all = True, append_images = self.__board_list[ 1 : ], duration = 600, loop = 0 ) 
        return ( self.__directory + '\\' + self.summary_gif_name )

# d.line( ( (50,50), (100,100) ), fill = (0, 0, 255), width = 10)