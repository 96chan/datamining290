from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

# function of compute jaccard coefficient
# source: http://love-python.blogspot.com/2012/07/python-code-to-compute-jaccard-index.html
def compute_jaccard_index(set_1, set_2):
    return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2))) 


# UserSimilarity MRJob
class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def extract_user(self, _, record):
        if record['type'] == 'review':
            yield [record['user_id'],record['business_id']]

    def count_business(self, user_id, biz_ids):
        unique_biz_id = set(biz_ids)
        yield [user_id, list(unique_biz_id)]

    def aggregate_jc(self, user_id, biz_ids):
        yield ["JC", [user_id,biz_ids]]

    def calculate_jc(self, stat, user_biz_id):
        container = []  # for containing all pairs of user_id, biz_id
        
        for pair in user_biz_id:
            container.append(pair)
        
        # calculate jaccard similarity coefficient
        for i, ub in enumerate(container):
            for j, ub_ in enumerate(container):                
                if ub[0] != ub_[0] and i < j:  # prevent from duplicating user_id pair
                    jc = compute_jaccard_index(set(ub[1]),set(ub_[1]))
                    if jc >= 0.5:
                        yield [(ub[0],ub_[0]),jc]
        
    def steps(self):
        return [self.mr(self.extract_user,self.count_business),
                   self.mr(self.aggregate_jc,self.calculate_jc)]

if __name__ == '__main__':
    UserSimilarity.run()
