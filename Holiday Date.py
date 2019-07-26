import pandas as p
print("\n".join([_.strftime('%-d.%-m.%Y')for _ in p.date_range('2019','2020',freq='D')if _.weekday()in[5,6]]))
