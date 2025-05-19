# babysc_note

## **Solution (Paste in Dockerfile)**

```bash
FROM harbor.ctf.onl/team_14/babysc_note:latest

COPY ./babysc_revenge /srv/app/run

CMD ["/jail/run"]
```

## **Walkthrough**

```bash
docker login harbor.ctf.onl -u team_14_dev -p htLXRcFlS7wtF8nX

docker pull harbor.ctf.onl/team_14/babysc_note:latest

docker inspect harbor.ctf.onl/team_14/babysc_note:latest | jq -r '.[0].Config.Cmd | join(" ")'

nano Dockerfile
<!-- paste the push command -->

docker run --privileged -d --name sla-check-team14 --stop-timeout=1800 -P harbor.ctf.onl/team_14/babysc_note:latest

docker build --platform linux/amd64 -t harbor.ctf.onl/team_14/babysc_note:latest .

docker push harbor.ctf.onl/team_14/babysc_note:latest
```

## **CMD Snippet**

```bash
rydzze ~ ❯ sudo docker push harbor.ctf.onl/team_14/babysc_note:latest
The push refers to repository [harbor.ctf.onl/team_14/babysc_note]
07715ffdd417: Pushed
5f70bf18a086: Layer already exists
f297d71fdfbd: Layer already exists
12b495d78371: Layer already exists
2957c511a56b: Layer already exists
2b757036b5a2: Layer already exists
latest: digest: sha256:c832541772a9d1d332686cbaef891f39853c9e5d1125dfac4eee36bc727186a5 size: 1775
```