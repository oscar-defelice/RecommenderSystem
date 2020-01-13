# Recommender System
This repository contains some code to implement a recommender system.

## Introduction
Given the constant rise of dating related apps - such as Tinder, Lovoo, Hitch - the algorithms for recommending new users have got a lot more complex. In a market with such a low entry barrier, suggesting users that are more likely to yield matches is for sure an important competitive edge.

Not only dating apps could benefit of such a system. Indeed, nowadays the existence of places collecting different industries - like co-working spaces, startup hubs, etc. - is becoming more and more frequent in our cities.

A user recommender system (where _the things to be recommended_ are users itself) can face issues from both of these applications.

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
