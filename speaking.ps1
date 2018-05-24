$startTime=0
$interval=60
$endTime=60
$sliceNum=4
$loopNum=1;
$locationRoot="C:/Users/10490/Desktop/ai/"
$originalVideo=$locationRoot + "aitry.mp4"
$pieceVideo
for($i=0;$i -lt $sliceNum; $i++){
	$pieceVideo = $locationRoot + "trans" + $i + ".pcm"
	ffmpeg -ss $startTime -t $endTime -y  -i $originalVideo -acodec pcm_s16le -f s16le -ac 1 -ar 16000 $pieceVideo
	$startTime = $startTime + $interval
	$endTime = $endTime + $interval
}
python recognize.py
for($i=0;$i -lt $sliceNum; $i++){
	$pieceVideo = $locationRoot + "trans" + $i + ".pcm"
	Remove-Item $pieceVideo
}