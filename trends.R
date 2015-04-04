file <- "mlb2014.csv"
data <- read.csv(file)
colnames(data) <- c("Player","Team","MLB","Spring")
fit <-lm(MLB ~ Spring, data=data)
summary(fit)

library(plyr)
models <- dlply(data,"Team",function(df) lm(MLB ~ Spring, data=df))
ldply(models,coef)
x<- ldply(models,coef)
write.table(x,file="team_trends")
