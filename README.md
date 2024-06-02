# Installation Guide
**TheHive**

_Задачи:_ 
  1. configure secret key:
cat > /etc/thehive/secret.conf << _EOF_
play.http.secret.key="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64 | head -n 1)"
_EOF_
  2. татат
