from dotenv import load_dotenv
import os
from PIL import Image
import json
import asyncio
from mcp_server.client import agent_instance
import streamlit as st
from mcp_server import client

# ---------------------------------------
# Command-line interface (commented out, kept for testing)
# ---------------------------------------
if __name__ == "__main__":
    load_dotenv()
    try:
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_key_id = os.getenv("AWS_SECRET_ACCESS_KEY")
        aws_session_token = os.getenv("AWS_SESSION_TOKEN")
    except Exception as e:
        raise RuntimeError(f"Failed to load AWS credentials from environment: {e}")
    user_prompt = input("Enter your research topic or keywords: ")
    asyncio.run(
        client.agent_instance(user_prompt, model="eu.anthropic.claude-sonnet-4-5-20250929-v1:0", aws_access_key_id=aws_access_key_id, 
                              aws_secret_key_id=aws_secret_key_id, aws_session_token=aws_session_token, 
                              aws_region="eu-west-1",
                              temperature=0)
    )


# ---------------------------------------
# Streamlit Configuration
# ---------------------------------------
# st.set_page_config(
#     page_title="AI Object Detection & Image Generation",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Model mapping: display name -> actual model ID
# model_mapping = {
#     "anthropic.claude-3-haiku": "anthropic.claude-3-haiku-20240307-v1:0",
#     "meta.llama3-2-1b-instruct": "meta.llama3-2-3b-instruct-v1:0",
#     "anthropic.claude-sonnet-4-5": "eu.anthropic.claude-sonnet-4-5-20250929-v1:0",
# }

# # ---------------------------------------
# # Helper Functions
# # ---------------------------------------

# def __load_aws_credentials():
#     """Load AWS credentials from .config file"""
#     config_path = ".config"
#     if os.path.exists(config_path):
#         with open(config_path, "r") as f:
#             credentials = json.load(f)
#         return credentials
#     return None

# def __store_aws_credentials(aws_access_key_id, aws_secret_access_key, aws_session_token, aws_region):
#     """Store AWS credentials from sidebar inputs to .config file"""
#     credentials = {
#         "AWS_ACCESS_KEY_ID": aws_access_key_id,
#         "AWS_SECRET_ACCESS_KEY": aws_secret_access_key,
#         "AWS_SESSION_TOKEN": aws_session_token,
#         "AWS_REGION": aws_region,
#     }
    
#     config_path = ".config"
#     with open(config_path, "w") as f:
#         json.dump(credentials, f, indent=4)
    
#     print("Button is clicked")
#     print(f"Stored credentials to {config_path}")
#     return credentials

# # ---------------------------------------
# # Main Application
# # ---------------------------------------

# def main():
#     # Load environment variables
#     load_dotenv()
    
#     # Load saved credentials
#     saved_credentials = __load_aws_credentials()
    
#     # Header with logos
#     col1, col2 = st.columns([0.3, 5.7])
    
#     with col1:
#         st.markdown("<br>", unsafe_allow_html=True)
#         try:
#             logo = Image.open("logo/01.png")
#             st.image(logo, width=40)
#         except FileNotFoundError:
#             st.write("👁️")
    
#     with col2:
#         st.title("AI Object Detection & Image Generation")
#         st.markdown("Generate images from text or analyze uploaded images with AI")
    
#     # Sidebar Configuration
#     with st.sidebar:
#         st.header("⚙️ Configuration")
        
#         # Model Selection
#         st.subheader("🤖 Model Selection")
#         selected_model_display = st.selectbox(
#             "Select Model",
#             options=list(model_mapping.keys()),
#             index=2,  # Default to claude-sonnet-4-5
#             help="Choose the AI model to use"
#         )
#         selected_model = model_mapping[selected_model_display]
        
#         # Temperature Control
#         st.subheader("🌡️ Temperature")
#         temperature = st.slider(
#             "Model Temperature",
#             min_value=0.0,
#             max_value=1.0,
#             value=0.0,
#             step=0.1,
#             help="Controls randomness: 0 = focused, 1 = creative"
#         )
        
#         # AWS Credentials
#         st.markdown("---")
#         st.subheader("🔐 AWS Credentials")
        
#         aws_access_key_id = st.text_input(
#             "AWS Access Key ID",
#             value=saved_credentials.get("AWS_ACCESS_KEY_ID", "") if saved_credentials else os.getenv("AWS_ACCESS_KEY_ID", ""),
#             type="password",
#             key="aws_access_key",
#             help="Your AWS Access Key ID",
#         )
        
#         aws_secret_access_key = st.text_input(
#             "AWS Secret Access Key",
#             value=saved_credentials.get("AWS_SECRET_ACCESS_KEY", "") if saved_credentials else os.getenv("AWS_SECRET_ACCESS_KEY", ""),
#             type="password",
#             key="aws_secret_key",
#             help="Your AWS Secret Access Key",
#         )
        
