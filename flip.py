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
        'unimpressed': 'u',
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
        'test': 'test',
        'u': 'ಠ_ಠ ',
        '~slap':'\x01ACTION slaps yyy around a bit with a large trout\x01',
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

    def OnLoad(self, args, message):
        tempNV = self.nv
        for k, v in self.nv.items():
            if k not in self._dongers:
                self._dongers[k] = v

        for k, v in self._dongers.items():
            if k not in self.nv:
                self.nv[k] = v

        self.PutModule("WooHoo, flip loaded")
        return znc.CONTINUE

    def OnModCommand(self, command):
        cmd = command.split()[0]
        args = command.replace(cmd, '').strip()
        outMod = ""
        if cmd == 'list':
            for k, v in self._dongers.items():
                self.PutModule(("{0}: {1}").format(k, v))
        if cmd == 'nv':
            for k, v in self.nv.items():
                self.PutModule(("{0}: {1}").format(k, v))
        elif cmd == 'add':
            if len(args.split()) > 1:
                k = args.split()[0]
                v = args.replace(k, '').strip()
                self._dongers[k] = v
                self.nv[k] = v
                outMod = (("Flip Alias Added: {0}->{1}").format(k, v))
            else:
                outMod = "Not enough arguments given: {0}".format(args)
        elif cmd == 'delete':
            if len(args) > 0:
                k = args.split()[0]
                self._dongers.pop(k, None)
                self.nv.pop(k, None)
                outMod = "Flip Alias '{0}' Removed.".format(k)
            else:
                outMod = "A flip alias must be defined in order to remove it."

        elif cmd == 'help':
            outMod = "This should be some help."

        if len(outMod) > 0:
            self.PutModule(outMod)

        return znc.HALT

    def OnUserMsg(self, target, message):
        outIRC = ""
        outUser = ""
        outRet = znc.CONTINUE
        outReverse = ""

        user = self.GetClient().GetNick()

        m = message.s

        if (m.split()[0][0]) != '\\':
            return outRet

        c = m.split()[0].replace('\\', '')
        a = m[1:].replace(c, '').strip()

        if c in self._aliases:
            c = self._aliases[c]

        if c in self._dongers or '~' + c in self._dongers:
            if len(a.split()) > 0 and '~' + c in self._dongers:
                str = self._dongers['~' + c]
                str = str.replace('uuu', user)
                str = str.replace('xxx', self._flipit(text=a))
                str = str.replace('yyy', a)
            elif c in self._dongers:
                str = self._dongers[c]
            else:
                return znc.HALT

            outIRC = "PRIVMSG {0} :{1}".format(target, str)
            outUser = (":{2} PRIVMSG {0} :{1}").format(target, str, user)
            outRet = znc.HALT

        if outIRC != "":
            self.PutIRC(outIRC)

        if outUser != "":
            self.PutUser(outUser)

        return outRet
