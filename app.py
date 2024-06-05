from app import App
from app_components import clear_background
from tildagonos import tildagonos
from . import logo as logo

class NottingHackApp(App):

  def __init__(self):
    tildagonos.init_display()

  def update(self, delta):
    pass

  def draw(self, ctx):
    clear_background(ctx)
    tildagonos.tft.bitmap(logo, 0, 0)

__app_export__ = NottingHackApp
