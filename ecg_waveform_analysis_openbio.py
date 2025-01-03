# -*- coding: utf-8 -*-
"""ECG_Waveform_Analysis_OpenBio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XJVkVYSP4sJ3w_bm5HxEMNBeWqE_ulB5
"""

pip install scipy matplotlib

import scipy.io
import matplotlib.pyplot as plt

# Load the .mat file
mat_file_path = "/content/HR00001.mat"  # Replace with your .mat file path
data = scipy.io.loadmat(mat_file_path)

# Inspect the keys in the loaded .mat file
print(data.keys())

# Extract the ECG signal (assuming the key is 'val')
# PTB-XL signals are typically stored under the key 'val'
ecg_signal = data['val']  # Shape: (number_of_leads, number_of_samples)

# Define parameters (replace with values from .hea if available)
sampling_frequency = 500  # Hz (default for PTB-XL)
time = [i / sampling_frequency for i in range(ecg_signal.shape[1])]

# Plot signals for all leads
plt.figure(figsize=(15, 10))
for lead_idx in range(ecg_signal.shape[0]):
    plt.plot(time, ecg_signal[lead_idx, :], label=f"Lead {lead_idx + 1}")

# Add titles and labels
plt.title("ECG Signal Visualization")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid(True)
plt.show()

import scipy.io
import matplotlib.pyplot as plt

# Load the .mat file
mat_file_path = "/content/HR00001.mat"  # Replace with your .mat file path
data = scipy.io.loadmat(mat_file_path)

# Extract the ECG signal (assuming the key is 'val')
ecg_signal = data['val']  # Shape: (number_of_leads, number_of_samples)

# Define parameters (replace with values from .hea if available)
sampling_frequency = 500  # Hz (default for PTB-XL)
time = [i / sampling_frequency for i in range(ecg_signal.shape[1])]

# Plot each lead in a separate subplot
num_leads = ecg_signal.shape[0]
plt.figure(figsize=(15, 2 * num_leads))  # Adjust height based on the number of leads

for lead_idx in range(num_leads):
    plt.subplot(num_leads, 1, lead_idx + 1)  # Create a subplot for each lead
    plt.plot(time, ecg_signal[lead_idx, :], color='blue')
    plt.title(f"Lead {lead_idx + 1}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (mV)")
    plt.grid(True)

# Adjust layout for better visibility
plt.tight_layout()
plt.show()

import pandas as pd

data = pd.read_csv('/content/ptbxl_database.csv')

data.head(10)

import pandas as pd

# Load the ptbxl database CSV file
df = pd.read_csv('/content/ptbxl_database.csv')

# Select only the relevant columns
df_filtered = df[['ecg_id', 'report', 'scp_codes', 'filename_lr', 'filename_hr']]

# Function to modify the filenames (remove 'records100', 'records500' and '_lr', '_hr')
def modify_filename(filename):
    # Remove 'records100' or 'records500' and '_lr' or '_hr'
    return filename.split('/')[1]  # This takes the part after '00000/00001_lr'

# Apply the filename modification to 'filename_lr' and 'filename_hr'
df_filtered['filename_lr'] = df_filtered['filename_lr'].apply(modify_filename)
df_filtered['filename_hr'] = df_filtered['filename_hr'].apply(modify_filename)

# Save the modified DataFrame to a new CSV file
df_filtered.to_csv('ptbxl_filtered.csv', index=False)

print("The filtered CSV has been saved as 'ptbxl_filtered.csv'")

import pandas as pd

# Load the ptbxl database CSV file
df = pd.read_csv('/content/ptbxl_database.csv')

# Select only the relevant columns
df_filtered = df[['ecg_id', 'report', 'scp_codes', 'filename_lr', 'filename_hr']]

# Function to modify the filenames (remove 'records100', 'records500' and '_lr', '_hr')
def modify_filename(filename):
    # Remove 'records100' or 'records500' and '_lr' or '_hr'
    filename_parts = filename.split('/')[-1]  # Get the last part (e.g., '00000/00001_lr')
    filename_clean = filename_parts.split('_')[0]  # Get the part before '_lr' or '_hr'
    return filename_clean

