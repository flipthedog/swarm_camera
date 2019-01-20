import synthesizer

chord = [231.23]
player = synthesizer.Player()
player.open_stream()
synth = synthesizer.Synthesizer(osc1_volume=1.0, osc1_waveform=synthesizer.Waveform.sine, use_osc2=False)

player.play_wave(synth.generate_constant_wave(440, 1))