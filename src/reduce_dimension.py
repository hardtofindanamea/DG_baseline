import pandas as pd
from model.reduce_dimension_mothed import reduce_dimension
import os

if __name__ == '__main__':
    df = pd.read_csv('../data/features/article2.csv')
    articles = []
    for i in range(df.shape[0]):
        articles.append(df.iloc[i,0])
    articles = [str(i) for i in articles]
    df = pd.read_csv('../data/features/word_seg2.csv')
    word_segs = []
    for i in range(df.shape[0]):
        word_segs.append(df.iloc[i,0])
    word_segs = [str(i) for i in word_segs]
    # for i in range(1,20):
    #     reduce_dimension('train_set_%d' % i,'train',articles,word_segs)
#    reduce_dimension('local_train','train',articles,word_segs)

    reduce_dimension('train_set','train',articles,word_segs)
