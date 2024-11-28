# すでに用意されているユーザーフォームのクラスをインポート
from django.contrib.auth.forms import UserCreationForm

# モデルをインポート
from .models import ProvisionUser

# サインアップを行うフォームを定義
# usercreationformで定義されているものが引き継がれるため
# 独自に設定する必要がない
class ProvisionCreationForm(UserCreationForm):
    class Meta:
    # 連携するモデルを設定
        model = ProvisionUser
        # 使用するフィールド
        fields = ('username','email','password1','password2')
