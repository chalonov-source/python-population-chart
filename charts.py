import matplotlib.pyplot as plt 

def generate_pie_chart(labels, values, title):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.title(title)
    plt.show()
    
