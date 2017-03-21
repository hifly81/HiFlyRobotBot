# HiFlyRobotBot
another bot 4 Telegram

Find me at http://t.me/HiflyRobotBot

HiFlyRobot uses icons from 
https://www.iconfinder.com/iconsets/stripe-flag-set

see license for icons at:
http://support.iconfinder.com/quick-guide-to-iconfinder/license-overview



Installing
==========

Required python libs:

    $ sudo pip install requests
    $ sudo pip install lxml


Configure
=========

Open the file bot.properties

Put the value of your Telegram Token in key 

bot_token=<your_telegram_bot_token>


Run
===

    $ python hifly_robot_bot.py

Ctrl-C or kill the process to stop the bot.


Usage
=====

So far the bot will answer to these messages/commands:

* Say ciao, hello, greet the bot and It will answer you!

* /start

* /<country_code>, 
where a country code must be as specified in https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 
or in https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3 
example: /it or /IT, /US or /USA...


License
=======

You may copy, distribute and modify the software provided that modifications are described and licensed for free under LGPL-3 <https://www.gnu.org/licenses/lgpl-3.0.html>. Derivatives works (including modifications or anything statically linked to the library) can only be redistributed under LGPL-3, but applications that use the library don't have to be.
