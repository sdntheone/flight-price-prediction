import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired
from wtforms.fields.html5 import TimeField

# Load your data
train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")

class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=[(value, value) for value in X_data.airline.dropna().unique().tolist()],
        validators=[DataRequired()]
    )
    date_of_journey = DateField(
        label="Date of Journey",
        format='%Y-%m-%d',  # Explicitly define the format
        validators=[DataRequired()]
    )
    source = SelectField(
        label="Source",
        choices=[(value, value) for value in X_data.source.dropna().unique().tolist()],
        validators=[DataRequired()]
    )
    destination = SelectField(
        label="Destination",
        choices=[(value, value) for value in X_data.destination.dropna().unique().tolist()],
        validators=[DataRequired()]
    )
    dep_time = TimeField(
        label="Departure Time",
        format="%H:%M",  # 24-hour format for time
        validators=[DataRequired()]
    )
    arrival_time = TimeField(
        label="Arrival Time",
        format="%H:%M",  # 24-hour format for time
        validators=[DataRequired()]
    )
    duration = IntegerField(
        label="Duration (minutes)",
        validators=[DataRequired()]
    )
    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices=[(value, value) for value in X_data.additional_info.dropna().unique().tolist()],
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
