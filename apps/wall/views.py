from django.shortcuts import render, redirect
from apps.login_registration.models import User 
from .models import Post, Comment

# posts_to_delete = Post.objects.all()
# posts_to_delete.delete()
def wall(request):
    if request.session.get('user_id'):
        current_user = User.objects.get(id = request.session['user_id'])
        context = {
            'user_first_name': current_user.first_name,
            'all_posts': Post.objects.all(),
            "current_user_id": current_user.id,
        }
        return render(request, 'wall/wall.html', context)
    return redirect('/')

def create_post(request):
    current_user = User.objects.get(id=request.session.get('user_id'))
    Post.objects.create(post_content=request.POST["post_content"], user_id=current_user.id)
    return redirect("/wall")

def create_comment(request, post_id): 
    current_user =User.objects.get(id=request.session.get('user_id'))
    Comment.objects.create(comment_content=request.POST["comment_content"], user_id=current_user.id, post_id=post_id)
    return redirect("/wall")

def delete_comment(request, comment_id):
    comment_to_delete = Comment.objects.get(id=comment_id)
    comment_to_delete.delete()
    return redirect("/wall")

def delete_post(request, post_id):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect("/wall")

def logout(request):
    request.session.clear()
    return redirect("/")
