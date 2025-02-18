import subprocess
import sys
import os

def build_docker_image(dockerfile_path, image_name, tag="latest"):
    """
    Build a Docker image using the provided Dockerfile.

    :param dockerfile_path: Path to the directory containing the Dockerfile.
    :param image_name: Name of the Docker image.
    :param tag: Tag for the Docker image (default is "latest").
    """
    try:
        # Ensure the Dockerfile exists
        if not os.path.isfile(dockerfile_path):
            raise FileNotFoundError(f"Dockerfile not found at {dockerfile_path}")

        # Construct the Docker build command
        command = ["docker", "build", "-t", f"{image_name}:{tag}", "."]

        # Run the Docker build command
        result = subprocess.run(command, check=True, text=True, capture_output=True)

        # Print the output of the Docker build process
        print("Docker build output:")
        print(result.stdout)

        print(f"Docker image '{image_name}:{tag}' built successfully!")

    except subprocess.CalledProcessError as e:
        # Handle errors during the Docker build process
        print(f"Error building Docker image: {e.stderr}")
    except FileNotFoundError as e:
        # Handle missing Dockerfile
        print(e)
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    dockerfile_path = "Dockerfile"  # Path to the Dockerfile
    image_name = "my-custom-image"  # Name of the Docker image
    tag = "1.0"  # Tag for the Docker image

    build_docker_image(dockerfile_path, image_name, tag)