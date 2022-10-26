# Flask on Docker

## <span style="color:orange">Docker 起動</span>

```
docker-compose build
```
```
docker-compose up -d
```
```
docker compose logs -f
```

## <span style="color:orange">Flask on Docker</span>

```
docker-compose exec flask bash
```
```
curl http://0.0.0.0:80
```

## <span style="color:orange">アクセス</span>
### docker compose上でのflaskへのアクセス  
- http://localhost:9000  
- http://0.0.0.0:9000  

### flaskコンテナからflaskへのアクセス  
- http://localhost:80  
- http://0.0.0.0:80  

### jupyter notebookへのアクセス    
基本vscodeで使うことを想定しているので、reopen in containerで行う  
Open a Remote Window ->Open Folder in Container
-> jupyter Data何ちゃらのコンテナ  

二回目以降はReopen in Container
  
<br>
一応これでもできる  
```
docker-compose up -d
```
- http://localhost:8888
