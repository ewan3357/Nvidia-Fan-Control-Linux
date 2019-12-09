import os

def main():
	inp = input("FAN-SPEED 0-100:")
	op = "nvidia-settings -a '[gpu:0]/GPUFanControlState=1' -a '[fan:0]/GPUTargetFanSpeed={}'"
	os.system(op.format(inp))
	

main()

