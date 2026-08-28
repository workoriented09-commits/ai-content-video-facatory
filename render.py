import os
import subprocess
from pathlib import Path

# --------------------------------------------------
# AI CONTENT FACTORY
# Stage 3 - Basic Cloud Video Renderer
# --------------------------------------------------

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

VIDEO_FILE = OUTPUT_DIR / "test_video.mp4"

WIDTH = 1080
HEIGHT = 1920
FPS = 30
DURATION = 10


def create_video():
    """
    Creates a simple vertical MP4 test video.

    This is intentionally simple.
    We are testing the cloud rendering system first.
    """

    print("Starting video renderer...")

    command = [
        "ffmpeg",

        "-y",

        # Generate a vertical test background.
        "-f",
        "lavfi",

        "-i",
        (
            f"color=c=black:"
            f"s={WIDTH}x{HEIGHT}:"
            f"r={FPS}"
        ),

        "-t",
        str(DURATION),

        # Encode to H.264.
        "-c:v",
        "libx264",

        # Compatibility setting.
        "-pix_fmt",
        "yuv420p",

        # Output.
        str(VIDEO_FILE)
    ]

    print("Running FFmpeg...")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        print("FFmpeg failed.")

        print(result.stderr)

        raise RuntimeError(
            "Video rendering failed."
        )

    print("Video created successfully:")
    print(VIDEO_FILE)


if __name__ == "__main__":
    create_video()
