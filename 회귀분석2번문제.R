getwd()
at = read.csv("AT2.txt",sep = "\t") #파일 불러오기

#데이터에 대한 값 조사
x = at[,2]
y = at[,3]
fit = lm(y ~ x)
su= summary(fit)
n = 23

y_bar = mean(y)
x_bar = mean(x)

#sxx와 syy Sxy구하기
Syy = 0
Sxx = 0
Sxy = 0

for(i in 1:n){
  Syy = Syy + (y[i] - y_bar) ^ 2
  Sxx = Sxx + (x[i] - x_bar) ^ 2
  Sxy = Sxy + (x[i] - x_bar)*(y[i] - y_bar)
}



#(b) b0와 b1 추정값
b0 = su$coefficients[,1][1] #답
b1 = su$coefficients[,1][2] #답



#(c) 시그마^2의 추정값 = residual standrd error이 sqrt(MSE) = 시그마의 추정이니 이 값을 제곱한다.
#residual standrd error = 8.955
se_hat = 8.955 ^2 #답


#(d) 가설검정 H0 : b0 = 0
#fit에서 intercept의 t value가 t검정통계량이다.
t_value_b0 = su$coefficients[1,3]
t_value_b0>qt(0.025,21,lower.tail = FALSE) #답 : FALSE가 나와서 유의수준 5%에서 기각 할 수 없다.


#(e) 가설검정 H0 : b1 = 0
#fit에서 x의 t value가 t검정통계량
t_value_b1 = su$coefficients[2,3]
t_value_b1>qt(0.025,21,lower.tail = FALSE) #답 : FALSE가 나와서 기각 할 수 없다.


#(f) 
#위에서 8.955 =sqrt(MSE)이니 MSE = 80.19
#MSE = SSE/n-2를 이용
#MSR = SSR / 자유도 = SSR
#F0은 fit에서 F_statistic 값이다.

MSE = 80.19 #답
SSE = MSE * (n-2) #답
SST = Syy #답
SSR = SST - SSE #답
MSR = SSR #답
F_value = 3.187 #답
# 답 : 자유도는 SSE_df <- 21 , SSR_df <- 1 , SST_df <- 22


#(g) fit에서 f값이 3.187이 나오고 p_value가 0.088이 나왔다. 따라서 
#유의수준 5%라고 한다면 p값보다 커서 기각 할 수 없다.
a  = 0.05
p_value = 0.088
p_value < a #답 : FALSE가 나와서 기각 할 수 없다.



#(h) b1에 있어서 95%의 신뢰구간 
#confint()를 이용
confint(fit)[2,] #답


#(i) b0에 대한 95% 신뢰구간
confint(fit)[1,] #답


#(j) x가 75라고 주어질때의 신뢰구간
#predict를 하면 특정 x일때의 y를 전부 구한다.
predict(fit)
newx = data.frame(x=75)
predict(fit,newx,interval = "confidence")[c(2,3)] #답


#(k) x가 75일때 새로운 y를 추정하기
#predict에서 interval를 predict로 하면 추정치와 신뢰구간을 얻을 수 있다.
predict(fit,newx,interval = "predict")[c(2,3)] #답


#(l) 결정계수 구하기
#결정계수 = 1 - (SSE/SST)
1 - (SSE/SST) #답
