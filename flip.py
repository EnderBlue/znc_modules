# flip.py

import znc

class flip(znc.Module):
    description = "DONGERS for ZNC"

    _aliases = {
        'flip':     'f',
        'chill':    'c',
        'fuckyou':  'b',
        'shrug':    's',
        'shruggie': 's',
        'meh':      's',
    }

    _dongers = {
        'f':  '(╯°□°)╯︵ ┻━┻',
        '~f': '(╯°□°)╯︵ xxx',
        't':  '(ノಠ益ಠ)ノ彡 ┻━┻',
        '~t': '(ノಠ益ಠ)ノ彡 xxx',
        'c':  ' ┬┬ ノ( ゜-゜ノ)',
        '~c':  'yyy ノ( ゜-゜ノ)',
        's':  '¯\_(ツ)_/¯',
        'b':  '╭∩╮( ͡° ͜ʖ͡°)',
        'u':  'test',
        '~slap':'uuu slaps yyy around a bit with a large trout',
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

        user = self.GetClient().GetNick()

        m = message.s
        c = m.split()[0].replace('\\', '')

        if c in self._aliases:
            c = self._aliases[c]

        if c in self._dongers or (len(m.split()) > 1 and '~' + c in self._dongers):
            if len(m.split()) > 1 and '~' + c in self._dongers:
                str = self._dongers['~' + c]
                str = str.replace('uuu', user)
                str = str.replace('xxx', self._flipit(text=m.split()[1]))
                str = str.replace('yyy', m.split()[1])
            else:
                str = self._dongers[c]
            outIRC = "PRIVMSG {0} :{1}".format(target, str)
            outUser = (":{2} PRIVMSG {0} :{1}").format(target, str, user)
            outRet = znc.HALT


        if outIRC != "":
            self.PutIRC(outIRC)

        if outUser != "":
            self.PutUser(outUser)

        return outRet
