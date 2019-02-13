import csv
import dataSetFields as fields
import numpy as np
import saveDatasetInDB
import saveUsersInDB
import plot_graph
import age_userid_type5
import age_userid_type4
import avg_vector
import plot2D
import clustering


def main():
    datasetPath = "data.csv"
    dataset = open(datasetPath, 'r')
    array = np.zeros(28)
    csvreader = csv.reader(dataset)
    print('LEGGO')
    stepsCount = 0
    for row in csvreader:
        type = int(row[fields.typeOfValue])
        array[type] +=1
        if(type ==1):
            stepsCount+=1
    print('Steps: '+str(stepsCount))
    print('SCRIVO')
    output = open("datasetClusteredByType.txt", 'w+')
    output.write("1: steps: "+str(array[1])+"\n")
    output.write("2: weight: "+str(+array[2])+"\n")
    output.write("3:  calculated BMI: "+str(+array[3])+"\n")
    output.write("4:  systolic blood pressure: "+str(+array[4])+"\n")
    output.write("5:  pulse wave velocity: "+str(+array[5])+"\n")
    output.write("6:  PWV healthiness: "+str(+array[6])+"\n")
    output.write("7:  heart rate avg: "+str(+array[7])+"\n")
    output.write("8:  heart rate min: "+str(+array[8])+"\n")
    output.write("9:  heart rate max: "+str(+array[9])+"\n")
    output.write("10: sleepduration: "+str(+array[10])+"\n")
    output.write("11: bedin: "+str(+array[11])+"\n")
    output.write("12: bedout: "+str(+array[12])+"\n")
    output.write("13: nbawake: "+str(+array[13])+"\n")
    output.write("14: awakeduration (hours): "+str(+array[14])+"\n")
    output.write("15: time to sleep (hours): "+str(+array[15])+"\n")
    output.write("16: time to wake up (hours): "+str(+array[16])+"\n")
    output.write("17: lightduration: "+str(+array[17])+"\n")
    output.write("18: remduration: "+str(+array[18])+"\n")
    output.write("19: deepduration: "+str(+array[19])+"\n")
    output.write("20: activity type: "+str(+array[20])+"\n")
    output.write("21: activity duration: "+str(+array[21])+"\n")
    output.write("22: activity calories: "+str(+array[22])+"\n")
    output.write("23: activity hr average: "+str(+array[23])+"\n")
    output.write("24: activity hr minimum: "+str(+array[24])+"\n")
    output.write("25: activity hr maximum: "+str(+array[25])+"\n")
    output.write("26: steps gait speed: "+str(+array[26])+"\n")
    output.write("27: distance gait speed: "+str(+array[27])+"\n")


    output.close()
    print('DONE')

if __name__=="__main__":
    #main()
    #saveDatasetInDB.saveData()
    #saveUsersInDB.saveData()
    #plot_graph.query_avg()
    #age_userid_type5.save_data()
    #age_userid_type4.save_data()
    #avg_vector.avg_behaviour(5,0,30)
    #plot2D.fromArray_toVectorTuples(5,6)
    clustering.cluster3D(3,5,11)
    #clustering.cluster(3,1,4)