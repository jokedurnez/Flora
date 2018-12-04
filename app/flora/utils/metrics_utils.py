import statistics

def preprocess_metrics(metrics):
    dts = [x[0] for x in metrics]
    dts.sort()
    cutoff = dts[len(dts)-21]
    dts = [x[0] for x in metrics if x[0] > cutoff]
    names = ['acc_x', 'acc_y', 'acc_z']
    outdict = {}
    for idx, name in enumerate(names):
        acc = [x[idx+1] for x in metrics if x[0] > cutoff]
        acc_mn = statistics.mean(acc)
        acc_st = statistics.stdev(acc)
        acc_stdz = [(x-acc_mn)/acc_st for x in acc]
        outdict[name] = acc_stdz
    return outdict
