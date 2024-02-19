import pagerank as pr

DAMPING = 0.85
corpus = {"1": {"2", "3"}, "2":{"3", "1"}}
page = "1"
pr.transition_model(corpus, page, DAMPING)