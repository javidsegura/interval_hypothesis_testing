import scipy.stats as ss 


class Main:
      def __init__(self, mean, std,n ,tails,alpha  = 0.05):
            self.mean = mean
            self.std = std
            self.n = n
            self.tails = tails
            self.alpha = alpha
            self.confidence_level = self.__set_up() 
            self.raw_interval = self.get_raw_interval()
      def __set_up(self):
            if self.tails == "lower":
                  confidence_level = self.alpha
                  return confidence_level
            elif self.tails == "upper":
                  confidence_level = 1 - self.alpha
                  print(confidence_level)
                  return confidence_level
            elif self.tails == "two-sided":
                  lower = (1 - (1-self.alpha))/2
                  upper = 1 -lower 
                  confidence_level = (lower, upper)
                  return confidence_level
      def get_raw_interval(self):
            if self.tails == "two-sided":
                  lower = ss.norm.ppf(self.confidence_level[0])
                  upper = ss.norm.ppf(self.confidence_level[1])
                  return ((lower, upper))
            elif self.tails == "lower":
                  lower = ss.norm.ppf(self.confidence_level)
                  return (lower, "inf")
            elif self.tails == "upper":
                  upper = ss.norm.ppf(self.confidence_level)
                  return ("inf", upper)
      def get_num_interval(self):
            if self.tails == "two-sided":
                  se = self.std / ((self.n) ** .5)
                  lower = self.raw_interval[0] * (se) + self.mean
                  upper = self.raw_interval[1] * (se) + self.mean
                  return ((lower, upper))

            
try1 = Main(n = 210, mean = 49, std = .5, alpha = 0.05,tails="two-sided")

print(try1.get_num_interval())

