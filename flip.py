# flip.py

import znc

class flip(znc.Module):
    description = "Example python3 module for ZNC"

    _dongers = {
        'f':  '(╯°□°)╯︵ ┻━┻',
        '~f': '(╯°□°)╯︵ xxx',
        't':  '(ノಠ益ಠ)ノ彡 ┻━┻',
        '~t': '(ノಠ益ಠ)ノ彡 xxx',
        'c':  ' ┬┬ ノ( ゜-゜ノ)',
        's':  '¯\_(ツ)_/¯',
        'b':  '╭∩╮( ͡° ͜ʖ͡°)',
    }


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
        user = self.GetUser()

        m = message.s
        c = m[:2].replace('\\', '');

        if self._dongers[c]:
            if len(m) > 2 and self._dongers['~' + c]:
                str = self._dongers['~' + c].replace('xxx', self._flipit(text=m[2:]))
            else:
                str = self._dongers[c]
            outIRC = "PRIVMSG {0} : {1}".format(target, str)
            outUser = (":{2} PRIVMSG {0} :{1}").format(target, str, user)
            outRet = znc.HALT


        if outIRC != "":
            self.PutIRC(outIRC)

        if outUser != "":
            self.PutUser(outUser)

        return outRet

#    def OnUserTextMessage(self, message):
#        self.PutModule("UserTextMessage said {0}".format(message))

