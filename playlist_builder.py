###############################################################################
# Playlist-builder: A python program that takes a list of songs from a CSV file
# # # and outputs a melodically structured playlist ordered to your tastes # #
# # # Written by Cathy Cowell # # # # # # # # # # # # # # # # # # # # # # # #
# # # Last updated: 10/4/2019 # # # # # # # # # # # # # # # # # # # # # # # #
###############################################################################

import csv
import operator
import statistics
import random 

f = open('song-data.csv', 'r')

reader = csv.reader(f)

tracks = {}

for row in reader:
	tracks[row[0]] = {'key':row[1], 'bpm':row[2], 'energy':row[3],
                          'visited':False,'keycode': ''}

# clean up data 
del tracks['Song Name']

# Convert keys to Camelot key code for harmonic mixing
for track, info in tracks.items():
        if info.get('key') == 'Abm':
                info['keycode'] = '01A'
        elif info.get('key') == 'Ebm':
                info['keycode'] = '02A'
        elif info.get('key') == 'Bbm':
                info['keycode'] = '03A'
        elif info.get('key') == 'Fm':
                info['keycode'] = '04A'
        elif info.get('key') == 'Cm':
                info['keycode'] = '05A'
        elif info.get('key') == 'Gm':
                info['keycode'] = '06A'
        elif info.get('key') == 'Dm':
                info['keycode'] = '07A'
        elif info.get('key') == 'Am':
                info['keycode'] = '08A'
        elif info.get('key') == 'Em':
                info['keycode'] = '09A'
        elif info.get('key') == 'Bm':
                info['keycode'] = '10A'
        elif info.get('key') == 'Fm' or info.get('key') == 'Gbm':
                info['keycode'] = '11A'
        elif info.get('key') == 'Dbm':
                info['keycode'] = '12A'
        elif info.get('key') == 'B':
                info['keycode'] = '01B'
        elif info.get('key') == 'Fm':
                info['keycode'] = '02B'
        elif info.get('key') == 'Db' or info.get('key') == 'Gb':
                info['keycode'] = '03B'
        elif info.get('key') == 'Ab':
                info['keycode'] = '04B'
        elif info.get('key') == 'Eb':
                info['keycode'] = '05B'
        elif info.get('key') == 'Bb':
                info['keycode'] = '06B'
        elif info.get('key') == 'F':
                info['keycode'] = '07B'
        elif info.get('key') == 'C':
                info['keycode'] = '08B'
        elif info.get('key') == 'G':
                info['keycode'] = '09B'
        elif info.get('key') == 'D':
                info['keycode'] = '10B'
        elif info.get('key') == 'A':
                info['keycode'] = '11B'
        elif info.get('key') == 'E':
                info['keycode'] = '12B'
        else:
                print('Key not found! Please make sure input is in',
                      'correct format. \n')
                info['keycode'] = 'not found'
                
###############################################################################
# Functions
###############################################################################

        
# Takes a playlist, and starting and ending tempos
# Returns the playlist, re-ordered by the given parameters
def playlist_by_tempo(playlist, start, end):
        tempos = []
        updated_playlist = []
        for track, info in tracks.items():
                info['visited'] = False
                tempos.append(int(info.get('bpm')))
        mid_tempo = statistics.median(tempos)

        if start == 'slow' and end == 'slow':
                for track, info in tracks.items():
                        if (int(info.get('bpm'))) < mid_tempo:
                            updated_playlist.append(track)
                            
        if start == 'fast' and end == 'fast':
                for track, info in tracks.items():
                        if (int(info.get('bpm'))) >= mid_tempo:
                                updated_playlist.append(track)

        if start == 'slow' and end == 'fast':
                tempos.sort()
                for t in tempos:
                        for track, info in tracks.items():
                                if(int(info.get('bpm'))) == t and (not (info.get('visited'))):
                                        updated_playlist.append(track)
                                        info['visited'] = True
                                        break
   
        if start == 'fast' and end == 'slow':
                tempos.sort(reverse=True)
                for t in tempos:
                        for track, info in tracks.items():
                                if (int(info.get('bpm'))) == t and (not (info.get('visited'))):
                                        updated_playlist.append(track)
                                        info['visited'] = True
                                        break
        return updated_playlist

