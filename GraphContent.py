"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
import MainNode.MainNode_Data
from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all our Industry's
from IndustryNodes import Aerospace_Data, AutomotiveIndustry_Data, CloudComputing_Data, Consulting_Data, \
    ConsumerGoods_Data, Cybersecurity_Data, Energy_Data, FinancialServices_Data, InformationTechnology_Data, \
    Insurance_Data, MechanicalEngineering_Data, MediaAndEntertainment_Data, PharmaceuticalsAndHealth_Data

# import all Company's
from CompanyNodes import Action_Data, AldiNord_Data, Audi_Data, Axa_Data, Bmw_Data, Boeing_Data, Coseon_Data, \
    ElectronicArts_Data, ESLGaming_Data, Google_Data, Hdi_Data, Innovas_Data, Lidl_Data, MercedesBenz_Data, \
    Microsoft_Data, Nestle_Data, Netcologne_Data, Netflix_Data, NextKraftwerke_Data, Obi_Data, Otto_Data, ParcIT_Data, \
    PferdWerkzeuge_Data, Porsche_Data, ReweDigital_Data, RhenagRheinischeEnergie_Data, RiotGames_Data, SAP_Data, \
    SchneiderElectric_Data, Secunet_Data, SollersConsulting_Data, SpaceX_Data, Tesla_Data, Volkswagen_Data, Zeiss_Data

from MainNode import  MainNode_Data

