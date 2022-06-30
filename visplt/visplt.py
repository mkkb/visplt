from vispy import scene, app
import sys
import numpy as np

figures = []
views = []
axes = []
lines = []
current_fig = 0
current_ax = 0

def figure(*args, **kwargs):
    global figures, axes, views, current_fig, current_ax

    title = ''
    if len(args) > 0:
        title = args[0]

    canvas = scene.SceneCanvas(keys='interactive', size=(600, 600), show=True)
    grid = canvas.central_widget.add_grid(margin=10)
    grid.spacing = 0

    title = scene.Label(title, color='white')
    title.height_max = 40
    grid.add_widget(title, row=0, col=0, col_span=2)

    view = grid.add_view(row=1, col=1, border_color='white')
    view.camera = 'panzoom'

    yaxis = scene.AxisWidget(orientation='left',
                             axis_label=' || ',
                             axis_font_size=18,
                             axis_label_margin=50,
                             tick_label_margin=5)
    yaxis.width_max = 80
    grid.add_widget(yaxis, row=1, col=0)

    xaxis = scene.AxisWidget(orientation='bottom',
                             axis_label=' -- ',
                             axis_font_size=18,
                             axis_label_margin=50,
                             tick_label_margin=5)

    xaxis.height_max = 80
    grid.add_widget(xaxis, row=2, col=1)

    right_padding = grid.add_widget(row=1, col=2, row_span=1)
    right_padding.width_max = 50

    scene.GridLines(color='white', parent=view.scene)

    xaxis.link_view(view)
    yaxis.link_view(view)

    figures.append(axes)
    axes.append((xaxis, yaxis))
    views.append(view)


def plot(*args, **kwargs):
    global figures, axes, views, current_fig, current_ax, lines
    x = np.zeros(1)
    y = np.zeros(1)
    if len(axes) > 0:
        view = views[current_ax]
        if len(args) == 2:
            x = args[0]
            y = args[1]
        elif len(args) == 1:
            y = args[0]
            x = np.arange(y.size)

        data = np.array([x, y]).transpose()
        color = np.ones(shape=(y.size, 4))
        line = scene.Line(data, color=color, parent=view.scene)
        lines.append(line)

        view.camera.set_range()

    if 'label' in kwargs.keys():
        print(" plot ->  adding legend: ", kwargs['label'])

def xlabel(lable):
    global axes, current_ax
    x_axis, y_axis = axes[current_ax]
    print(dir(x_axis))
    x_axis.axis.axis_label = lable

def ylabel(lable):
    global axes, current_ax
    x_axis, y_axis = axes[current_ax]
    y_axis.axis.axis_label = lable

def subplots():
    pass

def show():
    if sys.flags.interactive == 0:
        app.run()