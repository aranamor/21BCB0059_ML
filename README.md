Caching Strategy: 
We used Redis as the caching solution because of its efficient in-memory key-value store, 
which ensures quick retrieval of cached results. Redis is ideal for 
tasks where rapid access and low latency are crucial. By caching search 
results, we avoid reprocessing identical queries, thus improving 
performance. We chose Redis over memcached because Redis supports more 
advanced data structures (like sets and hashes), which can be useful for
extending the system in the future.
