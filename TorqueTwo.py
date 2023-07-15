import streamlit as st

from PIL import Image
image = Image.open('TorqueCalculator2.jpg')
st.image(image)

st.title('Torque calculator 2')
st.write('#### This online calculator finds a point where the sum of torque is zero.')
st.write('')

#받침대 정보 입력
st.header('1. Beam Information')
BeamLength = int(st.slider('How long is the Beam? (m)', 0, 100))
BeamMass = float(st.text_input('What is the mass of the Beam? (kg)'))
st.write('')

#받침대가 만들어내는 돌림힘 구하기
BeamTorque = BeamMass*(BeamLength/2)*10

#물체 갯수 입력받기
st.header('2. Object Information')
count = int(st.text_input('How many objects are there?'))

ObjectTorque = 0
ObjectMassSum = 0

#물체 갯수(번)만큼 물체의 질량과 위치 입력받기
for i in range (count):
    st.write('')
    st.write(f' #### {i+1}. Object {i+1}')
    ObjectMass = float(st.text_input('What is the mass of the object? (kg)', key = f'{i+1}'))
    ObjectPosition = int(st.slider('Where is the object? (Based on the far from left, m)', 0, BeamLength, key = f'{ObjectMass}_{i+1}'))

    #물체가 만들어내는 돌림힘의 총 합과 물체의 질량 총 합 구하기
    ObjectTorque += ObjectMass*ObjectPosition*10
    ObjectMassSum += ObjectMass

#받침대와 물체의 총 무게 구하기
WeightSum = (BeamMass+ObjectMassSum)*10

#무게중심 위치 구하기 및 결과 출력하기
if st.button('Calculate'):
    st.write('Done!')
    result = (BeamTorque+ObjectTorque)/WeightSum

    st.write('### The center of gravity is located', result, 'm from the left.')
    st.write('')
    st.write('If you want to calculate the direction and magnitude of the Torque, click this! https://torquecalculator.streamlit.app/')