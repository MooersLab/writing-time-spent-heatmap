#!/opt/homebrew/bin/python3.11
# Universal
import os
import calmap#!/opt/homebrew/bin/python3.11
# Universal
import os
import calmap
import calplot
import pandas as pd
import numpy as np
from vega_datasets import data as vds
import matplotlib.pyplot as plt
import sqlite3

conn4=sqlite3.connect('/Users/blaine/6003TimeTracking/cb/mytime.db')

# Specific to subsections of the projects
# FROM newTimeSpent WHERE ProjectID LIKE '[1-9][1-9][1-9]g' Failed
# FROM newTimeSpent where ProjectID BETWEEN 001 and 1999
## Manuscripts
datam = pd.read_sql( '''
SELECT DateDashed, ProjectID, SUM(TimeHr) TimeHr
FROM zTimeSpent where ProjectID BETWEEN 001 and 1999
GROUP BY DateDashed
''',conn4)
datam['Date'] = pd.to_datetime(datam['DateDashed'])
datam = datam.set_index('Date')
isinstance(datam.index, pd.DatetimeIndex)
GhrPerDay = pd.Series(datam.TimeHr)
calplot.calplot(data=GhrPerDay, cmap='Blues', vmin=0.0, how=None, figsize=(16,10));
plt.suptitle('Grant and Journal Article Writing Effort', y=1.0, fontsize=20);
#plt.savefig('hmj.png', dpi=300, w)
# Remove old version and write updated version
strFile = "/Users/blaine/6003TimeTracking/cb/hmgj.png"
if os.path.isfile(strFile):
   os.remove(strFile)   # Opt.: os.system("rm "+strFile)
plt.savefig(strFile, dpi=300)

plt.show()

import calplot
import pandas as pd
import numpy as np
from vega_datasets import data as vds
import matplotlib.pyplot as plt
import sqlite3

conn4=sqlite3.connect('/Users/blaine/6003TimeTracking/cb/mytime.db')

# Specific to subsections of the projects
# FROM newTimeSpent WHERE ProjectID LIKE '[1-9][1-9][1-9]g' Failed
# FROM newTimeSpent where ProjectID BETWEEN 001 and 1999
## Manuscripts
datam = pd.read_sql( '''
SELECT DateDashed, ProjectID, SUM(TimeHr) TimeHr
FROM zTimeSpent where ProjectID BETWEEN 001 and 1999
GROUP BY DateDashed
''',conn4)
datam['Date'] = pd.to_datetime(datam['DateDashed'])
datam = datam.set_index('Date')
isinstance(datam.index, pd.DatetimeIndex)
GhrPerDay = pd.Series(datam.TimeHr)
calplot.calplot(data=GhrPerDay, cmap='Blues', vmin=0.0, how=None, figsize=(16,10));
plt.suptitle('Grant and Journal Article Writing Effort', y=1.0, fontsize=20);
#plt.savefig('hmj.png', dpi=300, w)
# Remove old version and write updated version
strFile = "/Users/blaine/6003TimeTracking/cb/hmgj.png"
if os.path.isfile(strFile):
   os.remove(strFile)   # Opt.: os.system("rm "+strFile)
plt.savefig(strFile, dpi=300)

plt.show()
