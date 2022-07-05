from math import ceil
from matplotlib import pyplot as plt
import calculations
import settings

def plotGraph():
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams.update({'font.size': 14})

    plotConcentrationChange()
    plotCascade()


def plotConcentrationChange():
    plt.figure(figsize=(7, 5))
    fig1 = plt.plot(range(calculations.number_column+1), calculations.concentration_P0, 'rs--', label='$c_{1}$')
    fig2 = plt.plot(range(calculations.number_column+1), calculations.concentration_P, 'ko-', label='$c_{2}$')
    plt.ylim(calculations.concentration_P0[0], 1)
    plt.xlim(0, calculations.number_column)
    plt.title("Изменение концентрации") 
    plt.xlabel('$\it{N}$, колонна')
    plt.ylabel('$\it{c}$')
    plt.grid(True)
    plt.legend()
    plt.savefig("latex/figures/concentration_change.png")


def plotCascade():
    settings.cascadeSettings()
    settings.flowReversalNodeSetting()
    settings.setLineSettings()
    settings.arrowSettings()
    settings.flowSettings()

    fig,ax = plt.subplots(1)
    plt.axis('off')
    for i in range(calculations.number_column):
        drawColumn(ax, i)
        if (i < calculations.number_column-1):
            drawAmalgam(ax, i)
            drawAlkali(ax, i)
    drawFlowReversalNodes(ax)
    drawWaste(ax)
    drawProduct(ax)
    drawFeed(ax)

    plt.xlim(-(settings.width_cascade+settings.distance_cascade), (calculations.number_column+1)*(settings.width_cascade+settings.distance_cascade))
    plt.ylim(-2*settings.height_cascade, 2*settings.height_cascade)
    plt.savefig("latex/figures/cascade.png")


def drawColumn(ax:plt.Axes, i:int):
    # left line of column
    ax.vlines(i*(settings.width_cascade+settings.distance_cascade), -settings.height_cascade/2, settings.height_cascade/2,
        color = settings.color_line_cascade,
        linewidth = settings.width_line_cascade,
        linestyle = settings.type_line_cascade)

    # right line of column
    ax.vlines(settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), -settings.height_cascade/2, settings.height_cascade/2,
        color = settings.color_line_cascade,
        linewidth = settings.width_line_cascade,
        linestyle = settings.type_line_cascade)

    # top line of cascade
    ax.hlines(settings.height_cascade/2, i*(settings.distance_cascade+settings.width_cascade), settings.width_cascade+i*(settings.distance_cascade+settings.width_cascade),
        color = settings.color_line_cascade,
        linewidth = settings.width_line_cascade,
        linestyle = settings.type_line_cascade)

    # bottom line of cascade
    ax.hlines(-settings.height_cascade/2, i*(settings.distance_cascade+settings.width_cascade), settings.width_cascade+i*(settings.distance_cascade+settings.width_cascade),
        color = settings.color_line_cascade,
        linewidth = settings.width_line_cascade,
        linestyle = settings.type_line_cascade)

    ax.text(settings.width_cascade/2+i*(settings.distance_cascade+settings.width_cascade), 0, str(i+1))


