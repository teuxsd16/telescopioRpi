#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from datetime import date, datetime

import logging
from math import radians, acos, sin, cos, pi, degrees, asin
import math
from time import strftime, localtime


# \brief Biblioteca de funcoes para auxiliar na conversao de unidades.
#
#  Contem algumas funções necessárias para transformar os dados recebidos e enviados ao stellarium.
## Converte de radianos para horas (float)
# (rads * 180)/(15 * pi)
#
# \param rads Radianos em float
# \return retorna um float com o valor convertido em horas
def rad_2_hour(rads):
    h = round( (rads * 180)/(15 * math.pi), 6)
    if h > 24.0:
        h = h - 24.0
    if h < 0.0:
        h = 24.0 + h
    return h
 
 
## Transforms degrees from float to string format.
#
# \param deg Degrees in float format
# \return Degrees in string format ("DºM'S''")
def deg_2_degStr(deg):
 
    neg = False
    if deg < 0.0:
        neg = True
        deg = 0.0 - deg
 
    ndeg = math.floor(float(deg))
    nmins = (deg - ndeg) * 60
    mins = math.floor(nmins)
    secs = round( (nmins - mins) * 60 )
 
    if mins == 60:
        ndeg += 1
        mins = 0
    if secs == 60:
        mins += 1
        secs = 0
 
    if neg:
        ndeg = 0.0 - ndeg
 
    return "%dº%d'%d''" % (ndeg, mins, secs)
 

 
## Transforms hours from float to string format
#
# \param hours Hours in float format
# \return Hours in string format ("HhMmSSs")
def hour_2_hourStr(hours):
    (h, m, s) = hour_min_sec(hours)
    return '%dh%dm%00.1fs' % (h, m, s)
 
## From hours in float format, to a list with number of hours, minutes and seconds
#
# \param hours Hours in float format
# \return List with (hours, minutes, seconds)
def hour_min_sec(hours):
    h = math.floor(hours)
 
    hours_m = (hours - h)*60.0
    m = math.floor(hours_m)
 
    s = (hours_m - m)*60.0
 
    #Evitando los .60..
    if s >= 59.99:
        s = 0
        m += 1
    if m >= 60:
        m = 60-m
        h += 1
 
    return (h, m, s)
 
## From degrees in float format, to a list with number of degrees, minutes and seconds
#
# \param degs Degrees in float format
# \return List with (degrees, minutes, seconds)
def grad_min_sec(degs):
    #Evitando operaciones con valores negativos..
    to_neg = False
    if degs < 0:
        degs = math.fabs(degs)
        to_neg = True
 
    d = math.floor(degs)
 
    degs_m = (degs - d)*60.0
    m = math.floor(degs_m)
 
    s = (degs_m - m)*60.0
 
    #Evitando el .60..
    if s >= 59.99:
        s = 0
        m += 1
    if m >= 60.0:
        m = 60.0-m
        d += 1
 
    if to_neg:
        d = -d;
 
    return (d, m, s)

## Transforms the values obtained from "Stellarium Telescope Protocol", to a list with each value in string format
# ("HhMmSSs", "DºM'S''", "HhMmSs")
#
# \param ra Right ascension
# \param dec Declination
# \param mtime Timestamp in microseconds
# \return List with (Right ascension, declination, time) => ("HhMmSSs", "DºM'S''", "HhMmSs")
def eCoords2str(ra, dec, mtime):
    return (ra, dec, hour_2_hourStr(ra), deg_2_degStr(dec)), strftime("%Hh%Mm%Ss", localtime(mtime))

def int_2_rads(ra_uint, dec_int, mtime):
    ra = ra_uint*12.0/2147483648
    dec = dec_int*90.0/1073741824
    time_s = math.floor(mtime / 1000000)
    return (ra,dec,time_s)

## Transforms coordinates from radians to the "Stellarium Telescope Protocol" format
#
# \param ra Right ascension (float)
# \param dec Declination (float)
# \return List with (Right ascension, Declination) in the "Stellarium Telescope Protocol" format
def rad_2_stellarium_protocol(ra, dec):
    
    logging.debug("(RA/hours, DEC/degrees): (%f, %f) -> (%s, %s)" % (ra, dec, hour_2_hourStr(ra), deg_2_degStr(dec)))
 
    return (int(ra*(2147483648/12.0)), int(dec*(1073741824/90.0)))

class transformar_coordenadas:
    
    def __init__(self, dec, ra):
        self.today = datetime.utcnow()
        self.lgt = -0.8299860897981474
        self.lat = -0.2699099153798746
        self.dec = radians(dec)
        self.ra = radians(ra * 15)
    
    def get_azi_alt(self):
        return (transformar_coordenadas.get_horizontal_angle(self), transformar_coordenadas.get_vertical_angle(self))
    
    # restorna angulo horizontal/azimute
    def get_horizontal_angle(self):
        
        dec = self.dec
        lat = self.lat
        hra = transformar_coordenadas.hour_angle(self)
        alt = transformar_coordenadas.get_vertical_angle(self)
        
        hra = radians(hra)
        alt = radians(alt)
        
        res  =  acos ( ( sin(dec) - sin(lat) * sin(alt) ) /
                  ( cos(lat) * cos(alt) ) )
        
        if sin(hra) > 0.0:
            res = 2.0 * pi - res
        
        return degrees(res)
    
    # retorna angulo vertical/altura
    def get_vertical_angle(self):
        
        lat = self.lat
        dec = self.dec
        hra = transformar_coordenadas.hour_angle(self)
        
        hra = radians(hra)
        
        res  =  asin ( sin(dec) * sin(lat) +
                  cos(dec) * cos(lat) * cos(hra) )
        
        return degrees(res)
    
    # retorna a hora do dia em horas decimais    
    def ut(self):
        today = self.today
        
        dH = float(today.hour)
        dM = float(today.minute) / 60
        dS = float(today.second) / 3600
        
        return dH + dM + dS
    
    # retorna o LMST (Local Mean Sidereal Time)
    def lmst(self):
        
        lgt = self.lgt
        
        ## ut -> hora em valor decimal, ex: 12.5 = 12h30m
        ut = transformar_coordenadas.ut(self)
        
        # epoch equivale a data do J2000
        epoch = date(2000, 1, 1) 
        # data atual
        today = date.today()
        
        # subtrai os dias que passaram desde J2000 ate data atual
        days = (today - epoch).days
        # soma a hora decimal do ut para virar uma fracao do dia
        days = days + transformar_coordenadas.ut(self) / 24
        
        res = 100.46 + (0.985647 * days) + degrees(lgt) + (15 * ut)
        mod = int(res) / 360
        
        return res - (mod * 360) 
    
    # retorna a hora angular
    def hour_angle(self):
        ra = self.ra
        lmst = transformar_coordenadas.lmst(self)
        
        hra = lmst - degrees(ra)
        
        if hra < 0:
            hra = 360 + hra
        
        return hra
    
    def hour_to_radians(self, hour):
        return radians(hour * 15)         
        