# Apply the filename modification to 'filename_lr' and 'filename_hr'
df_filtered['filename_lr'] = df_filtered['filename_lr'].apply(modify_filename)
df_filtered['filename_hr'] = df_filtered['filename_hr'].apply(modify_filename)

# Save the modified DataFrame to a new CSV file
df_filtered.to_csv('ptbxl_filtered.csv', index=False)

print("The filtered CSV has been saved as 'ptbxl_filtered.csv'")

import pandas as pd

# Step 1: Load the ptbxl database CSV file
df = pd.read_csv('/content/ptbxl_database.csv')

# Step 2: Select only the relevant columns
df_filtered = df[['ecg_id', 'report', 'scp_codes', 'filename_lr', 'filename_hr']]

# Step 3: Function to modify the filenames
def modify_filename(filename):
    # Split by '/' to extract the numeric part (e.g., '00000/00001')
    path_parts = filename.split('/')
    numeric_part = path_parts[-1].split('_')[0]  # Extract the part before '_lr' or '_hr'
    return numeric_part

# Apply the filename modification to 'filename_lr' and 'filename_hr'
df_filtered['filename_lr'] = df_filtered['filename_lr'].apply(modify_filename)
df_filtered['filename_hr'] = df_filtered['filename_hr'].apply(modify_filename)

# Step 4: Save the modified DataFrame to a new CSV file
df_filtered.to_csv('ptbxl_filtered.csv', index=False)

# Print confirmation
print("The filtered CSV has been saved as 'ptbxl_filtered.csv'")

import pandas as pd

# Load the ptbxl database CSV file
df = pd.read_csv('/content/ptbxl_database.csv')

# Select only the relevant columns
df_filtered = df[['ecg_id', 'report', 'scp_codes', 'filename_lr', 'filename_hr']]

# Use slicing to modify the filenames
df_filtered['filename_lr'] = df_filtered['filename_lr'].str.slice(10, -3)  # Removes 'records100/' and '_lr'
df_filtered['filename_hr'] = df_filtered['filename_hr'].str.slice(10, -3)  # Removes 'records500/' and '_hr'

# Save the modified DataFrame to a new CSV file
df_filtered.to_csv('ptbxl_filtered.csv', index=False)

# Print confirmation
print("The filtered CSV has been saved as 'ptbxl_filtered.csv'")

import pandas as pd

# Load the filtered PTB-XL database
filtered_ptbxl = pd.read_csv("/content/ptbxl_filtered.csv")

# Load the SCP statements CSV
scp_statements = pd.read_csv("/content/scp_statements(1).csv")

# Prepare the output DataFrame
output_data = filtered_ptbxl.copy()

# Define maximum possible statements to handle
MAX_STATEMENTS = 5

# Add placeholder columns for new statements
for i in range(1, MAX_STATEMENTS + 1):
    output_data[f"Statement_{i}"] = None
    output_data[f"SCP_ECG_{i}"] = None

# Process each row in the filtered PTB-XL data
for index, row in filtered_ptbxl.iterrows():
    scp_codes = eval(row["scp_codes"])  # Convert the string representation of dict to actual dict
    matching_keys = [key for key, value in scp_codes.items() if value > 0]

    for i, key in enumerate(matching_keys[:MAX_STATEMENTS]):  # Limit to MAX_STATEMENTS
        match = scp_statements[scp_statements["diagnostic_subclass"] == key]
        if not match.empty:
            output_data.at[index, f"Statement_{i+1}"] = match.iloc[0]["Statement Category"]
            output_data.at[index, f"SCP_ECG_{i+1}"] = match.iloc[0]["SCP-ECG Statement Description"]

    # If only one statement exists, replicate it in the other columns
    if len(matching_keys) == 1:
        for j in range(1, MAX_STATEMENTS):
            output_data.at[index, f"Statement_{j+1}"] = output_data.at[index, "Statement_1"]
            output_data.at[index, f"SCP_ECG_{j+1}"] = output_data.at[index, "SCP_ECG_1"]

# Save the output to a new CSV file
output_data.to_csv("filtered_ptbxl_with_statements.csv", index=False)

!pip install googletrans

import pandas as pd
from googletrans import Translator

# Load the filtered PTB-XL database with statements
filtered_ptbxl_with_statements = pd.read_csv("/content/filtered_ptbxl_with_statements.csv")

