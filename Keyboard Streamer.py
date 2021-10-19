#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Install Modules
pip install pygame
pip install python-vlc
pip install youtube-dl


# In[1]:


#Import Modules
import pygame, sys
from pygame.locals import *
import vlc
import pafy

#Initialize pygame
pygame.init()

windowSurface = pygame.display.set_mode((1, 1))

pygame.display.iconify()

#Bind "m" key to pygame event.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_m]:
        #Stream media when "m" key is pressed.
        url = "https://www.youtube.com/watch?v=EK_LN3XEcnw"
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()


# In[ ]:




