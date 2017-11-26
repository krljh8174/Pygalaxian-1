#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *
from stars import stars
from player import player
from boss import boss
from enemy import enemy
from enemydrone import enemydrone
from enemysaucer import enemysaucer
from enemystation import enemystation
from healthpack import healthpack
from starship import starship
from bullet import bullet
from enemybullet import enemybullet
from explosion import explosion
from unit import *
from enemy import moveplayer


pygame.init()


def cpumove(cpu, target):
    if target.rect.left < cpu.rect.left:
        cpu.trigger = 1
        cpu.speed = -2
    elif target.rect.left > cpu.rect.left:
        cpu.trigger = 1
        cpu.speed = 2
    if random.randrange(0, 30) == 1:
        cpu.fire = 1
    else:
        cpu.fire = 0


def bossmove(cpu, target):
    if target.rect.left < cpu.rect.left and cpu.spree == False:
        cpu.trigger = 1
        cpu.speed = -2
    elif target.rect.left > cpu.rect.left and cpu.spree == False:
        cpu.trigger = 1
        cpu.speed = 2

    if random.randrange(0, 3) == 1 and cpu.spree == False:
        cpu.bulletformation = 0
        cpu.bulletspeed = 20
        cpu.fire = 1
    else:
        cpu.fire = 0

    if cpu.spree == False and random.randrange(0, 250) == 71:
        cpu.spree = True
    else:
        pass


def showhealthbar(
    health,
    barcolor,
    pos,
    unit,
    ):

    healthbar = pygame.Surface((health * unit, 10), pygame.SRCALPHA, 32)
    healthbar = healthbar.convert_alpha()
    pygame.draw.rect(screen, barcolor, pos)


def displaytext(
    text,
    fontsize,
    x,
    y,
    color,
    ):

    font = pygame.font.SysFont('sawasdee', fontsize, True)
    text = font.render(text, 1, color)
    textpos = text.get_rect(centerx=x, centery=y)
    screen.blit(text, textpos)


def storyboard(wavecounter):
    if wavecounter >= 0 and wavecounter <= 10:  # enemy
        return 0
    elif wavecounter > 10 and wavecounter <= 20:

                                                     # saucer

        return 1
    elif wavecounter > 20 and wavecounter <= 30:

                                                     # drone

        return 2
    elif wavecounter > 30 and wavecounter <= 40:

                                                     # station

        return 3
    elif wavecounter > 40 and wavecounter <= 50:

                                                     # drone

        return 4
    elif wavecounter > 50 and wavecounter <= 60:

                                                     # enemy and saucer

        return 5
    elif wavecounter > 60 and wavecounter <= 70:

                                                     # enemy

        return 6
    elif wavecounter > 70 and wavecounter <= 80:

                                                     # drone and saucer

        return 7
    elif wavecounter > 80 and wavecounter <= 90:

                                                     # saucer

        return 8
    elif wavecounter > 90 and wavecounter <= 100:

                                                     # enemy and drones

        return 9
    elif wavecounter > 100 and wavecounter <= 110:

                                                     # station

        return 10
    elif wavecounter > 110:

                             # boss

        return 11


def main():
    gameOver = False
    menuExit = False
    stageStart = False
    bossStage = False
    gameOverScreen = False

    menuselect = -1
    menuhighlight = 0

    wavecounter = 0
    wave = 0

    starfield1 = stars(1,white,50,5)
    starfield2 = stars(1,(150,150,150),75,3)
    starfield3 = stars(1,(75,75,75),200,1)

    bullets = pygame.sprite.Group()
    enemybullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    starships = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    shields = pygame.sprite.Group()
    drones = pygame.sprite.Group()
    saucers = pygame.sprite.Group()
    station = pygame.sprite.Group()
    healthpacks = pygame.sprite.Group()

    bullet.containers = bullets
    
    starship.containers =starships

    enemybullet.containers = enemybullets
    enemy.containers = enemies
    explosion.containers = explosions
    enemydrone.containers = drones
    enemysaucer.containers = saucers
    enemystation.containers = station
    
    starship.containers=starships
    
    healthpack.containers = healthpacks

    user = player()
    pygame.display.set_caption('PyGalaxian')
    bg_music = pygame.mixer.Sound('Sprites/bg_music.ogg')
    boss_music = pygame.mixer.Sound('Sprites/boss_music.ogg')

    (logoimage, logorect) = load_image('gamelogo.png', -1, -1, -1)
    logorect.left = width / 2 - logorect.width / 2
    logorect.top = height / 2 - logorect.height * 5 / 4

    while not gameOver:
        while not menuExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menuExit = True
                    gameOver = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key \
                        == pygame.K_UP:
                        menuhighlight += 1
                    elif event.key == pygame.K_RETURN:
                        menuselect = menuhighlight % 2

            if menuselect == 0:
                stageStart = True
                menuExit = True
                bg_music.play(-1)
            elif menuselect == 1:
                pygame.quit()
                quit()
            else:
                pass

            screen.fill(sky)
            starfield1.drawstars()
            starfield2.drawstars()
            starfield3.drawstars()
            user.drawplayer()
            screen.blit(logoimage, logorect)

            displaytext('Play', 32, width / 2 - 20, height * 3 / 4
                        - 40, white)
            displaytext('Exit', 32, width / 2 - 20, height * 3 / 4,
                        white)
            displaytext('PyGalaxian version 1.0', 12, width - 80, height - 20,
                        white)
            displaytext('Made by: Shivam Shekhar', 12, width - 80, height - 10,
                        white)

            if menuhighlight % 2 == 0:
                screen.blit(pygame.transform.scale(user.image, (25,
                            25)), [width / 2 - 100, height * 3 / 4
                            - 55, 15, 15])
            elif menuhighlight % 2 == 1:
                screen.blit(pygame.transform.scale(user.image, (25,
                            25)), [width / 2 - 100, height * 3 / 4
                            - 15, 15, 15])
            pygame.display.update()
            clock.tick(FPS)

        while stageStart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stageStart = False
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    user.trigger = 1
                    if event.key == pygame.K_LEFT:
                        user.speed = -2
                    elif event.key == pygame.K_RIGHT:
                        user.speed = 2
                    elif event.key == pygame.K_UP:
                        user.fire = 1
                    elif event.key == pygame.K_ESCAPE:
                    	quit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key \
                        == pygame.K_RIGHT:
                        user.trigger = 2
                        user.speed = 0
                    if event.key == pygame.K_UP:
                        user.fire = 0

            if wavecounter % 500 == 499 and random.randrange(0, 2) == 1 \
                and len(healthpacks) < 1:
                healthpack(random.randrange(0, width - 50), 0, 10)

            if random.randrange(0, 8) == 1 and len(enemies) < 10 \
                and (wave == 0 or wave == 5 or wave == 6 or wave == 9):
                enemy(random.randrange(0, 4))
                
            if random.randrange(0, 10) == 1 and len(starships) < 10 \
                and (wave == 2 or wave == 6 or wave == 8 or wave == 9):
                starship(random.randrange(0, 4))
        
            if random.randrange(0, 20) == 1 and len(saucers) < 3 \
                and (wave == 1 or wave == 5 or wave == 7 or wave == 8):
                enemysaucer(random.randrange(0, width - 50))

            if random.randrange(0, 30) == 21 and len(drones) < 2 \
                and (wave == 2 or wave == 4 or wave == 7 or wave == 9):
                if len(drones) > 0:
                    for drone in drones:
                        if drone.rect.left < width / 2:
                            enemydrone(random.randrange(width / 2 + 60,
                                    width - 60))
                        else:
                            enemydrone(random.randrange(0, width / 2
                                    - 60))
                else:
                    enemydrone(random.randrange(0, width - 60))

            
                

            if wave == 11 and len(enemies) == 0 and len(saucers) == 0 \
                and len(station) == 0 and len(drones) == 0:
                user.isautopilot = True
                bg_music.fadeout(6000)
                if user.rect.top <= -1*user.rect.height:
                    wave = 12

            if wave == 12:
                bossStage = True
                stageStart = False
                finalboss = boss()
                user.health += 80
                user.rect.left = width / 2
                user.rect.top = size[1] - 100
                user.isautopilot = False
                user.movement = [0, 0]
                boss_music.play(-1)

            for ship in enemies:
                cpumove(ship, user)

            for ship in starships:
                cpumove(ship, user)

                
            for enemyhit in pygame.sprite.groupcollide(enemies,
                    bullets, 0, 1):
                enemyhit.health -= 1
                if enemyhit.health <= 0:
                    user.kills += 1
                    user.score += 1

            for starshiphit in pygame.sprite.groupcollide(starships,
                    bullets, 0, 1):
                starshiphit.health -= 1
                if starshiphit.health <= 0:
                    user.kills += 1
                    user.score += 1
                    
            for dronehit in pygame.sprite.groupcollide(drones, bullets,
                    0, 1):
                dronehit.health -= 1
                if dronehit.health <= 0:
                    user.kills += 1
                    user.score += 10

            for saucerhit in pygame.sprite.groupcollide(saucers,
                    bullets, 0, 1):
                saucerhit.health -= 1
                if saucerhit.health <= 0:
                    user.kills += 1
                    user.score += 5

            for stationhit in pygame.sprite.groupcollide(station,
                    bullets, 0, 1):
                stationhit.health -= 1
                if stationhit.health <= 0:
                    user.kills += 1
                    user.score += 25
                    healthpack(stationhit.rect.centerx,
                               stationhit.rect.centery, 20)

            for firedbullet in pygame.sprite.spritecollide(user,
                    enemybullets, 1):
                user.health -= 1

            for enemycollided in enemies:
                if pygame.sprite.collide_mask(user, enemycollided):
                    user.health -= 2
                    enemycollided.health -= enemycollided.health

            for starshipcollided in starships:
                if pygame.sprite.collide_mask(user, starshipcollided):
                    user.health -= 4
                    starshipcollided.health -= starshipcollided.health

            for dronecollided in drones:
                if pygame.sprite.collide_mask(user, dronecollided):
                    user.health -= 10
                    dronecollided.health -= dronecollided.health

            for saucercollided in saucers:
                if pygame.sprite.collide_mask(user, saucercollided):
                    user.health -= 4
                    saucercollided.health -= saucercollided.health

            for stationcollided in station:
                if pygame.sprite.collide_mask(user, stationcollided):
                    user.health -= 50
                    stationcollided.health -= stationcollided.health

            for health_pack in healthpacks:
                if pygame.sprite.collide_mask(user, health_pack):
                    user.health += health_pack.health
                    health_pack.health -= health_pack.health

            if user.health <= 0:
                gameOverScreen = True
                stageStart = False

            user.update()
            user.checkbounds()

            screen.fill(sky)
            starfield1.drawstars()
            starfield2.drawstars()
            starfield3.drawstars()

            if user.health > 0:
                showhealthbar(user.health, green, [100, height - 20,
                              user.health * 4, 10], 4)
            displaytext('HEALTH', 22, 50, height - 15, white)
            displaytext('Score:', 22, width - 100, 15, white)
            displaytext(str(user.score), 22, width - 35, 15, white)
            user.drawplayer()

            enemies.update()
            bullets.update()
            enemybullets.update()
            explosions.update()
            drones.update()
            saucers.update()
            station.update()
            healthpacks.update()
            starships.update()

            bullets.draw(screen)
            enemybullets.draw(screen)
            enemies.draw(screen)
            explosions.draw(screen)
            drones.draw(screen)
            saucers.draw(screen)
            station.draw(screen)
            healthpacks.draw(screen)
            starships.draw(screen)
            
            wave = storyboard(wavecounter)

            wavecounter += 1

            pygame.display.update()

            clock.tick(FPS)

            moveplayer(user)

            print (
                wavecounter,
                wave,
                user.kills,
                user.health,
                user.rect.left,
                user.movement[0],
                user.rect.right,
                )

        while bossStage:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    bossStage = False
                if event.type == pygame.KEYDOWN:
                    user.trigger = 1
                    if event.key == pygame.K_LEFT:
                        user.speed = -2
                    elif event.key == pygame.K_RIGHT:
                        user.speed = 2
                    elif event.key == pygame.K_UP:
                        user.fire = 1
                    elif event.key == pygame.K_ESCAPE:
                    	quit()


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key \
                        == pygame.K_RIGHT:
                        user.trigger = 2
                        user.speed = 0
                    if event.key == pygame.K_UP:
                        user.fire = 0

            bossmove(finalboss, user)

            for ship in enemies:
                cpumove(ship, user)

            for userbullet in bullets:
                if pygame.sprite.collide_mask(finalboss, userbullet):
                    if finalboss.health > 2:
                        finalboss.health -= 1
                    else:
                        bossStage = False
                        gameOverScreen = True
                        user.score += 200
                        user.won = True
                    userbullet.kill()

            for enemyhit in pygame.sprite.groupcollide(enemies,
                    bullets, 0, 1):
                enemyhit.health -= 1
                if enemyhit.health <= 0:
                    user.kills += 1
                    user.score += 1

            for starshiphit in pygame.sprite.groupcollide(starships,
                    bullets, 0, 1):
                starshiphit.health -= 2
                if starshiphit.health <= 0:
                    user.kills += 1
                    user.score += 3

            for dronehit in pygame.sprite.groupcollide(drones, bullets,
                    0, 1):
                dronehit.health -= 1
                if dronehit.health <= 0:
                    user.kills += 1
                    user.score += 10

            for saucerhit in pygame.sprite.groupcollide(saucers,
                    bullets, 0, 1):
                saucerhit.health -= 1
                if saucerhit.health <= 0:
                    user.kills += 1
                    user.score += 5

            for firedbullet in pygame.sprite.spritecollide(user,
                    enemybullets, 1):
                user.health -= 1

            for enemycollided in enemies:
                if pygame.sprite.collide_mask(user, enemycollided):
                    user.health -= 2
                    enemycollided.health -= enemycollided.health

            for dronecollided in drones:
                if pygame.sprite.collide_mask(user, dronecollided):
                    user.health -= 10
                    dronecollided.health -= dronecollided.health

            for saucercollided in saucers:
                if pygame.sprite.collide_mask(user, saucercollided):
                    user.health -= 4
                    saucercollided.health -= saucercollided.health

            if user.health <= 0:
                gameOverScreen = True
                bossStage = False

            user.update()
            user.checkbounds()

            screen.fill(sky)
            starfield1.drawstars()
            starfield2.drawstars()
            starfield3.drawstars()

            if user.health > 0:
                showhealthbar(user.health, green, [100, height - 20,
                              user.health * 4, 10], 4)
            displaytext('HEALTH', 22, 50, height - 15, white)

            if finalboss.health > 0:
                showhealthbar(finalboss.health, red, [100, 20,
                              finalboss.health * 0.8, 10], 0.8)
            displaytext('BOSS', 22, 50, 25, white)

            displaytext('Score:', 22, width - 100, 15, white)
            displaytext(str(user.score), 22, width - 35, 15, white)

            user.drawplayer()

            enemies.update()
            bullets.update()
            enemybullets.update()
            drones.update()
            saucers.update()
            explosions.update()
            finalboss.update()
            starships.update()
            
            bullets.draw(screen)
            enemybullets.draw(screen)
            enemies.draw(screen)
            starships.draw(screen)
            drones.draw(screen)
            saucers.draw(screen)
            explosions.draw(screen)
            finalboss.drawplayer()
            
            pygame.display.update()
            clock.tick(FPS)
            moveplayer(user)

        while gameOverScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOverScreen = False
                    gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameOverScreen = False
                    gameOver = True

            screen.fill(sky)
            starfield1.drawstars()
            starfield2.drawstars()
            starfield3.drawstars()

            if user.won == False:
                displaytext('Game Over', 26, width / 2 - 30, height
                            / 2, white)
            else:
                displaytext('Congratulations! You Won!', 26, width / 2
                            - 30, height / 2, white)

            displaytext('Your score: ', 26, width / 2 - 40, height / 2
                        + 40, white)
            displaytext(str(user.score), 26, width / 2 + 50, height / 2
                        + 43, white)
            displaytext('Press Enter to exit...', 14, width / 2 - 30,
                        height / 2 + 90, white)
            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
    quit()


main()
