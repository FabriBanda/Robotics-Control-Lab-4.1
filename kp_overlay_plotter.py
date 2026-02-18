import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

JOINTS = ["shoulder_pan", "shoulder_lift", "elbow_flex", "wrist_flex", "wrist_roll"]

def generate_kp_overlays(results_dir):
    combo_dirs = sorted(glob.glob(os.path.join(results_dir, "combo_*")))

    for jn in JOINTS:
        plt.figure()

        for combo_dir in combo_dirs:
            csv_path = os.path.join(combo_dir, "log.csv")
            if not os.path.exists(csv_path):
                continue

            df = pd.read_csv(csv_path)
            plt.plot(df["t"], df[f"{jn}_q"], label=os.path.basename(combo_dir))

        plt.xlabel("time (s)")
        plt.ylabel("position (rad)")
        plt.title(f"P study — {jn} (5 Kp combinations)")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(results_dir, f"{jn}_overlay.png"), dpi=180)
        plt.close()

    print("[OK] Kp overlay plots generated.")
