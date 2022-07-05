from send_latex import sendLatex

# input data
def setInputData():
    global concentraion_product
    concentraion_product = 0.995
    global concentraion_feed
    concentraion_feed = 0.925
    global concentraion_waste
    concentraion_waste = 0.9
    global temperature
    temperature = 15
    global product_flow
    product_flow = 150
    global flow_reduction_share
    flow_reduction_share = 0.5
    global number_theoretical_plates
    number_theoretical_plates = 20
    sendInputDataLatex()


# send initial data to latex
def sendInputDataLatex():
    global concentraion_product, concentraion_feed, concentraion_waste, temperature
    global product_flow, flow_reduction_share, number_theoretical_plates
    sendLatex("concentraion_product", concentraion_product)
    sendLatex("concentraion_feed", concentraion_feed)
    sendLatex("concentraion_waste", concentraion_waste)
    sendLatex("temperature", temperature)
    sendLatex("product_flow", product_flow)
    sendLatex("flow_reduction_share", flow_reduction_share)
    sendLatex("number_theoretical_plates", number_theoretical_plates)
