from __future__ import annotations
import os
import mujoco

from so101_mujoco_utils2 import set_initial_pose
from so101_mujoco_pid_utils import move_to_pose_pid, hold_position_pid, DEFAULT_JOINTS
from so101_control import JointPID, PIDGains
from kp_overlay_plotter import generate_kp_overlays

MODEL_PATH = "model/scene_urdf.xml"

START_POSE = {
    "shoulder_pan":  -4.4003158666,
    "shoulder_lift": -92.2462050161,
    "elbow_flex":     89.9543738355,
    "wrist_flex":     55.1185398916,
    "wrist_roll":      0.0,
    "gripper":         0.0,
}

ZERO_POSE = {
    "shoulder_pan":  0.0,
    "shoulder_lift": 0.0,
    "elbow_flex":    0.0,
    "wrist_flex":    0.0,
    "wrist_roll":    0.0,
    "gripper":       0.0,
}

def make_pid_from_kp(kp_dict):
    gains = {}
    for jn in DEFAULT_JOINTS:
        gains[jn] = PIDGains(
            kp=float(kp_dict[jn]),
            ki=0.0,
            kd=0.0,
            i_limit=2.0,
            tau_limit=12.0,
        )
    return JointPID(DEFAULT_JOINTS, gains)

def main():
    m = mujoco.MjModel.from_xml_path(MODEL_PATH)
    os.makedirs("results/P_kp_study", exist_ok=True)

    KP_COMBOS = [
        {"shoulder_pan": 15, "shoulder_lift": 10, "elbow_flex": 8,  "wrist_flex": 5,  "wrist_roll": 3},
        {"shoulder_pan": 25, "shoulder_lift": 18, "elbow_flex": 14, "wrist_flex": 8,  "wrist_roll": 5},
        {"shoulder_pan": 40, "shoulder_lift": 28, "elbow_flex": 22, "wrist_flex": 12, "wrist_roll": 7},
        {"shoulder_pan": 55, "shoulder_lift": 38, "elbow_flex": 30, "wrist_flex": 16, "wrist_roll": 9},
        {"shoulder_pan": 70, "shoulder_lift": 50, "elbow_flex": 38, "wrist_flex": 20, "wrist_roll": 11},
    ]

    for idx, kp_dict in enumerate(KP_COMBOS, start=1):
        combo_dir = f"results/P_kp_study/combo_{idx:02d}"
        os.makedirs(combo_dir, exist_ok=True)

        d = mujoco.MjData(m)
        set_initial_pose(m, d, START_POSE)

        pid = make_pid_from_kp(kp_dict)

        move_to_pose_pid(m, d, viewer=None, target_pose_deg=ZERO_POSE, duration=2.0, realtime=False, pid=pid)
        hold_position_pid(m, d, viewer=None, hold_pose_deg=ZERO_POSE, duration=2.0, realtime=False, pid=pid)
        move_to_pose_pid(m, d, viewer=None, target_pose_deg=START_POSE, duration=2.0, realtime=False, pid=pid)
        hold_position_pid(m, d, viewer=None, hold_pose_deg=START_POSE, duration=2.0, realtime=False, pid=pid)

    generate_kp_overlays("results/P_kp_study")

if __name__ == "__main__":
    main()
