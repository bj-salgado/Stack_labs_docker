import pickle
import streamlit as st


# loading the trained model
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

st.title("Projeto Squad Docker")

@st.cache()
def prediction(gender, age, driving_license, previously_insured, vehicle_age, vehicle_damage, annual_premium,	vintage):

    # Pre-processing user input
    if gender == "Masculino":
        gender = 1
    else:
        gender = 0

    if driving_license == "Habilitado":
        driving_license = 1
    else:
        driving_license = 0

    if previously_insured == "Sim":
        previously_insured = 1
    else:
        previously_insured = 0

    if vehicle_age == "> 2 Anos":
        vehicle_age = 2

    if vehicle_age == "1-2 Anos":
        vehicle_age = 0

    if vehicle_age == "< 1 Ano":
        vehicle_age = 1

    if vehicle_damage == "Sim":
        vehicle_damage = 1
    else:
        vehicle_damage = 0

    # Making predictions
    prediction = classifier.predict(
        [[gender, age, driving_license, previously_insured, vehicle_age, vehicle_damage, annual_premium, vintage]])

    if prediction == 0:
        pred = 'Cliente tem interesse no seguro'
    if prediction == 1:
        pred = 'Cliente não tem interesse no seguro'
    return pred



def main():
    

    
    gender = st.selectbox('Genêro', ("Masculino", "Feminino"))
    age = st.number_input("Idade", min_value=18, max_value=80, value=25, step=1)
    driving_license = st.selectbox(
        'Habilitação', ("Habilitado", "Não Habilitado"))
    previously_insured = st.selectbox('Previamente segurado', ("Sim", "Não"))
    vehicle_age = st.selectbox(
        'vehicle_age', ("> 2 Anos", "1-2 Anos", "< 1 Ano"))
    vehicle_damage = st.selectbox('Danos no veiculo', ("Sim", "Não"))
    annual_premium = st.number_input("Apolice")
    vintage = st.number_input("vintage")
    result = ""

    
    if st.button("Fazer predição"):
        result = prediction(gender, age, driving_license, previously_insured,
                            vehicle_age, vehicle_damage, annual_premium, vintage)
        st.success('Seu resultado é: {}'.format(result))


if __name__ == '__main__':
    main()