class GraphContent:

    def __init__(self, graph: Graph):
        self.main_node = None
        self.aerospace = None
        self.automotive_industry = None
        self.cloud_computing = None
        self.consulting = None
        self.consumerGoods = None
        self.cybersecurity = None
        self.energy = None
        self.financial_services = None
        self.information_technology = None
        self.insurance = None
        self.mechanical_engineering = None
        self.media_and_entertainment = None
        self.pharmaceuticalsAndHealth = None

        self.create_main_node(graph)
        self.create_industry_nodes(graph, self.main_node)
        self.create_company_nodes(graph)
        self.connect_industry_with_node(graph)

    def create_main_node(self, graph: Graph):
        main_note = Node(MainNode_Data.CONTENT, MainNode.MainNode_Data.TITEL, MainNode_Data.IMAGE_NAME, radius=10, color=[153, 51, 255])
        graph.add_new_node_to_graph(main_note)
        self.main_node = main_note

    def create_industry_nodes(self, graph: Graph, main_node: Node):
        bright_violet = [204, 51, 255]

        node_aerospace = Node(Aerospace_Data.CONTENT, Aerospace_Data.TITEL, Aerospace_Data.IMAGE_NAME, radius=8,
                              color=bright_violet)

        node_automotive_industry = Node(AutomotiveIndustry_Data.CONTENT, AutomotiveIndustry_Data.TITEL,
                                        AutomotiveIndustry_Data.IMAGE_NAME, radius=8, color=bright_violet)

        node_cloud_computing = Node(CloudComputing_Data.CONTENT, CloudComputing_Data.TITEL,
                                    CloudComputing_Data.IMAGE_NAME, radius=8, color=bright_violet)

        node_consulting = Node(Consulting_Data.CONTENT, Consulting_Data.TITEL, Consulting_Data.IMAGE_NAME, radius=8,
                               color=bright_violet)

        node_consumer_goods = Node(ConsumerGoods_Data.CONTENT, ConsumerGoods_Data.TITEL, ConsumerGoods_Data.IMAGE_NAME,
                                   radius=8, color=bright_violet)

        node_cybersecurity = Node(Cybersecurity_Data.CONTENT, Cybersecurity_Data.TITEL, Cybersecurity_Data.IMAGE_NAME,
                                  radius=8, color=bright_violet)

        node_energy = Node(Energy_Data.CONTENT, Energy_Data.TITEL, Energy_Data.IMAGE_NAME, radius=8,
                           color=bright_violet)

        node_financial_services = Node(FinancialServices_Data.CONTENT, FinancialServices_Data.TITEL,
                                       FinancialServices_Data.IMAGE_NAME, radius=8, color=bright_violet)

        node_information_technology = Node(InformationTechnology_Data.CONTENT, InformationTechnology_Data.TITEL,
                                           InformationTechnology_Data.IMAGE_NAME, radius=8, color=bright_violet)

        node_insurance = Node(Insurance_Data.CONTENT, Insurance_Data.TITEL, Insurance_Data.IMAGE_NAME, radius=8,
                              color=bright_violet)

        node_mechanical_engineering = Node(MechanicalEngineering_Data.CONTENT, MechanicalEngineering_Data.TITEL,
                                           MechanicalEngineering_Data.IMAGE_NAME, radius=8, color=bright_violet)

        node_media_and_entertainment = Node(MediaAndEntertainment_Data.CONTENT, MediaAndEntertainment_Data.TITEL,
                                            MediaAndEntertainment_Data.IMAGE_NAME, radius=8, color=bright_violet)

        node_pharmaceuticals_and_health = Node(PharmaceuticalsAndHealth_Data.CONTENT,
                                               PharmaceuticalsAndHealth_Data.TITEL,
                                               PharmaceuticalsAndHealth_Data.IMAGE_NAME, radius=8, color=bright_violet)

        self.aerospace = node_aerospace
        self.automotive_industry = node_automotive_industry
        self.cloud_computing = node_cloud_computing
        self.consulting = node_consulting
        self.consumerGoods = node_consumer_goods
        self.cybersecurity = node_cybersecurity
        self.energy = node_energy
        self.financial_services = node_financial_services
        self.information_technology = node_information_technology
        self.insurance = node_insurance
        self.mechanical_engineering = node_mechanical_engineering
        self.media_and_entertainment = node_media_and_entertainment
        self.pharmaceuticalsAndHealth = node_pharmaceuticals_and_health

        main_node.connect(node_aerospace)
        main_node.connect(node_automotive_industry)
        main_node.connect(node_cloud_computing)
        main_node.connect(node_consulting)
        main_node.connect(node_consumer_goods)
        main_node.connect(node_cybersecurity)
        main_node.connect(node_energy)
        main_node.connect(node_financial_services)
        main_node.connect(node_information_technology)
        main_node.connect(node_insurance)
        main_node.connect(node_mechanical_engineering)
        main_node.connect(node_media_and_entertainment)
        main_node.connect(node_pharmaceuticals_and_health)

        graph.add_new_node_to_graph(node_aerospace)
        graph.add_new_node_to_graph(node_automotive_industry)
        graph.add_new_node_to_graph(node_cloud_computing)
        graph.add_new_node_to_graph(node_consulting)
        graph.add_new_node_to_graph(node_consumer_goods)
        graph.add_new_node_to_graph(node_cybersecurity)
        graph.add_new_node_to_graph(node_energy)
        graph.add_new_node_to_graph(node_financial_services)
        graph.add_new_node_to_graph(node_information_technology)
        graph.add_new_node_to_graph(node_insurance)
        graph.add_new_node_to_graph(node_mechanical_engineering)
        graph.add_new_node_to_graph(node_media_and_entertainment)
        graph.add_new_node_to_graph(node_pharmaceuticals_and_health)

    def create_company_nodes(self, graph):

        # all company nodes here:
        node_action = Node(Action_Data.CONTENT, Action_Data.TITEL, Action_Data.IMAGE_NAME,
                           industry=[self.consumerGoods])
        node_aldinord = Node(AldiNord_Data.CONTENT, AldiNord_Data.TITEL, AldiNord_Data.IMAGE_NAME,
                             industry=[self.consumerGoods])
        node_audi = Node(Audi_Data.CONTENT, Audi_Data.TITEL, Audi_Data.IMAGE_NAME, industry=[self.automotive_industry])
        node_axa = Node(Axa_Data.CONTENT, Axa_Data.TITEL, Axa_Data.IMAGE_NAME, industry=[self.insurance])
        node_bmw = Node(Bmw_Data.CONTENT, Bmw_Data.TITEL, Bmw_Data.IMAGE_NAME, industry=[self.automotive_industry])
        node_boeing = Node(Boeing_Data.CONTENT, Boeing_Data.TITEL, Boeing_Data.IMAGE_NAME, industry=[self.aerospace])
        node_coseon = Node(Coseon_Data.CONTENT, Coseon_Data.TITEL, Coseon_Data.IMAGE_NAME,
                           industry=[self.information_technology])
        node_electronic_arts = Node(ElectronicArts_Data.CONTENT, ElectronicArts_Data.TITEL,
                                    ElectronicArts_Data.IMAGE_NAME,
                                    industry=[self.information_technology, self.media_and_entertainment])
        node_esl_gaming = Node(ESLGaming_Data.CONTENT, ESLGaming_Data.TITEL, ESLGaming_Data.IMAGE_NAME,
                               industry=[self.media_and_entertainment])
        node_google = Node(Google_Data.CONTENT, Google_Data.TITEL, Google_Data.IMAGE_NAME,
                           industry=[self.information_technology, self.cloud_computing, self.cybersecurity])
        node_hdi = Node(Hdi_Data.CONTENT, Hdi_Data.TITEL, Hdi_Data.IMAGE_NAME, industry=[self.insurance])
        node_innnovas = Node(Innovas_Data.CONTENT, Innovas_Data.TITEL, Innovas_Data.IMAGE_NAME,
                             industry=[self.information_technology, self.pharmaceuticalsAndHealth])
        node_lidl = Node(Lidl_Data.CONTENT, Lidl_Data.TITEL, Lidl_Data.IMAGE_NAME, industry=[self.consumerGoods])
        node_mercedes_benz = Node(MercedesBenz_Data.CONTENT, MercedesBenz_Data.TITEL, MercedesBenz_Data.IMAGE_NAME,
                                  industry=[self.automotive_industry])
        node_microsoft = Node(Microsoft_Data.CONTENT, Microsoft_Data.TITEL, Microsoft_Data.IMAGE_NAME,
                              industry=[self.information_technology, self.cybersecurity, self.media_and_entertainment,
                                        self.cloud_computing])
        node_nestle = Node(Nestle_Data.CONTENT, Nestle_Data.TITEL, Nestle_Data.IMAGE_NAME,
                           industry=[self.consumerGoods])
        node_netcologne = Node(Netcologne_Data.CONTENT, Netcologne_Data.TITEL, Netcologne_Data.IMAGE_NAME,
                               industry=[self.information_technology])
        node_netflix = Node(Netflix_Data.CONTENT, Netflix_Data.TITEL, Netflix_Data.IMAGE_NAME,
                            industry=[self.information_technology, self.media_and_entertainment])
        node_next_kraftwerke = Node(NextKraftwerke_Data.CONTENT, NextKraftwerke_Data.TITEL,
                                    NextKraftwerke_Data.IMAGE_NAME, industry=[self.energy])
        node_obi = Node(Obi_Data.CONTENT, Obi_Data.TITEL, Obi_Data.IMAGE_NAME, industry=[self.consumerGoods])
        node_otto = Node(Otto_Data.CONTENT, Otto_Data.TITEL, Otto_Data.IMAGE_NAME, industry=[self.consumerGoods])
        node_parcit = Node(ParcIT_Data.CONTENT, ParcIT_Data.TITEL, ParcIT_Data.IMAGE_NAME,
                           industry=[self.financial_services, self.information_technology])
        node_pferd_werkzeuge = Node(PferdWerkzeuge_Data.CONTENT, PferdWerkzeuge_Data.TITEL,
                                    PferdWerkzeuge_Data.IMAGE_NAME, industry=[self.mechanical_engineering])
        node_porsche = Node(Porsche_Data.CONTENT, Porsche_Data.TITEL, Porsche_Data.IMAGE_NAME,
                            industry=[self.automotive_industry])
        node_rewe_digital = Node(ReweDigital_Data.CONTENT, ReweDigital_Data.TITEL, ReweDigital_Data.IMAGE_NAME,
                                 industry=[self.information_technology, self.consumerGoods])
        node_rhenag_rheinische_energie = Node(RhenagRheinischeEnergie_Data.CONTENT, RhenagRheinischeEnergie_Data.TITEL,
                                              RhenagRheinischeEnergie_Data.IMAGE_NAME, industry=[self.energy])
        node_riot_games = Node(RiotGames_Data.CONTENT, RiotGames_Data.TITEL, RiotGames_Data.IMAGE_NAME,
                               industry=[self.media_and_entertainment])
        node_sap = Node(SAP_Data.CONTENT, SAP_Data.TITEL, SAP_Data.IMAGE_NAME, industry=[self.information_technology])
        node_schneider_electric = Node(SchneiderElectric_Data.CONTENT, SchneiderElectric_Data.TITEL,
                                       SchneiderElectric_Data.IMAGE_NAME, industry=[self.information_technology])
        node_secunet = Node(Secunet_Data.CONTENT, Secunet_Data.TITEL, Secunet_Data.IMAGE_NAME,
                            industry=[self.cybersecurity, self.information_technology])
        node_sollers_consulting = Node(SollersConsulting_Data.CONTENT, SollersConsulting_Data.TITEL,
                                       SollersConsulting_Data.IMAGE_NAME,
                                       industry=[self.consulting, self.financial_services, self.information_technology, self.insurance])
        node_spacex = Node(SpaceX_Data.CONTENT, SpaceX_Data.TITEL, SpaceX_Data.IMAGE_NAME,
                           industry=[self.aerospace, self.information_technology])
        node_tesla = Node(Tesla_Data.CONTENT, Tesla_Data.TITEL, Tesla_Data.IMAGE_NAME,
                          industry=[self.information_technology, self.automotive_industry])
        node_volkswagen = Node(Volkswagen_Data.CONTENT, Volkswagen_Data.TITEL, Volkswagen_Data.IMAGE_NAME,
                               industry=[self.automotive_industry])
        node_zeiss = Node(Zeiss_Data.CONTENT, Zeiss_Data.TITEL, Zeiss_Data.IMAGE_NAME,
                          industry=[self.information_technology, self.pharmaceuticalsAndHealth])

        graph.add_new_node_to_graph(node_action)
        graph.add_new_node_to_graph(node_aldinord)
        graph.add_new_node_to_graph(node_audi)
        graph.add_new_node_to_graph(node_axa)
        graph.add_new_node_to_graph(node_bmw)
        graph.add_new_node_to_graph(node_boeing)
        graph.add_new_node_to_graph(node_coseon)
        graph.add_new_node_to_graph(node_electronic_arts)
        graph.add_new_node_to_graph(node_esl_gaming)
        graph.add_new_node_to_graph(node_google)
        graph.add_new_node_to_graph(node_hdi)
        graph.add_new_node_to_graph(node_innnovas)
        graph.add_new_node_to_graph(node_lidl)
        graph.add_new_node_to_graph(node_mercedes_benz)
        graph.add_new_node_to_graph(node_microsoft)
        graph.add_new_node_to_graph(node_nestle)
        graph.add_new_node_to_graph(node_netcologne)
        graph.add_new_node_to_graph(node_netflix)
        graph.add_new_node_to_graph(node_next_kraftwerke)
        graph.add_new_node_to_graph(node_obi)
        graph.add_new_node_to_graph(node_otto)
        graph.add_new_node_to_graph(node_parcit)
        graph.add_new_node_to_graph(node_pferd_werkzeuge)
        graph.add_new_node_to_graph(node_porsche)
        graph.add_new_node_to_graph(node_rewe_digital)
        graph.add_new_node_to_graph(node_rhenag_rheinische_energie)
        graph.add_new_node_to_graph(node_riot_games)
        graph.add_new_node_to_graph(node_sap)
        graph.add_new_node_to_graph(node_schneider_electric)
        graph.add_new_node_to_graph(node_secunet)
        graph.add_new_node_to_graph(node_sollers_consulting)
        graph.add_new_node_to_graph(node_spacex)
        graph.add_new_node_to_graph(node_tesla)
        graph.add_new_node_to_graph(node_volkswagen)
        graph.add_new_node_to_graph(node_zeiss)

    @staticmethod
    def connect_industry_with_node(graph):
        nodes = graph.nodes

        for node in nodes:
            if bool(node.industry):
                for industry in node.industry:
                    industry.connect(node)
 