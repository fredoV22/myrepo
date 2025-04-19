from django.shortcuts import render
from .forms import StudentForm
import joblib, numpy as np, os

model_path = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')
model = joblib.load(model_path)

def home(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            mode_encoded = {'online': 0, 'f2f': 1, 'hybrid': 2}
            input_data = np.array([
                data['gpa'],
                data['attendance'],
                data['income'],
                int(data['support']),
                data['mental_health'],
                int(data['activities']),
                int(data['materials']),
                mode_encoded[data['mode']]
            ]).reshape(1, -1)

            prediction = model.predict(input_data)[0]
            risk = "High Risk of Dropping Out" if prediction == 1 else "Low Risk"
            return render(request, "predictor/result.html", {"risk": risk})
    else:
        form = StudentForm()

    return render(request, "predictor/home.html", {"form": form})
