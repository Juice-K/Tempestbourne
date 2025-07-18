import pandas as pd
import eyed3

# Load the CSV file
df = pd.read_csv("your_music_data.csv")

# Iterate through the rows
for index, row in df.iterrows():
    file_path = row['filepath']  # Or wherever your file path is stored
    try:
        audio_file = eyed3.load(file_path)
        if audio_file is not None:
            # Access metadata
            title = audio_file.tag.title
            artist = audio_file.tag.artist
            album = audio_file.tag.album

            # Do something with the metadata, like printing or writing to another CSV
            print(f"Title: {title}, Artist: {artist}, Album: {album}")

            # Example of updating the dataframe with metadata
            df.loc[index, 'title'] = title
            df.loc[index, 'artist'] = artist
            df.loc[index, 'album'] = album

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Optionally, save the updated dataframe to a new CSV
df.to_csv("updated_music_data.csv", index=False)

# All the above is specifically for mp3s