#coding=utf-8

def LoadArticles():
	id = 1;
	articles = []
	#
	art = ClsArticle(id, "第一篇叽歪", "2014-06-24 19:00:18")
	art.add_tag("start")
	art.add_p("终于有个不是很像样但总归是完完全全属于自己的窝了。")
	art.add_p("过年的时候就开始有搭窝的想法到现在才有这么个不像样的东西，强烈鄙视一下自己的执行力。")
	art.add_p("以下是反省：")
	art.add_p("总想着先把窝搭起来，然后再填东西，很多想法没有记下来，前段时间一直纠结于整个网站该怎么设计，各种折腾各种不满意，不干正经事，净干些有的没的只看得到浪费的时间完全看不到产出的事，遍地都是无用功。")
	art.add_p("以下是反反省(人的脸皮要不要这么厚)")
	art.add_p("鉴于女生总是对自己的窝有天然的情结，无论神经多大条，所以不管在这上面花多少心思都是可原谅的不是么，于是姐姐就权且把你当做个妹子然后原谅你啦:)另外，还有个更冠冕堂皇又事实上还是比较正确的理由是：不折腾怎么知道到底想要啥，类似于折腾一圈高端洋气的记录工具、管理工具之后，最终还是返朴归真回归txt的怀抱。道理都是一样一样滴~~这么有哲理，好想给自己颁个奖~~")
	art.add_p("从有搭窝想法开始就一直在yy搭完窝以后的幸福生活，其实也无非是可以喝着不管什么反正顺口的东西，窝在自己那个柠檬布丁里，晒着暖乎乎的大太阳，然后或是梳理自己的一路走来，把它们一件件布置到窝里，或是娓娓道来当下的事当下的心情，又或是捣鼓一些很酷很好玩的事，一点点去完成自己一直以来的那个梦想，这是我现阶段能想到的最惬意的人生了。")
	art.add_p("作为首篇，说点不是很正事的正事吧~")
	art.add_p("Why here?")
	art.add_p("就像子标题写的，“找个地方跟自己扯扯淡，顺便让小日子有迹可循”，虽然微博、微信、人人，甚至QQ空间都有这功能，但人多人杂，所有人看所有人罢了，很多东西也并不想公诸于众，找个清净的地儿，用心经营这个虚拟的家，大门又是敞开的，爱来的主儿得空过来坐坐聊聊，不爱来的也就落得耳根子清静，多好。")
	art.add_p("此为初衷，过个一年再回头看看演变成啥样了...")
	art.add_p("Why Elaine?")
	art.add_p("出处是个人看的为数不多的偶像剧之一《命中注定我爱你》。契机是13年入职新公司买了新本本需要输入用户名，那个刹那突然有个念头，那么就从这个用户名开始新生活吧。一直以来，自己骨子里的性格跟主人公比较像，也很欣赏欣怡最后的蜕变，希望自己经历那件事之后也可以完成跟她一样的蜕变，也很希望可以跟她一样幸运有一双强有力的手出现把我拉出泥潭，这可能也是有生以来最期待有那么一个人出现的时间段了，但内心非常清楚这些总归是偶像剧里才容易出现的桥段，只是话说回来，相较于有这么个人拉我，完全靠着自己的力量爬出泥潭对自己内心的锻炼应该是更大一些，毕竟生命中总是有些路需要自己一个人走过来的。至于另一个愿望，现在看来，勉强也算及格喽。")
	art.add_p("Why Abumiao?")
	art.add_p("养的一只傻猫，原本以为傻猫跟了我是傻猫的福气，各种宠着各种护着各种心疼，无比强大的容忍度，然后...anyway，谨以这种方式念叨我的傻猫。")
	art.add_p("What to do?")
	art.add_p("三大块：学习向、生活向、工作向；互相之间又有交集，各种攒经验，各种记录。")
	art.add_p("好啦，迈出了第一步，接下来就是慢慢迭代慢慢积累了喽 O(∩_∩)O~")
	art.add_p("By the way，老妈生日快乐:)")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "关于blog的YY", "2014-06-25 21:04:18")
	art.add_tag("home_building")
	art.add_p("火车上关于博客内容yy了一些东西，记录下：")
	art.add_p("1. 文章不预先分类，只贴标签，可以多个，文章包括新写的和搬运过来的")
	art.add_p("2. 系统自动分类并展示")
	art.add_p("3. 文章分析，所有文章、按各种维度分类(时间轴横向、纵向，天气，等等能想到的)，看看自己脑子里到底都在想些什么...")
	art.add_p("这就好多事啦，粗粗一看，就涉及分类算法、中文分词、语义分析三个玩意了，还不包括前端展示。Hoho，ms很高端的样子，其实可以做得很傻...迫不及待准备动手喽~这磨刀霍霍的小样(*/ω＼*)")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "当前遇到的几个问题", "2014-06-25 21:04:18")
	art.add_tag("issue")
	art.add_p("1. 手贱装了wordexpress、nginx、mysql，卸不干净...nginx每次开机自启动地很嗨皮")
	art.add_p("2. 手动启动flask之后，总是时不时自己会断掉，不晓得是不是跟nginx有关系，一失手成千古恨啊")
	art.add_p("3. python传中文字符给前端ok，但是前端要显示的话就跪了，错误提示：Internal Server Error[The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.]。综上，可得，当前界面所有的中文都是静态的...所以，请尽情鄙视...")
	art.add_p("ps:嗯，问题列表可以作为一个单独的分类")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "九宫", "2014-06-26 06:34:12")
	art.add_tag("emotion")
	art.add_p("请诚实面对自己，有些事该承认的还是要承认的，怕顶个什么用啊亲，跟个鸵鸟似的。就是承认了又能怎么样呢，既然都是鸵鸟了，还不是尽给自己找不痛快...")
	art.add_p("转移注意力，其实前两天做得还可以，如果今天身体没有提醒自己的话，继续加油吧。")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "模板传中文变量前端显示时报错问题closed", "2014-06-26 11:16:57")
	art.add_tag("issue")
	art.add_p("1. python文件首行添加：#coding=utf-8")
	art.add_p("2. jinja模板中文变量处：{{中文变量名.decode('utf8')}}")
	art.add_p("都要这么设吗？ms稍显麻烦啊。不晓得还有没有其他更方便的办法")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "iptables管理单个ip以及ip段", "2014-06-26 15:40:32")
	art.add_tag("linux")
	art.add_p("屏蔽单个IP:	iptables -I INPUT -s 123.45.6.7 -j DROP")
	art.add_p("屏蔽封123.0.0.1到123.255.255.254:	iptables -I INPUT -s 123.0.0.0/8 -j DROP")
	art.add_p("屏蔽封123.45.0.1到123.45.255.254:	iptables -I INPUT -s 123.45.0.0/16 -j DROP")
	art.add_p("屏蔽封123.45.6.1到123.45.6.254:		iptables -I INPUT -s 123.45.6.0/24 -j DROP")
	art.add_p("解封:	iptables -I INPUT -s 192.168.1.138 -j ACCEPT")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "git自用操作", "2014-06-26 19:55:43")
	art.add_tag("git")
	art.add_tag("dev_env")
	art.add_p("下载版本库上的代码到本地，相当于svn的checkout: git clone https://github.com/*/*.git")
	art.add_p("下载版本库上的更新到本地，相当于svn的update: git pull https://github.com/*/*.git")
	art.add_p("土人就用了这两个...")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "linux log 重定向", "2014-06-26 20:06:54")
	art.add_tag("linux")
	art.add_p("python index.py 2>>my_web_world_20140626.log")
	art.add_p("Mark一下，稍后整理...")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "这娘俩没救了", "2014-06-26 22:49:14")
	art.add_tag("family")
	art.add_p("跟老妈扯淡，老妈发新装修后的老家照片给我，于是有了以下对话，尖括号内为QQ表情：")
	art.add_p("    老妈:	'还可以伐<大笑>'")
	art.add_p("    我:		'相当可以啊，皇宫啊'(当然，为了拍老妈马屁，此处略夸张...)")
	art.add_p("    老妈:	'那明天请公主入宫<偷笑>'")
	art.add_p("    我:		'母后大人<膜拜>'")
	art.add_p("    老妈:	'平身'")
	art.add_p("    我:	'谢谢母后<膜拜>'")
	art.add_p("窃以为这娘俩真心没救了...")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "反省贴", "2014-06-27")
	art.add_tag("emotion")
	art.add_p("之前一直以为这段时间务虚过度要收着点，回过头来看其实压根没有务虚也没有务实，确切来说只是消耗过度，输入又太少，也就是入不敷出，又略显浮躁，不管从哪个角度来看对自己的成长都没有任何帮助。好在对别人的成长似乎还有些作用，所以也不能算完全浪费。只是这样来权衡生活，是否又略显功利了些，或许也是内心安全感缺失的一种表现，只能通过不断丰富自己来获取。话说回来，这种做法在迷惘阶段总是最妥当的，当不知道做什么的时候，做些什么总比什么都不做来得好不是么。所以，规划一下之后要做的事才是正经事哈。")
	art.add_p("1. 跟coursera的课")
	art.add_p("2. 每周一篇翻译")
	art.add_p("3. 看书要写东西，包括记录和感想，记录哪怕只是TOC，感想哪怕只是一句话。")
	art.add_p("4. 跑步、羽毛球")
	art.add_p("5. 自省，远了就要拉回来")
	art.add_p("6. 两个月回一次家")
	art.add_p("ps: 其实就是跑几个cronjob...")
	art.add_p("在另外那个领域，放任自己感性，不要急，不要等。")
	art.add_p("可能换一个角度，这个领域会更简单一些，因为只要坚持走在对的路上，展现最真实的自己，遇到的自然也就是对的人。需求再简单不过，情投意合，志同道合，而已。最美的画面是红袖添香，而后共剪西窗烛。每个人都还是期望找到soulmate的吧，只不过现实有时候很强大，强大到可以让那么多人向它低头，但也正因为如此，有些做法才显得很不现实却又弥足珍贵。最近状态不好，其实也知道自己怎么回事，只是不想承认罢了。")
	art.add_p("不管是哪个领域，只有尽力了，才有资格说：得之我幸，失之我命。")
	art.add_p("好了，梳理一下清晰了好多。悟以往之不谏，知来者之可追，实迷途其未远，觉今是而昨非:)")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "九宫", "2014-06-29")
	art.add_tag("emotion")
	art.add_p("重要的事：跟骁骁语音长聊两个小时，有这么个好朋友每次不管多久没联系距离有多远环境差异有多大只要一聊思维都能同步上实在太不容易了，你要是在国内该有多好；订婚快乐:)")
	art.add_p("有用的事：发现看书的时候边看边想，成型的想法po到微信上，可以锻炼总结提炼能力，可以强迫自己思考，还能看到大家的想法，这是很有意思的一件事。")
	art.add_p("该反省的事：吃零食，不好好吃饭")
	art.add_p("困了，睡觉~")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "以图搜图 & reCaptcha", "2014-06-30")
	art.add_tag("research")
	art.add_tag("cv")
	art.add_tag("algorithm")
	art.add_tag("search_by_image")
	art.add_tag("reCaptcha")
	art.add_p("对Google的以图搜图功能感兴趣很久了，前段时间翻译了一篇reCaptcha相关的文章，接下来稍微研究一下这两个玩意")
	art.add_p("以图搜图参考资料：")
	art.add_p("1. Dr. Neal Krawetz")
	art.add_p("2. http://www.ruanyifeng.com/blog/2011/07/principle_of_similar_image_search.html")
	art.add_p("3. http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html")
	art.add_p("4. 几个牛掰的：谷歌Search by Image、百度识图、TinEye、淘宝图想")
	art.add_p("reCaptcha待调研")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "wordexpress、nginx、mysql卸载问题close", "2014-07-02")
	art.add_tag("issue")
	art.add_p("1. apt-get remove nginx")
	art.add_p("2. 暴力删除nginx文件夹：/etc/nginx")
	art.add_p("3. 因为当时直接解压使用，所以直接删除wordexpress文件夹：/srv/www/wordxpress")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "Baader-Meinhof Phenomenon", "2014-07-02")
	art.add_tag("psychology")
	art.add_tag("fun")
	art.add_p("原来这货还有专有名词，还是个这么八竿子打不着的名词...太扯了,以后我们也可以随便yy啥啥现象咩...")
	art.add_p("References:")
	art.add_p("1. http://en.wikipedia.org/wiki/Baader-Meinhof_Phenomenon#Frequency_illusion")
	art.add_p("2. http://localhost-8080.com/2010/10/baader-meinhof-phenomenon/")
	art.add_p("Comments added later: 不对，这货不就是孕妇效应么@_@")
	#
	id = id + 1
	art = ClsArticle(id, "Dr. Neal Krawetz", "2014-07-02")
	art.add_tag("research")
	art.add_tag("cv")
	art.add_tag("algorithm")
	art.add_tag("search_by_image")
	art.add_p("Personal wensite: http://www.hackerfactor.com/")
	art.add_p("Web: http://fotoforensics.com/")
	art.add_p("Articels about search by image:")
	art.add_p("1. http://www.hackerfactor.com/blog/index.php?/archives/536-Humongous.html")
	art.add_p("2. http://www.hackerfactor.com/blog/index.php?/archives/551-Big-Data.html")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "Notes of <Tutorial: Similar Image Search>", "2014-07-03")
	art.add_tag("research")
	art.add_tag("cv")
	art.add_tag("algorithm")
	art.add_tag("search_by_image")
	art.add_p("Tutorial: Similar Image Search[http://fotoforensics.com/tutorial-search.php]")
	art.add_p("Methodology")
	art.add_p("context around the picture: available text-to-image search services; long-time keywords searching; not so useful")
	art.add_p("Approaches for finding visually similar images:")
	art.add_p("1. Using a cryptographic hash function, such as MD5 or SHA1. ")
	art.add_p("How: The same hash value identifies the exact same picture. ")
	art.add_p("However: a single byte change will result in significantly different hash values. ")
	art.add_p("2. Digital picture analysis typically relies on perceptual hash")
	art.add_p("	How:")
	art.add_p("		Similar hash values for visually-similar pictures. ")
	art.add_p("		Different algorithms may focus on colors, edges, corners, 'blobs', or frequency patterns.")
	art.add_p("	Can Do:")
	art.add_p("		Match similar pictures, even if there are significant size, quality, and coloring differences.")
	art.add_p("		Match pictures with minor differences in content, cropping, and rotation.")
	art.add_p("	Publicly Available Services:")
	art.add_p("		Function:")
	art.add_p("			input: image")
	art.add_p("			output: web pages that host variations of the picture")
	art.add_p("		Exs:")
	art.add_p("			1. TinEye")
	art.add_p("				Exceptional at finding partial matches. ")
	art.add_p("				Weak at new pictures")
	art.add_p("				Good at widely circulated pictures, and images from news outlets.")
	art.add_p("			2. Google Image Search")
	art.add_p("				Indexed most of the pictures found by Google, including late-breaking pictures that are only a few hours old.")
	art.add_p("				Exceptional at identifying textual content related to pictures.")
	art.add_p("				Not strong at identifying significant variations from cropping, splicing, or editing.")
	art.add_p("			3. Karma Decay")
	art.add_p("				Only identifies pictures on the Reddit social network.")
	art.add_p("				Useful for identifying topics such as memes and controversial current events.")
	art.add_p("")
	art.add_p("Identifying Quality")
	art.add_p("	Attributes to evaluate quality:")
	art.add_p("	1. Dimensions: The larger, the better (not always, but usually)")
	art.add_p("	2. File size: With same dimensions, The larger, the better.")
	art.add_p("	3. Cropping: More content along the edge, the better (cuz easy to remove, hard to add)")
	art.add_p("	4. Padding: No or thinner border, the better (cuz saving after adding border will lower the quality)")
	art.add_p("	5. Blur and noise. (original pictures with sensor noise not noticable)")
	art.add_p("	6. Attribution (such aslogos, watermarks, and copyright text): Better without attributions(cuz content obscured after adding attrs, and quality lowered after saving)")
	art.add_p("	7. Metadata(Data about data): Better with than without")
	art.add_p("	8. Source: Better from professional photo sites (such as Getty Images and Reuters) than online services (such as Facebook, Imgur, and Twitter)")
	art.add_p("	9. Age: The older, the better.")
	art.add_p("")
	art.add_p("")
	art.add_p("")
	art.add_p("Identifying Context")
	art.add_p("More authoritative text, higher quality")
	art.add_p("Discussion about the picture, time period")
	art.add_p("Google Image Search: attempt to associate common text to similar pictures")
	art.add_p("Karma Decay: identify discussion threads at Reddit that typically provide context.")
	art.add_p("TinEye: only identifies web sites that host the picture. You may need to visit multiple web sites in order to identify the context.")
	art.add_p("")
	art.add_p("Similar pictures, similar distribution patterns")
	art.add_p("Exs: ")
	art.add_p("1. if variations of a picture are widely found on social networking sites, then it is likely a widely discussed topic.")
	art.add_p("2. If variants are only found on Thai web sites, then the person who generated the variant that you are evaluating may be able to read Thai or may have ties to Thailand.")
	art.add_p("")
	art.add_p("")
	art.add_p("这段不好归纳...")
	art.add_p("When identifying textual context(文本语境), be wary of hoaxes and conspiracy theories. An established hoax/conspiracy typically results in contradicting textual descriptions. One description supports the concept, a different description debunks the issue, and a third may provide the initial story. In these cases, the amount of text and age of the text is typically independent of the ground truth. (There may be more articles around a hoax, but that doesn't mean it is real.) Do not assume that the initial story, or the most repeated explanation, is accurate. With hoaxes and conspiracies, look for cited sources and identifiable experts; unspecified sources and anonymous experts who are only identified by online handles are unlikely to be authoritative sources.")
	art.add_p("")
	art.add_p("Caveats")
	art.add_p("Variants of viral pictures with different MD5/SHA1 hash values result in search noise.")
	art.add_p("Hoaxes and conspiracy theories of images' context")
	art.add_p("Maybe unable to identify initial picture")
	art.add_p("Composite pictures")
	art.add_p("Similar does not mean identical")
	art.add_p("Similar image search is only one evaluation approach. Important to validate findings with other analysis techniques and algorithms.")
	art.add_p("")
	art.add_p("哎，格式不能忍...")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "长见识了", "2014-07-04")
	art.add_tag("fun")
	art.add_p("康威生命游戏(Conway's Game): http://zh.wikipedia.org/wiki/%E5%BA%B7%E5%A8%81%E7%94%9F%E5%91%BD%E6%B8%B8%E6%88%8F")
	art.add_p("细胞自动机(cellular automaton): http://zh.wikipedia.org/wiki/%E7%B4%B0%E8%83%9E%E8%87%AA%E5%8B%95%E6%A9%9F")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "纯扯淡", "2014-07-14")
	art.add_tag("emotion")
	art.add_p("又一个扯淡的周末晚上，价值观差异不小，完全理解，只是不认同，可能我这种才是最不好伺候的主儿吧，矫情巴拉地要什么心灵层平等的对话")
	art.add_p("工作4年多，最好吃的夜宵，真的还是玉泉门口的白粥锅贴")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "很久没动笔", "2014-08-05")
	art.add_tag("emotion")
	art.add_p("很久没动笔其实也是好事，说明过得比较充实，基本没有什么无病呻吟的时间。最近输入也确实比较多，但是需要过脑子整理成文，嗯，接下来就及时整理吧。")
	articles.insert(0,art)

	"""id = id + 1
	art = ClsArticle(id, "第一篇叽歪", "2014-06-26")
	art.add_tag("")
	art.add_p("")
	articles.insert(0,art)"""
	#
	return articles

class ClsArticle(object):
	"""docstring for ClsArticle"""
	def __init__(self, id, title, datetime):
		super(ClsArticle, self).__init__()
		self.id = "article_" + bytes(id)
		self.title = title
		self.datetime = datetime
		self.para_list = []
		self.tag_list = []
	def add_p(self, para):
		self.para_list.append(para)
	def add_tag(self, tag):
		self.tag_list.append(tag)
	def get_article(self):
		return self.para_list;