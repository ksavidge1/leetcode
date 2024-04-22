"""
933. Number of recent calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:
 * RecentCounter() Initializes the counter with zero recent requests.
 * int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
   and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).

Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

"""


class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        while t - self.queue[0] > 3000:
            self.queue.pop(0)

        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


obj = RecentCounter()
times = [[1], [100], [3001], [3002]]

num_recents = []
for i in times:
    recents = obj.ping(i[0])
    num_recents.append(recents)

print(f"Number of calls in last 3000ms, for each call to ping: {num_recents}")
