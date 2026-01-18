from modules.voicegen import RobVoiceGen

if __name__  == "__main__":
    buffer = RobVoiceGen()
    buffer.voice_conf = 0
    buffer.voice_rate_conf = -25
    
    #Modify the current text attribute if you already have the string (text)
    buffer.current_text = 'Hello world'

    #Use this setter if you have a txt file
    #buffer.text_script_conf = r'../scripts/text.txt'

    buffer.output_conf = r'../output/example.mp3'
    
    #buffer.run_speech()
    #buffer.voices_try_out()
    buffer.save_to_mp3()