def drawFlowReversalNodes(ax:plt.Axes):
    # amalgam
    # flow reversal node 1
    drawArrow(ax, settings.amalgam_input_coeff*settings.width_cascade, -settings.height_cascade*settings.placement_flow_reversal_node+settings.height_flow_reversal_node, -1)
    ax.vlines(settings.amalgam_input_coeff*settings.width_cascade, 
        -settings.height_cascade/2, 
        -settings.height_cascade*settings.placement_flow_reversal_node+settings.height_flow_reversal_node,
        color = settings.color_line_amalgam,
        linewidth = settings.width_line_amalgam,
        linestyle = settings.type_line_amalgam)

    # flow reversal node 2
    drawArrow(ax, settings.amalgam_input_coeff*settings.width_cascade+(calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade/2, -1)
    ax.vlines(settings.amalgam_input_coeff*settings.width_cascade+(calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade/2, 
        settings.height_cascade*settings.placement_flow_reversal_node-settings.height_flow_reversal_node,
        color = settings.color_line_amalgam,
        linewidth = settings.width_line_amalgam,
        linestyle = settings.type_line_amalgam)

    # alkali
    # flow reversal node 1
    drawArrow(ax, settings.alkali_input_coeff*settings.width_cascade, -settings.height_cascade/2, 1)
    ax.vlines(settings.alkali_input_coeff*settings.width_cascade, 
        -settings.height_cascade/2, 
        -settings.height_cascade*settings.placement_flow_reversal_node+settings.height_flow_reversal_node,
        color = settings.color_line_alkali,
        linewidth = settings.width_line_alkali,
        linestyle = settings.type_line_alkali)

    # flow reversal node 2
    drawArrow(ax, settings.alkali_input_coeff*settings.width_cascade+(calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade*settings.placement_flow_reversal_node-settings.height_flow_reversal_node, 1)
    ax.vlines(settings.alkali_input_coeff*settings.width_cascade+(calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade/2, 
        settings.height_cascade*settings.placement_flow_reversal_node-settings.height_flow_reversal_node,
        color = settings.color_line_alkali,
        linewidth = settings.width_line_alkali,
        linestyle = settings.type_line_alkali)

    # flow reversal node 1
    drawFlowReversalNode(ax, 1, -1)
    ax.text(0, 
        -(settings.height_cascade*settings.placement_flow_reversal_node-0.5*settings.height_flow_reversal_node),
        "УОП 1")

    # flow reversal node 2
    drawFlowReversalNode(ax, calculations.number_column, 1)
    ax.text((calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade), 
        (settings.height_cascade*settings.placement_flow_reversal_node-0.5*settings.height_flow_reversal_node),
        "УОП 2")


def drawFlowReversalNode(ax:plt.Axes, id:int, placement:int):
    # left line
    ax.vlines((id-1)*(settings.width_cascade+settings.distance_cascade), 
        placement*settings.height_cascade*settings.placement_flow_reversal_node, 
        placement*(settings.height_cascade*settings.placement_flow_reversal_node-settings.height_flow_reversal_node),
        color = settings.color_line_cascade,
        linewidth = settings.width_line_cascade,
        linestyle = settings.type_line_cascade)

    # right line
    ax.vlines(settings.width_cascade+(id-1)*(settings.width_cascade+settings.distance_cascade), 
        placement*settings.height_cascade*settings.placement_flow_reversal_node, 
        placement*(settings.height_cascade*settings.placement_flow_reversal_node-settings.height_flow_reversal_node),
        color = settings.color_line_cascade,
        linewidth = settings.width_line_cascade,
        linestyle = settings.type_line_cascade)

    # top line
    ax.hlines(placement*settings.height_cascade*settings.placement_flow_reversal_node, 
        (id-1)*(settings.width_cascade+settings.distance_cascade), 
        settings.width_cascade+(id-1)*(settings.width_cascade+settings.distance_cascade),
        color = settings.color_line_flow_reversal_node,
        linewidth = settings.width_line_flow_reversal_node,
        linestyle = settings.type_line_flow_reversal_node)

    # bottom line
    ax.hlines(placement*(settings.height_cascade*settings.placement_flow_reversal_node-settings.height_flow_reversal_node), 
        (id-1)*(settings.width_cascade+settings.distance_cascade), 
        settings.width_cascade+(id-1)*(settings.width_cascade+settings.distance_cascade),
        color = settings.color_line_flow_reversal_node,
        linewidth = settings.width_line_flow_reversal_node,
        linestyle = settings.type_line_flow_reversal_node)


def drawAmalgam(ax:plt.Axes, i:int):
    drawArrow(ax, settings.amalgam_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade/2, -1)
    ax.vlines(settings.amalgam_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade/2, 
        settings.height_cascade/2+settings.amalgam_first_line,
        color = settings.color_line_amalgam,
        linewidth = settings.width_line_amalgam,
        linestyle = settings.type_line_amalgam)

    ax.hlines(settings.height_cascade/2+settings.amalgam_first_line, 
        settings.amalgam_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.amalgam_second_line+settings.amalgam_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade),
        color = settings.color_line_amalgam,
        linewidth = settings.width_line_amalgam,
        linestyle = settings.type_line_amalgam)

    ax.vlines(settings.amalgam_second_line+settings.amalgam_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade/2+settings.amalgam_first_line, 
        -settings.height_cascade/2-settings.amalgam_fouth_line,
        color = settings.color_line_amalgam,
        linewidth = settings.width_line_amalgam,
        linestyle = settings.type_line_amalgam)

    ax.hlines(-settings.height_cascade/2-settings.amalgam_fouth_line, 
        settings.amalgam_second_line+settings.amalgam_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.amalgam_fifth_line+settings.amalgam_second_line+settings.amalgam_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade),
        color = settings.color_line_amalgam,
        linewidth = settings.width_line_amalgam,
        linestyle = settings.type_line_amalgam)

    ax.vlines(settings.amalgam_fifth_line+settings.amalgam_second_line+settings.amalgam_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        -settings.height_cascade/2-settings.amalgam_fouth_line, 
        -settings.height_cascade/2,
        color = settings.color_line_amalgam,
        linewidth = settings.width_line_amalgam,
        linestyle = settings.type_line_amalgam)


def drawAlkali(ax:plt.Axes, i:int):
    drawArrow(ax, settings.alkali_input_coeff*settings.width_cascade+(i+1)*(settings.width_cascade+settings.distance_cascade), 
        -settings.height_cascade/2, 1)
    ax.vlines(settings.alkali_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade/2, 
        settings.height_cascade/2+settings.alkali_first_line,
        color = settings.color_line_alkali,
        linewidth = settings.width_line_alkali,
        linestyle = settings.type_line_alkali)

    ax.hlines(settings.height_cascade/2+settings.alkali_first_line, 
        settings.alkali_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.alkali_second_line+settings.alkali_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade),
        color = settings.color_line_alkali,
        linewidth = settings.width_line_alkali,
        linestyle = settings.type_line_alkali)

    ax.vlines(settings.alkali_second_line+settings.alkali_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.height_cascade/2+settings.alkali_first_line, 
        -settings.height_cascade/2-settings.alkali_fouth_line,
        color = settings.color_line_alkali,
        linewidth = settings.width_line_alkali,
        linestyle = settings.type_line_alkali)

    ax.hlines(-settings.height_cascade/2-settings.alkali_fouth_line, 
        settings.alkali_second_line+settings.alkali_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        settings.alkali_fifth_line+settings.alkali_second_line+settings.alkali_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade),
        color = settings.color_line_alkali,
        linewidth = settings.width_line_alkali,
        linestyle = settings.type_line_alkali)

    ax.vlines(settings.alkali_fifth_line+settings.alkali_second_line+settings.alkali_input_coeff*settings.width_cascade+i*(settings.width_cascade+settings.distance_cascade), 
        -settings.height_cascade/2-settings.alkali_fouth_line, 
        -settings.height_cascade/2,
        color = settings.color_line_alkali,
        linewidth = settings.width_line_alkali,
        linestyle = settings.type_line_alkali)

