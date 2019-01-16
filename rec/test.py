import pandas as pd
if __name__ == '__main__':
    u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    users = pd.read_csv('C:/Users/Administrator/PycharmProjects/rec/data/u.user', sep='|', names=u_cols, encoding='latin-1')

    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    ratings = pd.read_csv('C:/Users/Administrator/PycharmProjects/rec/data/u.data', sep='\t', names=r_cols, encoding='latin-1')

    m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
    movies = pd.read_csv('C:/Users/Administrator/PycharmProjects/rec/data/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')
    movie_ratings = pd.merge(movies, ratings)
    lens = pd.merge(movie_ratings, users)
    most_rated = lens.groupby('title').size().sort_values(ascending=False)[:20]
    print(users.head(n=50))
    print(ratings.head(n=50))
    # print(users.dtypes)
    # print(most_rated)
    # print(ratings['rating'])
    # for i in ratings['rating']:
    #     print(i)
    # print(ratings[(ratings.movie_id ==22)])



    # print(users.index[2])
    # print(ratings[(ratings.index == 22)])
    # print(ratings[(ratings.index ==22)]['rating'])
    # print(ratings.shape)
    # print(ratings.info)
    # print(ratings.dtypes)
    # print(ratings.loc[3])
    # a=ratings.loc[3];
    # print(a.user_id )
    # print(ratings.iloc[0:10]);
    # b=ratings.iloc[0:10]
    #
    # print(b)
    #
    # list=[]
    # for num in range(0,10):
    #     a=ratings.loc[num]
    #     list.append(a)
    #
    #
    # for o in list:
    #     print(o.user_id)


