from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからPhotoPostFormをインポート
from .forms import ImgPostForm
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required
# photoのモデルをインポート
from .models import ImgPost, Category
# django.views.genericからDetailViewをインポート
from django.views.generic import DeleteView
#問い合わせ
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage


class MasterView(ListView):
    template_name = 'master.html'
    # 投稿のためのqueryset
    queryset = ImgPost.objects.order_by('-posted_at')
    paginate_by = 6

    # 2つ目のモデルを渡すための関数
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # 'category_list'という名前で参照できるようにしている。
        ctx['category_list'] = Category.objects.all()
        return ctx

@method_decorator(login_required, name='dispatch')
class CreateImgView(CreateView):
    form_class = ImgPostForm
    template_name = "post_collection.html"
    success_url = reverse_lazy('collection:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = "post_success.html"

class CategoryView(ListView):
    template_name ='master.html'
    paginate_by = 2
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = ImgPost.objects.filter(
        category=category_id).order_by('-posted_at')
        return categories


class UserNameView(ListView):
    template_name = 'master.html'
    paginate_by = 3
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_names = ImgPost.objects.filter(
            user = user_id).order_by('-posted_at')
        return user_names

class CollectDetailView(DetailView):
    template_name = 'collect_detail.html'
    model = ImgPost

class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 3
    def get_queryset(self):
        queryset = ImgPost.objects.filter(
            user = self.request.user).order_by('-posted_at')
        return queryset
    

class CollectDeleteView(DeleteView):
    template_name = 'collect_delete.html'
    model = ImgPost
    success_url = reverse_lazy('collection:master')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

# 問い合わせフォーム
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('collection:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        # メートルタイトルの書式を設定
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}'\
            .format(name,email,title,message)
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list,
                                )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)

