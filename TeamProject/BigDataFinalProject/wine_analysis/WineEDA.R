df12<-read.csv("df12.csv")
head(df12)

library(dplyr)
df12 %>% 
  group_by(choice1) %>% 
  summarise(n=n())

gender<-df12 %>% 
  group_by(gender,choice1) %>% 
  summarise(n=n())

gender %>% 
  group_by(gender) %>% 
  mutate(total=sum(n),
         rate=(n/total)*100)

df12 %>% 
  filter(marital=="SINGLE") %>% 
  group_by(gender,choice1) %>% 
  summarise(n=n())

df12 %>% 
  group_by(gender) %>% 
  summarise(n=n())

df12 %>% 
  group_by(age) %>% 
  summarise(n=n())

aa<-df12 %>%
  group_by(age,choice1) %>% 
  summarise(n=n())

df12 %>% 
  group_by(gender,choice1) %>% 
  summarise(n=n())

a<-df12 %>% 
  group_by(area_grade,choice1) %>% 
  summarise(n=n())

df12 %>% 
  group_by(age) %>% 
  summarise(n=n())

library(car)
install.packages("gmodels")
library(gmodels)

chisq.test(df12$area_grade,df12$choice1)
CrossTable(df12$area_grade,df12$choice1)
help("CrossTable")

a<-df12 %>% 
  group_by(job,choice1) %>% 
  summarise(n=n())

df12 %>% 
  group_by(gender,job,choice1) %>% 
  filter(job=="학생") %>% 
  summarise(n=n()) %>% 
  arrange(desc(n))

df12$winelove<-df12$wineFrequency/df12$frequency  
summary(df12$winelove)

table(is.na(df12$winelove))

df12 %>% 
  filter(winelove>0.7) %>% 
  group_by(choice1) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n))

df12 %>% 
  filter(winelove>0.7) %>%
  group_by(gender,choice1) %>% 
  summarise(n=n()) %>%
  arrange(desc(n))

df12 %>% 
  group_by(prefer,choice1) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n))

chisq.test(df12$prefer,df12$choice1)
CrossTable(df12$prefer,df12$choice1)

a<-df12 %>% 
  group_by(side,choice1n,choice2n) %>% 
  summarise(n=n())

chisq.test(df12$side,df12$choice2n)
CrossTable(df12$prefer,df12$choice2n)

df12 %>%
  group_by(province) %>%
  summarise(n=n())

df12$choice1n<-ifelse(df12$choice1=='A'|df12$choice1=='F'|df12$choice1=='H'|df12$choice1=='G','1',
                      ifelse(df12$choice1=='B'|df12$choice1=='C','2','3'))

df12$choice2n<-ifelse(df12$choice2=='A'|df12$choice2=='F'|df12$choice2=='H'|df12$choice2=='G','1',
                      ifelse(df12$choice2=='B'|df12$choice2=='C','2','3'))


#####################################
df12$gender<-as.factor(df12$gender)
df12$age<-as.factor(df12$age)
df12$marital<-as.factor(df12$marital)

fit<-aov(winelove~area_grade+age,data=df12)
summary(fit)

##########################################
head(df12)
df<-df12[,10:14]
head(df)
df<-df[,-2]

write.csv(df,"df.csv", quote = FALSE, row.names = TRUE)
library(arules)
df12ss<- read.transactions('df.csv', format = 'basket', sep=',')
summary(df12ss)  

association.rules <- apriori(df12ss, parameter = list(supp=0.01,conf=0.1,maxlen=3))
inspect(association.rules)

#######################################
basket<- read.transactions('what_about_this.csv', format = 'basket', sep=',')
summary(basket) 
association.rules <- apriori(basket, parameter = list(supp=0.01,maxlen=3))
association.rules <- apriori(basket, parameter = list(supp=0.001,conf=1,maxlen=2),appearance=list(rhs="Cabernet Sauvignon"))
association.rules <- apriori(basket, parameter = list(supp=0.01,conf=0.1,maxlen=2),appearance=list(lhs="Prosecco Sparkling Wine"))
aa<-inspect(association.rules)