def drawArrow(ax:plt.Axes, x:float, y:float, placement:int):
    import math
    ax.plot([x, x-placement*settings.size_arrow*math.sin(settings.angle_arrow*math.pi/180)], [y, y-placement*settings.size_arrow*math.cos(settings.angle_arrow*math.pi/180)],
        color = settings.color_line_arrow,
        linewidth = settings.width_line_arrow,
        linestyle = settings.type_line_arrow)

    ax.plot([x, x+placement*settings.size_arrow*math.sin(settings.angle_arrow*math.pi/180)], [y, y-placement*settings.size_arrow*math.cos(settings.angle_arrow*math.pi/180)],
        color = settings.color_line_arrow,
        linewidth = settings.width_line_arrow,
        linestyle = settings.type_line_arrow)


def drawWaste(ax:plt.Axes):
    ax.hlines(-(settings.height_cascade*settings.placement_flow_reversal_node-1/2*settings.height_flow_reversal_node),
        0, 
        -settings.size_flow, 
        color = settings.color_line_flow,
        linewidth = settings.width_line_flow,
        linestyle = settings.type_line_flow)

    drawArrowFlows(ax, -settings.size_flow, -(settings.height_cascade*settings.placement_flow_reversal_node-1/2*settings.height_flow_reversal_node), 1)
    ax.text(-0.5*settings.size_flow-(settings.height_cascade*settings.placement_flow_reversal_node-1/2*settings.height_flow_reversal_node), 
        -(settings.height_cascade*settings.placement_flow_reversal_node-0.5*settings.height_flow_reversal_node),
        "$W, c_{W}$")


