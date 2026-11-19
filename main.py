import mido

def list_inputs():
    inputs = mido.get_input_names()
    print("Ports MIDI disponibles :")
    for i, name in enumerate(inputs):
        print(f"{i}: {name}")
    return inputs

def main():
    inputs = list_inputs()

    if not inputs:
        print("Aucun périphérique MIDI détecté.")
        return

    # Choix automatique du premier périphérique (tu peux changer l’index)
    port_name = inputs[0]
    print(f"\nConnexion à : {port_name}\n")

    with mido.open_input(port_name) as inport:
        print("Lecture MIDI en cours (Ctrl+C pour quitter)\n")

        for msg in inport:
            print(msg)

if __name__ == "__main__":
    main()