help(apriori)

#inspect(head(coms, 2))
########################################
basket<- read.transactions('짬좀그만시켜요.csv', format = 'basket', sep=',')
summary(basket) 
association.rules <- apriori(basket, parameter = list(supp=0.01,maxlen=3))
association.rules <- apriori(basket, parameter = list(supp=0.001,conf=1,maxlen=2),appearance=list(rhs="Prosecco Sparkling Wine"))
association.rules <- apriori(basket, parameter = list(supp=0.01,conf=0.1,maxlen=2),appearance=list(lhs="Prosecco Sparkling Wine"))
abcd<-inspect(association.rules)
########################################
basket<- read.transactions('group4_parsed_in_twilight.csv', format = 'basket', sep=',')
summary(basket) 
inspect(basket[1:7])
itemFrequency(basket[,1:8])

association.rules <- apriori(basket, parameter = list(supp=0.1,maxlen=3))
association.rules <- apriori(basket, parameter = list(supp=0,conf=0,maxlen=5),appearance=list(lhs="5"))
association.rules <- apriori(basket, parameter = list(supp=0.01,conf=0.1,maxlen=2),appearance=list(lhs="Prosecco Sparkling Wine"))
inspect(association.rules)
#######################################
basket1<- read.transactions('30minutes_of_parsing.csv', format = 'basket', sep=',')
summary(basket1) 
inspect(basket1[1:7])
itemFrequency(basket1[,1:8])

dhassociation.rules <- apriori(basket1, parameter = list(supp=0.1,maxlen=3))
association.rules <- apriori(basket1, parameter = list(supp=0,conf=0,maxlen=3),appearance=list(lhs="5"))
association.rules <- apriori(basket1, parameter = list(supp=0.01,conf=0.1,maxlen=2),appearance=list(lhs="Prosecco Sparkling Wine"))
a<-inspect(association.rules)
############################################
basket<- read.transactions('30minutes_of_parsing2.csv', format = 'basket', sep=',')
summary(basket) 
inspect(basket[1:7])
itemFrequency(basket[,1:8])

dhassociation.rules <- apriori(basket, parameter = list(supp=0.1,maxlen=3))
association.rules <- apriori(basket, parameter = list(supp=0,conf=0,maxlen=1),appearance=list(lhs={}))
association.rules <- apriori(basket, parameter = list(supp=0.01,conf=0.1,maxlen=2),appearance=list(lhs="Prosecco Sparkling Wine"))
a<-inspect(association.rules)






sales<-read.csv("wine_data_sales_new.csv")

table(is.na(sales))

sales %>% 
  group_by(gender,age) %>% 
  summarise(n=n())

sales %>% 
  group_by(age) %>% 
  summarise(n=n())

sales %>% 
  group_by(gender) %>% 
  summarise(n=n())

df12s<-df12s %>% 
  mutate(class=ifelse(choice2=='A'|choice2=='F'| choice2=='H' | choice2=='G','1',
                      ifelse(choice2=='B'|choice2=='C','2','3')))
a<-df12s %>% 
  group_by(side,class) %>% 
  summarise(n=n())
a$num<-ifelse(a$class=='1',4,
                  ifelse(a$class=='2',2,2))
a$avg<-a$n/a$num

df12 %>% 
  group_by(gender,choice1) %>%
  summarise(n=n())
  

df12 %>% 
  filter(marital=='SINGLE') %>% 
  group_by(gender,choice1) %>% 
  summarise(n=n())

df12 %>% 
  filter(job=="자영업" ) %>% 
  group_by(gender, choice1) %>% 
  summarise(n=n())

df12 %>% 
  filter(job=="자영업")
#sales female male count
sales %>% 
  group_by(gender) %>% 
  summarise(n=n())

sales %>% 
  group_by(age) %>% 
  summarise(n=n())

sales %>% 
  group_by(gender,age) %>% 
  summarise(n=n())

sales %>% 
  group_by(age) %>% 
  summarise(n=n(),
            mean=mean(amount))
