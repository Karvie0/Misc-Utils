TIME=120
ITER=5

echo 3
sleep 1
echo 2
sleep 1
echo 1
sleep 1
mpv beep.wav


for (( i=$ITER; i>=1; i-- ))
do
	for (( j=$TIME; j>=1; j-- ))
	do
		echo $j
		sleep 1
	done
	mpv beep.wav
done
