# 1. Base Image
FROM python:3.10-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# 5. Copy the application code
COPY . .

# 6. Create a non-root use
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# 7. Create directory for Chainlit files and set permissions
WORKDIR $HOME/app
COPY --chown=user . $HOME/app

# 8. Expose the port required by Hugging Face Spaces
EXPOSE 7860

# 9. Run the application
# Note: --host 0.0.0.0 for Docker networking
# Note: --port 7860 exposed port
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"]