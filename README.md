# Recommender System
This repository contains some code to implement a recommender system.

## Introduction

A recommendation system is basically an information filtering system that seeks to predict the "rating" or "preference" a user would give to an item. It is widely used in different internet / online business such as Amazon, Netflix, Spotify, or social media like Facebook and Youtube. By using recommender systems, those companies are able to provide better or more suited products/services/contents that are personalized to a user based on his/her historical consumer behaviors

Recommender systems typically produce a list of recommendations through collaborative filtering or through content-based filtering.

This project will focus on collaborative filtering and use item-based collaborative filtering systems make users recommendation. In other words, the _things to be recommended_ are the users themselves.

Indeed, given the constant rise of dating related apps - such as Tinder, Lovoo, Hitch - the algorithms for recommending new users have got a lot more complex. In a market with such a low entry barrier, suggesting users that are more likely to yield matches is for sure an important competitive edge.

Not only dating apps could benefit of such a system. Indeed, nowadays the existence of places collecting different industries - like co-working spaces, startup hubs, etc. - is becoming more and more frequent in our cities.

## Installation instructions

To not mess up with versioning and package installation, we strongly advice to create a virtual environment.
One can follow [this guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) and the suitable section according to the OS.

Once the virtual environment has been set up, as usual, one has to run the following instruction from a command line

```bash
pip install -r requirements.txt
```

This installs all the packages the code in this repository needs.

## Data description

### Dataframes

We would like to satisfy a twofold requirement. First, just because of scientific interest, we consider the application of distributed computing like [Spark](https://spark.apache.org/) to handle data.
Second, in order to stay general in our discussion and to be able to apply the system to different contexts - as described above - we can take into account data spread in two dataframes:
1. Users features (user id, features);
2. Users ratings (user1, user2, rating).

We are going to use the first one to calculate similarities between users, while the second one will be useful to train the model and predict new ratings.

### Data sources

#### Love dataset

Following such requirements, initially we make use of [_LibimSeTi_](https://libimseti.cz/) data (a famous Czech dating website).

Files contain $17\,359\,346$ rows corresponding to anonymous ratings of $168\,791$ profiles made by $135\,359$ users.

#### Co-Working dataset

Another dataset satisfying our requirements is the one coming from profiles of professionals in co-working spaces.

This dataset contains $18\,647$ ratings of $2\,045$ users with their features.

## KNN collaborative filtering

In this project, we will build an item-based collaborative filtering system using Users datasets.
Specifically, we will train a KNN model to cluster similar users based on user's ratings and make user recommendation based on similarity score of previous rated profiles.

#### Item-based Collaborative Filtering
Collaborative filtering based systems use the actions of users to recommend other items. In general, they can either be user based or item based. User based collaborating filtering uses the patterns of users similar to me to recommend a product (users like me also looked at these other items). Item based collaborative filtering uses the patterns of users who browsed the same item as me to recommend me a product (users who looked at my item also looked at these other items). Item-based approach is usually preferred than user-based approach. User-based approach is often harder to scale because of the dynamic nature of users, whereas items usually don't change much, so item-based approach often can be computed offline.

The idea is - in the first phase - to train an unsupervised model to make predictions, only based on user similarities.

## ALS and supervised recommendations

At this stage, we want to take advantage of the given matches to train a supervised model.

What we would like to do is to create a so-called utility matrix $\rho$  where each entry ( 0  or  1 ) according to the match of the user in the row with the user in the column.

This will be a very sparsed matrix.
To cope with such a set of data we need to implement an algorithm able to deal with matrix factorisation. This is precisely what the __ALS__ (Alternating Least Square) algorithm does.

Alternating Least Square (ALS) is also a matrix factorization algorithm and it runs itself in a parallel fashion. ALS is implemented in _Apache Spark ML_ and built for a larges-scale collaborative filtering problems. ALS is doing a pretty good job at solving scalability and sparseness of the Ratings data, and it’s simple and scales well to very large datasets.
Some high-level ideas behind ALS are:

* Its objective function is slightly different than Funk SVD: ALS uses L2 regularization while Funk uses L1 regularization

* Its training routine is different: ALS minimizes two loss functions alternatively; It first holds user matrix fixed and runs gradient descent with item matrix; then it holds item matrix fixed and runs gradient descent with user matrix

* Its scalability: ALS runs its gradient descent in parallel across multiple partitions of the underlying training data from a cluster of machines

Just like other machine learning algorithms, ALS has its own set of hyper-parameters. We probably want to tune its hyper-parameters via some form of validation, _e.g._ __cross-validation__.

The most important hyper-parameters in Alternating Least Square (ALS) are the following ones.

1. `maxIter`: the maximum number of iterations to run (defaults to 10)
2. `rank`: the number of latent factors in the model (defaults to 10)
3. `regParam`: the regularization parameter in ALS (defaults to 1.0)

Hyper-parameter tuning is a highly recurring task in many machine learning projects.