# Takes a playlist, and starting and ending energies
# Returns the playlist, re-ordered by the given parameters
def playlist_by_energy(playlist, start, end):
        energies = []
        updated_playlist = []
        for track, info in tracks.items():
                energies.append(int(info.get('energy')))
                info['visited'] = False
        mid_e = statistics.median(energies)

        if start == 'low' and end == 'low':
                for track, info in tracks.items():
                        if (int(info.get('energy'))) < mid_e:
                            updated_playlist.append(track)
                            
        if start == 'high' and end == 'high':
                for track, info in tracks.items():
                        if (int(info.get('energy'))) >= mid_e:
                                upadted_playlist.append(track)

        if start == 'low' and end == 'high':
                energies.sort()
                for e in energies:
                        for track, info in tracks.items():
                                if(int(info.get('energy'))) == e and (not
                                                        (info.get('visited'))):
                                        updated_playlist.append(track)
                                        info['visited'] = True
                                        break
   
        if start == 'high' and end == 'low':
                energies.sort(reverse=True)
                for e in energies:
                        for track, info in tracks.items():
                                if (int(info.get('energy'))) == e and (not
                                                        (info.get('visited'))):
                                        updated_playlist.append(track)
                                        info['visited'] = True
                                        break
        return updated_playlist

# Takes a playlist, and key preference 
# Returns the playlist that you get from taking out songs not in specified key
def playlist_by_key(playlist, key):
        updated_playlist = []
        
        if key == 'minor':
                for p in playlist:
                        keycode = (tracks[p].get('keycode'))
                        if keycode.endswith('A'):
                                      updated_playlist.append(p)

        if key == 'major':
                for p in playlist:
                        keycode = (tracks[p].get('keycode'))
                        if keycode.endswith('B'):
                                      updated_playlist.append(p)
        if key == 'idc':
                updated_playlist = playlist
        
        return updated_playlist

# takes a playlist, and re-orders the songs for harmonic mixing with
# as little difference in key and bpm between adjacent songs as possible
def order_playlist(playlist, length, start_t, end_t):
        updated_playlist = []
        for track, info in tracks.items():
                info['visited'] = False
                
        # chose random song from 10 in playlist to start             
        first = random.randint(0,9)
        updated_playlist.append(playlist[first])
        tracks[playlist[first]]['visited'] = True
        next = ''

        rate = 'nuetral'
        if start_t == 'slow' and end_t == 'fast':
                rate = 'inc'
        elif start_t == 'fast' and end_t == 'slow':
                rate = 'dec'

        while len(updated_playlist) < length:
                next = next_song(updated_playlist[-1], playlist, rate)
                updated_playlist.append(next)
                
        return updated_playlist
        
# takes a playlist and returns a song that goes next nicely with previous song
def next_song(cur_track, playlist, rate):
        next = ''
        df = 0

        # find the next song where the difference factor between current
        # song and next is as low as possible
        while (next == ''):
                for p in playlist:
                        if (not tracks[p]['visited']):
                                if difference_factor(cur_track, p, rate) <= df:
                                        next = p
                                        tracks[p]['visited'] = True
                                        return next
                df += 1

                                              
# takes two songs and returns a difference factor calculated by their
# similarities in bpm, energy, and key
def difference_factor(track1, track2, rate):
        df = 0
        key_diff = 0
        # adjust constants for more or less emphasis on similar bpms or
        # harmonic mixing
        tempo_factor = 5
        harmonic_factor = 2

        # add difference of tempos to df minus constant for scale
        df += abs(int(tracks[track1]['bpm']) -
                  int(tracks[track2]['bpm'])) - tempo_factor

        # add to df of tracks that dont follow user selected rate
        if rate == 'inc':
                if int(tracks[track1]['bpm']) - int(tracks[track2]['bpm']) >= 0:
                        df += 7
        elif rate == 'dec':
                if int(tracks[track2]['bpm']) - int(tracks[track1]['bpm']) >= 0:
                        df += 7
                
          # dd difference of energies to df
