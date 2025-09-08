import random
from xoxxox.shared import Custom, LibLog

#---------------------------------------------------------------------------

class TttPrc:

  def __init__(self, config="xoxxox/config_ttttry_cmm001", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.dictxt = {}
    self.postxt = {}
    self.conlog = {}

  def status(self, config="xoxxox/config_ttttry_cmm001", **dicprm):
    diccnf = Custom.update(config, dicprm)
    if self.dictxt != diccnf["dictxt"]:
      self.dictxt = diccnf["dictxt"]
      self.output = diccnf["output"]
      for keytxt in self.dictxt.keys():
        self.postxt[keytxt] = 0
        if self.output == "random":
          random.shuffle(self.dictxt[keytxt])
    self.expert = diccnf["expert"]
    if not (self.expert in self.conlog):
      self.conlog[self.expert] = LibLog.getlog(diccnf["conlog"]) # LOG
      self.conlog[self.expert].catsys(diccnf) # LOG

  def infere(self, txtreq):
    prompt = self.conlog[self.expert].catreq(txtreq) # LOG
    print("prompt[", prompt, "]", sep="", flush=True) # DBG
    keytxt = txtreq
    try:
      t = self.dictxt[keytxt]
    except:
      keytxt = next(iter(self.dictxt))
    if self.postxt[keytxt] >= len(self.dictxt[keytxt]):
      self.postxt[keytxt] = 0
      if self.output == "random":
        random.shuffle(self.dictxt[keytxt])
    rawifr = self.dictxt[keytxt][self.postxt[keytxt]]
    print("rawifr[", rawifr, "]", sep="", flush=True) # DBG
    txtifr = rawifr
    print("txtifr[" + txtifr + "]", flush=True) # DBG
    txtres, txtopt = self.conlog[self.expert].arrres(txtifr) # LOG
    print("txtres[" + txtres + "]", flush=True) # DBG
    print("txtopt[" + txtopt + "]", flush=True) # DBG
    self.conlog[self.expert].catres(txtres) # LOG
    self.postxt[keytxt] = self.postxt[keytxt] + 1
    return (txtres, txtopt)
