from app import App
from app_components import clear_background
from tildagonos import tildagonos
from . import logo as logo

class NottingHackApp(App):

  def __init__(self):
    pass

  def update(self, delta):
    pass

  def draw(self, ctx):
    clear_background(ctx)
    tildagonos.tft.bitmap(logo, 0, 0)
    ctx.move_to(0, 0).gray(1).text("Hello, world!")

__app_export__ = NottingHackApp
