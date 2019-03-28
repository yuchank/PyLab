import os
import time
import threading

import cuckoo

from cuckoo.core.plugins import RunAuxiliary

class AnalysisManager(threading.Thread):

  def launch_analysis(self):
    self.aux = RunAuxiliary()
    self.aux.start()

    machinery.start()

  def run(self):
    self.launch_analysis()


class Scheduler(object):

  def __init__(self, maxcount=None):
    self.running = True

  def initialize(self):
    global machinery
    machinery_name = self.cfg.cuckoo.machinery
    machinery = cuckoo.machinery.plugins[machinery_name]()

  def start(self):
    self.initialize()

    while self.running:
      analysis = AnalysisManager()
