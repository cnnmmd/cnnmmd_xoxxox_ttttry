import random
from xoxxox.shared import Custom, LibLog

#---------------------------------------------------------------------------

class TttPrc:

  def __init__(self, config="xoxxox/config_ttttry_cmm001", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.postxt = 0
    self.lsttxt = []
    self.conlog = {}

  def status(self, config="xoxxox/config_ttttry_cmm001", **dicprm):
    diccnf = Custom.update(config, dicprm)
    if self.lsttxt != diccnf["lsttxt"]:
      self.lsttxt = diccnf["lsttxt"]
      self.postxt = 0
    self.expert = diccnf["expert"]
    if not (self.expert in self.conlog):
      self.conlog[self.expert] = LibLog.getlog(diccnf["conlog"]) # LOG
      self.conlog[self.expert].catsys(diccnf) # LOG

  def infere(self, txtreq):
    prompt = self.conlog[self.expert].catreq(txtreq) # LOG
    print("prompt[", prompt, "]", sep="", flush=True) # DBG
    if self.postxt >= len(self.lsttxt):
      self.postxt = 0
    rawifr = self.lsttxt[self.postxt]
    print("rawifr[", rawifr, "]", sep="", flush=True) # DBG
    txtifr = rawifr
    print("txtifr[" + txtifr + "]", flush=True) # DBG
    txtres, txtopt = self.conlog[self.expert].arrres(txtifr) # LOG
    print("txtres[" + txtres + "]", flush=True) # DBG
    print("txtopt[" + txtopt + "]", flush=True) # DBG
    self.conlog[self.expert].catres(txtres) # LOG
    self.postxt = self.postxt + 1
    return (txtres, txtopt)