# Initialize the Google Translator
translator = Translator()

# Translate the 'report' column from German to English
translated_reports = []
for report in filtered_ptbxl_with_statements['report']:
    try:
        if pd.isnull(report) or not isinstance(report, str):  # Check for None or invalid entries
            translated_reports.append(None)
            continue
        translated_text = translator.translate(report, src='de', dest='en').text
        translated_reports.append(translated_text)
    except Exception as e:
        translated_reports.append(None)  # Handle potential translation errors
        print(f"Error translating report '{report}': {e}")

# Add the translated reports to the DataFrame
filtered_ptbxl_with_statements['report_en'] = translated_reports

# Save the updated DataFrame to a new CSV file
filtered_ptbxl_with_statements.to_csv("filtered_ptbxl_with_statements_translated.csv", index=False)

pip install deep-translator

import pandas as pd
from deep_translator import GoogleTranslator

# Load the filtered PTB-XL database with statements
filtered_ptbxl_with_statements = pd.read_csv("/content/filtered_ptbxl_with_statements.csv")

# Translate the 'report' column from German to English
translated_reports = []
for report in filtered_ptbxl_with_statements['report']:
    try:
        if pd.isnull(report) or not isinstance(report, str):  # Check for None or invalid entries
            translated_reports.append(None)
            continue
        translated_text = GoogleTranslator(source='de', target='en').translate(report)
        translated_reports.append(translated_text)
    except Exception as e:
        translated_reports.append(None)  # Handle potential translation errors
        print(f"Error translating report '{report}': {e}")

# Add the translated reports to the DataFrame
filtered_ptbxl_with_statements['report_en'] = translated_reports

# Save the updated DataFrame to a new CSV file
filtered_ptbxl_with_statements.to_csv("filtered_ptbxl_with_statements_translated.csv", index=False)

data = pd.read_csv('/content/filtered_ptbxl_with_statements.csv')

data['report'].value_counts()

import pandas as pd

# Load the filtered PTB-XL database with statements
filtered_ptbxl_with_statements = pd.read_csv("/content/filtered_ptbxl_with_statements.csv")

# Get the value counts of the 'report' column
report_value_counts = filtered_ptbxl_with_statements['report'].value_counts().reset_index()
report_value_counts.columns = ['report', 'count']

# Save the value counts to a separate CSV
report_value_counts.to_csv("report_value_counts.csv", index=False)

print("Value counts of 'report' column saved to 'report_value_counts.csv'.")

GIVE ME 2 MINutes

import pandas as pd
from deep_translator import GoogleTranslator

# Load the value_counts CSV
report_value_counts = pd.read_csv("/content/report_value_counts.csv")

# Translate the 'report' column from German to English
translated_reports = []
for report in report_value_counts['report']:
    try:
        if pd.isnull(report) or not isinstance(report, str):
            translated_reports.append(None)
            continue
        translated_text = GoogleTranslator(source='de', target='en').translate(report)
        translated_reports.append(translated_text)
    except Exception as e:
        translated_reports.append(None)  # Handle translation errors
        print(f"Error translating report '{report}': {e}")

# Add the translations to the DataFrame
report_value_counts['report_translated'] = translated_reports

# Save the translated value_counts to a new CSV file
report_value_counts.to_csv("translated_report_value_counts.csv", index=False)

print("Translated value_counts saved as 'translated_report_value_counts.csv'.")

import pandas as pd

# Load the filtered PTB-XL database with statements
filtered_ptbxl_with_statements = pd.read_csv("filtered_ptbxl_with_statements.csv")

# Load the translated value_counts CSV
translated_reports = pd.read_csv("translated_report_value_counts.csv")

# Merge the translated reports back into the original DataFrame
filtered_ptbxl_with_statements = filtered_ptbxl_with_statements.merge(
    translated_reports, on='report', how='left', suffixes=('', '_translated')
)

# Save the updated DataFrame with translations
filtered_ptbxl_with_statements.to_csv("filtered_ptbxl_with_statements_translated.csv", index=False)

print("Merged translations into the PTB-XL dataset and saved as 'filtered_ptbxl_with_statements_translated.csv'.")