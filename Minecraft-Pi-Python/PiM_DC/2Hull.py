from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
woodp = 5
air = 0
wood = 17,3
sslab = 44,2
def init():
	mc = Minecraft.create("10.183.13.13",4711)
	x, y, z = mc.player.getPos()
	return mc
	
def ship(mc,x,y,z):
	mc.setBlocks(x-1,y,z-44,x+1,y,z+44,woodp)#Hull
	mc.setBlocks(x,y,z,x,y+3,z,wood)
	mc.setBlocks(x-3,y+1,z-44,x+3,y+1,z+44,woodp)
	mc.setBlocks(x-6,y+2,z-44,x+6,y+2,z+44,woodp)
	mc.setBlocks(x-2,y+2,z-44,x+2,y+2,z+44,air)
	mc.setBlocks(x-8,y+3,z-44,x+8,y+3,z+44,woodp)
	mc.setBlocks(x-5,y+3,z-44,x+5,y+3,z+44,air)
	mc.setBlocks(x-9,y+4,z-44,x+9,y+4,z+44,woodp)
	mc.setBlocks(x-7,y+4,z-44,x+7,y+4,z+44,air)
	mc.setBlocks(x-10,y+5,z-44,x+10,y+5,z+44,woodp)
	mc.setBlocks(x-8,y+5,z-44,x+8,y+5,z+44,air)
	mc.setBlocks(x-11,y+6,z-44,x+11,y+6,z+44,woodp)
	mc.setBlocks(x-9,y+6,z-44,x+9,y+6,z+44,air)
	mc.setBlocks(x-11,y+7,z-44,x+11,y+9,z+44,woodp)
	mc.setBlocks(x-10,y+7,z-44,x+10,y+9,z+44,air)
	mc.setBlocks(x-12,y+9,z-44,x+12,y+9,z+44,woodp)
	mc.setBlocks(x-10,y+9,z-44,x+10,y+9,z+44,air)
	mc.setBlocks(x-12,y+10,z-44,x+12,y+12,z+44,woodp)
	mc.setBlocks(x-11,y+10,z-44,x+11,y+12,z+44,air)
	mc.setBlocks(x-13,y+13,z-44,x+13,y+17,z+44,woodp)
	mc.setBlocks(x-13,y+17,z-44,x+13,y+17,z+44,sslab)
	mc.setBlocks(x-11,y+13,z-44,x+11,y+13,z+44,air)
	mc.setBlocks(x-12,y+14,z-44,x+12,y+17,z+44,air)
	
	mc.setBlocks(x-13,y+15,z-44,x+13,y+15,z+44,woodp)#deck
	
