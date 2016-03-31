library(effsize)

digs = read.csv("mean_igs.csv")
dnor = read.csv("mean_nor.csv")

tes <- wilcox.test(dnor[,1], digs[,1])
cat("WILCOX, IGS: ",tes$p.value,"\n")

tes <- cliff.delta(dnor[,1], digs[,1], conf.level=.99)
cat("CLIFF DELTA, IGS: ", tes$estimate,"\n")
