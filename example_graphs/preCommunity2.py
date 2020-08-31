'''
运行该代码，可以得到一个VBGMM_result.txt文件，里面包含了不同的参数及其对应的NMI指标的数值。
'''
import numpy as np
import itertools
from sklearn.mixture import BayesianGaussianMixture
from sklearn import metrics

filename = 'VBGMM_result.txt'
f = open(filename, 'a')
for i in [1, 3, 10, 30, 50, 90]:
    for j in [4, 8, 16, 32, 64, 128]:
        for k in [20, 40, 60, 80]:
            for l in range(5, 35, 5):
                dataset_name = str(i) + 'v' + str(j) + 'v' + str(k) + 'v' + str(l) + '.embeddings'
                labels_true = np.loadtxt('community(a).txt', dtype=int)
                labels_true = labels_true[:, 1]
                min_community = 40    # 假设的社区数目，实际数目小于这个数就可以
                expected_iter_times = 1000     ##若收敛，则自动停止
                color_iter = itertools.cycle(['navy', 'c', 'cornflowerblue', 'gold',
                                              'darkorange', 'blue', 'red', 'green', 'yellow', 'indigo'])

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
                maxscore, now_c = 0, 0
                model = BayesianGaussianMixture(n_components=min_community,  ####4 now_community
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
                label_pred = model.predict(data)  # label_pred=[] 错，多此一举
                pred_community = np.column_stack((num_list, label_pred))

                pred_community = pred_community[np.argsort(pred_community[:, 0])]
                labels_pred = pred_community[:, 1]
                score = metrics.normalized_mutual_info_score(labels_true, labels_pred)
                line = str(i) + 'v' + str(j) + 'v' + str(k) + 'v' + str(l) + ':' + str(score)
                f.writelines(line + '\n')

