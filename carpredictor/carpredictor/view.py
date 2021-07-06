from django.shortcuts import render
import pandas as pd
import pickle

def index(request):
    car = pd.read_csv('cleaned Car.csv')
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique(),reverse=True)
    years = sorted(car['year'].unique())
    fuel_type = sorted(car['fuel_type'].unique())
    param = {'companies':companies,'car_models':car_models,'years':years,'fuel_type':fuel_type}
    return render(request,'index.html',param)
def send_data(request):
    model = pickle.load(open('LinearRegressionModel.pk1','rb'))
    print(model)
    if request.method =='POST':
        company = request.POST.get('company','')
        car_model = request.POST.get('car_model','')
        year = request.POST.get('year','')
        kms_driven = request.POST.get('kilo_driven','')
        fuel_type = request.POST.get('Fuel_Type','')

        print(company,car_model,year,kms_driven,fuel_type)
        prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                                  columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))
        print(prediction)
        param = {'prediction':round(prediction[0],4)}

        return render(request,'output.html',param)