import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import xlrd
import itertools
from sklearn.utils import shuffle
from scipy import linalg
from sklearn.mixture import BayesianGaussianMixture
from sklearn import metrics
import time


dataset_name = '30v8v80v10.embeddings'  # 10v32v40v20
labels_true = np.loadtxt('community(a).txt', dtype=int)
labels_true = labels_true[:, 1]
min_community = 34    # 迭代开始的次数
max_community = 1000   # 迭代结束的社区数目
expected_iter_times = 1000     ##若收敛，则自动停止
color_iter = itertools.cycle(['navy', 'c', 'cornflowerblue', 'gold',
                              'darkorange','blue','red','green','yellow','indigo'])

dataset = []
with open(dataset_name) as f:
    for line in f:
        elem=line.strip('\n')
        elem=elem.split(' ')
        if len(elem) == 2:
            pass
        else:
            dataset.append(elem)

dataset = np.array(dataset)
dataset = dataset.astype(np.float)

num_list = dataset[:,0]
data = dataset[:,1:]

# def plot_results(X, Y_, means, covariances, index, title):
#     splot = plt.subplot(1, 1, 1 + index)
#     for i, (mean, covar, color) in enumerate(zip(
#             means, covariances, color_iter)):
#         v, w = linalg.eigh(covar)
#         v = 2. * np.sqrt(2.) * np.sqrt(v)
#         u = w[0] / linalg.norm(w[0])
#         # as the DP will not use every component it has access to
#         # unless it needs it, we shouldn't plot the redundant
#         # components.
#         if not np.any(Y_ == i):
#             continue
#         plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], .8, color=color)
#
#         # Plot an ellipse to show the Gaussian component
#         angle = np.arctan(u[1] / u[0])
#         angle = 180. * angle / np.pi  # convert to degrees
#         ell = mpl.patches.Ellipse(mean, v[0], v[1], 180. + angle, color=color)
#         ell.set_clip_box(splot.bbox)
#         ell.set_alpha(0.5)
#         splot.add_artist(ell)
#
#     plt.title(title)
#     plt.show()


maxscore, now_c = 0, 0
for now_community in range(min_community,max_community+1, 1):
    model = BayesianGaussianMixture(n_components=now_community,  ####4
                                    covariance_type="full",
                                    # reg_covar=0,   去掉提高了0.01
                                    max_iter=expected_iter_times,  # 100
                                    init_params="random",
                                    random_state=5,
                                    weight_concentration_prior_type="dirichlet_distribution",
                                    # weight_concentration_prior=1e-2,
                                    # mean_precision_prior=.8,
                                    verbose=0, verbose_interval=10, warm_start=True)  # 0.259

    model.fit(data)
    label_pred = model.predict(data)  # label_pred=[]，多此一举
    pred_community = np.column_stack((num_list, label_pred))

    pred_community = pred_community[np.argsort(pred_community[:, 0])]
    labels_pred = pred_community[:, 1]

    if metrics.normalized_mutual_info_score(labels_true, labels_pred) > maxscore:
        maxscore = metrics.normalized_mutual_info_score(labels_true, labels_pred)
        now_c = now_community
        print(now_c, maxscore)

    # plot_results(data, model.predict(data), model.means_, model.covariances_, 0, 'VBGMM')
