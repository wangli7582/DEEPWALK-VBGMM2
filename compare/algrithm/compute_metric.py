from sklearn import metrics
import numpy as np
import GN
import Louvain

dataset_path = '../network/network(a).txt'
labels_true = np.loadtxt('../network/community(a).txt')
labels_true = labels_true[:, 1]


GN_pred = np.array(GN.gn(dataset_path))
# louvain_pred = np.array(Louvain.louvian(dataset_path))


print "GN:", metrics.normalized_mutual_info_score(labels_true, GN_pred)
# print "louvain:", metrics.normalized_mutual_info_score(labels_true, louvain_pred)



