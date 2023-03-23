import xml.etree.ElementTree as ET
import random
import requests
import PySimpleGUI
import PySimpleGUI as sg
import os


def generate_xml_file(x, y, quantidade):
    proximo_edificio = 1
    while os.path.exists(f'edificio{proximo_edificio}.xml'):
        proximo_edificio += 1
    root = ET.Element(f'edificio{proximo_edificio}')
    def Gerar_PREDIO_COMUN():
        root = ET.Element('edificio', {
        'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 
        'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema', 
        'versao': '7.9.1', 
        'autorizacao': '2f64f11a7750ff860a55c2c534bc23b6', 
        'tipo': 'E'})
    gravado = ET.SubElement(root, 'gravado')
    gravado.text = 'false'
    idCEMobile = ET.SubElement(root, 'idCEMobile')
    idCEMobile.text = '1'
    coordX = ET.SubElement(root, 'coordX')
    coordX.text = x
    coordY = ET.SubElement(root, 'coordY')
    coordY.text = y
    codigoZona = ET.SubElement(root, 'codigoZona')
    codigoZona.text = 'zona-nutra'
    nomeZona = ET.SubElement(root, 'nomeZona')
    nomeZona.text = 'zona-nutra'
    localidade = ET.SubElement(root, 'localidade')
    localidade.text = 'cidade'
    enderecoEdificio = ET.SubElement(root, 'enderecoEdificio')
    logradouro = ET.SubElement(enderecoEdificio, 'logradouro')
    logradouro.text = 'endereço'
    numero_fachada = ET.SubElement(enderecoEdificio, 'numero_fachada')
    numero_fachada.text = '123'
    cep = ET.SubElement(enderecoEdificio, 'cep')
    cep.text = 'cep'
    bairro = ET.SubElement(enderecoEdificio, 'bairro')
    bairro.text = 'bairro'
    id_roteiro = ET.SubElement(enderecoEdificio, 'id_roteiro')
    id_roteiro.text = '6805644'
    id_localidade = ET.SubElement(enderecoEdificio, 'id_localidade')
    id_localidade.text = '1890624'
    cod_lograd = ET.SubElement(enderecoEdificio, 'cod_lograd')
    cod_lograd.text = '2260609890'
    tecnico = ET.SubElement(root, 'tecnico')
    id = ET.SubElement(tecnico, 'id')
    id.text = '1841340261'
    nome = ET.SubElement(tecnico, 'nome')
    nome.text = 'BRUNA CRISPIM ALVES'
    empresa = ET.SubElement(root, 'empresa')
    id = ET.SubElement(empresa, 'id')
    id.text = '42541126'
    nome = ET.SubElement(empresa, 'nome')
    nome.text = 'TELEMONT'
    data = ET.SubElement(root, 'data')
    data.text = '20230310201528'
    totalUCs = ET.SubElement(root, 'totalUCs')
    totalUCs.text = '1'
    ocupacao = ET.SubElement(root, 'ocupacao')
    ocupacao.text = 'EDIFICACAOCOMPLETA'
    redeInterna = ET.SubElement(root, 'redeInterna')
    redeInterna.text = 'N'
    infoFotos = ET.SubElement(root, 'infoFotos')
    fotoInteriorEdificio = ET.SubElement(infoFotos, 'fotoInteriorEdificio')
    fotoInteriorEdificio.text = '2_3.jpg'
    fotoExteriorEdificio = ET.SubElement(infoFotos, 'fotoExteriorEdificio')
    fotoExteriorEdificio.text = '2_3_1.jpg'
    fotoFachadaEdificio = ET.SubElement(infoFotos, 'fotoFachadaEdificio')
    fotoFachadaEdificio.text = '2_3_2.jpg'
    ucs = ET.SubElement(root, 'ucs')
    for i in range(int(quantidade)):
        uc = ET.SubElement(ucs, 'uc')
        destinacao = ET.SubElement(uc, 'destinacao')
        destinacao.text = 'RESIDENCIA'
        id_complemento3 = ET.SubElement(uc, 'id_complemento3')
        id_complemento3.text = '9'
        argumento3 = ET.SubElement(uc, 'argumento3')
        argumento3.text = '1'
        argumento3 = ET.SubElement(uc, 'argumento3')
        argumento3.text = str(random.randint(1, 10))
        id_complemento4 = ET.SubElement(uc, 'id_complemento4')
        id_complemento4.text = '7'
        argumento4_logico = ET.SubElement(uc, 'argumento4_logico')
        argumento4_logico.text = '1'
        argumento4_real = ET.SubElement(uc, 'argumento4_real')
        argumento4_real.text = '1'
        pass

    tree = ET.ElementTree(root)
    tree.write(f'edificio{proximo_edificio}.xml')
    

layout = [
    [sg.Text('coordenada X:')],
    [sg.Input(key='coordX', size=(10,1))],
    [sg.Text('coordenada Y:')],
    [sg.Input(key='coordY', size=(10,1))], 
    [sg.Text('quantidade de UCs:')],
    [sg.Input(key='quantidade', size=(10,1))],
    [sg.Button('Gerar arquivo'), sg.Button('Sair', button_color=('red'))]
]

window = sg.Window('Gerador de arquivos XML', layout, resizable = True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Gerar arquivo':
        x = values['coordX']
        y = values['coordY']
        quantidade = values['quantidade']
        generate_xml_file(x, y, quantidade)
        
window.close()