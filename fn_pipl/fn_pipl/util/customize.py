# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_pipl"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_pipl package"""
    reload_params = {"package": u"fn_pipl",
                    "incident_fields": [], 
                    "action_fields": [u"pipl_artifact_type"], 
                    "function_params": [u"pipl_artifact_type", u"pipl_artifact_value"], 
                    "datatables": [u"pipl_person_data"], 
                    "message_destinations": [u"fn_pipl"], 
                    "functions": [u"pipl_search_function"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [u"Create Artifact from Pipl Data"], 
                    "workflows": [u"example_pipl_search_function"], 
                    "actions": [u"Example: Create an Artifact from Pipl data", u"Example: Pipl search function"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Action fields:
    #     pipl_artifact_type
    #   Function inputs:
    #     pipl_artifact_type
    #     pipl_artifact_value
    #   DataTables:
    #     pipl_person_data
    #   Message Destinations:
    #     fn_pipl
    #   Functions:
    #     pipl_search_function
    #   Scripts:
    #     Create Artifact from Pipl Data
    #   Workflows:
    #     example_pipl_search_function
    #   Rules:
    #     Example: Create an Artifact from Pipl data
    #     Example: Pipl search function


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMCwgImJ1aWxkX251bWJl
ciI6IDQwMzUsICJ2ZXJzaW9uIjogIjMxLjAuNDAzNSJ9LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9u
IjogMiwgImlkIjogMSwgImV4cG9ydF9kYXRlIjogMTU0MjIxNjcyMjAxNCwgImZpZWxkcyI6IFt7
ImlkIjogMzgsICJuYW1lIjogImluY190cmFpbmluZyIsICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAi
cHJlZml4IjogbnVsbCwgInR5cGVfaWQiOiAwLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNp
ZGVudCBpcyBhIHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhpcyBmaWVsZCBp
cyByZWFkLW9ubHkuIiwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJoaWRlX25vdGlmaWNhdGlv
biI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBm
YWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAi
YzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2EzMzA4Y2NhIiwgIm9wZXJhdGlvbnMiOiBbXSwg
Im9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29ubHkiOiB0cnVlLCAi
Y2hhbmdlYWJsZSI6IHRydWUsICJyaWNoX3RleHQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiaW5j
aWRlbnQvaW5jX3RyYWluaW5nIiwgInRlbXBsYXRlcyI6IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNl
fSwgeyJpZCI6IDE0MCwgIm5hbWUiOiAicGlwbF9hcnRpZmFjdF90eXBlIiwgInRleHQiOiAiQXJ0
aWZhY3QgdHlwZSIsICJwcmVmaXgiOiAicHJvcGVydGllcyIsICJ0eXBlX2lkIjogNiwgInRvb2x0
aXAiOiAiIiwgInBsYWNlaG9sZGVyIjogIiIsICJpbnB1dF90eXBlIjogInNlbGVjdCIsICJyZXF1
aXJlZCI6ICJhbHdheXMiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImNob3NlbiI6IGZh
bHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiBm
YWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjogImM3NmM3YzY0LTU2YmQtNGFjZi04ZTk3
LTJjOGFlYzE5ZmFkYiIsICJvcGVyYXRpb25zIjogW10sICJvcGVyYXRpb25fcGVybXMiOiB7fSwg
InZhbHVlcyI6IFt7InZhbHVlIjogMTUwLCAibGFiZWwiOiAiRW1haWwgUmVjaXBpZW50IiwgImVu
YWJsZWQiOiB0cnVlLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlkIjogIjg5ZTM1OTQzLTI4MWEt
NDhmOS05Mzk4LTljYjk2Y2NhMGY1YSIsICJoaWRkZW4iOiBmYWxzZSwgImRlZmF1bHQiOiB0cnVl
fSwgeyJ2YWx1ZSI6IDE1MSwgImxhYmVsIjogIkVtYWlsIFNlbmRlciIsICJlbmFibGVkIjogdHJ1
ZSwgInByb3BlcnRpZXMiOiBudWxsLCAidXVpZCI6ICJjNGU2OTk5MC05YzUyLTQzNWMtODdmOC1m
OWQxMGUxMzEzOTEiLCAiaGlkZGVuIjogZmFsc2UsICJkZWZhdWx0IjogZmFsc2V9LCB7InZhbHVl
IjogMTUyLCAibGFiZWwiOiAiRW1haWwgU2VuZGVyIE5hbWUiLCAiZW5hYmxlZCI6IHRydWUsICJw
cm9wZXJ0aWVzIjogbnVsbCwgInV1aWQiOiAiODIxZWE5ZGYtYzY5MC00YWYyLThmMjItZDMyYTk4
MjE4YmNkIiwgImhpZGRlbiI6IGZhbHNlLCAiZGVmYXVsdCI6IGZhbHNlfSwgeyJ2YWx1ZSI6IDE1
MywgImxhYmVsIjogIlVzZXIgQWNjb3VudCIsICJlbmFibGVkIjogdHJ1ZSwgInByb3BlcnRpZXMi
OiBudWxsLCAidXVpZCI6ICI0ODgyMWNiYi04YWQ4LTQzZGUtYjlkNi05M2Y3YjA1Y2MyY2MiLCAi
aGlkZGVuIjogZmFsc2UsICJkZWZhdWx0IjogZmFsc2V9LCB7InZhbHVlIjogMTU0LCAibGFiZWwi
OiAiTWFsd2FyZSBNRDUgSGFzaCIsICJlbmFibGVkIjogdHJ1ZSwgInByb3BlcnRpZXMiOiBudWxs
LCAidXVpZCI6ICJjNTUzZTMxMy1hZTBkLTRkYTYtODZhYy0zM2IxMWUxMjJkNTUiLCAiaGlkZGVu
IjogZmFsc2UsICJkZWZhdWx0IjogZmFsc2V9LCB7InZhbHVlIjogMjAwLCAibGFiZWwiOiAiU3Ry
aW5nIiwgImVuYWJsZWQiOiB0cnVlLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlkIjogIjhlOTE4
NDhlLTkxYmMtNGY0Yy05YjUyLTFiNzRmYTkyMzA0MCIsICJoaWRkZW4iOiBmYWxzZSwgImRlZmF1
bHQiOiBmYWxzZX1dLCAicmVhZF9vbmx5IjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgInJp
Y2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3BpcGxfYXJ0
aWZhY3RfdHlwZSIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQi
OiAxNDIsICJuYW1lIjogInBpcGxfYXJ0aWZhY3RfdmFsdWUiLCAidGV4dCI6ICJwaXBsX2FydGlm
YWN0X3ZhbHVlIiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMTEsICJ0b29sdGlwIjogIiIs
ICJwbGFjZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInJlcXVpcmVkIjogImFs
d2F5cyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZh
dWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50
ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiOTkzZWIyZTMtNjVmMy00MjRkLTlhM2EtOWEzODkyMTgw
ZjcwIiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjog
W10sICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0Ijog
ZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vcGlwbF9hcnRpZmFjdF92YWx1ZSIsICJ0
ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQiOiAxNDEsICJuYW1lIjog
InBpcGxfYXJ0aWZhY3RfdHlwZSIsICJ0ZXh0IjogInBpcGxfYXJ0aWZhY3RfdHlwZSIsICJwcmVm
aXgiOiBudWxsLCAidHlwZV9pZCI6IDExLCAidG9vbHRpcCI6ICIiLCAicGxhY2Vob2xkZXIiOiAi
IiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAiaGlkZV9ub3Rp
ZmljYXRpb24iOiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2Vy
dmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1
dWlkIjogImU5YzAxNmU4LTQxZjYtNDc5MS1hOGEyLTRiNjVlY2QwYmQ4YiIsICJvcGVyYXRpb25z
IjogW10sICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5Ijog
ZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tl
eSI6ICJfX2Z1bmN0aW9uL3BpcGxfYXJ0aWZhY3RfdHlwZSIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRl
cHJlY2F0ZWQiOiBmYWxzZX1dLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE1
NDIzMDA4MjA5NTksICJjcmVhdGVfZGF0ZSI6IDE1NDIzMDA4MjA5NTksICJ1dWlkIjogImJmZWVj
MmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21p
emF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9u
IFBhY2thZ2VzIChpbnRlcm5hbCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChp
bnRlcm5hbCkiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQi
OiBudWxsLCAiaGlkZGVuIjogZmFsc2UsICJpZCI6IDB9XSwgInBoYXNlcyI6IFtdLCAiYXV0b21h
dGljX3Rhc2tzIjogW10sICJvdmVycmlkZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjog
W3sibmFtZSI6ICJmbl9waXBsIiwgInByb2dyYW1tYXRpY19uYW1lIjogImZuX3BpcGwiLCAiZGVz
dGluYXRpb25fdHlwZSI6IDAsICJleHBlY3RfYWNrIjogdHJ1ZSwgInVzZXJzIjogWyJhQGEuY29t
Il0sICJ1dWlkIjogImNjNWM1YWQ4LWNkMjQtNDBlOC1hZDdhLTU0NmQzYWYzY2QyMSIsICJleHBv
cnRfa2V5IjogImZuX3BpcGwifV0sICJhY3Rpb25zIjogW3siaWQiOiAxNSwgIm5hbWUiOiAiRXhh
bXBsZTogQ3JlYXRlIGFuIEFydGlmYWN0IGZyb20gUGlwbCBkYXRhIiwgInR5cGUiOiAxLCAib2Jq
ZWN0X3R5cGUiOiAicGlwbF9wZXJzb25fZGF0YSIsICJjb25kaXRpb25zIjogW10sICJhdXRvbWF0
aW9ucyI6IFt7InR5cGUiOiAicnVuX3NjcmlwdCIsICJ2YWx1ZSI6IG51bGwsICJzY3JpcHRzX3Rv
X3J1biI6ICJDcmVhdGUgQXJ0aWZhY3QgZnJvbSBQaXBsIERhdGEifV0sICJtZXNzYWdlX2Rlc3Rp
bmF0aW9ucyI6IFtdLCAid29ya2Zsb3dzIjogW10sICJ2aWV3X2l0ZW1zIjogW3sic3RlcF9sYWJl
bCI6IG51bGwsICJzaG93X2lmIjogbnVsbCwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVs
ZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAiY29udGVudCI6ICJjNzZjN2M2NC01NmJkLTRh
Y2YtOGU5Ny0yYzhhZWMxOWZhZGIiLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlfV0sICJ0aW1l
b3V0X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAiNjkxYTcwZDItNDA3MS00MmNjLTg0MDUtOGYy
OWI5N2E2ZjMyIiwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogQ3JlYXRlIGFuIEFydGlmYWN0IGZy
b20gUGlwbCBkYXRhIiwgImxvZ2ljX3R5cGUiOiAiYWxsIn0sIHsiaWQiOiAxNiwgIm5hbWUiOiAi
RXhhbXBsZTogUGlwbCBzZWFyY2ggZnVuY3Rpb24iLCAidHlwZSI6IDEsICJvYmplY3RfdHlwZSI6
ICJhcnRpZmFjdCIsICJjb25kaXRpb25zIjogW3sibWV0aG9kIjogImluIiwgImZpZWxkX25hbWUi
OiAiYXJ0aWZhY3QudHlwZSIsICJ2YWx1ZSI6IFsiRW1haWwgU2VuZGVyIiwgIkVtYWlsIFNlbmRl
ciBOYW1lIiwgIkVtYWlsIFJlY2lwaWVudCIsICJVc2VyIEFjY291bnQiLCAiU3RyaW5nIl0sICJ0
eXBlIjogbnVsbCwgImV2YWx1YXRpb25faWQiOiBudWxsfV0sICJhdXRvbWF0aW9ucyI6IFtdLCAi
bWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIndvcmtmbG93cyI6IFsiZXhhbXBsZV9waXBsX3Nl
YXJjaF9mdW5jdGlvbiJdLCAidmlld19pdGVtcyI6IFtdLCAidGltZW91dF9zZWNvbmRzIjogODY0
MDAsICJ1dWlkIjogIjI2N2IxMmM3LThkY2QtNDk2NS05NGNhLTQ4M2Y2NGExYTUwYiIsICJleHBv
cnRfa2V5IjogIkV4YW1wbGU6IFBpcGwgc2VhcmNoIGZ1bmN0aW9uIiwgImxvZ2ljX3R5cGUiOiAi
YWxsIn1dLCAibGF5b3V0cyI6IFtdLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJ0aW1lZnJhbWVz
IjogbnVsbCwgImxvY2FsZSI6IG51bGwsICJpbmR1c3RyaWVzIjogbnVsbCwgInJlZ3VsYXRvcnMi
OiBudWxsLCAiZ2VvcyI6IG51bGwsICJ0YXNrX29yZGVyIjogW10sICJhY3Rpb25fb3JkZXIiOiBb
XSwgInR5cGVzIjogW3siaWQiOiBudWxsLCAidHlwZV9pZCI6IDgsICJ0eXBlX25hbWUiOiAicGlw
bF9wZXJzb25fZGF0YSIsICJmaWVsZHMiOiB7InBpcGxfcG9zc2libGVfbWF0Y2hfbm8iOiB7Imlk
IjogMTM1LCAibmFtZSI6ICJwaXBsX3Bvc3NpYmxlX21hdGNoX25vIiwgInRleHQiOiAiUG9zc2li
bGUgcGVvcGxlIG1hdGNoIG5vLiIsICJwcmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDEwMDAsICJ0
b29sdGlwIjogIiIsICJwbGFjZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImhp
ZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJjaG9zZW4iOiB0cnVlLCAiZGVmYXVsdF9jaG9zZW5f
Ynlfc2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiB0cnVlLCAiaW50ZXJuYWwiOiBmYWxz
ZSwgInV1aWQiOiAiN2ZiNWNjOGEtYmM0MS00NmNjLWI2NzQtMWQwODM1OGU4ZGM5IiwgIm9wZXJh
dGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29u
bHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBv
cnRfa2V5IjogInBpcGxfcGVyc29uX2RhdGEvcGlwbF9wb3NzaWJsZV9tYXRjaF9ubyIsICJvcmRl
ciI6IDQsICJ3aWR0aCI6IDQ1LCAidGVtcGxhdGVzIjogW10sICJkZXByZWNhdGVkIjogZmFsc2V9
LCAicGlwbF9wcm9wZXJ0eSI6IHsiaWQiOiAxMzYsICJuYW1lIjogInBpcGxfcHJvcGVydHkiLCAi
dGV4dCI6ICJQcm9wZXJ0eSIsICJwcmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDEwMDAsICJ0b29s
dGlwIjogIiIsICJwbGFjZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImhpZGVf
bm90aWZpY2F0aW9uIjogZmFsc2UsICJjaG9zZW4iOiB0cnVlLCAiZGVmYXVsdF9jaG9zZW5fYnlf
c2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiB0cnVlLCAiaW50ZXJuYWwiOiBmYWxzZSwg
InV1aWQiOiAiYWE0Y2I2ODYtZTZhMi00NWY5LThlYTYtNDU5ODkyYjcyNzYzIiwgIm9wZXJhdGlv
bnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29ubHki
OiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBvcnRf
a2V5IjogInBpcGxfcGVyc29uX2RhdGEvcGlwbF9wcm9wZXJ0eSIsICJvcmRlciI6IDIsICJ3aWR0
aCI6IDUwLCAidGVtcGxhdGVzIjogW10sICJkZXByZWNhdGVkIjogZmFsc2V9LCAicGlwbF92YWx1
ZSI6IHsiaWQiOiAxMzgsICJuYW1lIjogInBpcGxfdmFsdWUiLCAidGV4dCI6ICJWYWx1ZSIsICJw
cmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDEwMDAsICJ0b29sdGlwIjogIiIsICJwbGFjZWhvbGRl
ciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0YXJlYSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZh
bHNlLCAiY2hvc2VuIjogdHJ1ZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAi
Ymxhbmtfb3B0aW9uIjogdHJ1ZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjogIjk5YzgwN2Ni
LTdmMmUtNDJiNS1hYzQ0LTAyYmNmZDNjOGI2OSIsICJvcGVyYXRpb25zIjogW10sICJvcGVyYXRp
b25fcGVybXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogZmFsc2UsICJjaGFuZ2Vh
YmxlIjogdHJ1ZSwgInJpY2hfdGV4dCI6IHRydWUsICJleHBvcnRfa2V5IjogInBpcGxfcGVyc29u
X2RhdGEvcGlwbF92YWx1ZSIsICJvcmRlciI6IDMsICJ3aWR0aCI6IDE2MywgInRlbXBsYXRlcyI6
IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNlfSwgInBpcGxfaW5mZXJyZWQiOiB7ImlkIjogMTMzLCAi
bmFtZSI6ICJwaXBsX2luZmVycmVkIiwgInRleHQiOiAiSW5mZXJyZWQiLCAicHJlZml4IjogbnVs
bCwgInR5cGVfaWQiOiAxMDAwLCAidG9vbHRpcCI6ICIiLCAicGxhY2Vob2xkZXIiOiAiIiwgImlu
cHV0X3R5cGUiOiAidGV4dCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjog
dHJ1ZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjog
dHJ1ZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjogIjAxODJjOGExLWE2MTgtNGMyNC05YjYy
LTUyNmVjNTUwYzAzYSIsICJvcGVyYXRpb25zIjogW10sICJvcGVyYXRpb25fcGVybXMiOiB7fSwg
InZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgInJp
Y2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJwaXBsX3BlcnNvbl9kYXRhL3BpcGxfaW5m
ZXJyZWQiLCAib3JkZXIiOiA2LCAid2lkdGgiOiA0MSwgInRlbXBsYXRlcyI6IFtdLCAiZGVwcmVj
YXRlZCI6IGZhbHNlfSwgInBpcGxfYXJ0aWZhY3RfdmFsdWUiOiB7ImlkIjogMTM5LCAibmFtZSI6
ICJwaXBsX2FydGlmYWN0X3ZhbHVlIiwgInRleHQiOiAiQXJ0aWZhY3QgdmFsdWUiLCAicHJlZml4
IjogbnVsbCwgInR5cGVfaWQiOiAxMDAwLCAidG9vbHRpcCI6ICIiLCAicGxhY2Vob2xkZXIiOiAi
IiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hv
c2VuIjogdHJ1ZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiYmxhbmtfb3B0
aW9uIjogdHJ1ZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjogIjliNGJhY2M1LTNkNDAtNGI3
MC05NGEwLThjZWNkODE0MGJiMiIsICJvcGVyYXRpb25zIjogW10sICJvcGVyYXRpb25fcGVybXMi
OiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1
ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJwaXBsX3BlcnNvbl9kYXRhL3Bp
cGxfYXJ0aWZhY3RfdmFsdWUiLCAib3JkZXIiOiAxLCAid2lkdGgiOiAxNDQsICJ0ZW1wbGF0ZXMi
OiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sICJwaXBsX21hdGNoIjogeyJpZCI6IDEzNywgIm5h
bWUiOiAicGlwbF9tYXRjaCIsICJ0ZXh0IjogIk1hdGNoIiwgInByZWZpeCI6IG51bGwsICJ0eXBl
X2lkIjogMTAwMCwgInRvb2x0aXAiOiAiIiwgInBsYWNlaG9sZGVyIjogIiIsICJpbnB1dF90eXBl
IjogInRleHQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImNob3NlbiI6IHRydWUsICJk
ZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IHRydWUsICJp
bnRlcm5hbCI6IGZhbHNlLCAidXVpZCI6ICI2YWM5NWU2ZS1mYjM1LTQzMWYtYTU5OS1kZGU1YTM3
NmY3OGUiLCAib3BlcmF0aW9ucyI6IFtdLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ2YWx1ZXMi
OiBbXSwgInJlYWRfb25seSI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJyaWNoX3RleHQi
OiBmYWxzZSwgImV4cG9ydF9rZXkiOiAicGlwbF9wZXJzb25fZGF0YS9waXBsX21hdGNoIiwgIm9y
ZGVyIjogNSwgIndpZHRoIjogMzMsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxz
ZX0sICJwaXBsX3RpbWVzdGFtcCI6IHsiaWQiOiAxMzQsICJuYW1lIjogInBpcGxfdGltZXN0YW1w
IiwgInRleHQiOiAiVGltZXN0YW1wIiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMTAwMCwg
InRvb2x0aXAiOiAiIiwgInBsYWNlaG9sZGVyIjogIiIsICJpbnB1dF90eXBlIjogImRhdGV0aW1l
cGlja2VyIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJjaG9zZW4iOiB0cnVlLCAiZGVm
YXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiB0cnVlLCAiaW50
ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiYzI0Y2VjMTItZjRjOC00Zjg1LTkzMjQtMjU5NjdlMDRl
N2RhIiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjog
W10sICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0Ijog
ZmFsc2UsICJleHBvcnRfa2V5IjogInBpcGxfcGVyc29uX2RhdGEvcGlwbF90aW1lc3RhbXAiLCAi
b3JkZXIiOiAwLCAid2lkdGgiOiAxMTUsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBm
YWxzZX19LCAicHJvcGVydGllcyI6IHsiY2FuX2NyZWF0ZSI6IGZhbHNlLCAiY2FuX2Rlc3Ryb3ki
OiBmYWxzZSwgImZvcl93aG8iOiBbXX0sICJwYXJlbnRfdHlwZXMiOiBbImluY2lkZW50Il0sICJk
aXNwbGF5X25hbWUiOiAiUGlwbCBwZXJzb24gZGF0YSIsICJmb3Jfbm90aWZpY2F0aW9ucyI6IGZh
bHNlLCAiZm9yX2FjdGlvbnMiOiBmYWxzZSwgImZvcl9jdXN0b21fZmllbGRzIjogZmFsc2UsICJl
eHBvcnRfa2V5IjogInBpcGxfcGVyc29uX2RhdGEiLCAidXVpZCI6ICI3NWRkN2I3YS02YTQ3LTQ2
ODctODdhZC1mMmVhMjQ4MjA2ZTgiLCAiYWN0aW9ucyI6IFtdLCAic2NyaXB0cyI6IFtdfV0sICJz
Y3JpcHRzIjogW3siaWQiOiAxLCAibmFtZSI6ICJDcmVhdGUgQXJ0aWZhY3QgZnJvbSBQaXBsIERh
dGEiLCAiZGVzY3JpcHRpb24iOiAiU2NyaXB0IGNyZWF0ZXMgYW4gYXJ0aWZhY3QgYmFzZWQgZnJv
bSBhIHNlbGVjdGVkIHJvdyBpbiBQaXBsIHBvc3NpYmxlIHBlcnNvbiBkYXRhLiIsICJsYW5ndWFn
ZSI6ICJweXRob24iLCAib2JqZWN0X3R5cGUiOiAicGlwbF9wZXJzb25fZGF0YSIsICJ1dWlkIjog
IjBmZTRjYzI2LWE0MjgtNDEwMy04NTU0LTdkMzE2NTZkNjBkZiIsICJhY3Rpb25zIjogW10sICJz
Y3JpcHRfdGV4dCI6ICIjIENyZWF0ZSBhbiBhcnRpZmFjdCBiYXNlZCBmcm9tIGEgc2VsZWN0ZWQg
cm93IGluIFBpcGwgcG9zc2libGUgcGVyc29uIGRhdGEuXG5cbiMgYXJ0aWZhY3QgZGVzY3JpcHRp
b25cbmFydGlmYWN0X2Rlc2NyaXB0aW9uID0gdVwiXCJcIkNyZWF0ZWQgYnkgUGlwbCBEYXRhIHJl
c3VsdHMgZ2VuZXJhdGVkIGZvciBhcnRpZmFjdF92YWx1ZSB7fVwiXCJcIi5mb3JtYXQocm93LnBp
cGxfYXJ0aWZhY3RfdmFsdWUpXG5cbiMgYXJ0aWZhY3QgdHlwZSAtIHJlYWQgaXQgZnJvbSB0aGUg
bWVudSBpdGVtJ3MgYWN0aXZpdHkgZmllbGRcbmFydGlmYWN0X3R5cGUgPSBydWxlLnByb3BlcnRp
ZXMucGlwbF9hcnRpZmFjdF90eXBlXG5cbiMgYXJ0aWZhY3QgdmFsdWVcbiMgcGlwbF92YWx1ZSBj
b2x1bW4gaW4gUGlwIHBvc3NpYmxlIHBlcnNvbiBkYXRhIGlzIGluIHRoaXMgZm9ybWF0IHt1J2Zv
cm1hdCc6IHUnaHRtbCcsIHUnY29udGVudCc6IHUneW91ciBhcGkgZGF0YSd9IFxucmljaF90ZXh0
X3BpcGxfdmFsdWUgPSByb3cucGlwbF92YWx1ZVxuYXJ0aWZhY3RfdmFsdWUgPSByaWNoX3RleHRf
cGlwbF92YWx1ZS5nZXQoXCJjb250ZW50XCIpXG5cbiMgY3JlYXRlIGFuIGFydGlmYWN0XG5pZiBh
cnRpZmFjdF92YWx1ZTpcbiAgaW5jaWRlbnQuYWRkQXJ0aWZhY3QoYXJ0aWZhY3RfdHlwZSwgYXJ0
aWZhY3RfdmFsdWUsIGFydGlmYWN0X2Rlc2NyaXB0aW9uKSIsICJjcmVhdG9yX2lkIjogImFAYS5j
b20iLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhQGEuY29tIiwgImxhc3RfbW9kaWZpZWRfdGltZSI6
IDE1NDIyMDgwNjAzNDQsICJleHBvcnRfa2V5IjogIkNyZWF0ZSBBcnRpZmFjdCBmcm9tIFBpcGwg
RGF0YSJ9XSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ3
b3JrZmxvd19pZCI6IDEsICJuYW1lIjogIkV4YW1wbGU6IFBpcGwgc2VhcmNoIiwgInByb2dyYW1t
YXRpY19uYW1lIjogImV4YW1wbGVfcGlwbF9zZWFyY2hfZnVuY3Rpb24iLCAib2JqZWN0X3R5cGUi
OiAiYXJ0aWZhY3QiLCAiZGVzY3JpcHRpb24iOiAiRW5yaWNoZXMgeW91ciBsZWFkcyAobmFtZSwg
ZW1haWwgYWRkcmVzcywgcGhvbmUgbnVtYmVyLCBvciBzb2NpYWwgbWVkaWEgdXNlcm5hbWUpIHdp
dGggUGlwbCBhbmQgZ2V0cyB0aGVpciBwZXJzb25hbCwgcHJvZmVzc2lvbmFsLCBkZW1vZ3JhcGhp
YywgYW5kIGNvbnRhY3QgaW5mb3JtYXRpb24uIiwgImNyZWF0b3JfaWQiOiAiYUBhLmNvbSIsICJs
YXN0X21vZGlmaWVkX2J5IjogImFAYS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU0MjIx
NDc5NjcyNiwgImV4cG9ydF9rZXkiOiAiZXhhbXBsZV9waXBsX3NlYXJjaF9mdW5jdGlvbiIsICJ1
dWlkIjogIjA2MzY0NDk2LWZmMjgtNGU0OS1iOTc1LTgyNTYyMzc4ZjRjNSIsICJjb250ZW50Ijog
eyJ3b3JrZmxvd19pZCI6ICJleGFtcGxlX3BpcGxfc2VhcmNoX2Z1bmN0aW9uIiwgInhtbCI6ICI8
P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1s
bnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6
YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5z
Om9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpv
bWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVz
aWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRw
Oi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMu
b3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3
dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFtcGxlX3BpcGxfc2VhcmNoX2Z1
bmN0aW9uXCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBQaXBsIHNlYXJj
aFwiPjxkb2N1bWVudGF0aW9uPkVucmljaGVzIHlvdXIgbGVhZHMgKG5hbWUsIGVtYWlsIGFkZHJl
c3MsIHBob25lIG51bWJlciwgb3Igc29jaWFsIG1lZGlhIHVzZXJuYW1lKSB3aXRoIFBpcGwgYW5k
IGdldHMgdGhlaXIgcGVyc29uYWwsIHByb2Zlc3Npb25hbCwgZGVtb2dyYXBoaWMsIGFuZCBjb250
YWN0IGluZm9ybWF0aW9uLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZl
bnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMWc1djV0Zzwvb3V0Z29pbmc+PC9z
dGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzBwamVnOWhcIiBuYW1lPVwi
UGlwbCBzZWFyY2ggZnVuY3Rpb25cIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVu
c2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjgwM2RmNDc0LTJkZjAtNGNm
Mi04ODgyLWNmMmM1MTljY2E3NlwiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3Nj
cmlwdFwiOlwiZnJvbSBqYXZhLnV0aWwgaW1wb3J0IERhdGVcXG5cXG5kZWYgYWRkX3Jvd190b19w
aXBsX2RhdGF0YWJsZShkYl90aW1lc3RhbXAsIGRiX2FydGlmYWN0X3ZhbHVlLCBkYl9tYXRjaF9u
bywgZGJfcHJvcGVydHksIGRiX3ZhbHVlLCBkYl9tYXRjaCwgZGJfaW5mZXJyZWQpOlxcbiAgcGlw
bF9wZXJzb25fZGF0YSA9IGluY2lkZW50LmFkZFJvdyhcXFwicGlwbF9wZXJzb25fZGF0YVxcXCIp
XFxuICBwaXBsX3BlcnNvbl9kYXRhLnBpcGxfdGltZXN0YW1wID0gZGJfdGltZXN0YW1wXFxuICBw
aXBsX3BlcnNvbl9kYXRhLnBpcGxfYXJ0aWZhY3RfdmFsdWUgPSBkYl9hcnRpZmFjdF92YWx1ZVxc
biAgcGlwbF9wZXJzb25fZGF0YS5waXBsX3Bvc3NpYmxlX21hdGNoX25vID0gZGJfbWF0Y2hfbm9c
XG4gIHBpcGxfcGVyc29uX2RhdGEucGlwbF9wcm9wZXJ0eSA9IGRiX3Byb3BlcnR5XFxuICBwaXBs
X3BlcnNvbl9kYXRhLnBpcGxfdmFsdWUgPSBkYl92YWx1ZVxcbiAgcGlwbF9wZXJzb25fZGF0YS5w
aXBsX21hdGNoID0gZGJfbWF0Y2hcXG4gIHBpcGxfcGVyc29uX2RhdGEucGlwbF9pbmZlcnJlZCA9
IGRiX2luZmVycmVkXFxuXFxuaWYgcmVzdWx0cy5zdWNjZXNzOlxcblxcbiAgIyBDcmVhdGUgYSBk
YXRhdGFibGUgZnJvbSBwaXBsIHJlc3BvbnNlXFxuICBwb3NzaWJsZV9wZXJzb25fY291bnRlciA9
IDBcXG4gIGZvciBwZXJzb24gaW4gcmVzdWx0cy5wZXJzb25fbGlzdDpcXG4gICAgXFxuICAgICMg
Z2VuZXJhdGUgcmVzdWx0X2lkIGFuZCB0aW1lc3RhbXBcXG4gICAgcG9zc2libGVfcGVyc29uX2Nv
dW50ZXIgKz0gMVxcbiAgICBub3cgPSBEYXRlKClcXG4gICAgXFxuICAgICMgMC0xLiBUaGUgbGV2
ZWwgb2YgY29uZmlkZW5jZSB3ZSBoYXZlIHRoYXQgdGhpcyBpcyB0aGUgcGVyc29uIHlvdVx1MjAx
OXJlIGxvb2tpbmcgZm9yLlxcbiAgICBtYXRjaCA9IHN0cihwZXJzb24uZ2V0KFxcXCJAbWF0Y2hc
XFwiLCBcXFwiXFxcIikpXFxuICAgIFxcbiAgICAjIFdoZXRoZXIgdGhpcyBwZXJzb24gaXMgbWFk
ZSB1cCBzb2xlbHkgZnJvbSBkYXRhIGluZmVycmVkIGJ5IHN0YXRpc3RpY2FsIGFuYWx5c2lzIGZy
b20geW91ciBzZWFyY2ggcXVlcnkuIFxcbiAgICAjIFlvdSBjYW4gY29udHJvbCBpbmZlcmVuY2Ug
dXNpbmcgdGhlIG1pbmltdW1fcHJvYmFiaWxpdHkgcGFyYW1ldGVyLCBhbmQgaW5mZXJlbmNlIG9m
IHBlcnNvbnMgdXNpbmcgdGhlIGluZmVyX3BlcnNvbnMgcGFyYW1ldGVyLlxcbiAgICBpbmZlcnJl
ZCA9IHN0cihwZXJzb24uZ2V0KFxcXCJAaW5mZXJyZWRcXFwiLCBcXFwiXFxcIikpXFxuICAgIFxc
biAgICAjIFBlcnNvbiBkYXRhXFxuICAgIG5hbWVzID0gcGVyc29uLmdldChcXFwibmFtZXNcXFwi
LCBbXSlcXG4gICAgZm9yIG5hbWUgaW4gbmFtZXM6XFxuICAgICAgYWRkX3Jvd190b19waXBsX2Rh
dGF0YWJsZShub3csIGFydGlmYWN0LnZhbHVlLCBwb3NzaWJsZV9wZXJzb25fY291bnRlciwgXFxc
Im5hbWVcXFwiLCBuYW1lLmdldChcXFwiZGlzcGxheVxcXCIsIFxcXCJcXFwiKSwgbWF0Y2gsIGlu
ZmVycmVkKVxcbiAgICBcXG4gICAgZW1haWxzID0gcGVyc29uLmdldChcXFwiZW1haWxzXFxcIiwg
W10pXFxuICAgIGZvciBlbWFpbCBpbiBlbWFpbHM6XFxuICAgICAgYWRkX3Jvd190b19waXBsX2Rh
dGF0YWJsZShub3csIGFydGlmYWN0LnZhbHVlLCBwb3NzaWJsZV9wZXJzb25fY291bnRlciwgXFxc
ImVtYWlsIGFkZHJlc3NcXFwiLCBlbWFpbC5nZXQoXFxcImFkZHJlc3NcXFwiLCBcXFwiXFxcIiks
IG1hdGNoLCBpbmZlcnJlZClcXG4gICAgICBhZGRfcm93X3RvX3BpcGxfZGF0YXRhYmxlKG5vdywg
YXJ0aWZhY3QudmFsdWUsIHBvc3NpYmxlX3BlcnNvbl9jb3VudGVyLCBcXFwiYWRkcmVzc19tZDVc
XFwiLCBlbWFpbC5nZXQoXFxcImFkZHJlc3NfbWQ1XFxcIiwgXFxcIlxcXCIpLCBtYXRjaCwgaW5m
ZXJyZWQpXFxuICAgIFxcbiAgICB1c2VybmFtZXMgPSBwZXJzb24uZ2V0KFxcXCJ1c2VybmFtZXNc
XFwiLCBbXSlcXG4gICAgZm9yIHVzcm5hbWUgaW4gdXNlcm5hbWVzOlxcbiAgICAgIGFkZF9yb3df
dG9fcGlwbF9kYXRhdGFibGUobm93LCBhcnRpZmFjdC52YWx1ZSwgcG9zc2libGVfcGVyc29uX2Nv
dW50ZXIsIFxcXCJ1c2VybmFtZVxcXCIsIHVzcm5hbWUuZ2V0KFxcXCJjb250ZW50XFxcIiwgXFxc
IlxcXCIpLCBtYXRjaCwgaW5mZXJyZWQpXFxuICAgICAgXFxuICAgIHBob25lcyA9IHBlcnNvbi5n
ZXQoXFxcInBob25lc1xcXCIsIFtdKVxcbiAgICBmb3IgcGhvbmUgaW4gcGhvbmVzOlxcbiAgICAg
IGFkZF9yb3dfdG9fcGlwbF9kYXRhdGFibGUobm93LCBhcnRpZmFjdC52YWx1ZSwgcG9zc2libGVf
cGVyc29uX2NvdW50ZXIsIFxcXCJwaG9uZVxcXCIsIHBob25lLmdldChcXFwiZGlzcGxheV9pbnRl
cm5hdGlvbmFsXFxcIiwgXFxcIlxcXCIpLCBtYXRjaCwgaW5mZXJyZWQpXFxuICAgICAgXFxuICAg
IGdlbmRlciA9IHBlcnNvbi5nZXQoXFxcImdlbmRlclxcXCIpXFxuICAgIGlmIGdlbmRlcjpcXG4g
ICAgICBhZGRfcm93X3RvX3BpcGxfZGF0YXRhYmxlKG5vdywgYXJ0aWZhY3QudmFsdWUsIHBvc3Np
YmxlX3BlcnNvbl9jb3VudGVyLCBcXFwiZ2VuZGVyXFxcIiwgZ2VuZGVyLmdldChcXFwiY29udGVu
dFxcXCIsIFxcXCJcXFwiKSwgbWF0Y2gsIGluZmVycmVkKVxcbiAgICBcXG4gICAgZG9iID0gcGVy
c29uLmdldChcXFwiZG9iXFxcIilcXG4gICAgaWYgZG9iOlxcbiAgICAgIGFkZF9yb3dfdG9fcGlw
bF9kYXRhdGFibGUobm93LCBhcnRpZmFjdC52YWx1ZSwgcG9zc2libGVfcGVyc29uX2NvdW50ZXIs
IFxcXCJkb2JcXFwiLCBkb2IuZ2V0KFxcXCJkaXNwbGF5XFxcIiwgXFxcIlxcXCIpLCBtYXRjaCwg
aW5mZXJyZWQpXFxuICAgIFxcbiAgICBhZGRyZXNzZXMgPSBwZXJzb24uZ2V0KFxcXCJhZGRyZXNz
ZXNcXFwiLCBbXSlcXG4gICAgZm9yIGFkZHJlc3MgaW4gYWRkcmVzc2VzOlxcbiAgICAgIGFkZF9y
b3dfdG9fcGlwbF9kYXRhdGFibGUobm93LCBhcnRpZmFjdC52YWx1ZSwgcG9zc2libGVfcGVyc29u
X2NvdW50ZXIsIFxcXCJhZGRyZXNzXFxcIiwgYWRkcmVzcy5nZXQoXFxcImRpc3BsYXlcXFwiLCBc
XFwiXFxcIiksIG1hdGNoLCBpbmZlcnJlZClcXG4gICAgICBcXG4gICAgam9icyA9IHBlcnNvbi5n
ZXQoXFxcImpvYnNcXFwiLCBbXSlcXG4gICAgZm9yIGpvYiBpbiBqb2JzOlxcbiAgICAgIGFkZF9y
b3dfdG9fcGlwbF9kYXRhdGFibGUobm93LCBhcnRpZmFjdC52YWx1ZSwgcG9zc2libGVfcGVyc29u
X2NvdW50ZXIsIFxcXCJqb2JcXFwiLCBqb2IuZ2V0KFxcXCJkaXNwbGF5XFxcIiwgXFxcIlxcXCIp
LCBtYXRjaCwgaW5mZXJyZWQpXFxuICAgIFxcbiAgICBlZHVjYXRpb25zID0gcGVyc29uLmdldChc
XFwiZWR1Y2F0aW9uc1xcXCIsIFtdKVxcbiAgICBmb3IgZWR1IGluIGVkdWNhdGlvbnM6XFxuICAg
ICAgYWRkX3Jvd190b19waXBsX2RhdGF0YWJsZShub3csIGFydGlmYWN0LnZhbHVlLCBwb3NzaWJs
ZV9wZXJzb25fY291bnRlciwgXFxcImVkdWNhdGlvblxcXCIsIGVkdS5nZXQoXFxcImRpc3BsYXlc
XFwiLCBcXFwiXFxcIiksIG1hdGNoLCBpbmZlcnJlZClcXG4gICAgICBcXG4gICAgdXNlcl9pZHMg
PSBwZXJzb24uZ2V0KFxcXCJ1c2VyX2lkc1xcXCIsIFtdKVxcbiAgICBmb3IgdXNyX2lkIGluIHVz
ZXJfaWRzOlxcbiAgICAgIGFkZF9yb3dfdG9fcGlwbF9kYXRhdGFibGUobm93LCBhcnRpZmFjdC52
YWx1ZSwgcG9zc2libGVfcGVyc29uX2NvdW50ZXIsIFxcXCJ1c2VyX2lkXFxcIiwgdXNyX2lkLmdl
dChcXFwiY29udGVudFxcXCIsIFxcXCJcXFwiKSwgbWF0Y2gsIGluZmVycmVkKVxcbiAgICAgIFxc
biAgICBpbWFnZXMgPSBwZXJzb24uZ2V0KFxcXCJpbWFnZXNcXFwiLCBbXSlcXG4gICAgZm9yIGlt
YWdlIGluIGltYWdlczpcXG4gICAgICBpbWFnZV91cmwgPSBcXFwiXFxcIlxcXCImbHQ7YSBocmVm
PSd7MH0nJmd0O3swfSZsdDsvYSZndDtcXFwiXFxcIlxcXCIuZm9ybWF0KGltYWdlLmdldChcXFwi
dXJsXFxcIiwgXFxcIlxcXCIpKSBpZiBpbWFnZS5nZXQoXFxcInVybFxcXCIsIFxcXCJcXFwiKSBl
bHNlIFxcXCJcXFwiXFxuICAgICAgYWRkX3Jvd190b19waXBsX2RhdGF0YWJsZShub3csIGFydGlm
YWN0LnZhbHVlLCBwb3NzaWJsZV9wZXJzb25fY291bnRlciwgXFxcImltYWdlXFxcIiwgaW1hZ2Vf
dXJsLCBtYXRjaCwgaW5mZXJyZWQpXFxuICAgICAgXFxuICAgIHVybHMgPSBwZXJzb24uZ2V0KFxc
XCJ1cmxzXFxcIiwgW10pXFxuICAgIGZvciB1cmwgaW4gdXJsczpcXG4gICAgICB1cmxfdXJsID0g
XFxcIlxcXCJcXFwiJmx0O2EgaHJlZj0nezB9JyZndDt7MH0mbHQ7L2EmZ3Q7XFxcIlxcXCJcXFwi
LmZvcm1hdCh1cmwuZ2V0KFxcXCJ1cmxcXFwiLCBcXFwiXFxcIikpIGlmIHVybC5nZXQoXFxcInVy
bFxcXCIsIFxcXCJcXFwiKSBlbHNlIFxcXCJcXFwiXFxuICAgICAgYWRkX3Jvd190b19waXBsX2Rh
dGF0YWJsZShub3csIGFydGlmYWN0LnZhbHVlLCBwb3NzaWJsZV9wZXJzb25fY291bnRlciwgXFxc
InVybFxcXCIsIHVybF91cmwsIG1hdGNoLCBpbmZlcnJlZClcXG4gICAgICBcXG4gICMgU2F2ZSB0
aGUganNvbiByZXN1bHQgYXMgYW4gTm90ZVxcbiAgcmF3X2RhdGEgPSByZXN1bHRzLnJhd19kYXRh
IGlmIHJlc3VsdHMucmF3X2RhdGEgZWxzZSBcXFwiXFxcIlxcbiAgY291bnRlciA9IHBvc3NpYmxl
X3BlcnNvbl9jb3VudGVyIGlmIHBvc3NpYmxlX3BlcnNvbl9jb3VudGVyICZndDsgMCBlbHNlIFxc
XCJcXFwiXFxuICBub3RlVGV4dCA9IHVcXFwiXFxcIlxcXCJQaXBsIERhdGEgQVBJIHJlc3BvbnNl
IGZvciBhcnRpZmFjdF92YWx1ZSB7fSByZXR1cm5lZCB7fSB7fTogXFxcXG57fVxcXCJcXFwiXFxc
Ii5mb3JtYXQoYXJ0aWZhY3QudmFsdWUsIGNvdW50ZXIsIHJlc3VsdHMucGlwbF9yZXNwb25zZSwg
cmF3X2RhdGEpXFxuICBpbmNpZGVudC5hZGROb3RlKG5vdGVUZXh0KVwiLFwicHJlX3Byb2Nlc3Np
bmdfc2NyaXB0XCI6XCIjIFJlcXVpcmVkIGlucHV0cyBhcmU6IHRoZSBhcnRpZmFjdF90eXBlIGFu
ZCBhcnRpZmFjdF92YWx1ZVxcbmlucHV0cy5waXBsX2FydGlmYWN0X3R5cGUgPSBhcnRpZmFjdC50
eXBlXFxuaW5wdXRzLnBpcGxfYXJ0aWZhY3RfdmFsdWUgPSBhcnRpZmFjdC52YWx1ZVwiLFwicmVz
dWx0X25hbWVcIjpcIlwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+
PGluY29taW5nPlNlcXVlbmNlRmxvd18xZzV2NXRnPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVu
Y2VGbG93XzExM2EwYm48L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1c
IlNlcXVlbmNlRmxvd18xZzV2NXRnXCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIg
dGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMHBqZWc5aFwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVu
dF8wNnpseHFhXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18xMTNhMGJuPC9pbmNvbWluZz48L2Vu
ZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMTEzYTBiblwiIHNvdXJjZVJl
Zj1cIlNlcnZpY2VUYXNrXzBwamVnOWhcIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8wNnpseHFhXCIv
Pjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFy
dCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24g
aWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3ht
XCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48L3Byb2Nlc3M+PGJwbW5k
aTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1u
RWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFw
ZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVh
c3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYy
XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBc
IiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwv
YnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5v
dGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6
Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwv
YnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRp
b25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2lu
dCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndh
eXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2Jw
bW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNr
XzBwamVnOWhcIiBpZD1cIlNlcnZpY2VUYXNrXzBwamVnOWhfZGlcIj48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMzEzXCIgeT1cIjE2NlwiLz48L2JwbW5kaTpC
UE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xZzV2
NXRnXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMWc1djV0Z19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwi
MTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50
IHg9XCIzMTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQ
TU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI1NS41
XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5k
aTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8wNnpseHFhXCIgaWQ9XCJFbmRFdmVu
dF8wNnpseHFhX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4
PVwiNTI2XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdo
dD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjU0NFwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxh
YmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2Vx
dWVuY2VGbG93XzExM2EwYm5cIiBpZD1cIlNlcXVlbmNlRmxvd18xMTNhMGJuX2RpXCI+PG9tZ2Rp
OndheXBvaW50IHg9XCI0MTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48
b21nZGk6d2F5cG9pbnQgeD1cIjUyNlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2
XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1c
IjBcIiB4PVwiNDY5LjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpC
UE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0
aW9ucz4iLCAidmVyc2lvbiI6IDh9LCAiYWN0aW9ucyI6IFtdfV0sICJyb2xlcyI6IFtdLCAid29y
a3NwYWNlcyI6IFtdLCAiZnVuY3Rpb25zIjogW3siaWQiOiAxLCAibmFtZSI6ICJwaXBsX3NlYXJj
aF9mdW5jdGlvbiIsICJkaXNwbGF5X25hbWUiOiAiUGlwbCBzZWFyY2ggZnVuY3Rpb24iLCAiZGVz
Y3JpcHRpb24iOiB7ImZvcm1hdCI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiRnVuY3Rpb24gZW5yaWNo
ZXMgeW91ciBsZWFkcyAobmFtZSwgZW1haWwgYWRkcmVzcywgcGhvbmUgbnVtYmVyLCBvciBzb2Np
YWwgbWVkaWEgdXNlcm5hbWUpIHdpdGggUGlwbCBhbmQgZ2V0cyB0aGVpciBwZXJzb25hbCwgcHJv
ZmVzc2lvbmFsLCBkZW1vZ3JhcGhpYywgYW5kIGNvbnRhY3QgaW5mb3JtYXRpb24uIn0sICJkZXN0
aW5hdGlvbl9oYW5kbGUiOiAiZm5fcGlwbCIsICJleHBvcnRfa2V5IjogInBpcGxfc2VhcmNoX2Z1
bmN0aW9uIiwgInV1aWQiOiAiODAzZGY0NzQtMmRmMC00Y2YyLTg4ODItY2YyYzUxOWNjYTc2Iiwg
InZlcnNpb24iOiAxLCAiY3JlYXRvciI6IHsiaWQiOiAzLCAidHlwZSI6ICJ1c2VyIiwgIm5hbWUi
OiAiYUBhLmNvbSIsICJkaXNwbGF5X25hbWUiOiAiUmVzaWxpZW50IFN5c2FkbWluIn0sICJsYXN0
X21vZGlmaWVkX2J5IjogeyJpZCI6IDMsICJ0eXBlIjogInVzZXIiLCAibmFtZSI6ICJhQGEuY29t
IiwgImRpc3BsYXlfbmFtZSI6ICJSZXNpbGllbnQgU3lzYWRtaW4ifSwgImxhc3RfbW9kaWZpZWRf
dGltZSI6IDE1MzUzNzEwNjUyNjksICJ2aWV3X2l0ZW1zIjogW3sic3RlcF9sYWJlbCI6IG51bGws
ICJzaG93X2lmIjogbnVsbCwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjog
Il9fZnVuY3Rpb24iLCAiY29udGVudCI6ICJlOWMwMTZlOC00MWY2LTQ3OTEtYThhMi00YjY1ZWNk
MGJkOGIiLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlfSwgeyJzdGVwX2xhYmVsIjogbnVsbCwg
InNob3dfaWYiOiBudWxsLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAi
X19mdW5jdGlvbiIsICJjb250ZW50IjogIjk5M2ViMmUzLTY1ZjMtNDI0ZC05YTNhLTlhMzg5MjE4
MGY3MCIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2V9XSwgIndvcmtmbG93cyI6IFt7Indvcmtm
bG93X2lkIjogMSwgIm5hbWUiOiAiRXhhbXBsZTogUGlwbCBzZWFyY2giLCAicHJvZ3JhbW1hdGlj
X25hbWUiOiAiZXhhbXBsZV9waXBsX3NlYXJjaF9mdW5jdGlvbiIsICJvYmplY3RfdHlwZSI6ICJh
cnRpZmFjdCIsICJkZXNjcmlwdGlvbiI6IG51bGwsICJ1dWlkIjogbnVsbCwgImFjdGlvbnMiOiBb
XX1dfV19
"""
    )