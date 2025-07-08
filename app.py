from data_loader import load_data
from model import train_model
from ui import create_interface

if __name__ == "__main__":
    df = load_data()
    model = train_model(df)
    demo = create_interface(model)
    demo.launch()
