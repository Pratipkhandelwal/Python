model1 = LassoCV(eps=1e-7)
## model training and prediction
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

model2 = LinearRegression()
## model training and prediction
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)

model3 = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=4, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10, 
                                   loss='huber', random_state =5)
## model training and prediction
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

model4 = xgb.XGBRegressor(colsample_bytree=0.2, gamma=0.0, 
                             learning_rate=0.05, max_depth=6, 
                             min_child_weight=1.5, n_estimators=7200,
                             reg_alpha=0.9, reg_lambda=0.6,
                             subsample=0.2,seed=42, silent=1)
## model training and prediction
model4.fit(X_train, y_train)
pred4 = model4.predict(X_test)

pred = (pred1+pred2+pred3+pred4)/4
# model performance
print("Ensemble model:\n")
print("r2_score: " + str(r2_score(pred, y_test.values)))





================================================


model1 = LassoCV(eps=1e-5)
## model training and prediction
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

model2 = LinearRegression()
## model training and prediction
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)
model3 = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=6, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10, 
                                   loss='huber', random_state = 5)
## model training and prediction
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

model4 = xgb.XGBRegressor(colsample_bytree=0.2, gamma=0.0, 
                             learning_rate=0.1, max_depth=6, 
                             min_child_weight=3, n_estimators=5000,
                             reg_alpha=0.8, reg_lambda=0.6,
                             subsample=0.4,seed=27, silent=1)
## model training and prediction
model4.fit(X_train, y_train)
pred4 = model4.predict(X_test)

pred = (pred1+pred2+pred3+pred4)/4
# model performance
print("Ensemble model:\n")
print("r2_score: " + str(r2_score(pred, y_test.values)))

r2_score: 0.9445808762383004

========================================


model1 = LassoCV(eps=1e-5)
## model training and prediction
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

model2 = LinearRegression()
## model training and prediction
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)
model3 = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=6, max_features='sqrt',
                                   min_samples_leaf=15, min_samples_split=10, 
                                   loss='huber', random_state = 5)
## model training and prediction
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

model4 = xgb.XGBRegressor(colsample_bytree=0.8, gamma=0.0, 
                             learning_rate=0.1, max_depth=6, 
                             min_child_weight=3, n_estimators=8000,
                             reg_alpha=0.8, reg_lambda=0.8,
                             subsample=0.8,seed=27, silent=1)
## model training and prediction
model4.fit(X_train, y_train)
pred4 = model4.predict(X_test)

pred = (pred1+pred2+pred3+pred4)/4
# model performance
print("Ensemble model:\n")
print("r2_score: " + str(r2_score(pred, y_test.values)))


r2_score: 0.9470229097363644

===============================================


model1 = LassoCV(eps=1e-5)
## model training and prediction
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

model2 = LinearRegression()
## model training and prediction
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)
model3 = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=10, max_features='sqrt',
                                   min_samples_leaf=5, min_samples_split=10, 
                                   loss='huber', random_state = 5)
## model training and prediction
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

model4 = xgb.XGBRegressor(colsample_bytree=0.8, gamma=0.0, 
                             learning_rate=0.1, max_depth=6, 
                             min_child_weight=3, n_estimators=8000,
                             reg_alpha=0.8, reg_lambda=0.8,
                             subsample=0.8,seed=27, silent=1)
## model training and prediction
model4.fit(X_train, y_train)
pred4 = model4.predict(X_test)

pred = (pred1+pred2+pred3+pred4)/4
# model performance
print("Ensemble model:\n")
print("r2_score: " + str(r2_score(pred, y_test.values)))

r2_score: 0.9481816551098282
=================================================

model1 = LassoCV(eps=1e-5)
## model training and prediction
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

model2 = LinearRegression()
## model training and prediction
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)
model3 = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=10, max_features='sqrt',
                                   min_samples_leaf=5, min_samples_split=10, 
                                   loss='huber', random_state = 5)
## model training and prediction
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

model4 = xgb.XGBRegressor(colsample_bytree=0.8, gamma=0.0, 
                             learning_rate=0.05, max_depth=10, 
                             min_child_weight=3, n_estimators=8000,
                             reg_alpha=0.8, reg_lambda=0.8,
                             subsample=0.8,seed=27, silent=1)
## model training and prediction
model4.fit(X_train, y_train)
pred4 = model4.predict(X_test)

pred = (pred1+pred2+pred3+pred4)/4
# model performance
print("Ensemble model:\n")
print("r2_score: " + str(r2_score(pred, y_test.values)))


r2_score: 0.9484476116071556
==================================================


model1 = LassoCV(eps=1e-5)
## model training and prediction
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

model2 = LinearRegression()
## model training and prediction
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)
model3 = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=10, max_features='sqrt',
                                   min_samples_leaf=5, min_samples_split=10, 
                                   loss='huber', random_state = 5)
## model training and prediction
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

model4 = xgb.XGBRegressor(colsample_bytree=0.8, gamma=0.0, 
                             learning_rate=0.05, max_depth=10, 
                             min_child_weight=5, n_estimators=8000,
                             reg_alpha=0.8, reg_lambda=0.6,
                             subsample=0.6,seed=27, silent=1)
## model training and prediction
model4.fit(X_train, y_train)
pred4 = model4.predict(X_test)

pred = (pred1+pred2+pred3+pred4)/4
# model performance
print("Ensemble model:\n")
print("r2_score: " + str(r2_score(pred, y_test.values)))


r2_score: 0.9487085510932642
=========================================


model1 = LassoCV(eps=1e-5)
## model training and prediction
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

model2 = LinearRegression()
## model training and prediction
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)
model3 = GradientBoostingRegressor(n_estimators=3000, learning_rate=0.05,
                                   max_depth=10, max_features='sqrt',
                                   min_samples_leaf=50, min_samples_split=10, 
                                   loss='huber', random_state = 5)
## model training and prediction
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

model4 = xgb.XGBRegressor(colsample_bytree=0.8, gamma=0.0, 
                             learning_rate=0.05, max_depth=10, 
                             min_child_weight=5, n_estimators=7000,
                             reg_alpha=0.6, reg_lambda=0.6,
                             subsample=0.8,random_state= 25, silent=1)
## model training and prediction
model4.fit(X_train, y_train)
pred4 = model4.predict(X_test)

pred = (pred1+pred2+pred3+pred4)/4
# model performance
print("Ensemble model:\n")
print("r2_score: " + str(r2_score(pred, y_test.values)))


r2_score: 0.9489093032459737
==========================================
