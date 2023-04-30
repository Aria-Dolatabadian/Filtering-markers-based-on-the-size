#Generates random data
# import pandas as pd
# import numpy as np
#
# # Generate random data
# n_rows = 1000  # Number of rows in the DataFrame
# markers = [f"Bn{i}" for i in range(1, 1001)]
# chromosomes = np.random.randint(1, 20, size=n_rows)
# start_positions = np.random.randint(1000000, 100000000, size=n_rows)
# end_positions = start_positions + np.random.randint(1, 1000000, size=n_rows)
#
# # Create DataFrame
# data = {'Markers': markers, 'Chromosome': chromosomes, 'Start': start_positions, 'End': end_positions}
# df = pd.DataFrame(data)
#
# # Export DataFrame as CSV
# df.to_csv('marker.csv', index=False)
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('marker.csv')

# Filter markers based on size
filtered_df = df[(df['Size'] >= 50000) & (df['Size'] <= 100000)]

# Export filtered markers as CSV
filtered_df.to_csv('filtered_markers.csv', index=False)

from docx import Document
# Create a new Word document
doc = Document()

# Add a table to the document
table = doc.add_table(rows=1, cols=len(filtered_df.columns))

# Write the column names
for i, column in enumerate(filtered_df.columns):
    table.cell(0, i).text = column

# Write the data rows
for _, row in filtered_df.iterrows():
    table.add_row()
    for i, value in enumerate(row):
        table.cell(-1, i).text = str(value)

# Save the document as a docx file
doc.save('filtered_markers.docx')


# Visualize the results
plt.scatter(filtered_df['Start'], filtered_df['End'])
plt.xlabel('Start')
plt.ylabel('End')
plt.title('Filtered Markers')
plt.show()





# Visualize the results
chromosomes = filtered_df['Chromosome'].unique()
colors = ['red', 'blue', 'green', 'orange', 'purple']  # Customize the colors if needed

# Create a scatter plot for each chromosome
for chromosome, color in zip(chromosomes, colors):
    chromosome_df = filtered_df[filtered_df['Chromosome'] == chromosome]
    plt.scatter(chromosome_df['Size'], chromosome_df['Start'], color=color, label=f'Chromosome {chromosome}')

plt.xlabel('Size')
plt.ylabel('Start')
plt.title('Filtered Markers')
plt.legend()
plt.show()

# Count the markers by chromosome
chromosome_counts = filtered_df['Chromosome'].value_counts().sort_index()

# Visualize the results as a bar chart
chromosomes = range(1, 20)
plt.bar(chromosomes, chromosome_counts.values)
plt.xlabel('Chromosome')
plt.ylabel('Count')
plt.title('Filtered Markers by Chromosome')
plt.xticks(chromosomes)
plt.show()






import pandas as pd

# Read the CSV file
df = pd.read_csv('marker.csv')

# Count the total number of markers
total_markers = df.shape[0]

# Count the number of markers on each chromosome
markers_per_chromosome = df['Chromosome'].value_counts().sort_index()

# Filter markers with size between 100000 and 300000
filtered_markers = df[(df['Size'] >= 100000) & (df['Size'] <= 300000)]

# Export the results as a new CSV file
results = pd.DataFrame({
    'Total Markers': [total_markers],
    'Markers per Chromosome': markers_per_chromosome.values
}, index=markers_per_chromosome.index)

filtered_markers.to_csv('filtered_markers.csv', index=False)
results.to_csv('summary.csv', index=False)
