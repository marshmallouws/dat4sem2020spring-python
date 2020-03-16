# Webscraping

### Exercise 1
Data: https://www.amazon.com/s?k=%22Bee+Movie%22+dvd&ref=nb_sb_noss_2	
- Hent en liste på Bee Movie sælgere ud	
- Find den dyreste og billigste version der er tilgængelig.

### Exercise 2
https://www.dba.dk/soeg/?soeg=centurion+cykel	
- Hent en liste på alle centurion cykler ud og find den dyreste og den billigste Herre og damecykkel 	
- Er herrercykler dyrere end damecykler gennemsnitligt? 
- Er cyklerne billigere i jylland end på sjælland?

### Exercise 3

#### part 1
* You must first retrieve the top 100 scoring posts from [https://old.reddit.com/top/?sort=top&t=all](https://old.reddit.com/top/?sort=top&t=all). You will need to walk through multiple pages, using the `next` button.
* Save the links in a list of `Post` objects. The `Post` object must contain:
    * The id of the post.
    * The title of the post.
    * The exact score of the post.
    * The subreddit the post was submitted to. 

#### part 2

- What are the most popular subreddits in the top 100 posts?

* Find the frequency of all the subreddits in the 100 top posts. Store them in a dictionary where `subreddit=>frequency`.
* Sort the dictionary by descending value. 
* Plot the frequencies on a bar chart, where the `y`-axis is the frequency, and the `x`-axis is the subreddit name.

#### part 3

Search reddit using selenium.

Create a function that can retrieve the top `n` search results (posts) given a `search_term`.

```python
def search_reddit(search_term, n):
   pass
```

*remember to use `old.reddit.com` to aviod SPA.*

If you get stuck, you can check out our solution [here](https://github.com/Thomas-Rosenkrans-Vestergaard/thomas-kristoffer-assignment-solution).

### Exercise 4

https://www.kaggle.com/datasets
- Hent en liste med de 10 datasets der har størst vote-counts	
- Find navnet på det dataset, der har den mindste filstørrelse

### Exercise 5
https://apex.tracker.gg/apex/leaderboards	
- Find the top 10 players with the most kills on origin/pc	
- For each weapon type find the player with the most kills with that weapon

### Exercise 6
https://www.jobindex.dk	
- Hente data ned om jobopslag med python og et andet valgfrit kodesprog	
- Lav et plot der viser hvor mange jobopslag der er pr region mellem python og det andet kodesprog som blev valgt

### Exercise 7
https://www.dba.dk/mobil-og-telefoni/mobiltelefoner-og-tilbehoer/iphone/model-7/hukommelsegb-128/	
- Er der en sammenhæng mellem postnummer og pris på iPhone 7 128 GB på dba? (linket laver søgningen for dig)	
- Find top 10 postnumre med de højeste priser på denne iPhone.