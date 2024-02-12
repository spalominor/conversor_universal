import streamlit as st

def temperatura():
    st.write("Conversiones de temperatura:")
    opcion = st.selectbox("Selecciona la conversión", ["Celsius a Fahrenheit", 
                                                      "Fahrenheit a Celsius", 
                                                      "Celsius a Kelvin", 
                                                      "Kelvin a Celsius"])
    if opcion == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingresa la temperatura en Celsius")
        fahrenheit = (celsius * 9/5) + 32
        st.write(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
    elif opcion == "Fahrenheit a Celsius":
        fahrenheit = st.number_input("Ingresa la temperatura en Fahrenheit")
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius.")
    elif opcion == "Celsius a Kelvin":
        celsius = st.number_input("Ingresa la temperatura en Celsius")
        kelvin = celsius + 273.15
        st.write(f"{celsius} grados Celsius equivalen a {kelvin} grados Kelvin.")
    elif opcion == "Kelvin a Celsius":
        kelvin = st.number_input("Ingresa la temperatura en Kelvin")
        celsius = kelvin - 273.15
        st.write(f"{kelvin} grados Kelvin equivalen a {celsius} grados Celsius.")

def longitud():
    st.write("Conversiones de longitud:")
    opcion = st.selectbox("Selecciona la conversión", ["Pies a Metros", 
                                                      "Metros a Pies", 
                                                      "Pulgadas a Centímetros", 
                                                      "Centímetros a Pulgadas"])
    if opcion == "Pies a Metros":
        pies = st.number_input("Ingresa la longitud en Pies")
        metros = pies * 0.3048
        st.write(f"{pies} pies equivalen a {metros} metros.")
    elif opcion == "Metros a Pies":
        metros = st.number_input("Ingresa la longitud en Metros")
        pies = metros / 0.3048
        st.write(f"{metros} metros equivalen a {pies} pies.")
    elif opcion == "Pulgadas a Centímetros":
        pulgadas = st.number_input("Ingresa la longitud en Pulgadas")
        centimetros = pulgadas * 2.54
        st.write(f"{pulgadas} pulgadas equivalen a {centimetros} centímetros.")
    elif opcion == "Centímetros a Pulgadas":
        centimetros = st.number_input("Ingresa la longitud en Centímetros")
        pulgadas = centimetros / 2.54
        st.write(f"{centimetros} centímetros equivalen a {pulgadas} pulgadas.")

def peso():
    st.write("Conversiones de peso/masa:")
    opcion = st.selectbox("Selecciona la conversión", ["Libras a Kilogramos", 
                                                      "Kilogramos a Libras", 
                                                      "Onzas a Gramos", 
                                                      "Gramos a Onzas"])
    if opcion == "Libras a Kilogramos":
        libras = st.number_input("Ingresa el peso en Libras")
        kilogramos = libras * 0.453592
        st.write(f"{libras} libras equivalen a {kilogramos} kilogramos.")
    elif opcion == "Kilogramos a Libras":
        kilogramos = st.number_input("Ingresa el peso en Kilogramos")
        libras = kilogramos / 0.453592
        st.write(f"{kilogramos} kilogramos equivalen a {libras} libras.")
    elif opcion == "Onzas a Gramos":
        onzas = st.number_input("Ingresa el peso en Onzas")
        gramos = onzas * 28.3495
        st.write(f"{onzas} onzas equivalen a {gramos} gramos.")
    elif opcion == "Gramos a Onzas":
        gramos = st.number_input("Ingresa el peso en Gramos")
        onzas = gramos / 28.3495
        st.write(f"{gramos} gramos equivalen a {onzas} onzas.")

def volumen():
    st.write("Conversiones de volumen:")
    opcion = st.selectbox("Selecciona la conversión", ["Galones a Litros", 
                                                      "Litros a Galones", 
                                                      "Pulgadas cúbicas a Centímetros cúbicos", 
                                                      "Centímetros cúbicos a Pulgadas cúbicas"])
    if opcion == "Galones a Litros":
        galones = st.number_input("Ingresa el volumen en Galones")
        litros = galones * 3.78541
        st.write(f"{galones} galones equivalen a {litros} litros.")
    elif opcion == "Litros a Galones":
        litros = st.number_input("Ingresa el volumen en Litros")
        galones = litros / 3.78541
        st.write(f"{litros} litros equivalen a {galones} galones.")
    elif opcion == "Pulgadas cúbicas a Centímetros cúbicos":
        pulgadas_cubicas = st.number_input("Ingresa el volumen en Pulgadas cúbicas")
        centimetros_cubicos = pulgadas_cubicas * 16.3871
        st.write(f"{pulgadas_cubicas} pulgadas cúbicas equivalen a {centimetros_cubicos} centímetros cúbicos.")
    elif opcion == "Centímetros cúbicos a Pulgadas cúbicas":
        centimetros_cubicos = st.number_input("Ingresa el volumen en Centímetros cúbicos")
        pulgadas_cubicas = centimetros_cubicos / 16.3871
        st.write(f"{centimetros_cubicos} centímetros cúbicos equivalen a {pulgadas_cubicas} pulgadas cúbicas.")

def tiempo():
    st.write("Conversiones de tiempo:")
    opcion = st.selectbox("Selecciona la conversión", ["Horas a Minutos", 
                                                      "Minutos a Segundos", 
                                                      "Días a Horas", 
                                                      "Semanas a Días"])
    if opcion == "Horas a Minutos":
        horas = st.number_input("Ingresa el tiempo en Horas")
        minutos = horas * 60
        st.write(f"{horas} horas equivalen a {minutos} minutos.")
    elif opcion == "Minutos a Segundos":
        minutos = st.number_input("Ingresa el tiempo en Minutos")
        segundos = minutos * 60
        st.write(f"{minutos} minutos equivalen a {segundos} segundos.")
    elif opcion == "Días a Horas":
        dias = st.number_input("Ingresa el tiempo en Días")
        horas = dias * 24
        st.write(f"{dias} días equivalen a {horas} horas.")
    elif opcion == "Semanas a Días":
        semanas = st.number_input("Ingresa el tiempo en Semanas")
        dias = semanas * 7
        st.write(f"{semanas} semanas equivalen a {dias} días.")

def velocidad():
    st.write("Conversiones de velocidad:")
    opcion = st.selectbox("Selecciona la conversión", ["Millas por hora a Kilómetros por hora", 
                                                      "Kilómetros por hora a Metros por segundo", 
                                                      "Nudos a Millas por hora", 
                                                      "Metros por segundo a Pies por segundo"])
    if opcion == "Millas por hora a Kilómetros por hora":
        mph = st.number_input("Ingresa la velocidad en Millas por hora")
        kph = mph * 1.60934
        st.write(f"{mph} millas por hora equivalen a {kph} kilómetros por hora.")
    elif opcion == "Kilómetros por hora a Metros por segundo":
        kph = st.number_input("Ingresa la velocidad en Kilómetros por hora")
        mps = kph * 0.277778
        st.write(f"{kph} kilómetros por hora equivalen a {mps} metros por segundo.")
    elif opcion == "Nudos a Millas por hora":
        nudos = st.number_input("Ingresa la velocidad en Nudos")
        mph = nudos * 1.15078
        st.write(f"{nudos} nudos equivalen a {mph} millas por hora.")
    elif opcion == "Metros por segundo a Pies por segundo":
        mps = st.number_input("Ingresa la velocidad en Metros por segundo")
        fps = mps * 3.28084
        st.write(f"{mps} metros por segundo equivalen a {fps} pies por segundo.")

def area():
    st.write("Conversiones de área:")
    opcion = st.selectbox("Selecciona la conversión", ["Metros cuadrados a Pies cuadrados", 
                                                      "Pies cuadrados a Metros cuadrados", 
                                                      "Kilómetros cuadrados a Millas cuadradas", 
                                                      "Millas cuadradas a Kilómetros cuadrados"])
    if opcion == "Metros cuadrados a Pies cuadrados":
        metros_cuadrados = st.number_input("Ingresa el área en Metros cuadrados")
        pies_cuadrados = metros_cuadrados * 10.7639
        st.write(f"{metros_cuadrados} metros cuadrados equivalen a {pies_cuadrados} pies cuadrados.")
    elif opcion == "Pies cuadrados a Metros cuadrados":
        pies_cuadrados = st.number_input("Ingresa el área en Pies cuadrados")
        metros_cuadrados = pies_cuadrados / 10.7639
        st.write(f"{pies_cuadrados} pies cuadrados equivalen a {metros_cuadrados} metros cuadrados.")
    elif opcion == "Kilómetros cuadrados a Millas cuadradas":
        km_cuadrados = st.number_input("Ingresa el área en Kilómetros cuadrados")
        millas_cuadradas = km_cuadrados * 0.386102
        st.write(f"{km_cuadrados} kilómetros cuadrados equivalen a {millas_cuadradas} millas cuadradas.")
    elif opcion == "Millas cuadradas a Kilómetros cuadrados":
        millas_cuadradas = st.number_input("Ingresa el área en Millas cuadradas")
        km_cuadrados = millas_cuadradas / 0.386102
        st.write(f"{millas_cuadradas} millas cuadradas equivalen a {km_cuadrados} kilómetros cuadrados.")

def energia():
    st.write("Conversiones de energía:")
    opcion = st.selectbox("Selecciona la conversión", ["Julios a Calorías", 
                                                      "Calorías a Kilojulios", 
                                                      "Kilovatios-hora a Megajulios", 
                                                      "Megajulios a Kilovatios-hora"])
    if opcion == "Julios a Calorías":
        julios = st.number_input("Ingresa la energía en Julios")
        calorias = julios * 0.238846
        st.write(f"{julios} julios equivalen a {calorias} calorías.")
    elif opcion == "Calorías a Kilojulios":
        calorias = st.number_input("Ingresa la energía en Calorías")
        kilojulios = calorias * 0.004184
        st.write(f"{calorias} calorías equivalen a {kilojulios} kilojulios.")
    elif opcion == "Kilovatios-hora a Megajulios":
        kilovatios_hora = st.number_input("Ingresa la energía en Kilovatios-hora")
        megajulios = kilovatios_hora * 3.6
        st.write(f"{kilovatios_hora} kilovatios-hora equivalen a {megajulios} megajulios.")
    elif opcion == "Megajulios a Kilovatios-hora":
        megajulios = st.number_input("Ingresa la energía en Megajulios")
        kilovatios_hora = megajulios / 3.6
        st.write(f"{megajulios} megajulios equivalen a {kilovatios_hora} kilovatios-hora.")

def presion():
    st.write("Conversiones de presión:")
    opcion = st.selectbox("Selecciona la conversión", ["Pascales a Atmósferas", 
                                                      "Atmósferas a Pascales", 
                                                      "Barras a Libras por pulgada cuadrada", 
                                                      "Libras por pulgada cuadrada a Barras"])
    if opcion == "Pascales a Atmósferas":
        pascales = st.number_input("Ingresa la presión en Pascales")
        atm = pascales * 0.00000986923
        st.write(f"{pascales} pascales equivalen a {atm} atmósferas.")
    elif opcion == "Atmósferas a Pascales":
        atm = st.number_input("Ingresa la presión en Atmósferas")
        pascales = atm / 0.00000986923
        st.write(f"{atm} atmósferas equivalen a {pascales} pascales.")
    elif opcion == "Barras a Libras por pulgada cuadrada":
        barras = st.number_input("Ingresa la presión en Barras")
        psi = barras * 14.5038
        st.write(f"{barras} barras equivalen a {psi} libras por pulgada cuadrada.")
    elif opcion == "Libras por pulgada cuadrada a Barras":
        psi = st.number_input("Ingresa la presión en Libras por pulgada cuadrada")
        barras = psi / 14.5038
        st.write(f"{psi} libras por pulgada cuadrada equivalen a {barras} barras.")

def tamano_datos():
    st.write("Conversiones de tamaño de datos:")
    opcion = st.selectbox("Selecciona la conversión", ["Megabytes a Gigabytes", 
                                                      "Gigabytes a Terabytes", 
                                                      "Kilobytes a Megabytes", 
                                                      "Terabytes a Petabytes"])
    if opcion == "Megabytes a Gigabytes":
        megabytes = st.number_input("Ingresa el tamaño en Megabytes")
        gigabytes = megabytes / 1024
        st.write(f"{megabytes} megabytes equivalen a {gigabytes} gigabytes.")
    elif opcion == "Gigabytes a Terabytes":
        gigabytes = st.number_input("Ingresa el tamaño en Gigabytes")
        terabytes = gigabytes / 1024
        st.write(f"{gigabytes} gigabytes equivalen a {terabytes} terabytes.")
    elif opcion == "Kilobytes a Megabytes":
        kilobytes = st.number_input("Ingresa el tamaño en Kilobytes")
        megabytes = kilobytes / 1024
        st.write(f"{kilobytes} kilobytes equivalen a {megabytes} megabytes.")
    elif opcion == "Terabytes a Petabytes":
        terabytes = st.number_input("Ingresa el tamaño en Terabytes")
        petabytes = terabytes / 1024
        st.write(f"{terabytes} terabytes equivalen a {petabytes} petabytes.")

def main():
    # Cambiar el color de fondo
    st.markdown(
        """
        <style>
        body {
            background-color: #87CEEB; /* Color azul claro */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Conversor Universal")
    categoria = st.selectbox("Selecciona una categoría", ["Temperatura", "Longitud", "Peso/Masa",
                                                          "Volumen", "Tiempo", "Velocidad",
                                                          "Área", "Energía", "Presión",
                                                          "Tamaño de Datos"])

    if categoria == "Temperatura":
        temperatura()
    elif categoria == "Longitud":
        longitud()
    elif categoria == "Peso/Masa":
        peso()
    elif categoria == "Volumen":
        volumen()
    elif categoria == "Tiempo":
        tiempo()
    elif categoria == "Velocidad":
        velocidad()
    elif categoria == "Área":
        area()
    elif categoria == "Energía":
        energia()
    elif categoria == "Presión":
        presion()
    elif categoria == "Tamaño de Datos":
        tamano_datos()

if __name__ == "__main__":
    main()
