def fibonnacci(nth: int) -> int:
    if nth <= 1:
        return 1
    else:
        return fibonnacci(nth - 1) + fibonnacci(nth - 2)

