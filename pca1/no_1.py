import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')  
def manchester_encoding(binary_data):
    encoded_data = []
    for bit in binary_data:
        if bit == '1':
            encoded_data.extend([1, 0])  # High to Low transition
        elif bit == '0':
            encoded_data.extend([0, 1])  # Low to High transition
    return encoded_data

def differential_manchester_encoding(binary_data):
    encoded_data = []
    last_level = 1  # Start with a high level
    for bit in binary_data:
        if bit == '0' and last_level == 1:
            encoded_data.extend([0,1])
            last_level = 1
        elif bit == '0' and last_level == 0:
            encoded_data.extend([1,0])
            last_level = 0
        elif bit == '1' and last_level == 1:
            encoded_data.extend([1,0])
            last_level = 0
        elif bit == '1' and last_level == 0:
            encoded_data.extend([0,1])
            last_level = 1
    return encoded_data

def plot_waveform(encoded_data, binary_data, title, filename):
    plt.figure(figsize=(12, 4))
    
    
    time_per_level = 1.25
    time_axis = [i * time_per_level for i in range(len(encoded_data))]
    
   
    plt.step(time_axis, encoded_data, where='post', label='Encoded Waveform', linewidth=2)
    
    
    bit_length = 2.5 
    for i, bit in enumerate(binary_data):
        x_pos = i * bit_length + bit_length / 2
        plt.text(x_pos, -0.3, bit, ha='center', va='center', fontsize=12, color='red', 
                 bbox=dict(facecolor='white', alpha=0.8))
    
    
    for i in range(len(binary_data) + 1):
        plt.axvline(x=i * bit_length, color='gray', linestyle='--', alpha=0.5)
    
    plt.title(title)
    plt.xlabel('Time (units)')
    plt.ylabel('Amplitude')
    plt.yticks([0, 1])
    plt.ylim(-0.5, 1.5)
    plt.legend(loc='upper right')

    try:
        plt.show()  
    except:
        plt.savefig(filename)  
        print(f"Plot saved as {filename}")
    finally:
        plt.close()  

# Input binary data
# binary_data = '1011100010'
binary_data = input("enter the data: ")

# Manchester Encoding
manchester_encoded = manchester_encoding(binary_data)
print("Manchester Encoded Data:", manchester_encoded)
plot_waveform(manchester_encoded, binary_data, "Manchester Encoding", "manchester_encoding.png")

# Differential Manchester Encoding
diff_manchester_encoded = differential_manchester_encoding(binary_data)
print("Differential Manchester Encoded Data:", diff_manchester_encoded)
plot_waveform(diff_manchester_encoded, binary_data, "Differential Manchester Encoding", "diff_manchester_encoding.png")
