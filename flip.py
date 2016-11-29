# flip.py

import znc

class flip(znc.Module):
    description = "Example python3 module for ZNC"


    _upside_down_map = {
        'A' : 'ɐ', 'B' : 'q', 'C' : 'ɔ', 'D' : 'p',
        'E' : 'ǝ', 'F' : 'Ⅎ', 'G' : 'b', 'H' : 'ɥ',
        'I' : 'ı', 'J' : 'ظ', 'K' : 'ʞ', 'L' : 'l',
        'M' : 'ɯ', 'N' : 'u', 'O' : 'o', 'P' : 'd',
        'Q' : 'b', 'R' : 'ɹ', 'S' : 's', 'T' : 'ʇ',
        'U' : 'n', 'V' : 'ʌ', 'W' : 'ʍ', 'X' : 'x',
        'Y' : 'ʎ', 'Z' : 'z',
        'a' : 'ɐ', 'b' : 'q', 'c' : 'ɔ', 'd' : 'p',
        'e' : 'ǝ', 'f' : 'ɟ', 'g' : 'b', 'h' : 'ɥ',
        'i' : 'ı', 'j' : 'ſ', 'k' : 'ʞ', 'l' : 'l',
        'm' : 'ɯ', 'n' : 'u', 'o' : 'o', 'p' : 'd',
        'q' : 'b', 'r' : 'ɹ', 's' : 's', 't' : 'ʇ',
        'u' : 'n', 'v' : 'ʌ', 'w' : 'ʍ', 'x' : 'x',
        'y' : 'ʎ', 'z' : 'z',

        '!' : '¡',
        ',' : '`', '.' : '˙',
        '1' : '|', '2' : 'ᄅ',
        '3' : 'Ɛ', '4' : 'ㄣ',
        '5' : 'ϛ', '6' : '9',
        '7' : 'ㄥ', '8' : '8',
        '9' : '6', '0' : '0',
        ';' : ';', '?' : '¿',
        '(' : ')', '[' : ']',
        '{' : '}', '<' : '>',
        '>' : '<', ' ' : ' ',
        '_' : '‾'
        }

    def _flipit(self, text):
        flipped = ''

        if text:
            for x in text:
                if x in self._upside_down_map:
                    flipped = self._upside_down_map[x] + flipped
                else:
                    flipped = x + flipped
        else:
            flipped = ' ^t  ^t^a ^t '

        return flipped


    def OnUserMsg(self, target, message):
        outIRC = ""
        outUser = ""
        outRet = znc.CONTINUE
        outReverse = ""

        if message.s[:2] == '\\f':
            if len(message.s) > 2:
                outReverse = "  " + self._flipit(message.s[2:])
            outIRC = "PRIVMSG {0} :(╯°□°)╯︵ ┻━┻".format(target) + outReverse
            outUser = ":EnderBlue PRIVMSG {0} :(╯°□°)╯︵ ┻━┻".format(target) + outReverse
            outRet = znc.HALT

        elif message.s[:2] == '\\t':
            if len(message.s) > 2:
                outReverse = "  " + self._flipit(message.s[2:])
            outIRC = "PRIVMSG {0} :(ノಠ益ಠ)ノ彡 ┻━┻".format(target) + outReverse
            outUser = ":EnderBlue PRIVMSG {0} :(ノಠ益ಠ)ノ彡 ┻━┻".format(target) + outReverse
            outRet = znc.HALT

        elif message.s[:2] == '\\c':
            outIRC = "PRIVMSG {0} : ┬┬ ノ( ゜-゜ノ)".format(target) + outReverse
            outUser = ":EnderBlue PRIVMSG {0} : ┬┬ ノ( ゜-゜ノ)".format(target) + outReverse
            outRet = znc.HALT

        elif message.s[:2] == '\\b':
            outIRC = "PRIVMSG {0} :╭∩╮( ͡°﻿ ͜ʖ͡°)".format(target) + outReverse
            outUser = ":EnderBlue PRIVMSG {0} :╭∩╮( ͡°﻿ ͜ʖ͡°)".format(target) + outReverse
            outRet = znc.HALT

        elif message.s[:2] == '\\s':
            outIRC = "PRIVMSG {0} :¯\_(ツ)_/¯".format(target) + outReverse
            outUser = ":EnderBlue PRIVMSG {0} :¯\_(ツ)_/¯".format(target) + outReverse
            outRet = znc.HALT


        if outIRC != "":
            self.PutIRC(outIRC)

        if outUser != "":
            self.PutUser(outUser)

        return outRet

#    def OnUserTextMessage(self, message):
#        self.PutModule("UserTextMessage said {0}".format(message))

