# Krrruncher

Why so many r's you might ask? To which I have no good answer, other than I felt like it

## What it does

Krrruncher is a POC (Proof of Concept) Docker environment for cracking MD5 hashes (really exciting huh!). The primary focus of this project was to learn the basics of Python Flask & gain a better understanding of docker containers. It will brute force any hash (given enough time), but the recommended length is four characters and below. The `Random` option will generate a random md5 hash with a 1 to 4 character space.

![Network Diagram](assets/networkdiagram.png?raw=true "Network Diagram")

## Getting Started

Make sure you have <img src="https://img.icons8.com/dusk/64/000000/docker.png" height="20"/> installed.......that's pretty much it. Then run `docker-compose up --build --abort-on-container-exit`, and it should be available at port 80. The environment takes ~15s to fully boot.

Occasionally Krrruncher incurs the `error #137`, simply exit out and rerun the above command.

## Persistent Hashes

By default, the hash list is preserved so that in the future if a hash has already been cracked, it will be immediately serverd. Remove: `- "./flaskserver/data:/data"` for no persistence between sessions.

## Scalability

The number of krrruncher worker nodes can be increased for parallel cracking

## To Do

- [ ] Add multi hash support
- [ ] Add location to view all cracked hashes
- [ ] Add Favicon
- [ ] Implement Websockets to remove the auto-refresh
- [ ] Debug reason for `Error #137`
- [ ] Clean up UI (AKA make it readable)
 
