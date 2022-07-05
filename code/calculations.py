import math
from send_latex import sendLatex, sendLatexC2, setName
import settings
import input
from plot import plotGraph

def startCalculations():
    settings.setSettings()
    setName(settings.name_variables)
    input.setInputData()
    reCalculateProductFlow()
    CoefficientSeparationEnrichment()
    NumberTheoreticalPlates()
    concentrationP0()
    concentrationP()
    plotGraph()
    materialBalance()


def reCalculateProductFlow():
    global product_flow_mol
    product_flow_mol = input.product_flow/(365*24)/((7*input.concentraion_product+6*(1-input.concentraion_product))*10**(-3))
    sendLatex("product_flow_mol", round(product_flow_mol, settings.rounder_value))


def CoefficientSeparationEnrichment():
    global coefficient_separation, coefficient_enrichment
    coefficient_separation = 1 + 4755/(273+input.temperature)**2 - 0.803/(273+input.temperature)
    sendLatex("coefficient_separation", round(coefficient_separation, settings.rounder_value))
    
    coefficient_enrichment = coefficient_separation - 1
    sendLatex("coefficient_enrichment", round(coefficient_enrichment, settings.rounder_value))


def NumberTheoreticalPlates():
    global number_theoretical_plates, number_column
    global number_theoretical_plates_enrichment, number_theoretical_plates_depleted
    number_theoretical_plates_enrichment = 1/coefficient_enrichment*math.log(input.concentraion_product*(1 - input.concentraion_feed)/(input.concentraion_feed*(1 - input.concentraion_product)))
    number_theoretical_plates_enrichment = math.ceil(number_theoretical_plates_enrichment)
    sendLatex("number_theoretical_plates_enrichment", number_theoretical_plates_enrichment)

    number_theoretical_plates_depleted = 1/coefficient_enrichment*math.log(input.concentraion_feed*(1 - input.concentraion_waste)/(input.concentraion_waste*(1 - input.concentraion_feed)))
    number_theoretical_plates_depleted = math.ceil(number_theoretical_plates_depleted)
    sendLatex("number_theoretical_plates_depleted", number_theoretical_plates_depleted)

    number_theoretical_plates = 2 * (number_theoretical_plates_enrichment + number_theoretical_plates_depleted)
    sendLatex("all_number_theoretical_plates", number_theoretical_plates)

    number_column = number_theoretical_plates / input.number_theoretical_plates
    number_column = math.ceil(number_column)
    sendLatex("number_column", number_column)


def concentrationP0():
    setName(settings.name_concentration_P0)
    global concentration_P0
    concentration_P0 = []
    for i in range(number_column+1):
        concentration_P0.append(input.concentraion_waste/(1 - input.concentraion_waste) * math.e**(coefficient_enrichment*input.number_theoretical_plates*i))
        concentration_P0[i] = (concentration_P0[i]/(1 + input.concentraion_waste/(1 - input.concentraion_waste) * math.e**(coefficient_enrichment*input.number_theoretical_plates*i)))
        sendLatex(str(i), round(concentration_P0[i], settings.rounder_value))
    setName(settings.name_variables)
    sendLatex("concentration_product_P0", round(concentration_P0[number_column], settings.rounder_value))


def concentrationP():
    global concentration_P, initial_flow, coefficient_cascade, mean_flow
    global coefficient_x1, coefficient_x2
    concentration_P = [0] * (number_column+1)
    mean_flow = [0] * (number_column+1)
    coefficient_x1 = [0] * (number_column+1)
    coefficient_x2 = [0] * (number_column+1)
    coefficient_cascade = 0
    while True:
        initial_flow = 2 * product_flow_mol * (input.concentraion_product - input.concentraion_feed) / (coefficient_enrichment * input.concentraion_feed * (1 - input.concentraion_feed))
        initial_flow = initial_flow * (1 - coefficient_cascade * settings.step_flow)
        for i in range((number_column+1)):
            mean_flow[i] = 1/2 * initial_flow * (1 - input.flow_reduction_share/100)**(input.number_theoretical_plates*(i+1)) * (1 + (1 - input.flow_reduction_share/100)**(-input.number_theoretical_plates))
            coefficient_x1[i] = 1/2*(1+product_flow_mol/(mean_flow[i]*coefficient_enrichment)) + math.sqrt(1/4*(1+product_flow_mol/(mean_flow[i]*coefficient_enrichment))**2 - product_flow_mol/(mean_flow[i]*coefficient_enrichment)*input.concentraion_product)
            coefficient_x2[i] = 1/2*(1+product_flow_mol/(mean_flow[i]*coefficient_enrichment)) - math.sqrt(1/4*(1+product_flow_mol/(mean_flow[i]*coefficient_enrichment))**2 - product_flow_mol/(mean_flow[i]*coefficient_enrichment)*input.concentraion_product)
            concentration_P[i] = (coefficient_x1[i] + (coefficient_x1[i] - input.concentraion_product)/(input.concentraion_product - coefficient_x2[i])*math.e**(input.number_theoretical_plates*(number_column-i)*coefficient_enrichment*(coefficient_x1[i]-coefficient_x2[i]))*coefficient_x2[i])
            concentration_P[i] = concentration_P[i] / (1 + (coefficient_x1[i] - input.concentraion_product)/(input.concentraion_product - coefficient_x2[i])*math.e**(input.number_theoretical_plates*(number_column-i)*coefficient_enrichment*(coefficient_x1[i]-coefficient_x2[i])))
        if ((abs(concentration_P[0] - input.concentraion_waste) < settings.accuracy_c2) and (concentration_P[0] > input.concentraion_waste)):
            sendLatex("initial_flow", round(initial_flow, settings.rounder_value))
            sendLatex("coefficient_cascade", 2*round(1 - coefficient_cascade * settings.step_flow, settings.rounder_value))
            for i in range(number_column+1):
                concentrationPSendLatex(i)
            break
        coefficient_cascade = coefficient_cascade + 1


def concentrationPSendLatex(i:int):
    setName(settings.name_mean_flow)
    sendLatex(str(i), round(mean_flow[i], settings.rounder_value))
    setName(settings.name_concentration_P)
    sendLatexC2(i, round(coefficient_x1[i], settings.rounder_value), round(coefficient_x2[i], settings.rounder_value), round(concentration_P[i], settings.rounder_value))


def materialBalance():
    setName(settings.name_variables)
    global result_waste, result_feed
    result_waste = product_flow_mol*(concentration_P[number_column]-input.concentraion_feed)/(input.concentraion_feed - concentration_P[0])
    result_feed = product_flow_mol + result_waste
    sendLatex("result_waste", round(result_waste, settings.rounder_value))
    sendLatex("result_feed", round(result_feed, settings.rounder_value))
    sendLatex("result_concentartion_product", round(concentration_P[number_column], settings.rounder_value))
    sendLatex("result_concentartion_waste", round(concentration_P[0], settings.rounder_value))
