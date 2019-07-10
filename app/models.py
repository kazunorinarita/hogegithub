from django.db import models
from django.core import validators
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator

from users.models import User

class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）自分の考えを相手に応じて、わかりやすく的確に伝えることができ、\
        また要点をついた説明ができる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）業務が滞りなく行われるように、他部門との連携・調整がスムーズにできる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）他部門（現場）が業務を円滑に進められるよう必要なサポートを行いまた、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）周りの空気を読み、自部署内および現場を含め法人全体の業務が円滑に進むための横串としての調整力に長けている。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）相手の言いたいことをきちんと聞き、理解できている。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えて行動ができている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分の責任の範囲をきちんと理解し、自分の行う行動や行為、言動に責任を持った発言や行動ができている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）やや困難な状況に直面しても責任を回避したり、途中で挫折することはなく自己の任務を遂行している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 人材育成
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）部下の意見に耳を傾け、部下に対し勇気づけや仕事への動機づけをはかっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）組織運営において、メンバー一人ひとりの能力を把握し、部署目標達成のために的確な役割分担と指示、指導を行っている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）メンバーの先頭に立ち、より良いものを目指す心持ちや姿勢を、日常の発言や行動から模範を示している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示す機会を定期的につくりメンバーと共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）チーム全員が協力して目標に向かうよう団結力とやる気を高めるための定期的な面談やミーティングを実施している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 企画推進力
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）現状に満足することなく、何事にも積極的に新しいことへ挑戦し成果をだしている。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）物事、状況を常により良く改善していこうという意識を持ち、それを日々の行動にうつしている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）自分たちの顧客は誰か、エンドユーザーは誰かを常に考え、そのニーズに応えるために迅速かつ積極的に対応している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）現場のニーズを常に把握し、現場力が最大限に発揮されるために必要なものは何かを判断し提供している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）状況に最も適したタイミングの良い計画・スケジュール化ができている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 経営感覚経営貢献
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）法人の業績に関心を持ち、自分や自部署だけでなく法人全体の利益のためにというひろい視野で物事を考えている。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織全体に利益をもたらす意思決定（意思決定のための調整も含め）がすばやくできる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）経営方針を理解し、貢献を意識した部署目標を設定し、部署としての成果をだしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点を持った発言、行動、判断ができている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # マネジメント力組織管理能力
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）仕事の進行につき問題が生じないように常に気を配り、部下への助言や援助を行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）常に広い問題意識を持っており、現在の仕事に問題が生じそうなときは早め早めに手を打っている。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）管理者としての役割を強く自覚しており、部下に対して模範となる行動・言動ができている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）複雑・困難な問題や突発的事態に対し、自己の責任において臨機応変な処置をとることができている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # 以下、管理項目
    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    flag = models.NullBooleanField(
        verbose_name='入力完了フラグ',
        default = None,
        null=True,
    )

    flag1 = models.NullBooleanField(
        verbose_name='入力完了フラグ1',
        default = None,
        null=True,
    )

    flag2 = models.NullBooleanField(
        verbose_name='入力完了フラグ2',
        default = None,
        null=True,
    )

    order = models.IntegerField(
        verbose_name='ソート順',
	    blank=False,
	    null=False,
        default=1,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by)
        
    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item'
        verbose_name_plural = 'item'

