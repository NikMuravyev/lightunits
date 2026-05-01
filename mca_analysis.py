"""
MCA with Row Labels (Col1) and Color Groups (Col2)
--------------------------------------------------
- First CSV column = row names (not in MCA)
- Second CSV column = grouping variable for color (not in MCA)
- All remaining columns = categorical variables for MCA

Required: pip install pandas prince matplotlib
"""

import pandas as pd
import prince
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from pathlib import Path

# ======================
# CONFIGURATION
# ======================
CSV_FILE = ("/home/yenotmur/Dropbox/TypConstr/nesti_threl.csv")
OUTPUT_IMAGE = "mca_map_colored.png"
DROP_MISSING = True
DPI = 300
FIG_SIZE = (10, 8)

# ======================
# 1. LOAD DATA & PREPARE
# ======================
print(f"Reading: {CSV_FILE}")
df = pd.read_csv(CSV_FILE, encoding='utf-8')

# Identify columns
row_id_col = df.columns[0]          # Labels
color_col   = df.columns[1]         # Group for coloring
mca_cols    = df.columns[2:]        # All other columns for MCA

print(f"Row labels   : '{row_id_col}'")
print(f"Color groups : '{color_col}'")
print(f"MCA columns  : {list(mca_cols)}")

# Extract labels and color groups (as strings)
row_labels = df[row_id_col].astype(str).tolist()
color_vals = df[color_col].astype(str).tolist()

# Prepare MCA data (only columns 3+)
df_mca = df[mca_cols].copy()

if DROP_MISSING:
    initial_rows = len(df_mca)
    df_mca = df_mca.dropna()
    kept_idx = df_mca.index
    row_labels = [row_labels[i] for i in kept_idx]
    color_vals = [color_vals[i] for i in kept_idx]
    print(f"Dropped {initial_rows - len(df_mca)} rows with missing values.")

# Ensure MCA columns are categorical
df_mca = df_mca.astype('category')

print(f"Data for MCA shape: {df_mca.shape}")

# ======================
# 2. PERFORM MCA
# ======================
print("Performing MCA...")
mca = prince.MCA(n_components=2, random_state=42)
mca = mca.fit(df_mca)

row_coords = mca.row_coordinates(df_mca)

eigenvalues = mca.eigenvalues_
explained_var = eigenvalues / eigenvalues.sum() * 100
print(f"Variance explained: Dim1 = {explained_var[0]:.2f}%, Dim2 = {explained_var[1]:.2f}%")

# ======================
# 3. PREPARE COLOR MAPPING
# ======================
# Get unique categories from the color column (sorted for consistent mapping)
unique_colors = sorted(set(color_vals))
n_colors = len(unique_colors)

# Choose a colormap (tab10, tab20, Set3, etc.)
cmap = plt.cm.get_cmap('tab10', n_colors)
color_map = {cat: cmap(i) for i, cat in enumerate(unique_colors)}

# Map each point to its color
point_colors = [color_map[val] for val in color_vals]

# ======================
# 4. PLOT INDIVIDUALS WITH LABELS & COLOR GROUPS
# ======================
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=FIG_SIZE)

# Scatter plot with colors from second column
scatter = ax.scatter(row_coords[0], row_coords[1],
                     c=point_colors, s=70, alpha=0.8,
                     edgecolors='black', linewidth=0.5)

# Add text labels for each point
for i, label in enumerate(row_labels):
    ax.annotate(label,
                (row_coords.iloc[i, 0], row_coords.iloc[i, 1]),
                fontsize=8, alpha=0.9,
                xytext=(5, 3), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.6, ec='none'))

# Axes lines through origin
ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
ax.axvline(x=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

# Labels and title
ax.set_xlabel(f"Dimension 1 ({explained_var[0]:.1f}%)")
ax.set_ylabel(f"Dimension 2 ({explained_var[1]:.1f}%)")
ax.set_title("MCA Factor Map – Colored by " + color_col, fontsize=14, pad=20)

# Create legend for color groups
handles = [plt.Line2D([0], [0], marker='o', color='w',
                      markerfacecolor=color_map[cat], markersize=8,
                      label=cat, markeredgecolor='black', markeredgewidth=0.5)
           for cat in unique_colors]
ax.legend(handles=handles, title=color_col, loc='best', fontsize=9)

ax.set_aspect('equal', adjustable='datalim')
plt.tight_layout()

# ======================
# 5. SAVE IMAGE
# ======================
output_path = Path(OUTPUT_IMAGE)
plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
print(f"Map saved to: {output_path.resolve()}")

# plt.show()