import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)
# checks if it works

"""
print (doc.toprettyxml())
# output to console comment this out once you know it works

# to open the xml in a file
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)
"""
"""
# to print the train codes
objTrainPositionNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionNode in objTrainPositionNodes:
    traincodenode = objTrainPositionNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    print (traincode)
"""
# store this property as a CSV
with  open('traincodes.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)

with open('traincodes_D.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []

        # Get TrainCode first
        train_code_node = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        train_code = train_code_node.firstChild.nodeValue.strip()

        # Only keep train codes starting with "D"
        if not train_code.startswith("D"):
            continue

        # Now collect the rest of the data
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())

        train_writer.writerow(dataList)