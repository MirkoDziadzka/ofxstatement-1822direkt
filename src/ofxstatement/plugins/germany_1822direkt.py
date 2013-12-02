from ofxstatement.plugin import Plugin
from ofxstatement.parser import CsvStatementParser
from ofxstatement.statement import StatementLine

class FrankfurterSparkasse1822Plugin(Plugin):
    def get_parser(self, filename):
        encoding = self.settings.get('charset', 'iso-8859-1')
        f = open(filename, 'r', encoding=encoding)
        parser = FrankfurterSparkasse1822Parser(f)
        parser.statement.account_id = self.settings['account']
        parser.statement.bank_id = self.settings.get('bank', '50050201')
        parser.statement.currency = self.settings.get('currency', 'EUR')
        return parser


class FrankfurterSparkasse1822Parser(CsvStatementParser):
    """
    This plugin tries to parse the provided CSV data into the same
    format, as the discontinued OFX export
    """
    date_format = "%d.%m.%Y"

    def parse_float(self, f):
	# convert a number in german localization (e.g. 1.234,56) into a float
        return float(f.replace('.','').replace(',','.'))

    def parse_record(self, line):
        # FIXME: add header validation
        if self.cur_record <= 2:
            return None
        if len(line) < 3:
            """e.g.: ['# 1 vorgemerkte Umsätze nicht angezeigt']"""
            return None
        if not line[2]:
            return None
        sl = StatementLine()
        sl.id = line[1]
        sl.date = self.parse_datetime(line[2])
        sl.amount = self.parse_float(line[4])
        sl.trntype = 'DEBIT' if sl.amount < 0 else 'CREDIT'
        sl.payee = line[7]
        sl.memo = "(%s/%s): %s"  % (line[8],line[9], " ".join(line[15:]).strip())

        return sl


