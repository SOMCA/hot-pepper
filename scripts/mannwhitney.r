library(effsize)


cat("\n GFX \n")

orig = read.csv("gfx_org_one.csv")
igs = read.csv("gfx_igs_one.csv")
mim = read.csv("gfx_mim_one.csv")
hmu = read.csv("gfx_hmu_one.csv")
all = read.csv("gfx_all_one.csv")

tes <- wilcox.test(orig[,1], igs[,1])
cat("IGS, ",tes$p.value,"\n")

tes <- wilcox.test(orig[,1], mim[,1])
cat("MIM, ",tes$p.value,"\n")

tes <- wilcox.test(orig[,1], hmu[,1])
cat("HMU, ",tes$p.value,"\n")

tes <- wilcox.test(orig[,1], all[,1])
cat("ALL, ",tes$p.value,"\n")

tes <- wilcox.test(igs[,1], all[,1])
cat("IGS ALL, ",tes$p.value,"\n")

tes <- wilcox.test(mim[,1], all[,1])
cat("MIM ALL, ",tes$p.value,"\n")

tes <- wilcox.test(hmu[,1], all[,1])
cat("HMU ALL, ",tes$p.value,"\n")

gc_o=c(866,438,433,432,435,436,434,437,847,437,431,436,437,437,438,438,435,437,436,433,438,858,437,437,436,435,440,441,438,437,436,433,437,436,452,439,439,438,437,436,437,437,436,433,433,436,439,438,848,437,433,431,853,436,432,853,437,449,439,436)
gc_i=c(853,431,852,442,442,443,441,445,442,443,442,577,436,448,442,443,443,442,445,444,445,442,443,444,450,855,443,443,444,443,449,441,442,444,443,444,445,852,444,444,444,472,443,448,443,443,447,853,443,446,445,847,443,445,444,853,442,442,443,462)
gc_m=c(442,443,443,444,445,444,445,443,446,445,442,444,434,850,471,445,444,442,852,444,442,444,446,445,464,444,449,443,445,452,445,446,444,444,854,446,444,443,445,446,446,444,445,446,444,445,457,441,455,457,487,445,443,449,853,444,444,446,446,446)
gc_h=c(454,445,448,854,442,440,444,443,443,444,447,446,442,443,444,438,441,442,440,445,448,438,444,452,445,446,436,447,451,468,442,443,442,442,444,457,444,445,463,453,467,447,448,452,448,446,459,450,451,860,449,448,449,859,450,451,449,458,450,448)
gc_a=c(465,447,434,856,447,445,447,447,448,447,449,449,858,446,446,445,447,446,446,451,448,452,449,448,446,446,447,446,449,449,447,446,447,446,447,448,447,448,447,446,449,448,445,447,448,855,448,447,448,449,447,446,446,447,451,449,457,451,448,447)


cat("\n MEM \n")
dorig = read.csv("dump_o_one.csv")
digs = read.csv("dump_igs_one.csv")
dmim = read.csv("dump_mim_one.csv")
dhmu = read.csv("dump_hmu_one.csv")
dall = read.csv("dump_all_one.csv")

tes <- wilcox.test(dorig[,1], digs[,1])
cat("IGS, ",tes$p.value,"\n")

tes <- wilcox.test(dorig[,1], dmim[,1])
cat("MIM, ",tes$p.value,"\n")

tes <- wilcox.test(dorig[,1], dhmu[,1])
cat("HMU, ",tes$p.value,"\n")

tes <- wilcox.test(dorig[,1], dall[,1])
cat("ALL, ",tes$p.value,"\n")

tes <- wilcox.test(digs[,1], dall[,1])
cat("IGS ALL, ",tes$p.value,"\n")

tes <- wilcox.test(dmim[,1], dall[,1])
cat("MIM ALL, ",tes$p.value,"\n")

tes <- wilcox.test(dhmu[,1], dall[,1])
cat("HMU ALL, ",tes$p.value,"\n")

cat("\n GC \n")


tes <- cliff.delta(gc_i, gc_o, conf.level=.99)
cat("IGS O,",tes$estimate,"\n")

