# Guilded Gen
[![MIT License](https://img.shields.io/github/last-commit/akimbo7/GuildedGen?color=%23BCF8EC&style=flat-square)](https://github.com/akimbo7/GuildedGen)
[![MIT License](https://img.shields.io/github/repo-size/akimbo7/GuildedGen?color=%239FA0C3&style=flat-square)](https://github.com/akimbo7/GuildedGen)
[![MIT License](https://img.shields.io/github/v/release/akimbo7/GuildedGen?color=%237B435B&style=flat-square)](https://github.com/akimbo7/GuildedGen/releases)

An account generator made for Guilded.

In terms of security, Guilded seems to have very poor security measures when it come to generating accounts. Captchas are non-existent.

The only form of security is restricting IPs, which can obviously be bypasses very easily.

![Untitled](https://user-images.githubusercontent.com/100610867/156846238-922a1b1d-b70a-4b40-90e3-01f51e3c55f4.gif)

```
What does it do?
> Creates a random username
> Creates a random gmail address
> Creates a unique client id
> Creates a unique device id
> Creates account with sessions for increased performance - as opposed to single requests
> Creates an account
> Creates a server for each account

>> This ensures that each account is ready to be used off the bat.

>> Format -> email:password:hmac-cookie
```


## Requirements
- requests
- colorama
- uuid
- datetime


