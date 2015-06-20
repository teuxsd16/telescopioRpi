#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Apr 27, 2015

@author: Israel P. Siqueira
'''

import asyncore, socket
import logging
from time import time
from bitstring import ConstBitStream
import coords
from motor import Motor
import RPi.GPIO as GPIO
from coords import transformar_coordenadas


logging.basicConfig(level=logging.DEBUG, format="%(filename)s: %(funcName)s - %(levelname)s: %(message)s")
 

#  Gerencia a Thread de conexao com o Stellarium
class Telescope_Channel(asyncore.dispatcher):

    def __init__(self, conn_sock):
        self.az_anterior = 0
        self.alt_anterior = 0
        self.is_writable = False
        self.buffer = ''
        asyncore.dispatcher.__init__(self, conn_sock)
        
    
    def readable(self):
        return True
 
    
    def writable(self):
        return self.is_writable
 
    
    def handle_close(self):
        logging.debug("Desconectado")
        self.close()
 
   
    def handle_read(self):
       
        data0 = self.recv(160);
        if data0:            
            data = ConstBitStream(bytes=data0, length=160)
            # print "All: %s" % data.bin
 
            msize = data.read('intle:16')
            mtype = data.read('intle:16')
            mtime = data.read('intle:64')
 
            # RA: 
            ant_pos = data.bitpos
            ra = data.read('hex:32')
            data.bitpos = ant_pos
            ra_uint = data.read('uintle:32')
 
            # DEC:
            ant_pos = data.bitpos
            dec = data.read('hex:32')
            data.bitpos = ant_pos
            dec_int = data.read('intle:32')
             
            logging.debug("Size: %d, Type: %d, Time: %d, RA: %d (%s), DEC: %d (%s)" % (msize, mtype, mtime, ra_uint, ra, dec_int, dec))
                       
            (ra, dec, time) = coords.int_2_rads(ra_uint, dec_int, mtime)

            x = transformar_coordenadas(dec, ra)
            az,alt = x.get_azi_alt()

            #instancia o motor de azimute nos pinos 12, 16, 20 e 21 do RPi
            motor_az = Motor([31,33,35,37])
            motor_az.rpm = 5
            motor_az.mode = 2
            motor_az.move_to(az-self.az_anterior)
            self.az_anterior = az

            #instancia o motor de azimute nos pinos 32, 36, 38 e 40 do RPi
            motor_alt = Motor([32,36,38,40])
            motor_alt.rpm = 5
            motor_alt.mode = 3
            motor_alt.move_to(alt-self.alt_anterior)
            self.alt_anterior = alt

            logging.debug("Azimute: %d, Altitude: %d" % (az,alt))
            
            # envia as cordenadas para o Stellarium
            self.act_pos(ra, dec)
 
    # Atualiza a posicao do telescopio no Stellarium
    def act_pos(self, ra, dec):
        (ra_p, dec_p) = coords.rad_2_stellarium_protocol(ra, dec)
        
        for i in range(10):
            self.move(ra_p, dec_p)
 
    # # Envia as coordenadas para o Stellarium novamente
    def move(self, ra, dec):
        msize = '0x1800'
        mtype = '0x0000'
        localtime = ConstBitStream(str.replace('int:64=%r' % time(), '.', ''))
        # print "move: (%d, %d)" % (ra, dec)
 
        sdata = ConstBitStream(msize) + ConstBitStream(mtype)
        sdata += ConstBitStream(intle=localtime.intle, length=64) + ConstBitStream(uintle=ra, length=32)
        sdata += ConstBitStream(intle=dec, length=32) + ConstBitStream(intle=0, length=32)
        self.buffer = sdata
        self.is_writable = True
        self.handle_write()
 
    def handle_write(self):
        self.send(self.buffer.bytes)
        self.is_writable = False
 


class Telescope_Server(asyncore.dispatcher):
 
   
    def __init__(self, port=10001):
        asyncore.dispatcher.__init__(self, None)
        
        self.tel = None
        self.port = port
 
   
    def run(self):
        logging.info(self.__class__.__name__ + " Servidor Rodando.")
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('192.168.25.128', self.port))
        self.listen(1)
        self.connected = False
        asyncore.loop()
 
   
    def handle_accept(self):
        self.conn, self.addr = self.accept()
        logging.debug('%s Conectado ao Stellarium', self.addr)
        self.connected = True
        self.tel = Telescope_Channel(self.conn)
 
  
    def close_socket(self):
        if self.connected:
            self.conn.close()
 
# Run a Telescope Server
if __name__ == '__main__':
    try:
        Server = Telescope_Server()
        Server.run()
    except KeyboardInterrupt:
        GPIO.cleanup()
        logging.debug("\nDesconectado!")
