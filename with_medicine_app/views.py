from django.shortcuts import render
from with_medicine_free.models import Free_board
from with_medicine_review.models import Review_board

# Create your views here.

def main(request):
    free_boards = Free_board.objects.all()[:7]
    review_boards = Review_board.objects.all()[:7]
    return render(request, 'main.html', {'free_boards': free_boards, 'review_boards':review_boards})