##        df += abs(int(tracks[track1]['energy']) -
##                  int(tracks[track2]['energy']))

        # add harmonic differnce to df through harmonic ranking
        key1 = (tracks[track1].get('keycode'))
        key2 = (tracks[track2].get('keycode'))
        # if key of track1 == key of track2, we don't add to df
        # If both major/minor, start harmonic ranking
        if key1.endswith('A') and key2.endswith('A'):
                key_diff = adjust_difference(abs(int(key1[:2])
                                                 - int(key2[:2])))
        elif key1.endswith('B') and key2.endswith('B'):
                key_diff = adjust_difference(abs(int(key1[:2])
                                                         - int(key2[:2])))
        # if first two digits of the keys are the same, they're a relative
        # major and minor pair and will mix well together
        elif key1[:2] == key2[:2]:
                key_diff = 1
        # not both major, minor, or relative of each other,
        # or key = 'not found' assign high diff
        else:
                key_diff = 7
        # multiply by constant for more emphasis on harmonic mixing
        df += key_diff*harmonic_factor

        return df

# adjust differences in key to account for circular Camelot wheel
def adjust_difference(key_diff):
        if key_diff == 11: # means we had 12B and 1B which touch on wheel
                key_diff = 1
        elif key_diff == 10:
                key_diff = 2
        elif key_diff == 9:
                key_diff = 3
        elif key_diff == 8:
                key_diff = 4
        elif key_diff == 7:
                key_diff = 5
                
        return key_diff

# prints out a playlist      
def print_playlist(playlist):
        print('This is the playlist I made you! \n')
        i = 1
        for p in playlist:
                print("Song", i, ":", p)
                print("Key:", tracks[p]['key'], "| Key (Camelot):",
                      tracks[p]['keycode'],
                      "| BPM:", tracks[p]['bpm'], '\n')
                i += 1
                
              
# builds playlist, considering a given length, starting tempo, ending tempo,
# and key
def playlist_builder(length, start_temp, end_temp, start_e, end_e, key):
        playlist = []
#       playlist = playlist_by_energy(playlist, start_e, end_e)
        playlist = playlist_by_tempo(playlist, start_temp, end_temp)
        playlist = playlist_by_key(playlist, key)
        playlist = order_playlist(playlist, length, start_temp, end_temp)
        print_playlist(playlist)


###############################################################################
# User Configurations
###############################################################################
playing = True
print('Welcome to your playlist builder! \n')

while (playing):
        playlist_len = int(input ("How many tracks would you like in your playlist? \n"))

        if playlist_len < 10 or playlist_len > 30:
                playlist_len = int(input ("Please chose a number between 10 and 30"))
        
        print("Do you want to start your set with fast or slow songs?")
        start_tempo = input("Please enter (fast/slow) \n")

        print ("Do you want to end your set with fast or slow songs?")  
        end_tempo = input("Please enter (fast/slow) \n")

##        print("Do you want to start your set with high or low energy songs?")
##        start_energy = input("Please enter (low/high)")
##
##        print("Do you want to end your set with high or low energy songs?")
##        end_energy = input("Please enter (low/high)")

        print("Do you want emphasize minor or major keyed songs in your set? \n",
              "Or do you not care?")
        key = input("Please enter (minor/major/idc) \n")

##        print('You said you want a playlist of', playlist_len, 'tracks, in', key,
##              'key, starting with', start_tempo, 'tempo', start_energy,'energy songs',
##              'and ending with', end_tempo, 'tempo,', end_energy, 'energy songs.')

        print('You said you want a playlist of', playlist_len, 'tracks, in',
              key,'keys, starting with', start_tempo, 'tempo songs',
              'and ending with', end_tempo, 'tempo songs.')                   

        print('You got it!  \n')
        playlist_builder(playlist_len, start_tempo, end_tempo, 'null', 'null',
                 key)
        again = input("Would you like try building another playlist? (Y/N)")
        if again == 'Y' or again == 'y':
                print("Great! Let's do it.")
        else:
                print("Glad I could be of service! Happy mixing :)")
                playing = False
                        


        



