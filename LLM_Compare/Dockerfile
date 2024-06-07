# This is the Dockerfile that pulls the base image with gradio hosting env
# An image will be build with source code integrated
FROM 201053736981.dkr.ecr.ap-east-1.amazonaws.com/clinmatch_gradio:v0

# Defining working directory and copy the requirements file. We will run the commands inside this new directory
WORKDIR /usr/src/gradioapp

# # Copy requirements.txt  to the working directory
# COPY requirements.txt .
# # Install required python packages if not installed 
# RUN pip install --no-cache-dir -r requirements.txt

# Copy all files in training-db local host directory to /usr/src/myapp in Docker container
COPY . .

# Expose the port that our app runs in
EXPOSE 7860
ENV GRADIO_SERVER_NAME 0.0.0.0

# Run our App
CMD ["python3","app.py"]


##################################################
# sudo docker build -t clinmatch_llm_comparsion_app:v0 .

# # -t to keep it running
# sudo docker run -d --name gradio -p 127.0.0.1:7863:7860 -e GRADIO_SERVER_NAME=0.0.0.0 simplegradio:v0
# sudo docker run -d -t --name gradio_bg_env -p 127.0.0.1:7863:7860 -e GRADIO_SERVER_NAME=0.0.0.0 simplegradio_noexe:v0
# sudo docker run -d -t --name gradio_bg_env -p 127.0.0.1:7863:7860 clinmatchgradio_bg:v0
# docker run -d -t --name gradio_llm_comparison_app -p 0.0.0.0:7861:7860 clinmatch_llm_comparsion_app:v0

# # crlt+d to exit
# sudo docker exec -it gradio_main_app bash 
# sudo docker exec -it webserver bash 

# sudo docker exec --env-file .env -t -d gradio_bg_env sh -c "python app.py"
# sudo docker exec -t -d gradio_bg_env sh -c "python app.py"

##################################################