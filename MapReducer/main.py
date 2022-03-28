from statistics import mean
from mrjob.job import MRJob
from mrjob.step import MRStep

class Rating(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
        ]
    
    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, int(rating)
        
    def reducer_count_ratings(self, key, values):
        yield key, mean(values)
        
        
if __name__ == '__main__':
    Rating.run()