class Item1(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """


        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）自分の考えを相手に応じて、わかりやすく的確に伝えることができ、\
        また要点をついた説明ができる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）業務が滞りなく行われるように、他部門との連携・調整がスムーズにできる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）他部門（現場）が業務を円滑に進められるよう必要なサポートを行いまた、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）周りの空気を読み、自部署内および現場を含め法人全体の業務が円滑に進むための横串としての調整力に長けている。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）相手の言いたいことをきちんと聞き、理解できている。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えて行動ができている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分の責任の範囲をきちんと理解し、自分の行う行動や行為、言動に責任を持った発言や行動ができている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）やや困難な状況に直面しても責任を回避したり、途中で挫折することはなく自己の任務を遂行している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 人材育成
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）部下の意見に耳を傾け、部下に対し勇気づけや仕事への動機づけをはかっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）組織運営において、メンバー一人ひとりの能力を把握し、部署目標達成のために的確な役割分担と指示、指導を行っている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）メンバーの先頭に立ち、より良いものを目指す心持ちや姿勢を、日常の発言や行動から模範を示している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示す機会を定期的につくりメンバーと共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）チーム全員が協力して目標に向かうよう団結力とやる気を高めるための定期的な面談やミーティングを実施している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 企画推進力
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）現状に満足することなく、何事にも積極的に新しいことへ挑戦し成果をだしている。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）物事、状況を常により良く改善していこうという意識を持ち、それを日々の行動にうつしている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）自分たちの顧客は誰か、エンドユーザーは誰かを常に考え、そのニーズに応えるために迅速かつ積極的に対応している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）現場のニーズを常に把握し、現場力が最大限に発揮されるために必要なものは何かを判断し提供している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）状況に最も適したタイミングの良い計画・スケジュール化ができている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 経営感覚経営貢献
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）法人の業績に関心を持ち、自分や自部署だけでなく法人全体の利益のためにというひろい視野で物事を考えている。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織全体に利益をもたらす意思決定（意思決定のための調整も含め）がすばやくできる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）経営方針を理解し、貢献を意識した部署目標を設定し、部署としての成果をだしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点を持った発言、行動、判断ができている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # マネジメント力組織管理能力
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）仕事の進行につき問題が生じないように常に気を配り、部下への助言や援助を行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）常に広い問題意識を持っており、現在の仕事に問題が生じそうなときは早め早めに手を打っている。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）管理者としての役割を強く自覚しており、部下に対して模範となる行動・言動ができている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）複雑・困難な問題や突発的事態に対し、自己の責任において臨機応変な処置をとることができている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    Itemkey = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
    )
    # 以下、管理項目
    # 作成者(ユーザー)
    created_by1 = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy1',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by1 = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy1',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by1)

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item1'
        verbose_name_plural = 'item1'

class Item2(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """


        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）自分の考えを相手に応じて、わかりやすく的確に伝えることができ、\
        また要点をついた説明ができる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）業務が滞りなく行われるように、他部門との連携・調整がスムーズにできる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）他部門（現場）が業務を円滑に進められるよう必要なサポートを行いまた、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）周りの空気を読み、自部署内および現場を含め法人全体の業務が円滑に進むための横串としての調整力に長けている。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）相手の言いたいことをきちんと聞き、理解できている。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えて行動ができている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分の責任の範囲をきちんと理解し、自分の行う行動や行為、言動に責任を持った発言や行動ができている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）やや困難な状況に直面しても責任を回避したり、途中で挫折することはなく自己の任務を遂行している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 人材育成
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）部下の意見に耳を傾け、部下に対し勇気づけや仕事への動機づけをはかっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）組織運営において、メンバー一人ひとりの能力を把握し、部署目標達成のために的確な役割分担と指示、指導を行っている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）メンバーの先頭に立ち、より良いものを目指す心持ちや姿勢を、日常の発言や行動から模範を示している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示す機会を定期的につくりメンバーと共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）チーム全員が協力して目標に向かうよう団結力とやる気を高めるための定期的な面談やミーティングを実施している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 企画推進力
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）現状に満足することなく、何事にも積極的に新しいことへ挑戦し成果をだしている。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）物事、状況を常により良く改善していこうという意識を持ち、それを日々の行動にうつしている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）自分たちの顧客は誰か、エンドユーザーは誰かを常に考え、そのニーズに応えるために迅速かつ積極的に対応している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）現場のニーズを常に把握し、現場力が最大限に発揮されるために必要なものは何かを判断し提供している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）状況に最も適したタイミングの良い計画・スケジュール化ができている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 経営感覚経営貢献
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）法人の業績に関心を持ち、自分や自部署だけでなく法人全体の利益のためにというひろい視野で物事を考えている。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織全体に利益をもたらす意思決定（意思決定のための調整も含め）がすばやくできる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）経営方針を理解し、貢献を意識した部署目標を設定し、部署としての成果をだしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点を持った発言、行動、判断ができている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # マネジメント力組織管理能力
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）仕事の進行につき問題が生じないように常に気を配り、部下への助言や援助を行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）常に広い問題意識を持っており、現在の仕事に問題が生じそうなときは早め早めに手を打っている。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）管理者としての役割を強く自覚しており、部下に対して模範となる行動・言動ができている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）複雑・困難な問題や突発的事態に対し、自己の責任において臨機応変な処置をとることができている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    Itemkey = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
    )
    # 以下、管理項目
    # 作成者(ユーザー)
    created_by2 = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy2',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by2 = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy2',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by2)

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item2'
        verbose_name_plural = 'item2'

class attribute(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    Itemkey = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        related_name='Itemkey',
        editable=False,
        blank=True,
        null=True,
    )

    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    full_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    department = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    job_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.Itemkey)

class Item3(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）患者・利用者・同僚に共感し、状況を把握しようと親身になって聴き、理解できる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）自分の意志や考えを、患者・利用者・同僚に応じてわかりやすく的確に伝えることができる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）患者・利用者・同僚の立場や状況を考え、その場に応じた的確な言動により周りと信頼関係を築くことができる。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）患者・利用者・同僚の視線や行動などから、患者・利用者・同僚が今何を必要としているかを察しそれに応えることができる。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）物事を対処する際、感情的にならず自身の感情を適切にコントロールしながら冷静に事実を見て判断、行動できる。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チームワーク
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）周囲の立場や状況を考えながら、自部署内に限らず他部署とも協力、連携しながら業務を遂行している。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分が多少忙しい中でも、周囲のスタッフが厳しい状況に置かれているときは、積極的にサポートしている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）考え方の異なる同僚との仕事であっても同じ目標にむかって協力して仕事を進めることができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）チームメンバーとして他者の意見を受け入れた上で、自分の思いや考えを発言することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）目標達成のため、一人ひとりが自分の役割に責任を持ちお互い依存することなく協働で成果をだしている。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 向上心
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）学会、院内外の研修や勉強会などキャリアアップのために進んで参加している。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）積極的に他部署や他施設の情報や、医療に関する新しい知識や技能を身につけている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）仕事について工夫や改善を意識し、常に何かをプラスして行動している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）新しい知識を習得し実際にそれを実務に取り入れたり、また同僚と共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）新しいことにも積極的にチャレンジし、挑戦の成果を確認できている。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 行動力
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）仕事に対して他人任せにしないで自分のこととして考え、主体的に発言、行動することができる。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）周りをよく観察し、必要性に気づいたら、自主的に行動できる。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）患者さん、自部署、法人にとって良いと思ったこと、改善できると思うことは、積極的に上位者に提案している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）言われたことは即行動。まずはやってみる。その上でよりよくするための建設的な発言や提案ができる。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）働く環境は与えられるものではなく、自らが作るものだという意識で思考、行動できている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 柔軟性
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）細かな状況の変化を見逃さず、その場の状況において臨機応変に最善の行動ができる。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）自分のやり方に固執するのではなく、患者・利用者・同僚の意見を尊重しその人に合った柔軟な対応ができる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）視野が広く持ち、いろいろな意見を取り入れ、それを仕事に活かしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）新しい仕事、新しい方法、新しい環境に対応し自分なりの成果をだすことができる。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）状況に合わせ仕事の優先順位を変更したり、やり方を変更するなどの判断ができる。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）与えられた役割（仕事）に対して、途中で投げ出さす最後まで責任を持って取り組み、期日までに完成させることができる。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）自分が犯したミスや失敗について他人に責任を押し付けず自分の行動を振り返りどうすればミスを防げたかを検証し改善できる。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）困難な状況や難しい仕事からも逃げずに対処しようと努力をする。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）上司、先輩、同僚や患者さんとの関係において、一度引き受けたことは誠実にやり遂げている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）最終目標までの段取りを組み、周りと協力しながら最後まで諦めず目標を達成することができる。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 基礎力
    Q7_1_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_1 = models.IntegerField(
        verbose_name='（１）報連相ができている。',
        choices=Q7_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )    

    Q7_2_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_2 = models.IntegerField(
        verbose_name='（２）毎日、誰に対しても明るく笑顔で挨拶をしている。',
        choices=Q7_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_3_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_3 = models.IntegerField(
        verbose_name='（３）時間管理ができる（勤務・業務すべてにおいて）',
        choices=Q7_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )
    Q7_4_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_4 = models.IntegerField(
        verbose_name='（４）常に患者さんファーストで考え、行動している。',
        choices=Q7_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )
    Q7_5_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_5 = models.IntegerField(
        verbose_name='（５）健康管理ができている。',
        choices=Q7_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_6_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_6 = models.IntegerField(
        verbose_name='（６）言われたことをまずは素直に受け入れている。',
        choices=Q7_6_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_7_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_7 = models.IntegerField(
        verbose_name='（７）やる気をもって仕事に取り組んでいる。',
        choices=Q7_7_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_8_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_8 = models.IntegerField(
        verbose_name='（８）自己管理ができ、公私の区別がきちんとできている。',
        choices=Q7_8_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_9_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_9 = models.IntegerField(
        verbose_name='（９）話を最後まできくことができる。',
        choices=Q7_9_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_10_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_10 = models.IntegerField(
        verbose_name='（１０）一緒に働く仲間に対し配慮した行動ができている。',
        choices=Q7_10_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # 以下、管理項目
    # 作成者(ユーザー)
    created_by3 = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy3',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by3 = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy3',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    flag = models.NullBooleanField(
        verbose_name='入力完了フラグ',
        default = None,
        null=True,
    )

    flag1 = models.NullBooleanField(
        verbose_name='入力完了フラグ1',
        default = None,
        null=True,
    )

    flag2 = models.NullBooleanField(
        verbose_name='入力完了フラグ2',
        default = None,
        null=True,
    )

    order = models.IntegerField(
        verbose_name='ソート順',
	    blank=False,
	    null=False,
        default=1,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by3)
        
    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item3'
        verbose_name_plural = 'item3'

class Item4(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）患者・利用者・同僚に共感し、状況を把握しようと親身になって聴き、理解できる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）自分の意志や考えを、患者・利用者・同僚に応じてわかりやすく的確に伝えることができる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）患者・利用者・同僚の立場や状況を考え、その場に応じた的確な言動により周りと信頼関係を築くことができる。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）患者・利用者・同僚の視線や行動などから、患者・利用者・同僚が今何を必要としているかを察しそれに応えることができる。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）物事を対処する際、感情的にならず自身の感情を適切にコントロールしながら冷静に事実を見て判断、行動できる。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チームワーク
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）周囲の立場や状況を考えながら、自部署内に限らず他部署とも協力、連携しながら業務を遂行している。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分が多少忙しい中でも、周囲のスタッフが厳しい状況に置かれているときは、積極的にサポートしている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）考え方の異なる同僚との仕事であっても同じ目標にむかって協力して仕事を進めることができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）チームメンバーとして他者の意見を受け入れた上で、自分の思いや考えを発言することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）目標達成のため、一人ひとりが自分の役割に責任を持ちお互い依存することなく協働で成果をだしている。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 向上心
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）学会、院内外の研修や勉強会などキャリアアップのために進んで参加している。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）積極的に他部署や他施設の情報や、医療に関する新しい知識や技能を身につけている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）仕事について工夫や改善を意識し、常に何かをプラスして行動している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）新しい知識を習得し実際にそれを実務に取り入れたり、また同僚と共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）新しいことにも積極的にチャレンジし、挑戦の成果を確認できている。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 行動力
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）仕事に対して他人任せにしないで自分のこととして考え、主体的に発言、行動することができる。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）周りをよく観察し、必要性に気づいたら、自主的に行動できる。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）患者さん、自部署、法人にとって良いと思ったこと、改善できると思うことは、積極的に上位者に提案している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）言われたことは即行動。まずはやってみる。その上でよりよくするための建設的な発言や提案ができる。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）働く環境は与えられるものではなく、自らが作るものだという意識で思考、行動できている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 柔軟性
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）細かな状況の変化を見逃さず、その場の状況において臨機応変に最善の行動ができる。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）自分のやり方に固執するのではなく、患者・利用者・同僚の意見を尊重しその人に合った柔軟な対応ができる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）視野が広く持ち、いろいろな意見を取り入れ、それを仕事に活かしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）新しい仕事、新しい方法、新しい環境に対応し自分なりの成果をだすことができる。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）状況に合わせ仕事の優先順位を変更したり、やり方を変更するなどの判断ができる。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）与えられた役割（仕事）に対して、途中で投げ出さす最後まで責任を持って取り組み、期日までに完成させることができる。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）自分が犯したミスや失敗について他人に責任を押し付けず自分の行動を振り返りどうすればミスを防げたかを検証し改善できる。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）困難な状況や難しい仕事からも逃げずに対処しようと努力をする。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）上司、先輩、同僚や患者さんとの関係において、一度引き受けたことは誠実にやり遂げている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）最終目標までの段取りを組み、周りと協力しながら最後まで諦めず目標を達成することができる。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

        # 基礎力
    Q7_1_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_1 = models.IntegerField(
        verbose_name='（１）報連相ができている。',
        choices=Q7_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )    

    Q7_2_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_2 = models.IntegerField(
        verbose_name='（２）毎日、誰に対しても明るく笑顔で挨拶をしている。',
        choices=Q7_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_3_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_3 = models.IntegerField(
        verbose_name='（３）時間管理ができる（勤務・業務すべてにおいて）',
        choices=Q7_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )
    Q7_4_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_4 = models.IntegerField(
        verbose_name='（４）常に患者さんファーストで考え、行動している。',
        choices=Q7_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )
    Q7_5_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_5 = models.IntegerField(
        verbose_name='（５）健康管理ができている。',
        choices=Q7_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_6_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_6 = models.IntegerField(
        verbose_name='（６）言われたことをまずは素直に受け入れている。',
        choices=Q7_6_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_7_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_7 = models.IntegerField(
        verbose_name='（７）やる気をもって仕事に取り組んでいる。',
        choices=Q7_7_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_8_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_8 = models.IntegerField(
        verbose_name='（８）自己管理ができ、公私の区別がきちんとできている。',
        choices=Q7_8_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_9_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_9 = models.IntegerField(
        verbose_name='（９）話を最後まできくことができる。',
        choices=Q7_9_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_10_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_10 = models.IntegerField(
        verbose_name='（１０）一緒に働く仲間に対し配慮した行動ができている。',
        choices=Q7_10_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    Itemkey = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
    )
    # 以下、管理項目
    # 作成者(ユーザー)
    created_by4 = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy4',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by4 = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy4',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by4)

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item4'
        verbose_name_plural = 'item4'

class Item5(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）患者・利用者・同僚に共感し、状況を把握しようと親身になって聴き、理解できる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）自分の意志や考えを、患者・利用者・同僚に応じてわかりやすく的確に伝えることができる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）患者・利用者・同僚の立場や状況を考え、その場に応じた的確な言動により周りと信頼関係を築くことができる。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）患者・利用者・同僚の視線や行動などから、患者・利用者・同僚が今何を必要としているかを察しそれに応えることができる。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）物事を対処する際、感情的にならず自身の感情を適切にコントロールしながら冷静に事実を見て判断、行動できる。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チームワーク
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）周囲の立場や状況を考えながら、自部署内に限らず他部署とも協力、連携しながら業務を遂行している。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分が多少忙しい中でも、周囲のスタッフが厳しい状況に置かれているときは、積極的にサポートしている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）考え方の異なる同僚との仕事であっても同じ目標にむかって協力して仕事を進めることができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）チームメンバーとして他者の意見を受け入れた上で、自分の思いや考えを発言することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）目標達成のため、一人ひとりが自分の役割に責任を持ちお互い依存することなく協働で成果をだしている。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 向上心
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）学会、院内外の研修や勉強会などキャリアアップのために進んで参加している。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）積極的に他部署や他施設の情報や、医療に関する新しい知識や技能を身につけている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）仕事について工夫や改善を意識し、常に何かをプラスして行動している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）新しい知識を習得し実際にそれを実務に取り入れたり、また同僚と共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）新しいことにも積極的にチャレンジし、挑戦の成果を確認できている。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 行動力
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）仕事に対して他人任せにしないで自分のこととして考え、主体的に発言、行動することができる。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）周りをよく観察し、必要性に気づいたら、自主的に行動できる。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）患者さん、自部署、法人にとって良いと思ったこと、改善できると思うことは、積極的に上位者に提案している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）言われたことは即行動。まずはやってみる。その上でよりよくするための建設的な発言や提案ができる。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）働く環境は与えられるものではなく、自らが作るものだという意識で思考、行動できている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 柔軟性
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）細かな状況の変化を見逃さず、その場の状況において臨機応変に最善の行動ができる。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）自分のやり方に固執するのではなく、患者・利用者・同僚の意見を尊重しその人に合った柔軟な対応ができる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）視野が広く持ち、いろいろな意見を取り入れ、それを仕事に活かしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）新しい仕事、新しい方法、新しい環境に対応し自分なりの成果をだすことができる。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）状況に合わせ仕事の優先順位を変更したり、やり方を変更するなどの判断ができる。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）与えられた役割（仕事）に対して、途中で投げ出さす最後まで責任を持って取り組み、期日までに完成させることができる。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）自分が犯したミスや失敗について他人に責任を押し付けず自分の行動を振り返りどうすればミスを防げたかを検証し改善できる。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）困難な状況や難しい仕事からも逃げずに対処しようと努力をする。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）上司、先輩、同僚や患者さんとの関係において、一度引き受けたことは誠実にやり遂げている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）最終目標までの段取りを組み、周りと協力しながら最後まで諦めず目標を達成することができる。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

        # 基礎力
    Q7_1_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_1 = models.IntegerField(
        verbose_name='（１）報連相ができている。',
        choices=Q7_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )    

    Q7_2_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_2 = models.IntegerField(
        verbose_name='（２）毎日、誰に対しても明るく笑顔で挨拶をしている。',
        choices=Q7_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_3_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_3 = models.IntegerField(
        verbose_name='（３）時間管理ができる（勤務・業務すべてにおいて）',
        choices=Q7_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )
    Q7_4_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_4 = models.IntegerField(
        verbose_name='（４）常に患者さんファーストで考え、行動している。',
        choices=Q7_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )
    Q7_5_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_5 = models.IntegerField(
        verbose_name='（５）健康管理ができている。',
        choices=Q7_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_6_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_6 = models.IntegerField(
        verbose_name='（６）言われたことをまずは素直に受け入れている。',
        choices=Q7_6_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_7_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_7 = models.IntegerField(
        verbose_name='（７）やる気をもって仕事に取り組んでいる。',
        choices=Q7_7_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_8_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_8 = models.IntegerField(
        verbose_name='（８）自己管理ができ、公私の区別がきちんとできている。',
        choices=Q7_8_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_9_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_9 = models.IntegerField(
        verbose_name='（９）話を最後まできくことができる。',
        choices=Q7_9_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    Q7_10_choice = (
        (3, '完璧にできている'),
        (2, 'ほぼできている'),
        (1, '努力している'),
    )

    Q7_10 = models.IntegerField(
        verbose_name='（１０）一緒に働く仲間に対し配慮した行動ができている。',
        choices=Q7_10_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(3)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    Itemkey = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
    )
    # 以下、管理項目
    # 作成者(ユーザー)
    created_by5 = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy5',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by5 = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy5',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by2_1)

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item5'
        verbose_name_plural = 'item5'

class Item6(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）他者のニーズや興味、感性や懸念を聞き取り理解することで、そのニーズに応えることに努力している。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）他者の反応を予測しながら傾聴し、言葉で示されていない問題に気づき行動にうつしている。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）患者さんが納得して治療を受けられるように、患者さんの意思を尊重し、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示しメンバーと共有している。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）リーダーとして、メンバーの強みを引き出し、育てることで、成果を出している。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）医師という仕事に信念持ち、自分の行う行動や行為、言動に責任を重んじる気持ちがある。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）すべてを自分事として捉え、目標に向けての段取りを早く組み、何事もあきらめずやり遂げる強い意志を持っている。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）諸情勢を察知し、問題に対し適切な判断を下し、その判断に責任をもっている。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 診療に対する熱意
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）診療の際に生じた問題の解決に取り組み、診療における様々な問題から逃げず、最後まで責任をもっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）常に新しい知識を学び研鑽し、医療の提供に力を注いでいる。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）患者・家族のニーズに応えるために、迅速かつ非防衛的に多大な努力をしている。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）最新医療や、医療事情に関する情報にアンテナをはり、自身を成長させるための行動をしている。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）医療人としての職業倫理を理解し、医師として相応しい態度で医療を実践している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チャレンジ精神
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）現状に満足することなく、何事にも積極的に新しいことへ挑戦している。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）メンバーの先頭に立ち、よりよいものを目指す心持ちや姿を見せている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）チャレンジングな目標を設定し、部署を巻き込み、達成に向け努力している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）目標達成のためには、障害を乗り越え懸命の努力を維持している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）新しいプロジェクトを自ら企画し、他者を巻き込み目標を達成している。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 経営感覚
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）経営方針を理解し、貢献を意識した行動ができる。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織に利益をもたらす意思決定ができる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）自分の専門職としての興味よりも、組織のニーズを満たすことを優先できる。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点をもっている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チーム医療
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）リーダーとして他職種への医療上の指示を適切に行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）患者さんにとってよりよい医療を提供するために医師同士・部長同士で連携している。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）地域医療に貢献すべく、相手の立場を尊重しながら診療所との適切な関係づくりをしている。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）実現すべき事を考えて計画を立て、周りの共感を得て事を動かしている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）状況に併せて自らの行動や方法を変え、戦略を修正できている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # 以下、管理項目
    # 作成者(ユーザー)
    created_by6 = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy6',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by6 = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy6',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    flag = models.NullBooleanField(
        verbose_name='入力完了フラグ',
        default = None,
        null=True,
    )

    flag1 = models.NullBooleanField(
        verbose_name='入力完了フラグ1',
        default = None,
        null=True,
    )

    flag2 = models.NullBooleanField(
        verbose_name='入力完了フラグ2',
        default = None,
        null=True,
    )

    order = models.IntegerField(
        verbose_name='ソート順',
	    blank=False,
	    null=False,
        default=1,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by6)
        
    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item6'
        verbose_name_plural = 'item6'

class Item7(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）他者のニーズや興味、感性や懸念を聞き取り理解することで、そのニーズに応えることに努力している。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）他者の反応を予測しながら傾聴し、言葉で示されていない問題に気づき行動にうつしている。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）患者さんが納得して治療を受けられるように、患者さんの意思を尊重し、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示しメンバーと共有している。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）リーダーとして、メンバーの強みを引き出し、育てることで、成果を出している。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）医師という仕事に信念持ち、自分の行う行動や行為、言動に責任を重んじる気持ちがある。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）すべてを自分事として捉え、目標に向けての段取りを早く組み、何事もあきらめずやり遂げる強い意志を持っている。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）諸情勢を察知し、問題に対し適切な判断を下し、その判断に責任をもっている。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 診療に対する熱意
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）診療の際に生じた問題の解決に取り組み、診療における様々な問題から逃げず、最後まで責任をもっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）常に新しい知識を学び研鑽し、医療の提供に力を注いでいる。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）患者・家族のニーズに応えるために、迅速かつ非防衛的に多大な努力をしている。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）最新医療や、医療事情に関する情報にアンテナをはり、自身を成長させるための行動をしている。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）医療人としての職業倫理を理解し、医師として相応しい態度で医療を実践している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チャレンジ精神
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）現状に満足することなく、何事にも積極的に新しいことへ挑戦している。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）メンバーの先頭に立ち、よりよいものを目指す心持ちや姿を見せている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）チャレンジングな目標を設定し、部署を巻き込み、達成に向け努力している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）目標達成のためには、障害を乗り越え懸命の努力を維持している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）新しいプロジェクトを自ら企画し、他者を巻き込み目標を達成している。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 経営感覚
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）経営方針を理解し、貢献を意識した行動ができる。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織に利益をもたらす意思決定ができる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）自分の専門職としての興味よりも、組織のニーズを満たすことを優先できる。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点をもっている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チーム医療
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）リーダーとして他職種への医療上の指示を適切に行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）患者さんにとってよりよい医療を提供するために医師同士・部長同士で連携している。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）地域医療に貢献すべく、相手の立場を尊重しながら診療所との適切な関係づくりをしている。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）実現すべき事を考えて計画を立て、周りの共感を得て事を動かしている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）状況に併せて自らの行動や方法を変え、戦略を修正できている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    Itemkey = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
    )
    # 以下、管理項目
    # 作成者(ユーザー)
    created_by7 = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy7',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by7 = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy7',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by7)

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item7'
        verbose_name_plural = 'item7'

class Item8(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
        # コミュニケーション
    Q1_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='（１）他者のニーズや興味、感性や懸念を聞き取り理解することで、そのニーズに応えることに努力している。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    
    Q1_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）他者の反応を予測しながら傾聴し、言葉で示されていない問題に気づき行動にうつしている。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）患者さんが納得して治療を受けられるように、患者さんの意思を尊重し、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示しメンバーと共有している。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）リーダーとして、メンバーの強みを引き出し、育てることで、成果を出している。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='（１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）医師という仕事に信念持ち、自分の行う行動や行為、言動に責任を重んじる気持ちがある。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）すべてを自分事として捉え、目標に向けての段取りを早く組み、何事もあきらめずやり遂げる強い意志を持っている。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）諸情勢を察知し、問題に対し適切な判断を下し、その判断に責任をもっている。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 診療に対する熱意
    Q3_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='（１）診療の際に生じた問題の解決に取り組み、診療における様々な問題から逃げず、最後まで責任をもっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）常に新しい知識を学び研鑽し、医療の提供に力を注いでいる。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）患者・家族のニーズに応えるために、迅速かつ非防衛的に多大な努力をしている。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）最新医療や、医療事情に関する情報にアンテナをはり、自身を成長させるための行動をしている。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）医療人としての職業倫理を理解し、医師として相応しい態度で医療を実践している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チャレンジ精神
    Q4_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='（１）現状に満足することなく、何事にも積極的に新しいことへ挑戦している。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）メンバーの先頭に立ち、よりよいものを目指す心持ちや姿を見せている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q4_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）チャレンジングな目標を設定し、部署を巻き込み、達成に向け努力している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）目標達成のためには、障害を乗り越え懸命の努力を維持している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）新しいプロジェクトを自ら企画し、他者を巻き込み目標を達成している。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # 経営感覚
    Q5_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='（１）経営方針を理解し、貢献を意識した行動ができる。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織に利益をもたらす意思決定ができる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）自分の専門職としての興味よりも、組織のニーズを満たすことを優先できる。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点をもっている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
        # チーム医療
    Q6_1_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='（１）リーダーとして他職種への医療上の指示を適切に行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）患者さんにとってよりよい医療を提供するために医師同士・部長同士で連携している。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）地域医療に貢献すべく、相手の立場を尊重しながら診療所との適切な関係づくりをしている。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）実現すべき事を考えて計画を立て、周りの共感を得て事を動かしている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (5, 'S：他者の模範となるくらいのレベルで行動できている'),
        (4, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (2, 'C：やや足りないが努力している'),
        (1, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）状況に併せて自らの行動や方法を変え、戦略を修正できている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)],
        default = None,
        null = True,
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    # key
    keyname = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        editable=False,
    )

    Itemkey = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
        null=True,
    )
    # 以下、管理項目
    # 作成者(ユーザー)
    created_by8 = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy8',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by8 = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy8',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def name2(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.created_by8)

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'item8'
        verbose_name_plural = 'item8'


