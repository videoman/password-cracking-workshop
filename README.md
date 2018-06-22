# Password Cracking Workshop

## Install GIT client
Windows: https://git-scm.com/download/gui/windows
Mac: See step one of mac install - install homebrew

Clone this repo:
2. "git clone git@github.com:videoman/password-cracking-workshop.git"

## Install Hashcat

### Mac:
1. Install home brew https://brew.sh
(may have to install mac os X tools too)
2. run "brew install hashcat"

### Windows:
1. Install your drivers for the card - SDK drivers may not work: https://hashcat.net/wiki/doku.php?id=frequently_asked_questions#gpu_device_not_found_why
2. Download hashcat: https://hashcat.net/hashcat/

## Test hashcat

* hashcat -b

### Cracking NTLM - with a dictionary list
hashcat -m 1000 -a 0 -w2 test-ntlm-hash.txt wordlist.txt

### NTLM #2
test2-ntlm-hash contains a year. How could we figure that out?

Hint - we need to use both the wordlist.txt and years.txt

