# djangoi model@ nerkayacnuma ham db table, ham business domain, 
# ham arandzin vercrac object(tvyal depqum piti "Book" sarqeir),
# hima pordzi nayel businessi koxmic 
# te inch kara petq ga u incha pakasum "Book" modelinm
# orinak -> azgayin grakanutyan 
# patkaneliutyun@(rusakan, haykakan, evropakan etc.) kam
# orinak zhanr@(drama, fantasy, historical etc.),
# u imaci cragravorman imasti 90% da businessin carayutyun
# matucelna, dra hamarem asum pordzi nayes xndrin
# vorpes businessman kam dra nerkayacucuich
#-------------
# hima qez xndir tam vorpes businessi nerkayacucich ->
# "Hov jan uzumem nenc lini vor admin panelum
# tesnem naev te girq@ erba avelacvel db u kuzem
# vor cankacac nor stexcvac girq 3 amis lini vorpes 50% zexchi tak u
# henc 3 amis lrana avtomat helni zexchi takic"




from django.db import models

# menak nayelov objecti anunin piti haskanali lini te inch objecta,
# inchi hamar u inch spasel iranic, hima nayelov
# anunin es chem haskanum te sa incha, 
# "Service" kara hazar tesaki service nshanaki
class Service(models.Model):      
    # aranc "verbose_name" vonces adminum haskanalu te 
    # inch piti lracvi tvyal dashtum ?
    title = models.CharField(max_length=100) 
    author = models.CharField(max_length=50)
    content = models.TextField(blank=True) # incha es dasht@ nerkayacnum ?
    price = models.IntegerField() # dram, dollar, euro, rubli .... ?
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    
    # 'Category' <- ok sencela ashxatum, bayc 90% tokos depqerum
    # aranc quotneri("") grel@ aveli chishta
    # vorovhetev nayeluc miangamic haskanumes vor da objecta,
    # isk senc skzbic tvuma te stringa heto nor haskanumes vor 
    # hxuma depi ayl model, dranic baci foreign_key dashter@
    # arji grel senc -> "cat_id"
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name