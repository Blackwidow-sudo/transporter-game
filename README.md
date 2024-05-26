# transporter-game

## Install

Clone the repository, then create a virtual environment and activate it:

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

After that, install the dependencies:

```
pip3 install -r requirements.txt
```

## Start game

```
python3 game
```

## Manual

The truck has the usual WASD controls, but you can also move with the arrow keys.

Move to the ore node to load some ore and then deliver it to the factory.

If you hit the configured win threshold (percentage of the amount in the ore node), you win.

If the helicopter steals too much ore from your truck, so that you cant complete the win threshold, the game is over. You will also lose when you don't have any fuel left.

You can pause the game at any time by pressing the Escape key.

In the menu you can adjust your difficulty by changing the settings.

A new game will be started when you press on the start button in the menu.