#         aws_session_token = st.text_input(
#             "AWS Session Token (Optional)",
#             value=saved_credentials.get("AWS_SESSION_TOKEN", "") if saved_credentials else os.getenv("AWS_SESSION_TOKEN", ""),
#             type="password",
#             key="aws_session_token",
#             help="Your AWS Session Token",
#         )
        
#         aws_region = st.text_input(
#             "AWS Region",
#             value=saved_credentials.get("AWS_REGION", "") if saved_credentials else os.getenv("AWS_REGION", "eu-west-1"),
#             key="aws_region",
#             help="AWS Region (e.g., eu-west-1, us-east-1)",
#         )
        
#         # Button to enter credentials
#         if st.button("🔄 Enter Credentials", key="aws_creds", use_container_width=True):
#             __store_aws_credentials(aws_access_key_id, aws_secret_access_key, aws_session_token, aws_region)
#             st.success("✅ Stored!")
    
#     # Main Content Area
#     st.markdown("---")
    
#     # Tabs for different functionalities
#     tab1, tab2 = st.tabs(["🎨 Generate Image", "🔍 Detect Objects"])
    
#     with tab1:
#         st.header("Generate Image from Text")
#         st.markdown("Enter a description and the AI will generate an image for you")
        
#         user_prompt_generate = st.text_area(
#             "Describe the image you want to generate:",
#             placeholder="e.g., A futuristic city with flying cars at sunset",
#             height=100,
#             key="generate_prompt"
#         )
        
#         if st.button("🎨 Generate Image", key="generate_btn", type="primary"):
#             if not user_prompt_generate:
#                 st.warning("⚠️ Please enter a description")
#             elif not aws_access_key_id or not aws_secret_access_key:
#                 st.error("❌ Please provide AWS credentials in the sidebar")
#             else:
#                 with st.spinner("🎨 Generating image..."):
#                     try:
#                         result = asyncio.run(
#                             client.agent_instance(
#                                 user_prompt_generate,
#                                 model=selected_model,
#                                 aws_access_key_id=aws_access_key_id,
#                                 aws_secret_key_id=aws_secret_access_key,
#                                 aws_session_token=aws_session_token,
#                                 aws_region=aws_region,
#                                 temperature=temperature
#                             )
#                         )
#                         st.success("✅ Image generated successfully!")
#                         st.write(result)
#                     except Exception as e:
#                         st.error(f"❌ Error: {str(e)}")
    
#     with tab2:
#         st.header("Upload Image for Object Detection")
#         st.markdown("Upload an image and the AI will analyze and explain what it detects")
        
#         uploaded_file = st.file_uploader(
#             "Choose an image...",
#             type=["png", "jpg", "jpeg", "webp"],
#             help="Upload an image for object detection and analysis"
#         )
        
#         if uploaded_file is not None:
#             # Display uploaded image
#             col_img, col_analysis = st.columns([1, 1])
            
#             with col_img:
#                 st.subheader("Uploaded Image")
#                 image = Image.open(uploaded_file)
#                 st.image(image, use_container_width=True)
            
#             with col_analysis:
#                 st.subheader("Analysis")
                
#                 analysis_prompt = st.text_area(
#                     "Additional instructions (optional):",
#                     placeholder="e.g., Focus on specific objects or provide detailed analysis",
#                     height=100,
#                     key="analysis_prompt"
#                 )
                
#                 if st.button("🔍 Analyze Image", key="analyze_btn", type="primary"):
#                     if not aws_access_key_id or not aws_secret_access_key:
#                         st.error("❌ Please provide AWS credentials in the sidebar")
#                     else:
#                         with st.spinner("🔍 Analyzing image..."):
#                             try:
#                                 # Prepare the prompt for object detection
#                                 detection_prompt = "Analyze this image and detect all objects present. Provide detailed explanations about what you see."
#                                 if analysis_prompt:
#                                     detection_prompt += f"\n\nAdditional instructions: {analysis_prompt}"
                                
#                                 result = asyncio.run(
#                                     client.agent_instance(
#                                         detection_prompt,
#                                         model=selected_model,
#                                         aws_access_key_id=aws_access_key_id,
#                                         aws_secret_key_id=aws_secret_access_key,
#                                         aws_session_token=aws_session_token,
#                                         aws_region=aws_region,
#                                         temperature=temperature
#                                     )
#                                 )
#                                 st.success("✅ Analysis complete!")
#                                 st.write(result)
#                             except Exception as e:
#                                 st.error(f"❌ Error: {str(e)}")

# # ---------------------------------------
# # Run Application
# # ---------------------------------------
# if __name__ == "__main__":
#     main()