def hull(mc,x,y,z):
	mc.setBlocks(x,y,z,x,y,z+15,woodp)#0
	mc.setBlocks(x-1,y,z,x+1,y,z+13,woodp)
	mc.setBlocks(x-4,y+1,z+11,x+4,y+1,z+11,woodp)#1
	mc.setBlocks(x-3,y+1,z+13,x+3,y+1,z+13,woodp)
	mc.setBlocks(x-2,y+1,z+14,x+2,y+1,z+14,woodp)
	mc.setBlocks(x-1,y+1,z+16,x+2,y+1,z+16,woodp)
	mc.setBlocks(x,y+1,z+18,x,y+1,z+18,woodp)
	mc.setBlocks(x-7,y+2,z+3,x+7,y+2,z+3,woodp)#2
	mc.setBlocks(x-6,y+2,z+8,x+6,y+2,z+8,woodp)
	mc.setBlocks(x-5,y+2,z+10,x+5,y+2,z+10,woodp)
	mc.setBlocks(x-4,y+2,z+13,x+4,y+2,z+13,woodp)
	mc.setBlocks(x-3,y+2,z+15,x+3,y+2,z+15,woodp)
	mc.setBlocks(x-2,y+2,z+16,x+2,y+2,z+16,woodp)
	mc.setBlocks(x-1,y+2,z+17,x+1,y+2,z+17,woodp)
	mc.setBlocks(x,y+2,z+20,x,y,z,woodp)
	mc.setBlocks(x-8,y+3,z+3,x+8,y+3,z+3,woodp)#3
	mc.setBlocks(x-7,y+3,z+8,x+7,y+3,z+8,woodp)
	mc.setBlocks(x-7,y+3,z+3,x+7,y+3,z+3,air)
	mc.setBlocks(x-6,y+3,z+11,x+6,y+3,z+11,woodp)
	mc.setBlocks(x-6,y+3,z+8,x+6,y+3,z+8,air)
	mc.setBlocks(x-5,y+3,z+14,x+5,y+3,z+14,woodp)
	mc.setBlocks(x-5,y+3,z+10,x+5,y+3,z+20,air)
	mc.setBlocks(x-4,y+3,z+16,x+4,y+3,z+16,woodp)
	mc.setBlocks(x-4,y+3,z+13,x+4,y+3,z+13,air)
	mc.setBlocks(x-3,y+3,z+18,x+3,y+3,z+18,woodp)
	mc.setBlocks(x-3,y+3,z+15,x+3,y+3,z+15,air)
	mc.setBlocks(x-2,y+3,z+19,x+2,y+3,z+19,woodp)
	mc.setBlocks(x-2,y+3,z+16,x+2,y+3,z+16,air)
	mc.setBlocks(x-1,y+3,z+20,x+1,y+3,z+20,woodp)
	mc.setBlocks(x-1,y+3,z+17,x+1,y+3,z+17,air)
	mc.setBlocks(x,y+3,z+21,x,y,z,woodp)
	mc.setBlocks(x,y+3,z+20,x,y,z,air)
	mc.setBlocks(x-9,y+4,z+2,x+9,y+4,z+2,woodp)#4
	mc.setBlocks(x-8,y+4,z+8,x+8,y+4,z+8,woodp)
	mc.setBlocks(x-8,y+4,z+2,x+8,y+4,z+2,air)
	mc.setBlocks(x-7,y+4,z+12,x+7,y+4,z+12,woodp)
	mc.setBlocks(x-7,y+4,z+8,x+7,y+4,z+8,air)
	mc.setBlocks(x-6,y+4,z+15,x+6,y+4,z+15,woodp)
	mc.setBlocks(x-6,y+4,z+11,x+6,y+4,z+11,air)
	mc.setBlocks(x-5,y+4,z+17,x+5,y+4,z+17,woodp)
	mc.setBlocks(x-5,y+4,z+14,x+5,y+4,z+14,air)
	mc.setBlocks(x-4,y+4,z+19,x+4,y+4,z+19,woodp)
	mc.setBlocks(x-4,y+4,z+16,x+4,y+4,z+16,air)
	mc.setBlocks(x-3,y+4,z+20,x+3,y+4,z+20,woodp)
	mc.setBlocks(x-3,y+4,z+18,x+3,y+4,z+18,air)
	mc.setBlocks(x-2,y+4,z+21,x+2,y+4,z+21,woodp)
	mc.setBlocks(x-2,y+4,z+19,x+2,y+4,z+19,air)
	mc.setBlocks(x-1,y+4,z+22,x+1,y+4,z+22,woodp)
	mc.setBlocks(x-1,y+4,z+20,x+1,y+4,z+20,air)
	mc.setBlocks(x,y+4,z+23,x,y+4,z+23,woodp)
	mc.setBlocks(x,y+4,z+22,x,y+4,z+22,air)
	mc.setBlocks(x-9,y+5,z+9,x+9,y+5,z+9,woodp)#5
	mc.setBlocks(x-8,y+5,z+12,x+8,y+5,z+12,woodp)
	mc.setBlocks(x-8,y+5,z+8,x+8,y+5,z+8,air)
	mc.setBlocks(x-7,y+5,z+15,x+7,y+5,z+15,woodp)
	mc.setBlocks(x-7,y+5,z+12,x+7,y+5,z+12,air)
	mc.setBlocks(x-6,y+5,z+17,x+6,y+5,z+17,woodp)
	mc.setBlocks(x-6,y+5,z+15,x+6,y+5,z+15,air)
	mc.setBlocks(x-5,y+5,z+19,x+5,y+5,z+19,woodp)
	mc.setBlocks(x-5,y+5,z+17,x+5,y+5,z+17,air)
	mc.setBlocks(x-4,y+5,z+20,x+4,y+5,z+20,woodp)
	mc.setBlocks(x-4,y+5,z+19,x+4,y+5,z+19,air)
	mc.setBlocks(x-3,y+5,z+21,x+3,y+5,z+21,woodp)
	mc.setBlocks(x-3,y+5,z+20,x+3,y+5,z+20,air)
	mc.setBlocks(x-2,y+5,z+22,x+2,y+5,z+22,woodp)
	mc.setBlocks(x-2,y+5,z+21,x+2,y+5,z+21,air)
	mc.setBlocks(x-1,y+5,z+23,x+1,y+5,z+23,woodp)
	mc.setBlocks(x-1,y+5,z+22,x+1,y+5,z+22,air)
	mc.setBlocks(x,y+5,z+24,x,y,z,woodp)
	mc.setBlocks(x,y+5,z+23,x,y,z,air)
	mc.setBlocks(x-10,y+6,z+7,x+10,y+6,z+7,woodp)#6
	mc.setBlocks(x-9,y+6,z+10,x+9,y+6,z+7,woodp)
	mc.setBlocks(x-9,y+6,z+7,x+9,y+6,z+7,air)
	mc.setBlocks(x-8,y+6,z+15,x+8,y+6,z+15,woodp)
	mc.setBlocks(x-8,y+6,z+12,x+8,y+6,z+12,air)
	mc.setBlocks(x-7,y+6,z+17,x+7,y+6,z+17,woodp)
	mc.setBlocks(x-7,y+6,z+15,x+7,y+6,z+15,air)
	mc.setBlocks(x-6,y+6,z+19,x+6,y+6,z+19,woodp)
	mc.setBlocks(x-6,y+6,z+19,x+6,y+6,z+19,air)
	mc.setBlocks(x-5,y+6,z+20,x+5,y+6,z+20,woodp)
	mc.setBlocks(x-5,y+6,z+19,x+5,y+6,z+19,air)
	mc.setBlocks(x-4,y+6,z+21,x+4,y+6,z+21,woodp)
	mc.setBlocks(x-4,y+6,z+20,x+4,y+6,z+20,air)
	mc.setBlocks(x-3,y+6,z+22,x+3,y+6,z+22,woodp)
	mc.setBlocks(x-3,y+6,z+21,x+3,y+6,z+21,air)
	mc.setBlocks(x-2,y+6,z+23,x+2,y+6,z+23,woodp)
	mc.setBlocks(x-2,y+6,z+22,x+2,y+6,z+22,air)
	mc.setBlocks(x-1,y+6,z+24,x+1,y+6,z+24,woodp)
	mc.setBlocks(x-1,y+6,z+23,x+1,y+6,z+23,air)
	mc.setBlocks(x,y+6,z+25,x,y+6,z,woodp)
	mc.setBlocks(x,y+6,z+24,x,y+6,z,air)
	mc.setBlocks(x-10,y+7,z+10,x+10,y+7,z+10,woodp)#7
	mc.setBlocks(x-9,y+7,z+13,x+9,y+7,z+13,woodp)
	mc.setBlocks(x-9,y+7,z+10,x+9,y+7,z+10,air)
	mc.setBlocks(x-8,y+7,z+16,x+8,y+7,z+16,woodp)
	mc.setBlocks(x-8,y+7,z+15,x+8,y+7,z+15,air)
	mc.setBlocks(x-7,y+7,z+18,x+7,y+7,z+18,woodp)
	mc.setBlocks(x-7,y+7,z+17,x+7,y+7,z+17,air)
	mc.setBlocks(x-6,y+7,z+20,x+6,y+7,z+20,woodp)
	mc.setBlocks(x-6,y+7,z+19,x+6,y+7,z+19,air)
	mc.setBlocks(x-5,y+7,z+21,x+5,y+7,z+21,woodp)
	mc.setBlocks(x-5,y+7,z+20,x+5,y+7,z+20,air)
	mc.setBlocks(x-4,y+7,z+22,x+4,y+7,z+22,woodp)
	mc.setBlocks(x-4,y+7,z+21,x+4,y+7,z+21,air)
	mc.setBlocks(x-3,y+7,z+23,x+3,y+7,z+23,woodp)
	mc.setBlocks(x-3,y+7,z+22,x+3,y+7,z+22,air)
	mc.setBlocks(x-2,y+7,z+24,x+2,y+7,z+24,woodp)
	mc.setBlocks(x-2,y+7,z+23,x+2,y+7,z+23,air)
	mc.setBlocks(x-1,y+7,z+25,x+1,y+7,z+25,woodp)
	mc.setBlocks(x-1,y+7,z+24,x+1,y+7,z+24,air)
	mc.setBlocks(x,y+7,z+26,x,y+7,z,woodp)
	mc.setBlocks(x,y+7,z+25,x,y+7,z,air)
	mc.setBlocks(x-11,y+8,z+6,x+11,y+8,z+6,woodp)#8
	mc.setBlocks(x-10,y+8,z+11,x+10,y+8,z+11,woodp)
	mc.setBlocks(x-10,y+8,z+6,x+10,y+8,z+6,air)
	mc.setBlocks(x-9,y+8,z+14,x+9,y+8,z+14,woodp)
	mc.setBlocks(x-9,y+8,z+13,x+9,y+8,z+13,air)
	mc.setBlocks(x-8,y+8,z+17,x+8,y+8,z+17,woodp)
	mc.setBlocks(x-8,y+8,z+16,x+8,y+8,z+16,air)
	mc.setBlocks(x-7,y+8,z+19,x+7,y+8,z+19,woodp)
	mc.setBlocks(x-7,y+8,z+18,x+7,y+8,z+18,air)
	mc.setBlocks(x-6,y+8,z+20,x+6,y+8,z+20,woodp)
	mc.setBlocks(x-6,y+8,z+19,x+6,y+8,z+19,air)
	mc.setBlocks(x-5,y+8,z+21,x+5,y+8,z+21,woodp)
	mc.setBlocks(x-5,y+8,z+20,x+5,y+8,z+20,air)
	mc.setBlocks(x-4,y+8,z+22,x+4,y+8,z+22,woodp)
	mc.setBlocks(x-4,y+8,z+21,x+4,y+8,z+21,air)
	mc.setBlocks(x-3,y+8,z+23,x+3,y+8,z+23,woodp)
	mc.setBlocks(x-3,y+8,z+22,x+3,y+8,z+22,air)
	mc.setBlocks(x-2,y+8,z+24,x+2,y+8,z+24,woodp)
	mc.setBlocks(x-2,y+8,z+23,x+2,y+8,z+23,air)
	mc.setBlocks(x-1,y+8,z+26,x+1,y+8,z+26,woodp)
	mc.setBlocks(x-1,y+8,z+25,x+1,y+8,z+25,air)
	mc.setBlocks(x,y+8,z+27,x,y,z,woodp)
	mc.setBlocks(x,y+8,z+26,x,y,z,air)
	mc.setBlocks(x-11,y+9,z+11,x+11,y+9,z+11,woodp)#9
	mc.setBlocks(x-10,y+9,z+12,x+10,y+9,z+12,woodp)
	mc.setBlocks(x-10,y+9,z+11,x+10,y+9,z+11,air)
	mc.setBlocks(x-9,y+9,z+15,x+9,y+9,z+15,woodp)
	mc.setBlocks(x-9,y+9,z+15,x+9,y+9,z+15,air)
	mc.setBlocks(x-8,y+9,z+18,x+8,y+9,z+18,woodp)
	mc.setBlocks(x-8,y+9,z+17,x+8,y+9,z+17,air)
	mc.setBlocks(x-7,y+9,z+20,x+7,y+9,z+20,woodp)
	mc.setBlocks(x-7,y+9,z+18,x+7,y+9,z+18,air)
	mc.setBlocks(x-6,y+9,z+21,x+6,y+9,z+21,woodp)
	mc.setBlocks(x-6,y+9,z+20,x+6,y+9,z+20,air)
	mc.setBlocks(x-5,y+9,z+22,x+5,y+9,z+22,woodp)
	mc.setBlocks(x-5,y+9,z+21,x+5,y+9,z+21,air)
	mc.setBlocks(x-4,y+9,z+23,x+4,y+9,z+23,woodp)
	mc.setBlocks(x-4,y+9,z+22,x+4,y+9,z+22,air)
	mc.setBlocks(x-3,y+9,z+24,x+3,y+9,z+24,woodp)
	mc.setBlocks(x-3,y+9,z+23,x+3,y+9,z+23,air)
	mc.setBlocks(x-2,y+9,z+25,x+2,y+9,z+25,woodp)
	mc.setBlocks(x-2,y+9,z+24,x+2,y+9,z+24,air)
	mc.setBlocks(x-1,y+9,z+27,x+1,y+9,z+27,woodp)
	mc.setBlocks(x-1,y+9,z+25,x+1,y+9,z+25,air)
	mc.setBlocks(x,y+9,z+28,x,y,z,woodp)
	mc.setBlocks(x,y+9,z+27,x,y,z,air)
	mc.setBlocks(x-11,y+10,z+12,x+11,y+10,z+12,woodp)#10
	mc.setBlocks(x-10,y+10,z+13,x+10,y+10,z+13,woodp)
	mc.setBlocks(x-10,y+10,z+12,x+10,y+10,z+12,air)
	mc.setBlocks(x-9,y+10,z+17,x+9,y+10,z+17,woodp)
	mc.setBlocks(x-9,y+10,z+15,x+9,y+10,z+15,air)
	mc.setBlocks(x-8,y+10,z+19,x+8,y+10,z+19,woodp)
	mc.setBlocks(x-8,y+10,z+17,x+8,y+10,z+17,air)
	mc.setBlocks(x-7,y+10,z+20,x+7,y+10,z+20,woodp)
	mc.setBlocks(x-7,y+10,z+19,x+7,y+10,z+19,air)
	mc.setBlocks(x-6,y+10,z+21,x+6,y+10,z+21,woodp)
	mc.setBlocks(x-6,y+10,z+20,x+6,y+10,z+20,air)
	mc.setBlocks(x-5,y+10,z+23,x+5,y+10,z+23,woodp)
	mc.setBlocks(x-5,y+10,z+21,x+5,y+10,z+21,air)
	mc.setBlocks(x-4,y+10,z+24,x+4,y+10,z+24,woodp)
	mc.setBlocks(x-4,y+10,z+23,x+4,y+10,z+23,air)
	mc.setBlocks(x-3,y+10,z+25,x+3,y+10,z+25,woodp)
	mc.setBlocks(x-3,y+10,z+24,x+3,y+10,z+24,air)
	mc.setBlocks(x-2,y+10,z+26,x+2,y+10,z+26,woodp)
	mc.setBlocks(x-2,y+10,z+25,x+2,y+10,z+25,air)
	mc.setBlocks(x-1,y+10,z+27,x+1,y+10,z+27,woodp)
	mc.setBlocks(x-1,y+10,z+26,x+1,y+10,z+26,air)
	mc.setBlocks(x,y+10,z+28,x,y,z+28,woodp)
	mc.setBlocks(x,y+10,z+28,x,y,z+28,air)
	mc.setBlocks(x-12,y+11,z+7,x+12,y+11,z+7,woodp)#11
	mc.setBlocks(x-11,y+11,z+10,x+11,y+11,z+10,woodp)
	mc.setBlocks(x-11,y+11,z+7,x+11,y+11,z+7,air)
	mc.setBlocks(x-10,y+11,z+15,x+10,y+11,z+15,woodp)
	mc.setBlocks(x-10,y+11,z+12,x+10,y+11,z+12,air)
	mc.setBlocks(x-9,y+11,z+18,x+9,y+11,z+18,woodp)
	mc.setBlocks(x-9,y+11,z+15,x+9,y+11,z+15,air)
	mc.setBlocks(x-8,y+11,z+19,x+8,y+11,z+19,woodp)
	mc.setBlocks(x-8,y+11,z+18,x+8,y+11,z+18,air)
	mc.setBlocks(x-7,y+11,z+20,x+7,y+11,z+20,woodp)
	mc.setBlocks(x-7,y+11,z+19,x+7,y+11,z+19,air)
	mc.setBlocks(x-6,y+11,z+22,x+6,y+11,z+22,woodp)
	mc.setBlocks(x-6,y+11,z+20,x+6,y+11,z+20,air)
	mc.setBlocks(x-5,y+11,z+23,x+5,y+11,z+23,woodp)
	mc.setBlocks(x-5,y+11,z+22,x+5,y+11,z+22,air)
	mc.setBlocks(x-4,y+11,z+24,x+4,y+11,z+24,woodp)
	mc.setBlocks(x-4,y+11,z+23,x+4,y+11,z+23,air)
	mc.setBlocks(x-3,y+11,z+25,x+3,y+11,z+25,woodp)
	mc.setBlocks(x-3,y+11,z+24,x+3,y+11,z+24,air)
	mc.setBlocks(x-2,y+11,z+26,x+2,y+11,z+26,woodp)
	mc.setBlocks(x-2,y+11,z+25,x+2,y+11,z+25,air)
	mc.setBlocks(x-1,y+11,z+27,x+1,y+11,z+27,woodp)
	mc.setBlocks(x-1,y+11,z+26,x+1,y+11,z+26,air)
	mc.setBlocks(x,y+11,z+28,x,y,z,woodp)
	mc.setBlocks(x,y+10,z+27,x,y,z,air)
	mc.setBlocks(x-12,y+12,z+10,x+12,y+12,z+10,woodp)#12
	mc.setBlocks(x-11,y+12,z+11,x+11,y+12,z+11,woodp)
	mc.setBlocks(x-11,y+12,z+11,x+11,y+12,z+11,air)
	mc.setBlocks(x-10,y+12,z+26,x+10,y+12,z+26,woodp)
	mc.setBlocks(x-10,y+12,z+23,x+10,y+12,z+23,air)
	mc.setBlocks(x-9,y+12,z+28,x+9,y+12,z+28,woodp)
	mc.setBlocks(x-9,y+12,z+26,x+9,y+12,z+26,air)
	mc.setBlocks(x-8,y+12,z+20,x+8,y+12,z+20,woodp)
	mc.setBlocks(x-8,y+12,z+18,x+8,y+12,z+18,air)
	mc.setBlocks(x-7,y+12,z+22,x+7,y+12,z+22,woodp)
	mc.setBlocks(x-7,y+12,z+20,x+7,y+12,z+20,air)
	mc.setBlocks(x-6,y+12,z+24,x+6,y+12,z+24,woodp)
	mc.setBlocks(x-6,y+12,z+23,x+6,y+12,z+23,air)
	mc.setBlocks(x-5,y+12,z+25,x+5,y+12,z+25,woodp)
	mc.setBlocks(x-5,y+12,z+24,x+5,y+12,z+24,air)
	mc.setBlocks(x-4,y+12,z+26,x+4,y+12,z+26,woodp)
	mc.setBlocks(x-4,y+12,z+25,x+4,y+12,z+25,air)
	mc.setBlocks(x-3,y+12,z+27,x+3,y+12,z+27,woodp)
	mc.setBlocks(x-3,y+12,z+26,x+3,y+12,z+26,air)
	mc.setBlocks(x-2,y+12,z+28,x+2,y+12,z+28,woodp)
	mc.setBlocks(x-2,y+12,z+27,x+2,y+12,z+27,air)
	mc.setBlocks(x-1,y+12,z+29,x+1,y+12,z+29,woodp)
	mc.setBlocks(x-1,y+12,z+28,x+1,y+12,z+28,air)
	mc.setBlocks(x,y+12,z+30,x,y,z,woodp)
	mc.setBlocks(x,y+12,z+29,x,y,z,air)
	mc.setBlocks(x-12,y+13,z+11,x+12,y+13,z+11,woodp)#13
	mc.setBlocks(x-11,y+13,z+14,x+11,y+13,z+14,woodp)
	mc.setBlocks(x-11,y+13,z+11,x+11,y+13,z+11,air)
	mc.setBlocks(x-10,y+13,z+26,x+10,y+13,z+26,woodp)
	mc.setBlocks(x-10,y+13,z+24,x+10,y+13,z+24,air)
	mc.setBlocks(x-9,y+13,z+19,x+9,y+13,z+19,woodp)
	mc.setBlocks(x-9,y+13,z+16,x+9,y+13,z+16,air)
	mc.setBlocks(x-8,y+13,z+21,x+8,y+13,z+21,woodp)
	mc.setBlocks(x-8,y+13,z+19,x+8,y+13,z+19,air)
	mc.setBlocks(x-7,y+13,z+22,x+7,y+13,z+22,woodp)
	mc.setBlocks(x-7,y+13,z+21,x+7,y+13,z+21,air)
	mc.setBlocks(x-6,y+13,z+23,x+6,y+13,z+23,woodp)
	mc.setBlocks(x-6,y+13,z+22,x+6,y+13,z+22,air)
	mc.setBlocks(x-5,y+13,z+24,x+5,y+13,z+24,woodp)
	mc.setBlocks(x-5,y+13,z+23,x+5,y+13,z+23,air)
	mc.setBlocks(x-4,y+13,z+25,x+4,y+13,z+25,woodp)
	mc.setBlocks(x-4,y+13,z+24,x+4,y+13,z+24,air)
	mc.setBlocks(x-3,y+13,z+26,x+3,y+13,z+26,woodp)
	mc.setBlocks(x-3,y+13,z+25,x+3,y+13,z+25,air)
	mc.setBlocks(x-2,y+13,z+27,x+2,y+13,z+27,woodp)
	mc.setBlocks(x-2,y+13,z+26,x+2,y+13,z+26,air)
	mc.setBlocks(x-1,y+13,z+28,x+1,y+13,z+28,woodp)
	mc.setBlocks(x-1,y+13,z+27,x+1,y+13,z+27,air)
	mc.setBlocks(x,y+13,z+29,x,y,z,woodp)
	mc.setBlocks(x,y+13,z+28,x,y,z,air)
	mc.setBlocks(x-12,y+14,z+12,x+12,y+14,z+12,woodp)#14
	mc.setBlocks(x-11,y+14,z+14,x+11,y+14,z+14,woodp)
	mc.setBlocks(x-11,y+14,z+12,x+11,y+14,z+12,air)
	mc.setBlocks(x-10,y+14,z+17,x+10,y+14,z+17,woodp)
	mc.setBlocks(x-10,y+14,z+14,x+10,y+14,z+14,air)
	mc.setBlocks(x-9,y+14,z+19,x+9,y+14,z+19,woodp)
	mc.setBlocks(x-9,y+14,z+17,x+9,y+14,z+17,air)
	mc.setBlocks(x-8,y+14,z+21,x+8,y+14,z+21,woodp)
	mc.setBlocks(x-8,y+14,z+19,x+8,y+14,z+19,air)
	mc.setBlocks(x-7,y+14,z+22,x+7,y+14,z+22,woodp)
	mc.setBlocks(x-7,y+14,z+21,x+7,y+14,z+21,air)
	mc.setBlocks(x-6,y+14,z+23,x+6,y+14,z+23,woodp)
	mc.setBlocks(x-6,y+14,z+22,x+6,y+14,z+22,air)
	mc.setBlocks(x-5,y+14,z+24,x+5,y+14,z+24,woodp)
	mc.setBlocks(x-5,y+14,z+23,x+5,y+14,z+23,air)
	mc.setBlocks(x-4,y+14,z+25,x+4,y+14,z+25,woodp)
	mc.setBlocks(x-4,y+14,z+24,x+4,y+14,z+24,air)
	mc.setBlocks(x-3,y+14,z+26,x+3,y+14,z+26,woodp)
	mc.setBlocks(x-3,y+14,z+25,x+3,y+14,z+25,air)
	mc.setBlocks(x-2,y+14,z+27,x+2,y+14,z+27,woodp)
	mc.setBlocks(x-2,y+14,z+26,x+2,y+14,z+26,air)
	mc.setBlocks(x-1,y+14,z+28,x+1,y+14,z+28,woodp)
	mc.setBlocks(x-1,y+14,z+27,x+1,y+14,z+27,air)
	mc.setBlocks(x,y+14,z+29,x,y,z,woodp)
	mc.setBlocks(x,y+14,z+28,x,y,z,air)
	mc.setBlocks(x-12,y+15,z+12,x+12,y+15,z+12,woodp)#15
	mc.setBlocks(x-11,y+15,z+14,x+11,y+15,z+14,woodp)
	mc.setBlocks(x-11,y+15,z+12,x+11,y+15,z+12,air)
	mc.setBlocks(x-10,y+15,z+17,x+10,y+15,z+17,woodp)
	mc.setBlocks(x-10,y+15,z+14,x+10,y+15,z+14,air)
	mc.setBlocks(x-9,y+15,z+19,x+9,y+15,z+19,woodp)
	mc.setBlocks(x-9,y+15,z+17,x+9,y+15,z+17,air)
	mc.setBlocks(x-8,y+15,z+21,x+8,y+15,z+21,woodp)
	mc.setBlocks(x-8,y+15,z+19,x+8,y+15,z+19,air)
	mc.setBlocks(x-7,y+15,z+23,x+7,y+15,z+23,woodp)
	mc.setBlocks(x-7,y+15,z+21,x+7,y+15,z+21,air)
	mc.setBlocks(x-6,y+15,z+24,x+6,y+15,z+24,woodp)
	mc.setBlocks(x-6,y+15,z+23,x+6,y+15,z+23,air)
	mc.setBlocks(x-5,y+15,z+25,x+5,y+15,z+25,woodp)
	mc.setBlocks(x-5,y+15,z+24,x+5,y+15,z+24,air)
	mc.setBlocks(x-4,y+15,z+26,x+4,y+15,z+26,woodp)
	mc.setBlocks(x-4,y+15,z+25,x+4,y+15,z+25,air)
	mc.setBlocks(x-3,y+15,z+27,x+3,y+15,z+27,woodp)
	mc.setBlocks(x-3,y+15,z+26,x+3,y+15,z+26,air)
	mc.setBlocks(x-2,y+15,z+28,x+2,y+15,z+28,woodp)
	mc.setBlocks(x-2,y+15,z+27,x+2,y+15,z+27,air)
	mc.setBlocks(x-1,y+15,z+29,x+1,y+15,z+29,woodp)
	mc.setBlocks(x-1,y+15,z+28,x+1,y+15,z+28,air)
	mc.setBlocks(x,y+15,z+30,x,y,z,woodp)
	mc.setBlocks(x,y+15,z+29,x,y,z,air)
	mc.setBlocks(x-12,y+16,z+14,x+12,y+16,z+14,woodp)#16
	mc.setBlocks(x-11,y+16,z+17,x+11,y+16,z+17,woodp)
	mc.setBlocks(x-11,y+16,z+14,x+11,y+16,z+14,air)
	mc.setBlocks(x-10,y+16,z+19,x+10,y+16,z+19,woodp)
	mc.setBlocks(x-10,y+16,z+17,x+10,y+16,z+17,air)
	mc.setBlocks(x-9,y+16,z+21,x+9,y+16,z+21,woodp)
	mc.setBlocks(x-9,y+16,z+19,x+9,y+16,z+19,air)
	mc.setBlocks(x-8,y+16,z+23,x+8,y+16,z+23,woodp)
	mc.setBlocks(x-8,y+16,z+21,x+8,y+16,z+21,air)
	mc.setBlocks(x-7,y+16,z+24,x+7,y+16,z+24,woodp)
	mc.setBlocks(x-7,y+16,z+23,x+7,y+16,z+23,air)
	mc.setBlocks(x-6,y+16,z+25,x+6,y+16,z+25,woodp)
	mc.setBlocks(x-6,y+16,z+24,x+6,y+16,z+24,air)
	mc.setBlocks(x-5,y+16,z+26,x+5,y+16,z+26,woodp)
	mc.setBlocks(x-5,y+16,z+25,x+5,y+16,z+25,air)
	mc.setBlocks(x-4,y+16,z+27,x+4,y+16,z+27,woodp)
	mc.setBlocks(x-4,y+16,z+26,x+4,y+16,z+26,air)
	mc.setBlocks(x-3,y+16,z+28,x+3,y+16,z+28,woodp)
	mc.setBlocks(x-3,y+16,z+27,x+3,y+16,z+27,air)
	mc.setBlocks(x-2,y+16,z+29,x+2,y+16,z+29,woodp)
	mc.setBlocks(x-2,y+16,z+28,x+2,y+16,z+28,air)
	mc.setBlocks(x-1,y+16,z+30,x+1,y+16,z+30,woodp)
	mc.setBlocks(x-1,y+16,z+29,x+1,y+16,z+29,air)
#mc.postToChat("It ran into Obi's Empire State Building, it then proceeded to break itself")
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	ship(mc,x,y+10,z)	
	hull(mc,x,y+10,z+45)
main()

"""xc
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
"""
Non-API Blocks
=======================
PAINTING            321
STONE_STAIRS         67
OAK_STAIRS           53
OAK_STAIRS           59
NETHERRACK           87
TRAPDOOR             96
MELON_SEEDS         105
BRICK_STAIRS        108
SANDSTONE_STAIRS    128
STONE_BRICK_STAIRS  109
NETHER_BRICK        112
NETHER_BRICK_STAIRS 114
QUARTZ_BLOCK        155
QUARTZ_STAIRS       156
STONE_CUTTER        245
BONE_MEAL           351
"""
