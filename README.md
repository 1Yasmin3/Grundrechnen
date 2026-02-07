# Grundrechnen

# Grundeinrichtung

## Ssh Schlüssel
C:\Users\Nutzer> ssh-keygen
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\Nutzer/.ssh/id_ed25519):
Created directory 'C:\\Users\\Nutzer/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\Nutzer/.ssh/id_ed25519
Your public key has been saved in C:\Users\Nutzer/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:K+uhK7We8uLubJSKOLHIHWwskvyoAuEs0BMG+Ths3lw nutzer@Nutzer-PC
The key's randomart image is:
+--[ED25519 256]--+
|.o               |
|. o              |
|.= .             |
|=o+  E           |
|B+=o.   S        |
|**oB.    .       |
|O=*...o .        |
|O+=o.o +         |
|+*=**oo          |
+----[SHA256]-----+

C:\Users\Nutzer> cd .ssh

C:\Users\Nutzer\.ssh> dir
 Volume in drive C has no label.
 Volume Serial Number is 36CE-A1A3

 Directory of C:\Users\Nutzer\.ssh

07/02/2026  16:32    <DIR>          .
07/02/2026  16:32    <DIR>          ..
07/02/2026  16:32               411 id_ed25519
07/02/2026  16:32                99 id_ed25519.pub
               2 File(s)            510 bytes
               2 Dir(s)     461,217,792 bytes free

Der Private Schlüssel wird in GitHub in Settings hinterlegt

## Installation Git
Quelle: https://git-scm.com/install/windows

Git Bash bei Installation aktivieren

## Anlegen von Projekt
Verzeichnis git in Onedrive erstellen

Im Verzeichnis git:

git clone https://github.com/1Yasmin3/Grundrechnen.git

# Git befehle

git add

git commit -m

git push

git status
