"""
MCA with Row Labels (Col1), Color Groups (Col2), and Dot Size (Col3)
--------------------------------------------------------------------
- First CSV column  = row names (not in MCA)
- Second CSV column = grouping variable for color (not in MCA)
- Third CSV column  = numeric variable for dot size (not in MCA)
- All remaining columns = categorical variables for MCA

Required: pip install pandas prince matplotlib
"""

import pandas as pd
import prince
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np
from pathlib import Path

# ======================
# CONFIGURATION
# ======================
CSV_FILE = ("/home/yenotmur/Dropbox/TypConstr/CARRYING/LV_carrying_v2_cut_ipm.csv")
OUTPUT_IMAGE = "mca_map_colored.png"
DROP_MISSING = True
DPI = 300
FIG_SIZE = (10, 8)

# Dot size scaling parameters (points^2)
IPM_MIN_DOT_SIZE = 40     # smallest point (increased from 20)
IPM_MAX_DOT_SIZE = 400    # largest point  (increased from 200)
DOT_SIZE_SCALE = 2.0      # multiplier to proportionally enlarge all dots

# ======================
# 1. LOAD DATA & PREPARE
# ======================
print(f"Reading: {CSV_FILE}")
df = pd.read_csv(CSV_FILE, encoding='utf-8')

# Identify columns
row_id_col = df.columns[0]          # Labels
color_col   = df.columns[1]         # Group for coloring
ipm_col     = df.columns[2]         # Numeric column for dot size (NOT used in MCA)
mca_cols    = df.columns[3:]        # All other columns for MCA

print(f"Row labels   : '{row_id_col}'")
print(f"Color groups : '{color_col}'")
print(f"Dot size (ipm): '{ipm_col}'")
print(f"MCA columns  : {list(mca_cols)}")

# Extract labels, color groups, and ipm values (all as lists)
row_labels = df[row_id_col].astype(str).tolist()
color_vals = df[color_col].astype(str).tolist()
ipm_vals   = pd.to_numeric(df[ipm_col], errors='coerce')   # force numeric, NaN if bad

# Prepare MCA data (only columns 4+)
df_mca = df[mca_cols].copy()

if DROP_MISSING:
    initial_rows = len(df_mca)
    df_mca = df_mca.dropna()
    kept_idx = df_mca.index
    # Align all metadata to the same kept rows
    row_labels = [row_labels[i] for i in kept_idx]
    color_vals = [color_vals[i] for i in kept_idx]
    ipm_vals   = ipm_vals.loc[kept_idx]   # keep only rows that survived MCA drop
    print(f"Dropped {initial_rows - len(df_mca)} rows with missing MCA values.")

    # Also drop any remaining rows where ipm is missing (after MCA drop)
    ipm_nan = ipm_vals.isna()
    if ipm_nan.any():
        drop_ipm_idx = ipm_vals.index[ipm_nan]
        print(f"Dropping {len(drop_ipm_idx)} additional rows with missing ipm values.")
        kept_idx = df_mca.index.difference(drop_ipm_idx)
        df_mca = df_mca.loc[kept_idx]
        row_labels = [row_labels[i] for i in range(len(row_labels)) if i not in drop_ipm_idx]  # careful: row_labels is list, rebuild
        # Safer: rebuild all lists from kept_idx
        row_labels = [row_labels[i] for i, idx in enumerate(df_mca.index) if idx in kept_idx]
        color_vals = [color_vals[i] for i, idx in enumerate(df_mca.index) if idx in kept_idx]
        ipm_vals = ipm_vals.loc[kept_idx]

# Ensure MCA columns are categorical
df_mca = df_mca.astype('category')

print(f"Data for MCA shape: {df_mca.shape}")
print(f"ipm value range: {ipm_vals.min():.2f} – {ipm_vals.max():.2f}")

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
# 3. PREPARE DOT SIZES FROM IPM
# ======================
ipm_min = ipm_vals.min()
ipm_max = ipm_vals.max()
if ipm_max > ipm_min:
    # Linear scaling between min and max dot sizes, then apply overall scale factor
    ipm_sizes = (ipm_vals - ipm_min) / (ipm_max - ipm_min) * \
                (IPM_MAX_DOT_SIZE - IPM_MIN_DOT_SIZE) + IPM_MIN_DOT_SIZE
    ipm_sizes *= DOT_SIZE_SCALE          # Proportionally enlarge all dots
else:
    # All values identical → use a constant middle size, scaled
    ipm_sizes = np.full_like(ipm_vals, (IPM_MIN_DOT_SIZE + IPM_MAX_DOT_SIZE) / 2 * DOT_SIZE_SCALE)

# ======================
# 4. PREPARE COLOR MAPPING
# ======================
unique_colors = sorted(set(color_vals))
n_colors = len(unique_colors)

cmap = plt.cm.get_cmap('tab10', n_colors)
color_map = {cat: cmap(i) for i, cat in enumerate(unique_colors)}
point_colors = [color_map[val] for val in color_vals]

# ======================
# 5. PLOT INDIVIDUALS WITH LABELS, COLOR GROUPS & VARYING DOT SIZES
# ======================
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=FIG_SIZE)

# Scatter plot – dot size now comes from ipm, proportionally enlarged
scatter = ax.scatter(row_coords[0], row_coords[1],
                     c=point_colors, s=ipm_sizes, alpha=0.8,
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
ax.set_title("MCA Factor Map – Colored by " + color_col + ", size by " + ipm_col, fontsize=14, pad=20)

# Legend for color groups
handles = [plt.Line2D([0], [0], marker='o', color='w',
                      markerfacecolor=color_map[cat], markersize=8,
                      label=cat, markeredgecolor='black', markeredgewidth=0.5)
           for cat in unique_colors]
ax.legend(handles=handles, title=color_col, loc='best', fontsize=9)

ax.set_aspect('equal', adjustable='datalim')
plt.tight_layout()

# ======================
# 6. SAVE IMAGE
# ======================
output_path = Path(OUTPUT_IMAGE)
plt.savefig(output_path, dpi=DPI, bbox_inches='tight')
print(f"Map saved to: {output_path.resolve()}")

# plt.show()