def drawProduct(ax:plt.Axes):
    ax.hlines((settings.height_cascade*settings.placement_flow_reversal_node-1/2*settings.height_flow_reversal_node),
        settings.width_cascade+(calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade), 
        settings.width_cascade+(calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade)+settings.size_flow, 
        color = settings.color_line_flow,
        linewidth = settings.width_line_flow,
        linestyle = settings.type_line_flow)

    drawArrowFlows(ax, settings.width_cascade+(calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade)+settings.size_flow, (settings.height_cascade*settings.placement_flow_reversal_node-1/2*settings.height_flow_reversal_node), -1)
    ax.text(0.5*settings.size_flow+settings.width_cascade+(calculations.number_column-1)*(settings.width_cascade+settings.distance_cascade), 
        (settings.height_cascade*settings.placement_flow_reversal_node-0.5*settings.height_flow_reversal_node),
        "$P, c_{P}$")


def drawFeed(ax:plt.Axes):
    import input
    column_feed = 0
    plate_feed = 0
    for i in range(calculations.number_column-1):
        if ((input.concentraion_feed > calculations.concentration_P[i]) and ((input.concentraion_feed <= calculations.concentration_P[i+1]))):
            column_feed = i
            plate_feed = input.number_theoretical_plates -input.number_theoretical_plates/(calculations.concentration_P[i]-calculations.concentration_P[i+1]) * (input.concentraion_feed - calculations.concentration_P[i+1])

            ax.hlines(settings.height_cascade/2*plate_feed/input.number_theoretical_plates,
                column_feed*(settings.width_cascade+settings.distance_cascade), 
                column_feed*(settings.width_cascade+settings.distance_cascade)-settings.size_flow, 
                color = settings.color_line_flow,
                linewidth = settings.width_line_flow,
                linestyle = settings.type_line_flow)

            drawArrowFlows(ax, column_feed*(settings.width_cascade+settings.distance_cascade), 
                settings.height_cascade/2*plate_feed/input.number_theoretical_plates, -1)

            ax.text(-settings.size_flow+column_feed*(settings.width_cascade+settings.distance_cascade), 
                settings.height_cascade/2*plate_feed/input.number_theoretical_plates,
                "$F, c_{F}$")

            break


def drawArrowFlows(ax:plt.Axes, x:float, y:float, placement:int):
    import math
    ax.plot([x, x+placement*settings.size_arrow*math.cos(settings.angle_arrow*math.pi/180)], [y, y+placement*settings.size_arrow*math.sin(settings.angle_arrow*math.pi/180)],
        color = settings.color_line_arrow,
        linewidth = settings.width_line_arrow,
        linestyle = settings.type_line_arrow)

    ax.plot([x, x+placement*settings.size_arrow*math.cos(settings.angle_arrow*math.pi/180)], [y, y-placement*settings.size_arrow*math.sin(settings.angle_arrow*math.pi/180)],
        color = settings.color_line_arrow,
        linewidth = settings.width_line_arrow,
        linestyle = settings.type_line_arrow)
