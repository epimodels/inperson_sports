#################################################################
# Statistical Analysis of COVID-19 in In-person Sporting Events #
#################################################################

## Import Packages and Import Data
library(vioplot)

# Main Scenarios
fb <- as.data.frame(read.csv(("wsu_football.csv")))

fb$ScenarioFactor<- as.character(fb$Scenario)

CasesTest <- kruskal.test(fb$Cases ~ fb$ScenarioFactor)

print(CasesTest)

pairwise.wilcox.test(fb$Cases,fb$ScenarioFactor,
                     p.adjust.method = "BH")

low_control <- subset(fb,ScenarioFactor=="0")
high_control <- subset(fb,ScenarioFactor=="1")
lowbeta_lowprev_lowmix <- subset(fb,ScenarioFactor=="2")
lowbeta_lowprev_highmix <- subset(fb,ScenarioFactor=="3")
lowbeta_highprev_lowmix <- subset(fb,ScenarioFactor=="4")
lowbeta_highprev_highmix <- subset(fb,ScenarioFactor=="5")

highbeta_highprev_lowmix <- subset(fb,ScenarioFactor=="6")
highbeta_highprev_highmix <- subset(fb,ScenarioFactor=="7")
highbeta_lowprev_lowmix <- subset(fb,ScenarioFactor=="8")
highbeta_lowprev_highmix <- subset(fb,ScenarioFactor=="9")

par(mfrow=c(1,1))
vioplot(low_control$Cases,high_control$Cases,names=c("Control - R0 < 1","Control - R0 > 1"),col="Grey90",drawRect=FALSE)
title(ylab="Cumulative COVID-19 Cases",cex.lab=1.5)
title(xlab="Scenario",cex.lab=1.5)
segments(0.75,median(low_control$Cases),1.25,median(low_control$Cases),col="black",lwd=3)
segments(1.75,median(high_control$Cases),2.25,median(high_control$Cases),col="black",lwd=3)
legend("topright", c("Scenario Median"), lwd=3,col=c("black"),lty=1, bty='n', cex=1.25)

vioplot(low_control$Cases,lowbeta_lowprev_lowmix$Cases,lowbeta_lowprev_highmix$Cases,col="Grey90",drawRect=FALSE,names=c("Control - Ro <1", "Low Prevalence/Low Mixing", "Low Prevalence/High Mixing"))
title(ylab="Cumulative COVID-19 Cases",cex.lab=1.5)
title(xlab="Scenario",cex.lab=1.5)
segments(0.75,median(low_control$Cases),1.25,median(low_control$Cases),col="black",lwd=3)
segments(1.75,median(lowbeta_lowprev_lowmix$Cases),2.25,median(lowbeta_lowprev_lowmix$Cases),col="black",lwd=3)
segments(2.75,median(lowbeta_lowprev_highmix$Cases),3.25,median(lowbeta_lowprev_highmix$Cases),col="black",lwd=3)
legend("topright", c("Scenario Median"), lwd=3,col=c("black"),lty=1, bty='n', cex=1.25)

vioplot(low_control$Cases,lowbeta_highprev_lowmix$Cases,lowbeta_highprev_highmix$Cases,col="Grey90",drawRect=FALSE,names=c("Control - Ro <1", "High Prevalence/Low Mixing", "High Prevalence/High Mixing"))
title(ylab="Cumulative COVID-19 Cases",cex.lab=1.5)
title(xlab="Scenario",cex.lab=1.5)
segments(0.75,median(low_control$Cases),1.25,median(low_control$Cases),col="black",lwd=3)
segments(1.75,median(lowbeta_highprev_lowmix$Cases),2.25,median(lowbeta_highprev_lowmix$Cases),col="black",lwd=3)
segments(2.75,median(lowbeta_highprev_highmix$Cases),3.25,median(lowbeta_highprev_highmix$Cases),col="black",lwd=3)
legend("topright", c("Scenario Median"), lwd=3,col=c("black"),lty=1, bty='n', cex=1.25)

