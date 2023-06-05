import datetime, calendar

990 * 680 # calender

header = """
<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1250">
  <!-- Define the styles for the calendar -->
  <rect x="0" y="0" width="1080" height="1250" rx="0" ry="0" fill="white"/>
  <style>
    .header {
      font-family: Arial, sans-serif;
      font-size: 24px;
      text-anchor: middle;
      fill: black;
    }
    
    .college {
      font-family: sans-serif;
      font-size: 40px;
      text-anchor: middle;
      fill: black;
    }
    
    .title {
      font-family: sans-serif;
      font-size: 30px;
      text-anchor: middle;
      fill: black;
    }
    
    .tile {
      font-family: sans-serif;
      font-size: 23px;
      text-anchor: middle;
      fill: black;
    }
    
    .legend {
      font-family: sans-serif;
      font-size: 16px;
      text-anchor: end;
    }
    
    .holiday {
      font-family: sans-serif;
      font-size: 16px;
      fill: black;
    }
    
    .date {
      font-family: monospace;
      font-size: 16px;
      fill: black;
      font-weight:bold;
    }
    
    .day {
      font-family: Arial, sans-serif;
      font-size: 16px;
      text-anchor: middle;
    }
  </style>

  <!-- Draw the calendar -->
"""

a = [30, 75, 120, 165, 210, 255, 300]
b = [120, 160, 200, 240, 280, 320]

month = f"""<rect x="10" y="10" width="310" height="45" rx="10" ry="10" fill="lightblue" />
  <text x="170" y="40" class="header">{"month_name"}</text>
  <!-- Days of the week -->
  <text font-family="sans-serif" text-anchor="middle" x="{a[0]}" y="80" font-size="12px" fill="red">Sun</text>
  <text font-family="sans-serif" text-anchor="middle" x="{a[1]}" y="80"  font-size="12px">Mon</text>
  <text font-family="sans-serif" text-anchor="middle" x="{a[2]}" y="80" font-size="12px">Tue</text>
  <text font-family="sans-serif" text-anchor="middle" x="{a[3]}" y="80" font-size="12px">Wed</text>
  <text font-family="sans-serif" text-anchor="middle" x="{a[4]}" y="80"  font-size="12px">Thu</text>
  <text font-family="sans-serif" text-anchor="middle" x="{a[5]}" y="80"  font-size="12px">Fri</text>
  <text font-family="sans-serif" text-anchor="middle" x="{a[6]}" y="80"  font-size="12px">Sat</text>"""

file = header

def day(x, y, d, fill="none", text_fill="black"):
  return f'<circle cx="{x}" cy="{y-6}" r="15" fill="{fill}" stroke="black" stroke-width="1"/><text x="{x}" y="{y}" class="day" fill="{text_fill}" font-weight="bold">{d}</text>'

