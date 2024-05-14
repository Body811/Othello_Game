from Player import Player


class AiPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, depth, opponent):
        
        valid_moves = board.get_valid_moves(self)
        if len(valid_moves) == 1:
            return valid_moves[0]
        
        _, move = self.minimax(board, depth, float("-inf"), float("inf"), True, opponent)
        return move

    def evaluate(self, board):

        black_count, white_count = board.count_disks()
        if self.color == "W":
            return white_count - black_count
        else:
            return black_count - white_count

    def minimax(self, board, depth, alpha, beta, maximizing_player, opponent):

        # base case
        if depth == 0 or board.is_finished(self, opponent):
             return self.evaluate(board), None

        if maximizing_player:
            max_eval = float("-inf")
            best_move = None
            valid_moves = board.get_valid_moves(self) 
            for move in valid_moves:
                new_board = board.copy()
                new_board.make_move(move[0], move[1], self, valid_moves)
                eval, _ = self.minimax(new_board, depth - 1, alpha, beta, False, opponent)
                self.diskNum +=1
                if eval > max_eval:
                    max_eval = eval
                    best_move = move

                alpha = max(alpha, eval)

                if beta <= alpha:
                    break

            return max_eval, best_move
        else:
            min_eval = float("inf")
            best_move = None
            valid_moves = board.get_valid_moves(opponent)

            for move in valid_moves:
                new_board = board.copy()
                new_board.make_move(move[0], move[1], opponent, valid_moves)
                eval, _ = self.minimax(new_board, depth - 1, alpha, beta, True, opponent)
                opponent.diskNum +=1
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)

                if beta <= alpha:
                    break

            return min_eval, best_move