vioplot(high_control$Cases,highbeta_lowprev_lowmix$Cases,highbeta_lowprev_highmix$Cases,col="Grey90",drawRect=FALSE,names=c("Control - Ro >1", "Low Prevalence/Low Mixing", "Low Prevalence/High Mixing"))
title(ylab="Cumulative COVID-19 Cases",cex.lab=1.5)
title(xlab="Scenario",cex.lab=1.5)
segments(0.75,median(high_control$Cases),1.25,median(high_control$Cases),col="black",lwd=3)
segments(1.75,median(highbeta_lowprev_lowmix$Cases),2.25,median(highbeta_lowprev_lowmix$Cases),col="black",lwd=3)
segments(2.75,median(highbeta_lowprev_highmix$Cases),3.25,median(highbeta_lowprev_highmix$Cases),col="black",lwd=3)
legend("topright", c("Scenario Median"), lwd=3,col=c("black"),lty=1, bty='n', cex=1.25)

vioplot(high_control$Cases,highbeta_highprev_lowmix$Cases,highbeta_highprev_highmix$Cases,col="Grey90",drawRect=FALSE,names=c("Control - Ro >1", "HighPrevalence/Low Mixing", "High Prevalence/High Mixing"))
title(ylab="Cumulative COVID-19 Cases",cex.lab=1.5)
title(xlab="Scenario",cex.lab=1.5)
segments(0.75,median(high_control$Cases),1.25,median(high_control$Cases),col="black",lwd=3)
segments(1.75,median(highbeta_highprev_lowmix$Cases),2.25,median(highbeta_highprev_lowmix$Cases),col="black",lwd=3)
segments(2.75,median(highbeta_highprev_highmix$Cases),3.25,median(highbeta_highprev_highmix$Cases),col="black",lwd=3)
legend("topright", c("Scenario Median"), lwd=3,col=c("black"),lty=1, bty='n', cex=1.25)

median(low_control$Cases)
median(high_control$Cases)

median(lowbeta_lowprev_lowmix$Cases)
median(lowbeta_lowprev_highmix$Cases)

median(lowbeta_highprev_lowmix$Cases)
median(lowbeta_highprev_highmix$Cases)

median(highbeta_lowprev_lowmix$Cases)
median(highbeta_lowprev_highmix$Cases)

median(highbeta_highprev_lowmix$Cases)
median(highbeta_highprev_highmix$Cases)

# Sensitivity Analysis
# Base Parameter Model Analysis
sweep <- read.csv("football_sweep.csv", header = T, sep = ",")

quantile(sweep$Ratio, c(0.25,0.50,0.75))

global_model <- lm(Ratio ~ Sigma + Gamma + Alpha + Delta_I + Delta_A,data=sweep)

summary(global_model)

## Plot Sensitivity ##

coefficients <- global_model$coefficients[2:6]*0.1

cols <- c("grey90", "grey50")[(coefficients < 0) + 1]  

greek_names <- c(expression(sigma),expression(gamma),expression(alpha),expression(delta[I]),expression(delta[A]))

barplot(coefficients,horiz=TRUE,names.arg=greek_names,main="",ylab="Parameter",
        xlab="Change in Cumulative Acquisition Ratio",cex.main=1.25,cex.lab=1.5,cex.axis=1.5,cex.names=1.75,
        xlim = c(-3,3),col=cols)


# Beta Sensitivity
beta_sweep <- read.csv("football_beta_sweep.csv", header = T, sep = ",")
beta_sweep$rescaled_ratio <- beta_sweep$mix_ratio*100

beta_fit <- glm(cases ~ rescaled_ratio,family="poisson",data=beta_sweep)

summary(beta_fit)
ratio.grid<-seq(from=0, to = 100)
pred_fit <- exp(predict(beta_fit,newdata = list(rescaled_ratio=ratio.grid)))

plot(beta_sweep$rescaled_ratio,beta_sweep$cases,pch=21,col="grey80",bg="grey80",ylab="COVID-19 Cases",xlab="Relative Mixing Rate")
points(ratio.grid,pred_fit,col="darkred",lwd=3,type="l")

legend("topleft", c("Poisson Fit","Individual Simulation"), 
       lwd=c(3,NA),pch=c(NA,21),pt.cex=c(1,1),col=c("darkred","grey80"),pt.bg=c(NA,"grey80"),lty=c(1,NA), bty='n', cex=1.1)