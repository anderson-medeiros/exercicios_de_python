"""
# Tocando um MP3

Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
"""

import pygame

pygame.init()
pygame.mixer.music.load('sound-sample.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Reproduzindo áudio..')

