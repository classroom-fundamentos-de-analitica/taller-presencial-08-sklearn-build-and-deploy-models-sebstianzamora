import pickle

with open("house_predictor.pickle", "wb") as file:
    
    loaded_model = pickle.load(file)

print(loaded_model.coef_)
print(loaded_model.intercept_)