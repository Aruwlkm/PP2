import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Музыка керекпа")

music_files = [ "1.mp3", "getta.mp3","Отпусти.mp3"]
current_song = 0
playing = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play/Pause
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.load(music_files[current_song])
                        pygame.mixer.music.play()
                    else:
                        pygame.mixer.music.unpause()
                    playing = True
            
            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
                playing = False
            
            elif event.key == pygame.K_n:  # Next
                current_song = (current_song + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song])
                pygame.mixer.music.play()
                playing = True
            
            elif event.key == pygame.K_b: 
                current_song = (current_song - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song])
                pygame.mixer.music.play()
                playing = True
    
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('Arial', 20)
    
    if music_files:
        text = font.render(f"Now: {music_files[current_song]}", True, (0, 0, 0))
        screen.blit(text, (50, 50))
    
    status = "Playing" if playing else "Stopped"
    status_text = font.render(f"Status: {status}", True, (0, 0, 0))
    screen.blit(status_text, (50, 80))
    
    controls = font.render("P:Play S:Stop  N:Next  B:Back", True, (0, 0, 0))
    screen.blit(controls, (50, 120))
    
    pygame.display.flip()

pygame.quit()