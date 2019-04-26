from django.db import models
from django.core import validators

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
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='【コミュニケーション力】（情報伝達・発信力）<br>\
        自分の考えを相手に応じてわかりやすく的確に伝えられる。\
        組織において必要な情報を、的確にわかりやすく正確に伝える力。\
        自己の理論や企画を実行に移すために、関係者を説得、調整する力<br><br>\
        （１）自分の考えを相手に応じて、わかりやすく的確に伝えることができ、\
        また要点をついた説明ができる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    
    Q1_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）業務が滞りなく行われるように、他部門との連携・調整がスムーズにできる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）他部門（現場）が業務を円滑に進められるよう必要なサポートを行いまた、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）周りの空気を読み、自部署内および現場を含め法人全体の業務が円滑に進むための横串としての調整力に長けている。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）相手の言いたいことをきちんと聞き、理解できている。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='【責任感】<br>\
        自己の責任を意識しそれを果たそうとする力<br><br>\
        （１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えて行動ができている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分の責任の範囲をきちんと理解し、自分の行う行動や行為、言動に責任を持った発言や行動ができている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）やや困難な状況に直面しても責任を回避したり、途中で挫折することはなく自己の任務を遂行している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 人材育成
    Q3_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='【人材育成】<br>\
        チームメンバーのやる気と生産性を高め、一人ひとりの成長を促す力<br><br>\
        （１）部下の意見に耳を傾け、部下に対し勇気づけや仕事への動機づけをはかっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）組織運営において、メンバー一人ひとりの能力を把握し、部署目標達成のために的確な役割分担と指示、指導を行っている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）メンバーの先頭に立ち、より良いものを目指す心持ちや姿勢を、日常の発言や行動から模範を示している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示す機会を定期的につくりメンバーと共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）チーム全員が協力して目標に向かうよう団結力とやる気を高めるための定期的な面談やミーティングを実施している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 企画推進力
    Q4_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='【企画推進力】<br>\
        長期的視点での部署運営より高い課題、ハードルに挑戦し克服していこうとする力<br><br>\
        （１）現状に満足することなく、何事にも積極的に新しいことへ挑戦し成果をだしている。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）物事、状況を常により良く改善していこうという意識を持ち、それを日々の行動にうつしている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）自分たちの顧客は誰か、エンドユーザーは誰かを常に考え、そのニーズに応えるために迅速かつ積極的に対応している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）現場のニーズを常に把握し、現場力が最大限に発揮されるために必要なものは何かを判断し提供している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）状況に最も適したタイミングの良い計画・スケジュール化ができている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 経営感覚経営貢献
    Q5_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='【経営感覚・経営貢献】<br>\
        業績に関心を持ち自部署だけでなく法人の利益のための広い視野で物事を考える力<br><br>\
        （１）法人の業績に関心を持ち、自分や自部署だけでなく法人全体の利益のためにというひろい視野で物事を考えている。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織全体に利益をもたらす意思決定（意思決定のための調整も含め）がすばやくできる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）経営方針を理解し、貢献を意識した部署目標を設定し、部署としての成果をだしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点を持った発言、行動、判断ができている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # マネジメント力組織管理能力
    Q6_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='【マネジメント力・組織管理能力】<br>\
        表面的な情報だけでなく、自分自身の考察を加え、真の課題、問題を的確に捉え、解決策を見出し、チーム全体で行動を促す力<br><br>\
        （１）仕事の進行につき問題が生じないように常に気を配り、部下への助言や援助を行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）常に広い問題意識を持っており、現在の仕事に問題が生じそうなときは早め早めに手を打っている。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）管理者としての役割を強く自覚しており、部下に対して模範となる行動・言動ができている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）複雑・困難な問題や突発的事態に対し、自己の責任において臨機応変な処置をとることができている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1)],
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
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='【コミュニケーション力】（情報伝達・発信力）<br>\
        自分の考えを相手に応じてわかりやすく的確に伝えられる。\
        組織において必要な情報を、的確にわかりやすく正確に伝える力。\
        自己の理論や企画を実行に移すために、関係者を説得、調整する力<br><br>\
        （１）自分の考えを相手に応じて、わかりやすく的確に伝えることができ、\
        また要点をついた説明ができる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）業務が滞りなく行われるように、他部門との連携・調整がスムーズにできる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）他部門（現場）が業務を円滑に進められるよう必要なサポートを行いまた、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）周りの空気を読み、自部署内および現場を含め法人全体の業務が円滑に進むための横串としての調整力に長けている。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）相手の言いたいことをきちんと聞き、理解できている。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='【責任感】<br>\
        自己の責任を意識しそれを果たそうとする力<br><br>\
        （１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えて行動ができている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分の責任の範囲をきちんと理解し、自分の行う行動や行為、言動に責任を持った発言や行動ができている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）やや困難な状況に直面しても責任を回避したり、途中で挫折することはなく自己の任務を遂行している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 人材育成
    Q3_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='【人材育成】<br>\
        チームメンバーのやる気と生産性を高め、一人ひとりの成長を促す力<br><br>\
        （１）部下の意見に耳を傾け、部下に対し勇気づけや仕事への動機づけをはかっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）組織運営において、メンバー一人ひとりの能力を把握し、部署目標達成のために的確な役割分担と指示、指導を行っている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）メンバーの先頭に立ち、より良いものを目指す心持ちや姿勢を、日常の発言や行動から模範を示している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示す機会を定期的につくりメンバーと共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）チーム全員が協力して目標に向かうよう団結力とやる気を高めるための定期的な面談やミーティングを実施している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 企画推進力
    Q4_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='【企画推進力】<br>\
        長期的視点での部署運営より高い課題、ハードルに挑戦し克服していこうとする力<br><br>\
        （１）現状に満足することなく、何事にも積極的に新しいことへ挑戦し成果をだしている。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）物事、状況を常により良く改善していこうという意識を持ち、それを日々の行動にうつしている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）自分たちの顧客は誰か、エンドユーザーは誰かを常に考え、そのニーズに応えるために迅速かつ積極的に対応している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）現場のニーズを常に把握し、現場力が最大限に発揮されるために必要なものは何かを判断し提供している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）状況に最も適したタイミングの良い計画・スケジュール化ができている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 経営感覚経営貢献
    Q5_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='【経営感覚・経営貢献】<br>\
        業績に関心を持ち自部署だけでなく法人の利益のための広い視野で物事を考える力<br><br>\
        （１）法人の業績に関心を持ち、自分や自部署だけでなく法人全体の利益のためにというひろい視野で物事を考えている。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織全体に利益をもたらす意思決定（意思決定のための調整も含め）がすばやくできる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）経営方針を理解し、貢献を意識した部署目標を設定し、部署としての成果をだしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点を持った発言、行動、判断ができている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # マネジメント力組織管理能力
    Q6_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='【マネジメント力・組織管理能力】<br>\
        表面的な情報だけでなく、自分自身の考察を加え、真の課題、問題を的確に捉え、解決策を見出し、チーム全体で行動を促す力<br><br>\
        （１）仕事の進行につき問題が生じないように常に気を配り、部下への助言や援助を行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）常に広い問題意識を持っており、現在の仕事に問題が生じそうなときは早め早めに手を打っている。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）管理者としての役割を強く自覚しており、部下に対して模範となる行動・言動ができている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）複雑・困難な問題や突発的事態に対し、自己の責任において臨機応変な処置をとることができている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1)],
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
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_1 = models.IntegerField(
        verbose_name='【コミュニケーション力】（情報伝達・発信力）<br>\
        自分の考えを相手に応じてわかりやすく的確に伝えられる。\
        組織において必要な情報を、的確にわかりやすく正確に伝える力。\
        自己の理論や企画を実行に移すために、関係者を説得、調整する力<br><br>\
        （１）自分の考えを相手に応じて、わかりやすく的確に伝えることができ、\
        また要点をついた説明ができる。',
        choices=Q1_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_2 = models.IntegerField(
        verbose_name='（２）業務が滞りなく行われるように、他部門との連携・調整がスムーズにできる。',
        choices=Q1_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_3 = models.IntegerField(
        verbose_name='（３）他部門（現場）が業務を円滑に進められるよう必要なサポートを行いまた、わかりやすい情報提供を行っている。',
        choices=Q1_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_4 = models.IntegerField(
        verbose_name='（４）周りの空気を読み、自部署内および現場を含め法人全体の業務が円滑に進むための横串としての調整力に長けている。',
        choices=Q1_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q1_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q1_5 = models.IntegerField(
        verbose_name='（５）相手の言いたいことをきちんと聞き、理解できている。',
        choices=Q1_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 責任感
    Q2_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_1 = models.IntegerField(
        verbose_name='【責任感】<br>\
        自己の責任を意識しそれを果たそうとする力<br><br>\
        （１）自分の失敗はチームの失敗であり、チームの失敗は、自分の失敗であると捉えて行動ができている。',
        choices=Q2_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q2_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_2 = models.IntegerField(
        verbose_name='（２）自分の責任の範囲をきちんと理解し、自分の行う行動や行為、言動に責任を持った発言や行動ができている。',
        choices=Q2_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_3 = models.IntegerField(
        verbose_name='（３）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_4 = models.IntegerField(
        verbose_name='（４）問題や課題に対して、自分事として捉え、他責にすることなく対処することができる。',
        choices=Q2_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q2_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q2_5 = models.IntegerField(
        verbose_name='（５）やや困難な状況に直面しても責任を回避したり、途中で挫折することはなく自己の任務を遂行している。',
        choices=Q2_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 人材育成
    Q3_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_1 = models.IntegerField(
        verbose_name='【人材育成】<br>\
        チームメンバーのやる気と生産性を高め、一人ひとりの成長を促す力<br><br>\
        （１）部下の意見に耳を傾け、部下に対し勇気づけや仕事への動機づけをはかっている。',
        choices=Q3_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q3_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_2 = models.IntegerField(
        verbose_name='（２）組織運営において、メンバー一人ひとりの能力を把握し、部署目標達成のために的確な役割分担と指示、指導を行っている。',
        choices=Q3_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_3 = models.IntegerField(
        verbose_name='（３）メンバーの先頭に立ち、より良いものを目指す心持ちや姿勢を、日常の発言や行動から模範を示している。',
        choices=Q3_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_4 = models.IntegerField(
        verbose_name='（４）自分の発する言葉の重要性を意識した上で、部署のビジョン・方向性を示す機会を定期的につくりメンバーと共有している。',
        choices=Q3_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q3_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q3_5 = models.IntegerField(
        verbose_name='（５）チーム全員が協力して目標に向かうよう団結力とやる気を高めるための定期的な面談やミーティングを実施している。',
        choices=Q3_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 企画推進力
    Q4_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_1 = models.IntegerField(
        verbose_name='【企画推進力】<br>\
        長期的視点での部署運営より高い課題、ハードルに挑戦し克服していこうとする力<br><br>\
        （１）現状に満足することなく、何事にも積極的に新しいことへ挑戦し成果をだしている。',
        choices=Q4_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q4_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_2 = models.IntegerField(
        verbose_name='（２）物事、状況を常により良く改善していこうという意識を持ち、それを日々の行動にうつしている。',
        choices=Q4_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_3 = models.IntegerField(
        verbose_name='（３）自分たちの顧客は誰か、エンドユーザーは誰かを常に考え、そのニーズに応えるために迅速かつ積極的に対応している。',
        choices=Q4_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_4 = models.IntegerField(
        verbose_name='（４）現場のニーズを常に把握し、現場力が最大限に発揮されるために必要なものは何かを判断し提供している。',
        choices=Q4_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q4_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q4_5 = models.IntegerField(
        verbose_name='（５）状況に最も適したタイミングの良い計画・スケジュール化ができている。',
        choices=Q4_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # 経営感覚経営貢献
    Q5_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_1 = models.IntegerField(
        verbose_name='【経営感覚・経営貢献】<br>\
        業績に関心を持ち自部署だけでなく法人の利益のための広い視野で物事を考える力<br><br>\
        （１）法人の業績に関心を持ち、自分や自部署だけでなく法人全体の利益のためにというひろい視野で物事を考えている。',
        choices=Q5_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q5_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_2 = models.IntegerField(
        verbose_name='（２）組織全体に利益をもたらす意思決定（意思決定のための調整も含め）がすばやくできる。',
        choices=Q5_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_3 = models.IntegerField(
        verbose_name='（３）経営方針を理解し、貢献を意識した部署目標を設定し、部署としての成果をだしている。',
        choices=Q5_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_4 = models.IntegerField(
        verbose_name='（４）組織の長期的な利益に対しては、自部署の短期的利益も犠牲にできる視点を持った発言、行動、判断ができている。',
        choices=Q5_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q5_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q5_5 = models.IntegerField(
        verbose_name='（５）リスクマネジメント、医療事故防止、院内感染対策の必要性を理解し安全管理の方策を身につけ危機管理に積極的に参加している。',
        choices=Q5_5_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
        # マネジメント力組織管理能力
    Q6_1_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_1 = models.IntegerField(
        verbose_name='【マネジメント力・組織管理能力】<br>\
        表面的な情報だけでなく、自分自身の考察を加え、真の課題、問題を的確に捉え、解決策を見出し、チーム全体で行動を促す力<br><br>\
        （１）仕事の進行につき問題が生じないように常に気を配り、部下への助言や援助を行っている。',
        choices=Q6_1_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )

    Q6_2_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_2 = models.IntegerField(
        verbose_name='（２）常に広い問題意識を持っており、現在の仕事に問題が生じそうなときは早め早めに手を打っている。',
        choices=Q6_2_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_3_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_3 = models.IntegerField(
        verbose_name='（３）自らの感情をコントロールするだけでなく、周りの落ち着きも取り戻せるよう冷静に対処している。',
        choices=Q6_3_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_4_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_4 = models.IntegerField(
        verbose_name='（４）管理者としての役割を強く自覚しており、部下に対して模範となる行動・言動ができている。',
        choices=Q6_4_choice,
        validators=[validators.MinValueValidator(1)],
        default = None,
        null = True,
    )
    Q6_5_choice = (
        (1, 'S：他者の模範となるくらいのレベルで行動できている'),
        (2, 'A：他者からみても、高評価を得られるくらいのレベルで行動できている'),
        (3, 'B：ほぼ、行動できている'),
        (4, 'C：やや足りないが努力している'),
        (5, 'D：まだ足りない'),
    )

    Q6_5 = models.IntegerField(
        verbose_name='（５）複雑・困難な問題や突発的事態に対し、自己の責任において臨機応変な処置をとることができている。',
        choices=Q6_5_choice,
        validators=[validators.MinValueValidator(1)],
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

class Key(models.Model):
        # 評価者
    Key_1 = models.CharField(max_length=10)
    Key_2 = models.CharField(max_length=10)
    Key_3 = models.CharField(max_length=10)
    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return str(self.Key_1)

