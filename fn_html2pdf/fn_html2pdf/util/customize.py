# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_html2pdf"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     html2pdf_data
    #     html2pdf_data_type
    #     html2pdf_stylesheet
    #   Message Destinations:
    #     fn_html2pdf
    #   Functions:
    #     html2pdf
    #   Workflows:
    #     example_html2pdf
    #   Rules:
    #     Example: HTML2PDF


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMCwgImJ1aWxkX251bWJl
ciI6IDAsICJ2ZXJzaW9uIjogIjMxLjAuMCJ9LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9uIjogMiwg
ImlkIjogMSwgImV4cG9ydF9kYXRlIjogMTUzNzIwOTAwMTA1NCwgImZpZWxkcyI6IFt7ImlkIjog
NTEsICJuYW1lIjogImluY190cmFpbmluZyIsICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAicHJlZml4
IjogbnVsbCwgInR5cGVfaWQiOiAwLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNpZGVudCBp
cyBhIHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhpcyBmaWVsZCBpcyByZWFk
LW9ubHkuIiwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZh
bHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwg
ImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiYzNmMGUz
ZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2EzMzA4Y2NhIiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJh
dGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29ubHkiOiB0cnVlLCAiY2hhbmdl
YWJsZSI6IHRydWUsICJyaWNoX3RleHQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQv
aW5jX3RyYWluaW5nIiwgInRlbXBsYXRlcyI6IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNlfSwgeyJp
ZCI6IDE2MywgIm5hbWUiOiAiaHRtbDJwZGZfc3R5bGVzaGVldCIsICJ0ZXh0IjogImh0bWwycGRm
X3N0eWxlc2hlZXQiLCAicHJlZml4IjogbnVsbCwgInR5cGVfaWQiOiAxMSwgInRvb2x0aXAiOiAi
Y3NzIGZvcm1hdHRlZCBzdHlsZXNoZWV0IGluZm9ybWF0aW9uIHRvIHVzZSB3aGVuIHJlbmRlcmlu
ZyBQREYgZG9jdW1lbnQiLCAicGxhY2Vob2xkZXIiOiAiQHBhZ2UgeyBzaXplOiBsYW5kc2NhcGU7
IH0qIHsgZm9udC1mYW1pbHk6IEFyaWFsOyBmb250LXNpemU6IHNtYWxsOyB9dGFibGUgeyBib3Jk
ZXItY29sbGFwc2U6IGNvbGxhcHNlOyB9dGFibGUsIHRoLCB0ZCB7IGJvcmRlcjogMXB4IHNvbGlk
IGJsYWNrOyB9IiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZh
bHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwg
ImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiM2IwMWQ2
MWYtY2Q5My00N2Q3LWFiNGEtYjMyYzJiOGUxYmZhIiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJh
dGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5n
ZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rp
b24vaHRtbDJwZGZfc3R5bGVzaGVldCIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBm
YWxzZX0sIHsiaWQiOiAxNTksICJuYW1lIjogImh0bWwycGRmX2RhdGFfdHlwZSIsICJ0ZXh0Ijog
Imh0bWwycGRmX2RhdGFfdHlwZSIsICJwcmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDExLCAidG9v
bHRpcCI6ICJ0aGUgdHlwZSBvZiBkYXRhIHBhc3NlZCwgdXN1YWxseSB0aGUgYXJ0aWZhY3QgdHlw
ZS4gVVJMIG9yIFVSSSBhcmUgbmVlZGVkIGZvciB3ZWJwYWdlIHNjYXBpbmciLCAicGxhY2Vob2xk
ZXIiOiAiIiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAiaGlk
ZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5f
Ynlfc2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImludGVybmFsIjogZmFs
c2UsICJ1dWlkIjogIjIxYWMyYWMwLWFiYzktNDg1YS1hNjZlLTVhYjY4MDQxNWI0MCIsICJvcGVy
YXRpb25zIjogW10sICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9v
bmx5IjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAiZXhw
b3J0X2tleSI6ICJfX2Z1bmN0aW9uL2h0bWwycGRmX2RhdGFfdHlwZSIsICJ0ZW1wbGF0ZXMiOiBb
XSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQiOiAxNTMsICJuYW1lIjogImh0bWwycGRmX2Rh
dGEiLCAidGV4dCI6ICJodG1sMnBkZl9kYXRhIiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjog
MTEsICJ0b29sdGlwIjogInNwZWNpZnkgZWl0aGVyIGEgaHRtbCBzdHJpbmcgb3IgdXJsIHJlZmVy
ZW5jZSIsICJwbGFjZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInJlcXVpcmVk
IjogImFsd2F5cyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2Us
ICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNl
LCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiOWQwZTI4ODctOTFiYy00NWVjLTgzMWYtYjUx
OTk2ZTAxZmE2IiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFs
dWVzIjogW10sICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90
ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vaHRtbDJwZGZfZGF0YSIsICJ0
ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX1dLCAiaW5jaWRlbnRfdHlwZXMiOiBb
eyJ1cGRhdGVfZGF0ZSI6IDE1MzcyMTAxMjg2MjUsICJjcmVhdGVfZGF0ZSI6IDE1MzcyMTAxMjg2
MjUsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNj
cmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tl
eSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAibmFtZSI6ICJDdXN0b21p
emF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjog
ZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2UsICJpZCI6IDB9XSwgInBo
YXNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJvdmVycmlkZXMiOiBbXSwgIm1lc3Nh
Z2VfZGVzdGluYXRpb25zIjogW3sibmFtZSI6ICJmbl9odG1sMnBkZiIsICJwcm9ncmFtbWF0aWNf
bmFtZSI6ICJmbl9odG1sMnBkZiIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgImV4cGVjdF9hY2si
OiB0cnVlLCAidXNlcnMiOiBbImJAYS5jb20iXSwgInV1aWQiOiAiOTA5ODYzODgtODIzZi00ZTI0
LWExMTAtYjJkY2ZmNjAyNzliIiwgImV4cG9ydF9rZXkiOiAiZm5faHRtbDJwZGYifV0sICJhY3Rp
b25zIjogW3siaWQiOiAzNSwgIm5hbWUiOiAiRXhhbXBsZTogSFRNTDJQREYiLCAidHlwZSI6IDEs
ICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJjb25kaXRpb25zIjogW10sICJhdXRvbWF0aW9u
cyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIndvcmtmbG93cyI6IFsiZXhhbXBs
ZV9odG1sMnBkZiJdLCAidmlld19pdGVtcyI6IFtdLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAs
ICJ1dWlkIjogImNkYjQ5YTM0LTA5MTItNGM0YS1iZWYzLTBiZjVjY2UzNGFlNiIsICJleHBvcnRf
a2V5IjogIkV4YW1wbGU6IEhUTUwyUERGIiwgImxvZ2ljX3R5cGUiOiAiYWxsIn1dLCAibGF5b3V0
cyI6IFtdLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJ0aW1lZnJhbWVzIjogbnVsbCwgImxvY2Fs
ZSI6IG51bGwsICJpbmR1c3RyaWVzIjogbnVsbCwgInJlZ3VsYXRvcnMiOiBudWxsLCAiZ2VvcyI6
IG51bGwsICJ0YXNrX29yZGVyIjogW10sICJhY3Rpb25fb3JkZXIiOiBbXSwgInR5cGVzIjogW10s
ICJzY3JpcHRzIjogW10sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAid29ya2Zsb3dz
IjogW3sid29ya2Zsb3dfaWQiOiAyMiwgIm5hbWUiOiAiRXhhbXBsZTogSFRNTDJQREYiLCAicHJv
Z3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9odG1sMnBkZiIsICJvYmplY3RfdHlwZSI6ICJhcnRp
ZmFjdCIsICJkZXNjcmlwdGlvbiI6ICIiLCAiY3JlYXRvcl9pZCI6ICJiQGEuY29tIiwgImxhc3Rf
bW9kaWZpZWRfYnkiOiAiYkBhLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTM3MjA4ODIz
MTk0LCAiZXhwb3J0X2tleSI6ICJleGFtcGxlX2h0bWwycGRmIiwgInV1aWQiOiAiYjMxZTkwZjgt
NTgzYy00NWMwLWE3YzAtMTVkOTRiOTY5YjM3IiwgImNvbnRlbnQiOiB7IndvcmtmbG93X2lkIjog
ImV4YW1wbGVfaHRtbDJwZGYiLCAieG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGlu
Zz1cIlVURi04XCI/PjxkZWZpbml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVj
L0JQTU4vMjAxMDA1MjQvTU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcv
c3BlYy9CUE1OLzIwMTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcv
c3BlYy9ERC8yMDEwMDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3Nw
ZWMvREQvMjAxMDA1MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50Lmli
bS5jb20vYnBtblwiIHhtbG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1h
XCIgeG1sbnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2Vc
IiB0YXJnZXROYW1lc3BhY2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48cHJvY2Vz
cyBpZD1cImV4YW1wbGVfaHRtbDJwZGZcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4
YW1wbGU6IEhUTUwyUERGXCI+PGRvY3VtZW50YXRpb24vPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRF
dmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wc3d6Nm9iPC9vdXRnb2luZz48
L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMDhucHVuZFwiIG5hbWU9
XCJIVE1MMlBERlwiIHJlc2lsaWVudDp0eXBlPVwiZnVuY3Rpb25cIj48ZXh0ZW5zaW9uRWxlbWVu
dHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlkPVwiM2Y5MjhlYWYtMTExNi00Yzg5LWE2ZTItZmVj
MTkxOGI1ZGJhXCI+e1wiaW5wdXRzXCI6e1wiOWQwZTI4ODctOTFiYy00NWVjLTgzMWYtYjUxOTk2
ZTAxZmE2XCI6e1wiaW5wdXRfdHlwZVwiOlwic3RhdGljXCIsXCJzdGF0aWNfaW5wdXRcIjp7XCJt
dWx0aXNlbGVjdF92YWx1ZVwiOltdLFwidGV4dF92YWx1ZVwiOlwiJmx0O3RhYmxlJmd0OyZsdDt0
ciZndDsmbHQ7dGQmZ3Q7YSZsdDsvdGQmZ3Q7Jmx0O3RkJmd0O2ImbHQ7L3RkJmd0OyZsdDsvdHIm
Z3Q7Jmx0O3RyJmd0OyZsdDt0ZCZndDtjJmx0Oy90ZCZndDsmbHQ7dGQmZ3Q7ZCZsdDsvdGQmZ3Q7
Jmx0Oy90ciZndDsmbHQ7L3RhYmxlJmd0O1wifX0sXCIyMWFjMmFjMC1hYmM5LTQ4NWEtYTY2ZS01
YWI2ODA0MTViNDBcIjp7XCJpbnB1dF90eXBlXCI6XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwi
OntcIm11bHRpc2VsZWN0X3ZhbHVlXCI6W10sXCJ0ZXh0X3ZhbHVlXCI6XCJzdHJpbmdcIn19LFwi
M2IwMWQ2MWYtY2Q5My00N2Q3LWFiNGEtYjMyYzJiOGUxYmZhXCI6e1wiaW5wdXRfdHlwZVwiOlwi
c3RhdGljXCIsXCJzdGF0aWNfaW5wdXRcIjp7XCJtdWx0aXNlbGVjdF92YWx1ZVwiOltdLFwidGV4
dF92YWx1ZVwiOlwiQHBhZ2UgeyBzaXplOiBsYW5kc2NhcGU7IH0qIHsgZm9udC1mYW1pbHk6IEFy
aWFsOyBmb250LXNpemU6IHNtYWxsOyB9dGFibGUgeyBib3JkZXItY29sbGFwc2U6IGNvbGxhcHNl
OyB9dGFibGUsIHRoLCB0ZCB7IGJvcmRlcjogMXB4IHNvbGlkIGJsYWNrOyB9XCJ9fX0sXCJwb3N0
X3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIHJlc3VsdHMgaW4gYmFzZTY0LiBzZWUgb3V0cHV0IHBy
b3BlcnR5ICdwZGYnXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48
aW5jb21pbmc+U2VxdWVuY2VGbG93XzBzd3o2b2I8L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5j
ZUZsb3dfMHZwcjc5eDwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48c2VxdWVuY2VGbG93IGlkPVwi
U2VxdWVuY2VGbG93XzBzd3o2b2JcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0
YXJnZXRSZWY9XCJTZXJ2aWNlVGFza18wOG5wdW5kXCIvPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50
XzA5M3dzeHdcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzB2cHI3OXg8L2luY29taW5nPjwvZW5k
RXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wdnByNzl4XCIgc291cmNlUmVm
PVwiU2VydmljZVRhc2tfMDhucHVuZFwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzA5M3dzeHdcIi8+
PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0
IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBp
ZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1c
IiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjx0ZXh0QW5ub3RhdGlvbiBp
ZD1cIlRleHRBbm5vdGF0aW9uXzFvZG14MnhcIj48dGV4dD5SZXN1bHRzIGluIGJhc2U2NDwvdGV4
dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFnM2g4bThc
IiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wOG5wdW5kXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90
YXRpb25fMW9kbXgyeFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5E
aWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlk
PVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZl
bnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBo
ZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQ
TU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wi
IHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRp
OkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRl
eHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lk
dGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRp
OkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2Np
YXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJv
bWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlw
ZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQ
TU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzA4bnB1bmRcIiBpZD1cIlNlcnZpY2VU
YXNrXzA4bnB1bmRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBc
IiB4PVwiMjU4XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRn
ZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wc3d6Nm9iXCIgaWQ9XCJTZXF1ZW5jZUZsb3df
MHN3ejZvYl9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIyNThcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjIyOFwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBN
TkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwi
RW5kRXZlbnRfMDkzd3N4d1wiIGlkPVwiRW5kRXZlbnRfMDkzd3N4d19kaVwiPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjQ0N1wiIHk9XCIxODhcIi8+PGJwbW5k
aTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI0
NjVcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJw
bW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wdnByNzl4XCIgaWQ9XCJT
ZXF1ZW5jZUZsb3dfMHZwcjc5eF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzU4XCIgeHNpOnR5
cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI0NDdcIiB4
c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21n
ZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQwMi41XCIgeT1cIjE4NFwi
Lz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUg
YnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xb2RteDJ4XCIgaWQ9XCJUZXh0QW5ub3RhdGlv
bl8xb2RteDJ4X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMVwiIHdpZHRoPVwiMTMzXCIg
eD1cIjM3NVwiIHk9XCI4M1wiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBi
cG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFnM2g4bThcIiBpZD1cIkFzc29jaWF0aW9uXzFnM2g4
bThfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM1MlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRc
IiB5PVwiMTcwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNDIzXCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIxMTRcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwv
YnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgInZlcnNpb24iOiAyfSwgImFjdGlv
bnMiOiBbXX1dLCAicm9sZXMiOiBbXSwgIndvcmtzcGFjZXMiOiBbXSwgImZ1bmN0aW9ucyI6IFt7
ImlkIjogMjYsICJuYW1lIjogImh0bWwycGRmIiwgImRpc3BsYXlfbmFtZSI6ICJIVE1MMlBERiIs
ICJkZXNjcmlwdGlvbiI6IHsiZm9ybWF0IjogInRleHQiLCAiY29udGVudCI6ICJjb252ZXJ0IGh0
bWwgdGV4dCBvciBhIHVybCByZWZlcmVuY2UgdG8gYSBiYXNlNjQgZW5jb2RlZCBwZGYgZG9jdW1l
bnQuIn0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAiZm5faHRtbDJwZGYiLCAiZXhwb3J0X2tleSI6
ICJodG1sMnBkZiIsICJ1dWlkIjogIjNmOTI4ZWFmLTExMTYtNGM4OS1hNmUyLWZlYzE5MThiNWRi
YSIsICJ2ZXJzaW9uIjogMSwgImNyZWF0b3IiOiB7ImlkIjogMywgInR5cGUiOiAidXNlciIsICJu
YW1lIjogImJAYS5jb20iLCAiZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiJ9LCAi
bGFzdF9tb2RpZmllZF9ieSI6IHsiaWQiOiAzLCAidHlwZSI6ICJ1c2VyIiwgIm5hbWUiOiAiYkBh
LmNvbSIsICJkaXNwbGF5X25hbWUiOiAiUmVzaWxpZW50IFN5c2FkbWluIn0sICJsYXN0X21vZGlm
aWVkX3RpbWUiOiAxNTM3MjA4Mjk5OTgxLCAidmlld19pdGVtcyI6IFt7InN0ZXBfbGFiZWwiOiBu
dWxsLCAic2hvd19pZiI6IG51bGwsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlw
ZSI6ICJfX2Z1bmN0aW9uIiwgImNvbnRlbnQiOiAiOWQwZTI4ODctOTFiYy00NWVjLTgzMWYtYjUx
OTk2ZTAxZmE2IiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZX0sIHsic3RlcF9sYWJlbCI6IG51
bGwsICJzaG93X2lmIjogbnVsbCwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBl
IjogIl9fZnVuY3Rpb24iLCAiY29udGVudCI6ICIyMWFjMmFjMC1hYmM5LTQ4NWEtYTY2ZS01YWI2
ODA0MTViNDAiLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlfSwgeyJzdGVwX2xhYmVsIjogbnVs
bCwgInNob3dfaWYiOiBudWxsLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUi
OiAiX19mdW5jdGlvbiIsICJjb250ZW50IjogIjNiMDFkNjFmLWNkOTMtNDdkNy1hYjRhLWIzMmMy
YjhlMWJmYSIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2V9XSwgIndvcmtmbG93cyI6IFt7Indv
cmtmbG93X2lkIjogMjIsICJuYW1lIjogIkV4YW1wbGU6IEhUTUwyUERGIiwgInByb2dyYW1tYXRp
Y19uYW1lIjogImV4YW1wbGVfaHRtbDJwZGYiLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAi
ZGVzY3JpcHRpb24iOiBudWxsLCAidXVpZCI6IG51bGwsICJhY3Rpb25zIjogW119XX1dfQ==
"""
    )
