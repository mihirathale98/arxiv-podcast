import asyncio

async def generate_speech_async(tts_wrapper, text, speaker):
    return await asyncio.to_thread(tts_wrapper.generate_speech, text, speaker)

async def process_podcast(merged_podcast, tts_wrapper):
    speaker_map = {
        'host': 'Gracie Wise',
        'co-host': 'Aaron Dreschner'
    }

    tasks = []
    for segment in merged_podcast:
        speaker = speaker_map.get(segment['speaker'], segment['speaker'])
        text = segment['text']
        task = generate_speech_async(tts_wrapper, text, speaker)
        tasks.append(task)

    wavs = await asyncio.gather(*tasks)
    return tts_wrapper.concatenate_wavs(wavs)