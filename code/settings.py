from send_latex import preSendLatex, preSendLatexC2

# settings
def setSettings():
    setOutputName()
    setLatex()
    global rounder_value, step_flow, accuracy_c2
    rounder_value = 5
    step_flow = 0.0001
    accuracy_c2 = 0.0001


def setOutputName():
    global name_variables, name_concentration_P0
    global name_mean_flow, name_concentration_P
    name_variables = "output/variables.csv"
    name_concentration_P0 = "output/concentration_P0.csv"
    name_mean_flow = "output/flow.csv"
    name_concentration_P = "output/concentration_P.csv"


def setLatex():
    preSendLatex(name_variables)
    preSendLatex(name_concentration_P0)
    preSendLatex(name_mean_flow)
    preSendLatexC2(name_concentration_P)


def cascadeSettings():
    cascadeLineSettings()
    global height_cascade, width_cascade, distance_cascade
    height_cascade = 3
    width_cascade = 5
    distance_cascade = 2


def cascadeLineSettings():
    global width_line_cascade, color_line_cascade, type_line_cascade
    width_line_cascade = 1
    color_line_cascade = 'k'
    type_line_cascade = '-'


def flowReversalNodeSetting():
    flowReversalNodeLineSettings()
    global height_flow_reversal_node, width_flow_reversal_node
    global placement_flow_reversal_node
    height_flow_reversal_node = 1
    width_flow_reversal_node = width_cascade
    placement_flow_reversal_node = 1.5


def flowReversalNodeLineSettings():
    global width_line_flow_reversal_node, color_line_flow_reversal_node, type_line_flow_reversal_node
    width_line_flow_reversal_node = 1
    color_line_flow_reversal_node = 'k'
    type_line_flow_reversal_node = '-'

def setLineSettings():
    alkaliSettings()
    alkaliLineSettings()
    amalgamSettings()
    amalgamLineSettings()

def alkaliSettings():
    global alkali_input_coeff
    global alkali_first_line, alkali_second_line, alkali_fouth_line, alkali_fifth_line
    alkali_input_coeff = 3/4
    alkali_first_line = 1
    alkali_second_line = distance_cascade
    alkali_fouth_line = 1.5
    alkali_fifth_line = width_cascade

def alkaliLineSettings():
    global width_line_alkali, color_line_alkali, type_line_alkali
    width_line_alkali = 1
    color_line_alkali = 'k'
    type_line_alkali = '-'


def amalgamSettings():
    global amalgam_input_coeff
    global amalgam_first_line, amalgam_second_line, amalgam_fouth_line, amalgam_fifth_line
    amalgam_input_coeff = 1/4
    amalgam_first_line = 1.5
    amalgam_second_line = width_cascade
    amalgam_fouth_line = 1
    amalgam_fifth_line = distance_cascade


def amalgamLineSettings():
    global width_line_amalgam, color_line_amalgam, type_line_amalgam
    width_line_amalgam = 1
    color_line_amalgam = 'k'
    type_line_amalgam = '--'


def arrowSettings():
    arrowLineSetting()
    global size_arrow, angle_arrow
    size_arrow = 1/3
    angle_arrow = 25

def arrowLineSetting():
    global width_line_arrow, color_line_arrow, type_line_arrow
    width_line_arrow = 1
    color_line_arrow = 'k'
    type_line_arrow = '-'


def flowSettings():
    flowLineSettings()
    global size_flow
    size_flow = 5


def flowLineSettings():
    global width_line_flow, color_line_flow, type_line_flow
    width_line_flow = 1
    color_line_flow = 'k'
    type_line_flow = '-'