def gen_month(month_name, lst):
  first_day = datetime.datetime.strptime("1 " + month_name, '%d %m %Y').weekday()
  days = calendar.monthrange(int(month_name.split(" ")[1]), int(month_name.split(" ")[0]))[1]
  str_month = month.replace("month_name", calendar.month_name[int(month_name.split(" ")[0])] + " " + month_name.split(" ")[1])
  cal = [[[0, "none", "black"] for _ in range(7)] for i in range(6)]
  j = 1
  for i in range(first_day, first_day+days):
    cal[i//7][i%7] = [j, "none", "black"]    
    j += 1
  if len(lst) != 0:
    for d, back_col, col in lst:
      date = d + first_day - 1
      cal[date//7][date%7][1] = back_col
      cal[date//7][date%7][2] = col
  for i in range(42):
    if cal[i//7][i%7][0] != 0:
      if i%7!=0 and cal[i//7][i%7][2] == "black":
        str_month += day(a[i%7], b[i//7], cal[i//7][i%7][0], cal[i//7][i%7][1])
      elif i%7 == 0:
        str_month += day(a[i%7], b[i//7], cal[i//7][i%7][0], cal[i//7][i%7][1], "red")
      else:
        str_month += day(a[i%7], b[i//7], cal[i//7][i%7][0], cal[i//7][i%7][1], cal[i//7][i%7][2])
  return str_month

# def makecal(start, n, *args):
#   global cal
#   j = 1
#   for i in range(start, start+n):
#     cal[i//7][i%7] = [j, "none"]    
#     j += 1
#   for d, col in args:
#     date = d + start - 1
#     cal[date//7][date%7][1] = col


# iscm.jpg
file += '<image href="https://i.ibb.co/vYPQRcR/iscm.jpg" x="60" y="50" width="105" height="105" />'
file += '<text  x="550" y="85" class="college" font-weight="bold">The Institute of Science, Mumbai</text>'
file += '<text  x="550" y="135" class="title" font-weight="bold">Academic Calendar 2023-24</text>'

# one = gen_month("1 2023", [(1, "red", "black"), (5, "blue", "red")])
# two = gen_month("2 2023", [(1, "red", "black"), (5, "blue", "red")])
# three = gen_month("3 2023", [(1, "red", "black"), (5, "blue", "red")])
# four = gen_month("4 2023", [(1, "red", "black"), (5, "blue", "red")])


def gen_cal(months, lst):
  dis = {}
  for date in lst:
    tup = date[0].split(" ")
    if tup[1] + " " + tup[2] in dis:
      dis[tup[1] + " " + tup[2]].append((int(tup[0]), date[1], date[2]))
    else:
      dis[tup[1] + " " + tup[2]] = [(int(tup[0]), date[1], date[2])]
  m = 180
  n = 50
  dd = [(0, 0), (330, 0), (660, 0), (0, 340), (330, 340), (660, 340)]
  text = ""
  for i, month in enumerate(months):
    if month in dis:
      text += '<svg x="{}" y="{}">'.format(dd[i][0]+n, dd[i][1]+m) + gen_month(month, dis[month]) + "</svg>"
    else:
      text += '<svg x="{}" y="{}">'.format(dd[i][0]+n, dd[i][1]+m) + gen_month(month, []) + "</svg>"
  return text
# m = 180
# n = 50
# file += '<svg x="{}" y="{}">'.format(0 +n, 0+m) + one + "</svg>"
# file += '<svg x="{}" y="{}">'.format(330+n, 0+m) + two + "</svg>"
# file += '<svg x="{}" y="{}">'.format(660+n, 0+m) + three + "</svg>"
# file += '<svg x="{}" y="{}">'.format(0+n, 340+m) + three + "</svg>"
# file += '<svg x="{}" y="{}">'.format(330+n, 340+m) + four + "</svg>"

# x="330" 
# y="340"
months = ["1 2023", "2 2023", "3 2023", "4 2023", "5 2023", "6 2023"]
dates = [
  ("2 1 2023", "blue", "yellow", "something 1"),
  ("3 3 2023", "yellow", "red", "something 2"),
  ("20 4 2023", "yellow", "black", "something 3")
]

legends = [
  ("red", "something 1"),
  ("yellow", "something 2"),
  ("blue", "something 3")
]

file += gen_cal(months, dates)

def make_note(title, width, leg):
  text = f"""
  <svg x="60" y="880"> 
  <rect x="0" y="0" width="{width}" height="330" rx="10" ry="10" fill="lightblue"/>
  <text x="125" y="35" class="tile" font-weight="bold">{title}</text>
  """
  m = 75
  for i, l in enumerate(leg):
    text += f"""<circle cx="40" cy="{m}" r="12" fill="{l[1]}"/>
    <text x="160" y="{m+5}" class="legend" fill="{l[1]}">{l[0]}</text>"""
    m += 40
  text += "</svg>"
  return text


# legends = """<svg x="50" y="880"> 
# <rect x="0" y="0" width="240" height="330" rx="10" ry="10" fill="lightblue"/>
# <text x="125" y="35" class="tile" font-weight="bold">Something</text>

# <circle cx="40" cy="75" r="12" fill="red"/>
# <text x="160" y="80" class="legend">Something</text>

# <circle cx="40" cy="115" r="12" fill="red"/>
# <text x="160" y="120" class="legend">Something</text>

# <circle cx="40" cy="155" r="12" fill="red"/>
# <text x="160" y="160" class="legend">Something</text>

# <circle cx="40" cy="195" r="12" fill="red"/>
# <text x="160" y="200" class="legend">Something</text>
# </svg>"""

file += make_note("Notes", 310, [
  ("Something 1", "red"),
  ("Something 2", "blue"),
  ("Something 3", "yellow")
])


def gen_holi(title, lst, x):
  text = f"""
  <svg x="{x}" y="880"> 
  <rect x="0" y="0" width="310" height="330" rx="10" ry="10" fill="lightblue"/>
  <text x="155" y="35" class="tile" font-weight="bold">{title}</text>
  """
  m = 80
  for date, holi in lst:
    text += f"""
    <text x="20" y="{m}" class="date">{calendar.month_name[int(date.split(" ")[1])][:3] + " " + date.split(" ")[0]}</text>
    <text x="280" y="{m}" class="holiday" text-anchor="end">{holi}</text>
    """
    m += 20
  text += "</svg>"
  return text
# holidays = """<svg x="375" y="880"> 
# <rect x="0" y="0" width="300" height="330" rx="10" ry="10" fill="lightblue"/>
# <text x="155" y="35" class="tile" font-weight="bold">Something</text>

# <text x="50" y="80" class="date">Jan 25</text>
# <text x="280" y="80" class="holiday" text-anchor="end">Something something</text>
# </svg>"""
file += gen_holi("Holidays", [
  ("1 1 2023", "Holi"),
  ("24 3 2023", "Holi1"),
  ("15 6 2023", "Holi2"),
  ("12 5 2023", "Holi3")
], 390)

file += gen_holi("Holidays", [
  ("1 1 2023", "Holi"),
  ("24 3 2023", "Holi1"),
  ("15 6 2023", "Holi2"),
  ("12 5 2023", "Holi3")
], 390 + 330)

other = """
</svg>
"""
file += other

with open("main.svg", "w") as svgfile:
    svgfile.write(file)
    
from cairosvg import svg2png

svg2png(url="main.svg", write_to="main.png", output_height=1080)