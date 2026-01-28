#!/opt/homebrew/bin/python3.11
import os
import calplot
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn4 = sqlite3.connect('/Users/blaine/6003TimeTracking/cb/mytime.db')

# Manuscripts and Grants (ProjectID 001-1999)
datam = pd.read_sql('''
    SELECT DateDashed, ProjectID, SUM(TimeHr) TimeHr
    FROM zTimeSpent 
    WHERE ProjectID BETWEEN 001 AND 1999
    GROUP BY DateDashed
''', conn4)

datam['Date'] = pd.to_datetime(datam['DateDashed'])
datam = datam.set_index('Date')
GhrPerDay = pd.Series(datam.TimeHr)

# Create the calendar plot with adjusted figure size
fig, ax = calplot.calplot(
    data=GhrPerDay, 
    cmap='Blues', 
    vmin=0.0, 
    how=None, 
    figsize=(16, 10),
    colorbar=False  # Disable default colorbar
)

plt.suptitle('Grant and Journal Article Writing Effort', y=0.98, fontsize=20)

# Adjust margins to make room for colorbar on far right
plt.subplots_adjust(left=0.06, right=0.85, top=0.94, bottom=0.05)

# Add colorbar manually with custom position
# Get the scalar mappable from one of the axes for the colorbar
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=0, vmax=GhrPerDay.max()))
sm.set_array([])

# Position: [left, bottom, width, height] in figure coordinates
cbar_ax = fig.add_axes([0.88, 0.15, 0.02, 0.7])
cbar = fig.colorbar(sm, cax=cbar_ax)
cbar.set_label('Hours', fontsize=12)

# Remove old version and write updated version
strFile = "/Users/blaine/6003TimeTracking/cb/hmgj.png"
if os.path.isfile(strFile):
    os.remove(strFile)

plt.savefig(strFile, dpi=300, bbox_inches='tight')
plt.show()

conn4.close()
