# python_websocket_test

1. 先用 python websocketServer.py 開啟server，，此時會用flask在localhost:5000開啟http server並有websocket功能。

2. 在瀏覽器中輸入http://localhost:5000 可開啟網頁輸入文字，server會以websocket回傳同樣的字串。

3. 用 python websocketClient.py 可開啟websocket client，此範例執行時會開一thread並用websocket跟server溝通。