tes <- cliff.delta(gc_m, gc_o, conf.level=.99)
cat("MIM O,",tes$estimate,"\n")

tes <- cliff.delta(gc_h, gc_o, conf.level=.99)
cat("HMU O,",tes$estimate,"\n")

tes <- cliff.delta(gc_a, gc_o, conf.level=.99)
cat("ALL O,",tes$estimate,"\n")

tes <- cliff.delta(gc_a, gc_i, conf.level=.99)
cat("ALL IGS,",tes$estimate,"\n")

tes <- cliff.delta(gc_a, gc_m, conf.level=.99)
cat("ALL MIM,",tes$estimate,"\n")

tes <- cliff.delta(gc_a, gc_h, conf.level=.99)
cat("ALL HMU,",tes$estimate,"\n")


df_o =c(75, 42, 54, 53, 56, 76, 78, 46, 55, 65, 51, 51, 68, 67, 60, 53, 52, 55, 52, 49, 61, 64, 76, 64, 77, 63, 36, 69, 45, 55, 79, 69, 64, 67, 69, 70, 59, 53, 54, 69, 86, 60, 54, 58, 79, 57, 55, 40, 75, 52, 61, 70, 73, 56, 60, 62, 69, 51, 60, 62)
df_i = c(58, 49, 39, 54, 34, 36, 42, 82, 46, 75, 63, 54, 69, 49, 49, 66, 41, 38, 42, 54, 69, 67, 45, 61, 59, 47, 38, 60, 52, 41, 37, 38, 56, 53, 54, 55, 62, 54, 62, 45, 54, 54, 59, 51, 79, 83, 43, 51, 88, 65, 75, 37, 50, 60, 67, 55, 83, 60, 47, 37)
df_m = c(54, 72, 79, 79, 46, 62, 44, 49, 60, 78, 75, 62, 64, 35, 70, 51, 68, 46, 78, 48, 42, 32, 30, 47, 62, 50, 61, 42, 43, 41, 30, 53, 63, 57, 29, 56, 82, 49, 55, 47, 67, 49, 61, 48, 54, 56, 52, 56, 39, 50, 33, 55, 66, 59, 43, 48, 79, 85, 62, 34)
df_h = c(88, 62, 56, 69, 81, 37, 57, 45, 55, 64, 65, 64, 64, 58, 54, 70, 65, 50, 49, 75, 72, 73, 46, 59, 51, 57, 44, 67, 38, 53, 82, 54, 67, 56, 65, 70, 45, 49, 53, 39, 61, 55, 53, 56, 46, 54, 66, 42, 61, 39, 52, 85, 42, 46, 46, 63, 47, 55, 66, 29)
df_a = c(45, 52, 51, 54, 72, 46, 48, 52, 41, 62, 46, 48, 36, 43, 58, 62, 61, 57, 62, 83, 42, 59, 44, 47, 58, 57, 52, 44, 48, 46, 60, 55, 43, 45, 72, 61, 60, 63, 53, 45, 72, 50, 66, 65, 68, 66, 48, 59, 41, 49, 43, 44, 54, 67, 54, 48, 43, 80, 53, 61)


cat("\n DF \n")

tes <- cliff.delta(df_i, df_o, conf.level=.99)
cat("IGS O,",tes$estimate,"\n")

tes <- cliff.delta(df_m, df_o, conf.level=.99)
cat("MIM O,",tes$estimate,"\n")

tes <- cliff.delta(df_h, df_o, conf.level=.99)
cat("HMU O,",tes$estimate,"\n")

tes <- cliff.delta(df_a, df_o, conf.level=.99)
cat("ALL O,",tes$estimate,"\n")

tes <- cliff.delta(df_a, df_i, conf.level=.99)
cat("ALL IGS,",tes$estimate,"\n")

tes <- cliff.delta(df_a, df_m, conf.level=.99)
cat("ALL MIM,",tes$estimate,"\n")

tes <- cliff.delta(df_a, df_h, conf.level=.99)
cat("ALL HMU,",tes$estimate,"\n")

