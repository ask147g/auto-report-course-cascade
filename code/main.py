from send_latex import sendLatex, preSendLatex
from settings import *
from input import *

# calculations
def main():
    preSendLatex()
    setSettings()
    setInputData()
    print(rounder_value)

    product_flow_mol = product_flow/(365*24)/((7*concentraion_product+6*(1-concentraion_product))*10**(-3))
    sendLatex("product_flow_mol", round(product_flow_mol, rounder_value))

    coefficient_separation = 1 + 4755/(273+temperature)**2 - 0.803/(273+temperature)
    sendLatex("coefficient_separation", round(coefficient_separation, rounder_value))

    coefficient_enrichment = coefficient_separation - 1
    sendLatex("coefficient_enrichment", round(coefficient_enrichment, rounder_value))


if __name__ == '__main__':
    main()