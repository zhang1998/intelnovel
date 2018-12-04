from tools.tokenizer.wordCut import WordCut
mydict = ["mysenicdict.txt", "myfooddict.txt"]
file_path = '/home/zcy/haiNan/texttravelgen/data/clean_comments.txt' # 默认是精确模式
test = WordCut()
test.addDictionary(mydict) # 加载自定义词典 # 分词，去停用词（集成在类中了），不显示在console，保存分词后的文件到file_path目录
test.seg_file(file_path, show=False, write=True)


# 词频矩阵：矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer() # 统计每个词语的tf-idf权值
transformer = TfidfTransformer()
freq_word_matrix = vectorizer.fit_transform(corpus) #获取词袋模型中的所有词语
word = vectorizer.get_feature_names()
tfidf = transformer.fit_transform(freq_word_matrix) # 元素w[i][j]表示j词在i类文本中的tf-idf权重
weight = tfidf.toarray()z


# doc2vec #训练并保存模型
import gensim
sentences = gensim.models.doc2vec.TaggedLineDocument(token_path)
model = gensim.models.Doc2Vec(sentences, size=100, window=2, min_count=3)
model.train(sentences,total_examples=model.corpus_count, epochs=1000)
model.save('../model/demoDoc2Vec.pkl')


# K-means聚类
print 'Start K-means:'
from sklearn.cluster import KMeans
clf = KMeans(n_clusters=20)
s = clf.fit(model.docvecs)
print s #20个中心点
print(clf.cluster_centers_) #每个样本所属的簇
print(clf.labels_)
i = 1
while i <= len(clf.labels_):
    print i, clf.labels_[i-1]
    i = i + 1 #用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
print(clf.inertia_)









# dbscan 密度聚类
from sklearn.cluster import DBSCAN # Compute DBSCAN
db = DBSCAN(eps=0.005, min_samples=10).fit(weight)
print db.core_sample_indices_
db.labels_



from tools.labelMap.labelText import LabelText
label = clf.labels_
ori_path = "../data/clean_comments.txt"
labelAndText = LabelText(label, ori_path)
labelAndText.sortByLabel(write=True)
